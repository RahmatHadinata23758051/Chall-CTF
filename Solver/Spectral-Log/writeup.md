# Spectral Log - Writeup

## Analisis Awal
Diberikan sebuah file disk image `spectral.img`. Jika kita mencoba melihat tabel partisi menggunakan `fdisk -l` atau `mmls`, file ini akan terlihat korup karena 1024 byte pertamanya sudah di-wipe (MBR/GPT hilang).

## Recovery Filesystem
Meskipun tabel partisi hilang, kita bisa mencari signature Ext4 (Superblock) yang biasanya ada di offset 1024. Kita bisa menggunakan `fls -o 0` (setelah memperbaiki header) atau mencari langsung data di dalamnya.

Jika kita melakukan mounting atau melihat isi filesystem, kita akan mendapati bahwa filesystem tersebut kosong (hanya ada `lost+found`). Tidak ada file `secret_data.txt`.

## Forensic JBD2 (Journaling)
Kunci dari soal ini adalah penggunaan **Ext4 Journaling (JBD2)**. Di Ext4, setiap operasi tulis akan dicatat di jurnal sebelum benar-benar di-commit ke disk. Meskipun file sudah dihapus (`rm`), catatan transaksinya (termasuk isinya jika menggunakan mode `data=journal` atau jika datanya masih tersisa di block log) seringkali masih ada di area jurnal.

### Step 1: Ekstrak Jurnal
Kita bisa menggunakan `debugfs` untuk mengekstrak file jurnal internal (inode <8>):
```bash
debugfs -R "dump <8> journal.bin" spectral.img
```

### Step 2: Cari String
Karena kita mencari password, kita bisa melakukan pencarian string langsung pada file jurnal atau image:
```bash
strings -t d spectral.img | grep "password"
```
Atau menggunakan tool seperti `ext4magic` untuk mencoba me-recover file yang sudah terhapus dari journal.

## Solution
Ditemukan password: `sp3ctral_ghost_jbd2_r3v3l4t10n`

Gunakan password tersebut untuk mengakses `https://pastebin.com/raw/u8vS1fK2` (Note: Ini adalah link simulasi, ganti dengan link asli jika dipublish).

**Flag:** `iet{jbd2_n3v3r_f0rg3ts_y0ur_s3cr3ts}`
