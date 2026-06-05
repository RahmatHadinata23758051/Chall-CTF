import subprocess

def solve():
    img_path = "../../Spectral-Log/spectral.img"
    # The simplest way to solve this specific challenge is strings, 
    # but in a more complex one, you'd need to parse JBD2.
    
    # Let's simulate a 'smart' solver that looks for the pattern
    try:
        output = subprocess.check_output(["strings", img_path])
        for line in output.decode().split("\n"):
            if "The password for Pastebin is:" in line:
                print(f"Found: {line}")
                return
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    solve()
