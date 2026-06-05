# Abyssal Archive - Writeup

## Analisis
Diberikan sebuah file `abyssal.matryoshka` yang merupakan arsip kompresi. Jika diperiksa, file ini berisi lapisan arsip lain di dalamnya. Berdasarkan deskripsi, terdapat 1337 lapisan.

## Solusi
Melakukan ekstraksi manual sebanyak 1337 kali sangat tidak efisien. Solusi yang tepat adalah menggunakan script (Python/Bash) untuk mendeteksi jenis kompresi di setiap lapisan dan mengekstraknya secara rekursif atau iteratif.

Algoritma script:
1. Identifikasi jenis file (Zip, Tar, Gzip, Bz2, Xz).
2. Ekstrak file tersebut.
3. Hapus file lama untuk menghemat ruang.
4. Ulangi sampai menemukan file `flag.txt`.

**Flag:** `iet{1337_l4y3rs_0f_m4try0shk4_m4dn3ss}`
