# Simple Blockchain Implementation

This repository contains a simple implementation of a blockchain, written in Python. The purpose of this project is to provide an educational introduction to the basic concepts of blockchain technology. It demonstrates how blocks are created, validated, and linked together to form a chain, ensuring data integrity.

---

## Features

- **Block Structure**: Each block contains essential fields such as index, timestamp, data, previous hash, and the current hash.
- **Hashing Mechanism**: SHA-256 hashing is used to ensure the integrity of each block.
- **Chain Validation**: The blockchain ensures all blocks are valid and correctly linked.

---

## Prerequisites

- **Python**: Version 3.6 or higher is required to run the code.
- **Libraries**: The implementation uses built-in libraries such as `hashlib`, `datetime`, and `json`. Ensure these are available in your Python environment.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SmruthiRavichandran/Simple_block_chain.git
   cd Simple_block_chain
   ```

2. Ensure you have Python installed. Check the version using:
   ```bash
   python --version
   ```

3. Run the main script:
   ```bash
   python blockchain.py
   ```

---

## File Structure

- **blockchain.py**: Contains the main implementation of the blockchain and its functionalities.
- **README.md**: Documentation for understanding and using the project.

---

## Usage

1. Run the script to create and interact with the blockchain.
2. Add new blocks with your custom data.
3. Observe the proof-of-work mechanism and the hash linkage between blocks.

---

## Example Output

When running the script, you will see outputs similar to the following:

```plaintext
Creating the genesis block...
Block #0 has been added to the blockchain!
Hash: 0000abcd1234...

Adding a new block...
Block #1 has been added to the blockchain!
Hash: 0000efgh5678...
```

This output illustrates the creation of the genesis block and subsequent blocks in the chain.

---

## How It Works

1. **Genesis Block**: The first block in the chain is created manually with a predefined hash.
2. **Adding New Blocks**:
   - A new block is created with data provided by the user.
   - The block's hash is calculated based on its contents and the hash of the previous block.
3. **Validation**: The chain is validated to ensure the integrity of all blocks.

---

## Concepts Demonstrated

- **Blockchain Basics**: Understanding block structure and chaining mechanism.
- **Cryptographic Hashing**: Using SHA-256 to ensure block immutability.
- **Proof of Work**: Simulating mining by solving computational puzzles.
- **Chain Integrity**: Verifying that the chain is valid and tamper-proof.

---

## Contributions

Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests to improve the project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Smruthi Ravichandran  
For any queries or suggestions, please contact me via [GitHub](https://github.com/SmruthiRavichandran).

---
