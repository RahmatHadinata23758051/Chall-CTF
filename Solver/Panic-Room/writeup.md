# Panic Room - Writeup

## Analisis Binary
Binary diberikan dalam bentuk executable Rust yang sudah di-optimasi dan di-strip.

## Reversing Logic
Rust memiliki fitur `panic` untuk menangani error fatal. Secara default, `panic` akan melakukan "stack unwinding". Program ini menyalahgunakan fitur tersebut sebagai *control flow*.

Logika pengecekan flag dibungkus di dalam banyak lapisan `std::panic::catch_unwind`. 
- Program mengecek karakter pertama.
- Jika benar, program memanggil `panic!()`.
- Panic tersebut ditangkap oleh `catch_unwind`, yang kemudian melanjutkan eksekusi ke pengecekan karakter kedua.
- Jika salah, program tidak panic, `catch_unwind` mengembalikan `Ok`, dan program akan keluar dengan pesan "Cupu!".

## Solution
Karena setiap pengecekan karakter berada di dalam scope penanganan panic yang berbeda, alur eksekusi di decompiler (seperti Ghidra atau IDA) akan terlihat sangat terfragmentasi. Player harus mengikuti jejak fungsi unwinding Rust.

Namun, karena setiap blok pengecekan memiliki pola yang sama: `(input[i] ^ CONST_1) == CONST_2`, kita bisa mengekstrak konstanta tersebut secara statis.

## Solver
```python
# (Lihat solve.py)
# Flag[i] = CONST_1 ^ CONST_2
```

**Flag:** `iet{p4n1c_unw1nd_1s_n0t_4_bug}`
