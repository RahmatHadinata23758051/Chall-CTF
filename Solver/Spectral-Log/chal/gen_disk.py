import os
import subprocess

def create_challenge():
    img_name = "spectral.img"
    # 1. Create a 20MB image
    subprocess.run(["dd", "if=/dev/zero", f"of={img_name}", "bs=1M", "count=20"])
    
    # 2. Format as ext4
    subprocess.run(["/usr/sbin/mkfs.ext4", "-F", img_name])
    
    # 3. Use debugfs to write the password file then delete it
    # This will leave traces in the journal
    password = "sp3ctral_ghost_jbd2_r3v3l4t10n"
    
    # Writing commands for debugfs
    # - write <local_file> <remote_file>
    # - rm <remote_file>
    with open("pass.txt", "w") as f:
        f.write(f"The password for Pastebin is: {password}\n")
    
    debugfs_cmds = f"""write pass.txt secret_data.txt
ls -l
rm secret_data.txt
ls -l
freeb 0
"""
    with open("cmds.txt", "w") as f:
        f.write(debugfs_cmds)
        
    subprocess.run(["debugfs", "-w", "-f", "cmds.txt", img_name])
    
    # 4. Corruption: Wipe the first 1024 bytes (Superblock is at 1024, so wipe MBR/Partition table)
    # We want them to have to fix the image or find the ext4 offset
    with open(img_name, "r+b") as f:
        f.write(b"\x00" * 1024)
        
    print(f"Challenge image {img_name} created.")

if __name__ == "__main__":
    create_challenge()
