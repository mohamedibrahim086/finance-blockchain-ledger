import hashlib
import json
from time import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': ''
        }
        block['hash'] = self.hash_block(block)
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time()
        }
        self.pending_transactions.append(transaction)
        return transaction

    def hash_block(self, block):
        block_copy = block.copy()
        block_copy['hash'] = ''
        block_string = json.dumps(block_copy, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_chain(self):
        return self.chain


# Create blockchain instance
ledger = Blockchain()

# Add some financial transactions
ledger.add_transaction(sender='Alice', receiver='Bob', amount=100)
ledger.add_transaction(sender='Bob', receiver='Charlie', amount=50)

# Mine a block (confirm transactions)
ledger.create_block(previous_hash=ledger.chain[-1]['hash'])

# Add more transactions
ledger.add_transaction(sender='Charlie', receiver='Diana', amount=25)

# Mine next block
ledger.create_block(previous_hash=ledger.chain[-1]['hash'])

# Display full blockchain ledger
import pprint
pprint.pprint(ledger.get_chain())
