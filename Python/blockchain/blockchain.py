# imports the Block class from block.py
from block import Block
from hashlib import sha256

class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    # def genesis_block(self):
    #    gen_block = Block([], 0)
    #    self.chain.append(gen_block)
    #    pass

    def genesis_block(self):
        transactions = {}
        genesis_block = Block(transactions, "0")
        self.chain.append(genesis_block)
        return self.chain

        # prints contents of blockchain

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_block()

    def add_block(self, transactions):
        new_block = Block(transactions, self.chain[-1].hash)
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("Error! The current hash of the block does not equal the generated hash of the block.")
                return False
            if current.previous_hash != previous.generate_hash():
                print("Error! The previous block's hash does not equal the previous hash value stored in the current "
                      "block.")
                return False
        return True

    #def proof_of_work(self, block, difficulty=2):
    #    proof = block.generate_hash()
    #   while proof[:difficulty] != '0' * difficulty:
    #        block.nonce += 1
    #        proof = block.generate_hash()
    #    block.nonce = 0
    #    return proof
    def proof_of_work(self, block, difficulty=2):
        proof = str(block.nonce) + str(block.transactions)
        hash_value = sha256(proof.encode()).hexdigest()
        while hash_value[:difficulty] != '0' * difficulty:
            block.nonce += 1
            proof = str(block.nonce) + str(block.transactions)
            hash_value = sha256(proof.encode()).hexdigest()
        block.nonce = 0
        return proof
