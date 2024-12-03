from Crypto.Hash import SHA256
from dataclasses import dataclass

#crypto_chain = []
#data class
@dataclass
class block:
    transaction_data: str
    current_hash: str
    previous_hash : str
        
    @staticmethod
    def calculate_hash(data: str) -> str:
        return SHA256.new(data.encode()).hexdigest()

    
#creating the block chain inside the blockchain class
# Define the Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_first_block()]

    def create_first_block(self):#genesiss block
        transaction_data = "First Block"
        previous_hash = "0"  # Genesis block's previous hash
        current_hash = block.calculate_hash(transaction_data + previous_hash)
        return block(transaction_data, current_hash, previous_hash)

    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, transaction_data):
        latest_block = self.get_latest_block()
        previous_hash = latest_block.current_hash
        current_hash = block.calculate_hash(transaction_data + previous_hash)
        new_block = block(transaction_data, current_hash, previous_hash)
        self.chain.append(new_block)


    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Verify the hash
            if current_block.current_hash != block.calculate_hash(
                current_block.transaction_data +current_block.previous_hash):
                return False

            # Verify the previous hash
            if current_block.previous_hash != previous_block.current_hash:
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
        print(f"  Hash: {block.current_hash}")
        print()
        print()

    # Validating the chain
    print("Is blockchain valid?", my_blockchain.is_chain_valid())