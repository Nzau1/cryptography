import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, proof_of_personhood):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.proof_of_personhood = proof_of_personhood
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.proof_of_personhood)
        return hashlib.sha256(data_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block", "Genesis User")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block, proof_of_personhood):
        # Perform basic proof-of-personhood verification
        if proof_of_personhood == new_block.data:
            new_block.previous_hash = self.get_latest_block().hash
            new_block.hash = new_block.calculate_hash()
            self.chain.append(new_block)
        else:
            print("Proof of personhood verification failed. Block not added.")

# Create a new blockchain
my_blockchain = Blockchain()

# Add some transactions with proof-of-personhood
my_blockchain.add_block(Block(1, my_blockchain.get_latest_block().hash, int(time.time()), "Transaction 1", "User1"), "User1")
my_blockchain.add_block(Block(2, my_blockchain.get_latest_block().hash, int(time.time()), "Transaction 2", "User2"), "User2")

# Attempt to add a block with incorrect proof-of-personhood
my_blockchain.add_block(Block(3, my_blockchain.get_latest_block().hash, int(time.time()), "Transaction 3", "User3"), "User4")

# Print the blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index} - Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Proof of Personhood: {block.proof_of_personhood}")
    print("\n")
