# Calculated Silence - Writeup

## Analisis
Diberikan 100 tanda tangan ECDSA (`secp256k1`). Kunci dari soal ini adalah kelemahan pada *nonce* ($k$). 

Dalam ECDSA:
$$s = k^{-1}(z + rd) \pmod n$$
$$k = s^{-1}z + s^{-1}rd \pmod n$$

Dapat ditulis ulang sebagai:
$$k_i - s_i^{-1}r_id \equiv s_i^{-1}z_i \pmod n$$

Misalkan $t_i = s_i^{-1}r_i \pmod n$ dan $u_i = s_i^{-1}z_i \pmod n$:
$$k_i - t_id \equiv u_i \pmod n$$

Jika $k_i$ benar-benar acak 256-bit, ini adalah masalah yang sulit. Namun, di soal ini disebutkan bahwa 8-bit teratas $k$ adalah nol ($k < 2^{248}$). Ini adalah variansi dari **Hidden Number Problem (HNP)**.

## Solusi
HNP dapat diselesaikan menggunakan **Lattice Reduction (LLL)**. Kita menyusun matriks kisi sebagai berikut:

$$
M = \begin{pmatrix}
n & 0 & \dots & 0 & 0 & 0 \\
0 & n & \dots & 0 & 0 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\
0 & 0 & \dots & n & 0 & 0 \\
t_1 & t_2 & \dots & t_m & B/n & 0 \\
u_1 & u_2 & \dots & u_m & 0 & B
\end{pmatrix}
$$

Di mana $B = 2^{248}$ adalah batas atas (bound) dari $k_i$. Dengan menjalankan algoritma LLL pada matriks ini, kita akan mendapatkan vektor pendek yang mengandung informasi tentang Private Key $d$.

## Solver (SageMath)
```python
import json
from sage.all import *

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

with open("signatures.json", "r") as f:
    data = json.load(f)

sigs = data["signatures"][:50]
ts = []
us = []

for sig in sigs:
    z = int(sig["z"], 16)
    r = int(sig["r"], 16)
    s = int(sig["s"], 16)
    s_inv = pow(s, N - 2, N)
    ts.append((s_inv * r) % N)
    us.append((s_inv * z) % N)

m = len(ts)
B = 2**248

matrix = Matrix(QQ, m + 2, m + 2)
for i in range(m):
    matrix[i, i] = N
    matrix[m, i] = ts[i]
    matrix[m+1, i] = us[i]

matrix[m, m] = B / N
matrix[m+1, m+1] = B

reduced = matrix.LLL()

for row in reduced:
    potential_d = (row[m] * N / B) % N
    if potential_d != 0:
        print(f"Private Key: {hex(int(potential_d))}")
```

**Flag:** `iet{0xdeadbeef1337c0d34b40f4728d321947239482734892734892374892374}`
