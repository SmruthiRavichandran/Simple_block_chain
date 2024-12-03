from Crypto.Hash import SHA256
#data class

# Define the Block
class Block:
    def __init__(self, transaction_data, previous_hash=""):
        self.transaction_data = transaction_data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        data_to_hash = (self.previous_hash + self.transaction_data).encode()
        hash_obj = SHA256.new(data_to_hash)
        return hash_obj.hexdigest()

# Define the Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_first_block()]

    def create_first_block(self):
        return Block("First Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_transaction_data):
        latest_block = self.get_latest_block()
        new_block = Block(new_transaction_data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Verify the hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Verify the previous hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True
        #return print("yes, the block chain is valid")
        


# calling main fumction
if __name__ == "__main__":
    my_blockchain = Blockchain()#--> object creation/ instance of a class

    # Adding blocks
    my_blockchain.add_block("Transaction 1: Smruthi pays Arjun 10 BTC")# --> method calling of a class from the object
    my_blockchain.add_block("Transaction 2: Arjun pays Samuel 5 BTC")
    my_blockchain.add_block("Transaction 3: Samuel pays Smruthi 2 BTC")

    # Displaying the blockchain
    for i, block in enumerate(my_blockchain.chain):
        print(f"Block {i}:")
        print(f"  Transaction Data: {block.transaction_data}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Hash: {block.hash}")
        print()
        print

    # Validating the chain
    print("Is blockchain valid?", my_blockchain.is_chain_valid())
