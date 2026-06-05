import random

def generate_challenge():
    random.seed(1337)
    flag = "iet{g0_ch4nn3l_m4z3_1s_p41n_!!!}"
    assert len(flag) == 32

    header = """package main

import (
	"fmt"
	"os"
)

func gateXOR(c1, c2 <-chan int, out chan<- int) {
	out <- (<-c1) ^ (<-c2)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: ./stygian <flag>")
		return
	}
	input := os.Args[1]
	if len(input) != 32 {
		fmt.Println("Goblok! Panjangnya aja salah.")
		return
	}

	chans := make([]chan int, 10000)
	for i := range chans {
		chans[i] = make(chan int, 1)
	}
"""

    body = ""
    # Map input chars to random channels
    input_indices = list(range(32))
    random.shuffle(input_indices)
    current_chans = [0] * 32
    for i, idx in enumerate(input_indices):
        body += f"\tgo func() {{ chans[{idx}] <- int(input[{i}]) }}()\n"
        current_chans[i] = idx

    current_chan_ptr = 100
    
    # Simulation state
    sim_vals = [ord(c) for c in flag]

    # Layers of logic
    for layer in range(5):
        next_chans = [0] * 32
        next_vals = [0] * 32
        
        # Randomize mapping for next layer
        mapping = list(range(32))
        random.shuffle(mapping)
        
        for i in range(32):
            k = random.randint(1, 255)
            # k_chan
            k_idx = current_chan_ptr
            body += f"\tgo func() {{ chans[{k_idx}] <- {k} }}()\n"
            current_chan_ptr += 1
            
            # output of this layer
            out_idx = current_chan_ptr
            body += f"\tgo gateXOR(chans[{current_chans[i]}], chans[{k_idx}], chans[{out_idx}])\n"
            current_chan_ptr += 1
            
            # Map to next layer
            dest = mapping[i]
            next_chans[dest] = out_idx
            next_vals[dest] = sim_vals[i] ^ k
            
        current_chans = next_chans
        sim_vals = next_vals

    # Final check
    body += "\n\tcorrect := true\n"
    # To make it even harder, we don't check in order
    check_indices = list(range(32))
    random.shuffle(check_indices)
    for i in check_indices:
        body += f"\tif <-chans[{current_chans[i]}] != {sim_vals[i]} {{ correct = false }}\n"

    footer = """
	if correct {
		fmt.Println("Anjay, kok bener? Hoki doang lu pasti.")
	} else {
		fmt.Println("Tuh kan, beneran cupu. Balik belajar rev lagi sana!")
	}
}
"""
    return header + body + footer

if __name__ == "__main__":
    with open("main.go", "w") as f:
        f.write(generate_challenge())
