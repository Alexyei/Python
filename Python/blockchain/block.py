# import datetime library
from datetime import datetime
# import sha256
from hashlib import sha256


# print current date and time
# print(datetime.now())

class Block:
    # default constructor for block class
    #def __init__(self, transactions, previous_hash, nonce=0):
    #    self.timestamp = datetime.now()
    #    self.transactions = transactions
    #    self.previous_hash = previous_hash
    #    self.nonce = nonce
    #    self.hash = self.generate_hash()
    #    pass
    def __init__(self, transactions, previous_hash):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def print_block(self):
        # prints block contents
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)

    def generate_hash(self):
        block_contents = str(self.timestamp)
        block_contents += str(self.transactions)
        block_contents += str(self.previous_hash)

        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()


# text to hash
# text = 'I am excited to learn about blockchain!'
# hash_result = sha256(text.encode())
# print result
# print(hash_result.hexdigest())
