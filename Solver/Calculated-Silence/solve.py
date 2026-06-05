import json

# This script would normally be run in SageMath.
# ECDSA HNP (Hidden Number Problem) via LLL.

# N (secp256k1 order)
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

def solve():
    with open("../../Calculated-Silence/signatures.json", "r") as f:
        data = json.load(f)
    
    sigs = data["signatures"]
    
    # ECDSA: s = k^-1 * (z + r*d) (mod N)
    # k = s^-1 * z + s^-1 * r * d (mod N)
    # k - s^-1 * r * d = s^-1 * z (mod N)
    
    # We have k_i = t_i * d + u_i (mod N)
    # where t_i = s_i^-1 * r_i (mod N)
    # and u_i = s_i^-1 * z_i (mod N)
    # and k_i is small (248 bits instead of 256 bits, so k_i < N/2^8)
    
    # LLL Matrix Construction:
    # [ N  0  0 ... 0 ]
    # [ 0  N  0 ... 0 ]
    # [ ...           ]
    # [ t1 t2 t3 .. 2^-8 * N ] (Wait, this is the standard HNP matrix)
    
    # Since I cannot run SageMath here, I will provide the script as a reference.
    print("Solver script for SageMath:")
    print("-" * 20)
    print("""
import json

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

with open("signatures.json", "r") as f:
    data = json.load(f)

sigs = data["signatures"][:50] # 50 is enough
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
# LLL matrix
# k_i - t_i*d = u_i (mod N)
# k_i = t_i*d + u_i + N*X_i
matrix = Matrix(QQ, m + 2, m + 2)
for i in range(m):
    matrix[i, i] = N
    matrix[m, i] = ts[i]
    matrix[m+1, i] = us[i]

# Bounds
B = 2^248
matrix[m, m] = B / N
matrix[m+1, m+1] = B

# LLL reduction
reduced = matrix.LLL()

for row in reduced:
    # potential d is at row[m]
    # (Simplified, need to check properly)
    potential_d = (row[m] * N / B) % N
    # Verify with pub key...
    print(hex(int(potential_d)))
    """)

if __name__ == "__main__":
    solve()
