import random

def generate_rust():
    random.seed(42)
    flag = "iet{p4n1c_unw1nd_1s_n0t_4_bug}"
    assert len(flag) == 30

    header = """use std::panic;
use std::env;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Usage: ./panic_room <flag>");
        return;
    }
    let input = args[1].as_bytes();
    if input.len() != 30 {
        println!("Goblok! Panjangnya aja salah. AI lu nggak ngasih tau?");
        process::exit(1);
    }

    let mut state: u8 = 0;
    
    // Disable default panic hook to keep it quiet
    panic::set_hook(Box::new(|_| {}));

"""

    body = ""
    # We will use a chain of catch_unwind
    # Each catch_unwind checks one byte and panics if correct to go to next
    # Or something more complex: nested catch_unwind
    
    current_indent = "\t"
    
    for i in range(30):
        k = random.randint(1, 255)
        target = ord(flag[i]) ^ k
        
        body += f"{current_indent}let r = panic::catch_unwind(|| {{\n"
        body += f"{current_indent}    if (input[{i}] ^ {k}) == {target} {{\n"
        body += f"{current_indent}        panic!(\"next\");\n"
        body += f"{current_indent}    }}\n"
        body += f"{current_indent}}});\n"
        body += f"{current_indent}if r.is_err() {{\n"
        current_indent += "    "

    body += f"{current_indent}println!(\"Anjay, kok bener? Hoki doang lu pasti.\");\n"
    
    # Close all the if r.is_err() blocks
    for i in range(30):
        current_indent = current_indent[:-4]
        body += f"{current_indent}}} else {{\n"
        body += f"{current_indent}    println!(\"Cupu! Balik belajar rev lagi sana.\");\n"
        body += f"{current_indent}    process::exit(1);\n"
        body += f"{current_indent}}}\n"

    footer = "}\n"
    
    return header + body + footer

if __name__ == "__main__":
    with open("main.rs", "w") as f:
        f.write(generate_rust())
