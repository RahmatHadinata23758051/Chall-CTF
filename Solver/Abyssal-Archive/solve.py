import os
import tarfile
import zipfile
import gzip
import bz2
import lzma
import shutil

def solve():
    current_file = "abyssal.matryoshka"
    # Copy to work area
    shutil.copy(f"../../Abyssal-Archive/{current_file}", current_file)
    
    while True:
        print(f"Extracting: {current_file}...", end="\r")
        
        # Check file type
        # We can use file signature or just try all extractors
        extracted = False
        
        # Try Zip
        if zipfile.is_zipfile(current_file):
            with zipfile.ZipFile(current_file, 'r') as z:
                names = z.namelist()
                z.extractall()
                next_file = names[0]
                extracted = True
        
        # Try Tar
        elif tarfile.is_tarfile(current_file):
            with tarfile.open(current_file, "r") as t:
                names = t.getnames()
                t.extractall()
                next_file = names[0]
                extracted = True
        
        # Try Gzip
        else:
            try:
                with gzip.open(current_file, 'rb') as f_in:
                    # We need to guess the filename or look at headers
                    # For simplicity in this challenge, we know the pattern
                    next_file = "extracted_content" 
                    # But wait, gz/bz2/xz don't store multiple files like zip/tar
                    # Let's try to detect based on extension or magic
                    with open(next_file, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    extracted = True
            except:
                pass
                
            if not extracted:
                try:
                    with bz2.open(current_file, 'rb') as f_in:
                        next_file = "extracted_content"
                        with open(next_file, 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)
                        extracted = True
                except:
                    pass
            
            if not extracted:
                try:
                    with lzma.open(current_file, 'rb') as f_in:
                        next_file = "extracted_content"
                        with open(next_file, 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)
                        extracted = True
                except:
                    pass

        if not extracted:
            # If we reach here, it might be the flag.txt
            if os.path.exists(current_file):
                with open(current_file, 'r') as f:
                    content = f.read()
                    if "iet{" in content:
                        print(f"\nFlag found: {content}")
                        break
            print("\nFinished or Error.")
            break
            
        # Cleanup and move to next
        if current_file != "abyssal.matryoshka":
            os.remove(current_file)
        current_file = next_file
        
        # Rename to keep it simple if it's a raw stream
        if current_file == "extracted_content":
            # Peek into the file to see what it is
            os.rename("extracted_content", "temp_file")
            current_file = "temp_file"

if __name__ == "__main__":
    solve()
