# import sha256
from hashlib import sha256

new_transactions = [{'amount': '30', 'sender': 'alice', 'receiver': 'bob'},
                    {'amount': '55', 'sender': 'bob', 'receiver': 'alice'}]
# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0
iteration = 0
# creating the proof
proof = str(nonce) + str(new_transactions)
# printing proof
hash_value = sha256(proof.encode()).hexdigest()
# print(hash_value)
# finding a proof that has 2 leading zeros
while hash_value[:difficulty] != '0' * difficulty:
    print(hash_value)
    nonce += 1
    iteration += 1
    proof = str(nonce) + str(new_transactions)
    hash_value = sha256(proof.encode()).hexdigest()
# printing final proof that was found
final_proof = hash_value
print(final_proof)
print(iteration)
