import hashlib
import random

def generate_proof(private_key):
    proof = hashlib.sha256(private_key.encode()).hexdigest()
    return proof

if __name__ == "__main__":
    private_key = input("Enter your private key: ")
    proof = generate_proof(private_key)
    print(f"Generated proof: {proof}")
