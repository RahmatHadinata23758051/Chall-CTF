# Stygian Circuit - Writeup

## Analisis Binary
Binary diberikan dalam bentuk ELF 64-bit yang sudah di-strip (`-s -w`). Binary ini dibuat menggunakan Go. 

Jika dijalankan, binary akan meminta satu argumen berupa flag dengan panjang 32 karakter.

## Reversing Logic
Ketika dibuka di decompiler (Ghidra/IDA), binary ini akan terlihat sangat berantakan karena penggunaan goroutine dan channel yang masif. 

Pola utama yang ditemukan adalah:
1. Input dibaca dan dimasukkan ke dalam beberapa channel.
2. Banyak goroutine dijalankan (`runtime.newproc`).
3. Goroutine-goroutine tersebut memanggil fungsi `main.gateXOR` yang mengambil dua input dari channel dan mengirimkan hasilnya ke channel lain.
4. Terdapat 5 "layer" transformasi di mana setiap layer melakukan operasi XOR dengan konstanta dan mengacak urutan channel (mapping).
5. Di akhir, hasil dari channel-channel tersebut dibandingkan dengan konstanta hardcoded.

Karena operasi yang digunakan hanya XOR, seluruh sistem ini sebenarnya adalah sistem linear di atas GF(2). Setiap output channel di akhir adalah hasil dari `input[i] ^ K_total`.

## Solution
Meskipun trace manual hampir mustahil karena banyaknya goroutine asinkron, kita bisa menyelesaikan soal ini dengan dua cara:

### Method 1: Static Analysis Scripting (Recommended)
Karena source code Go-nya sangat repetitif, kita bisa mem-parse binary atau source code (jika tersedia) untuk mengekstrak:
- Mapping input ke channel awal.
- Konstanta XOR di setiap langkah.
- Alur `gateXOR` (input channels -> output channel).
- Nilai akhir yang diharapkan.

Dengan data tersebut, kita bisa melakukan "Symbolic Execution" sederhana atau cukup melakukan tracking XOR untuk setiap byte input.

### Method 2: Dynamic Instrumentation (Frida)
Kita bisa menggunakan Frida untuk meng-hook fungsi `main.gateXOR` atau fungsi internal `runtime.chansend` untuk melihat data apa saja yang dikirim antar channel dan merekonstruksi grafnya.

## Solver Script
Berikut adalah logika inti dari solver yang mem-parse source code (rekonstruksi graf):
```python
# (Lihat solve.py untuk implementasi lengkap)
# 1. Parse mappings input[i] -> chan[X]
# 2. Parse constants chans[Y] -> K
# 3. Trace gateXOR(chan A, chan B, chan C) => state[C] = state[A] ^ state[B]
# 4. Extract expected values at the end
# 5. input[i] = expected ^ total_K
```

**Flag:** `iet{g0_ch4nn3l_m4z3_1s_p41n_!!!}`
