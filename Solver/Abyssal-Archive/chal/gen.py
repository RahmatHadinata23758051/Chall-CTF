import os
import tarfile
import zipfile
import gzip
import bz2
import lzma
import shutil

def create_challenge():
    flag = "iet{1337_l4y3rs_0f_m4try0shk4_m4dn3ss}"
    current_file = "flag.txt"
    
    with open(current_file, "w") as f:
        f.write(flag)
    
    layers = 1337
    
    for i in range(layers):
        ext_idx = i % 5
        # 0: .zip, 1: .tar, 2: .gz, 3: .bz2, 4: .xz
        
        new_filename = f"layer_{layers - i}"
        
        if ext_idx == 0:
            new_file = new_filename + ".zip"
            with zipfile.ZipFile(new_file, 'w') as z:
                z.write(current_file)
        elif ext_idx == 1:
            new_file = new_filename + ".tar"
            with tarfile.open(new_file, "w") as t:
                t.add(current_file)
        elif ext_idx == 2:
            new_file = new_filename + ".gz"
            with open(current_file, 'rb') as f_in:
                with gzip.open(new_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        elif ext_idx == 3:
            new_file = new_filename + ".bz2"
            with open(current_file, 'rb') as f_in:
                with bz2.open(new_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        elif ext_idx == 4:
            new_file = new_filename + ".xz"
            with open(current_file, 'rb') as f_in:
                with lzma.open(new_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        
        # Cleanup old file and move to next
        if current_file != "flag.txt":
            os.remove(current_file)
        current_file = new_file
        print(f"Layer {i+1}/{layers} created: {current_file}", end="\r")

    os.rename(current_file, "abyssal.matryoshka")
    if os.path.exists("flag.txt"):
        os.remove("flag.txt")
    print("\nChallenge generated: abyssal.matryoshka")

if __name__ == "__main__":
    create_challenge()
