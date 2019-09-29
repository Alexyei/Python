# import datetime library
from datetime import datetime
# import sha256
from hashlib import sha256

transaction1 = {
    'amount': '30',
    'sender': 'Alice',
    'receiver': 'Bob'}
transaction2 = {
    'amount': '200',
    'sender': 'Bob',
    'receiver': 'Alice'}
transaction3 = {
    'amount': '300',
    'sender': 'Alice',
    'receiver': 'Timothy'}
transaction4 = {
    'amount': '300',
    'sender': 'Rodrigo',
    'receiver': 'Thomas'}
transaction5 = {
    'amount': '200',
    'sender': 'Timothy',
    'receiver': 'Thomas'}
transaction6 = {
    'amount': '400',
    'sender': 'Tiffany',
    'receiver': 'Xavier'}

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

# add your code below
my_transaction = {
    'amount': '400',
    'sender': 'Tim',
    'receiver': 'Mike'
}

mempool.append(my_transaction)

block_transactions = mempool[1:4]

# print current date and time
print(datetime.now())


class Block:
    # default constructor for block class
    def __init__(self, transactions, previous_hash, nonce=0):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()
        pass

    def print_block(self):
        # prints block contents
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())

    def generate_hash(self):
        block_contents = str(self.timestamp)
        block_contents += str(self.transactions)
        block_contents += str(self.previous_hash)

        block_hash = sha256(block_contents.encode())

        return block_hash.hexdigest()
        pass


# text to hash
text = 'I am excited to learn about blockchain!'
hash_result = sha256(text.encode())
# print result
print(hash_result.hexdigest())
