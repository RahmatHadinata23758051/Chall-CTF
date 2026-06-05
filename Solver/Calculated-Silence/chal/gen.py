import json
import secrets
from hashlib import sha256

# secp256k1 parameters
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
A = 0
B = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

def inv(a, n):
    return pow(a, n - 2, n)

def point_add(P1, P2):
    if P1 is None: return P2
    if P2 is None: return P1
    x1, y1 = P1
    x2, y2 = P2
    if x1 == x2 and y1 != y2: return None
    if x1 == x2:
        m = (3 * x1 * x1 + A) * inv(2 * y1, P)
    else:
        m = (y2 - y1) * inv(x2 - x1, P)
    x3 = (m * m - x1 - x2) % P
    y3 = (m * (x1 - x3) - y1) % P
    return (x3, y3)

def point_mul(P1, k):
    res = None
    base = P1
    while k:
        if k & 1:
            res = point_add(res, base)
        base = point_add(base, base)
        k >>= 1
    return res

def generate_challenge():
    # Private Key
    # iet{d34db33f_1337_c0de_dead_beef}
    priv_key = 0xdeadbeef1337c0d34b40f4728d321947239482734892734892374892374
    G = (Gx, Gy)
    pub_key = point_mul(G, priv_key)
    
    signatures = []
    
    for i in range(100):
        # Biased nonce k: top 8 bits are zero
        k = secrets.randbits(248) 
        
        msg = f"Transaction #{i}".encode()
        z = int(sha256(msg).hexdigest(), 16)
        
        k_inv = inv(k, N)
        R = point_mul(G, k)
        r = R[0] % N
        s = (k_inv * (z + r * priv_key)) % N
        
        signatures.append({
            "z": hex(z),
            "r": hex(r),
            "s": hex(s)
        })
        
    data = {
        "curve": "secp256k1",
        "pub_key": {"x": hex(pub_key[0]), "y": hex(pub_key[1])},
        "signatures": signatures
    }
    
    with open("signatures.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Signatures generated.")

if __name__ == "__main__":
    generate_challenge()
