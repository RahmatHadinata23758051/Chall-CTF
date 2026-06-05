import re

def solve():
    with open("chal/main.go", "r") as f:
        content = f.read()

    # 1. Map input bytes to channels
    # go func() { chans[4] <- int(input[0]) }()
    input_to_chan = {}
    for match in re.finditer(r"chans\[(\d+)\] <- int\(input\[(\d+)\]\)", content):
        chan, idx = map(int, match.groups())
        input_to_chan[idx] = chan

    # 2. Map constant values to channels
    # go func() { chans[100] <- 4 }()
    chan_to_const = {}
    for match in re.finditer(r"chans\[(\d+)\] <- (\d+)\b", content):
        chan, val = map(int, match.groups())
        # Ignore input mappings and final checks
        if "input" not in match.group(0):
            chan_to_const[chan] = val

    # 3. Track XOR operations
    # go gateXOR(chans[4], chans[100], chans[101])
    # We want to know: chan C = chan A ^ chan B
    xor_ops = []
    for match in re.finditer(r"gateXOR\(chans\[(\d+)\], chans\[(\d+)\], chans\[(\d+)\]\)", content):
        xor_ops.append(map(int, match.groups()))

    # 4. Final checks
    # if <-chans[403] != 112 { correct = false }
    final_checks = {}
    for match in re.finditer(r"<-chans\[(\d+)\] != (\d+)", content):
        chan, val = map(int, match.groups())
        final_checks[chan] = val

    # 5. Symbolic execution (simplified for XOR)
    # Each channel value is input[i] ^ K
    # We track which input and what total XOR key
    chan_state = {} # chan -> (input_idx, xor_key)
    
    for idx, chan in input_to_chan.items():
        chan_state[chan] = (idx, 0)
        
    for chan, val in chan_to_const.items():
        chan_state[chan] = (None, val)

    # Process XORs in order
    # Since it's a DAG (Go code order ensures this), we can just iterate
    for a, b, c in xor_ops:
        state_a = chan_state.get(a)
        state_b = chan_state.get(b)
        
        if state_a and state_b:
            idx_a, key_a = state_a
            idx_b, key_b = state_b
            
            if idx_a is not None and idx_b is None:
                # input ^ key_a ^ key_b
                chan_state[c] = (idx_a, key_a ^ key_b)
            elif idx_a is None and idx_b is not None:
                # key_a ^ input ^ key_b
                chan_state[c] = (idx_b, key_a ^ key_b)
            elif idx_a is None and idx_b is None:
                # key_a ^ key_b
                chan_state[c] = (None, key_a ^ key_b)
            else:
                # Both are inputs? Not in our current generator but possible
                pass

    # 6. Solve for flag
    flag = [0] * 32
    for chan, expected_val in final_checks.items():
        if chan in chan_state:
            idx, total_key = chan_state[chan]
            if idx is not None:
                # input[idx] ^ total_key = expected_val
                flag[idx] = expected_val ^ total_key

    print("".join(chr(c) for c in flag))

if __name__ == "__main__":
    solve()
