import hashlib

def verify_proof(stored_proof, input_proof):
    return stored_proof == input_proof

if __name__ == "__main__":
    stored_proof = input("Enter stored proof: ")
    input_proof = input("Enter proof to verify: ")
    if verify_proof(stored_proof, input_proof):
        print("Proof is valid.")
    else:
        print("Invalid proof.")
