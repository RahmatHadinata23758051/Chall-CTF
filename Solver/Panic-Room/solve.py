import re

def solve():
    # In a real scenario, the player would open the binary in Ghidra/IDA
    # and find the constants in each catch_unwind block.
    # Since I'm the creator, I'll parse the generated main.rs for the solver example.
    
    with open("chal/main.rs", "r") as f:
        content = f.read()
    
    # Each block looks like: if (input[i] ^ K) == TARGET
    # We find all (K, TARGET) pairs in order
    matches = re.findall(r"\(input\[\d+\] \^ (\d+)\) == (\d+)", content)
    
    flag = ""
    for k, target in matches:
        flag += chr(int(k) ^ int(target))
        
    print(flag)

if __name__ == "__main__":
    solve()
