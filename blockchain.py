#imports the Block class from block.py
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()

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
      current_block.print_contents()    
  
  # add block to blockchain `chain`
 def add_block(self, transactions):
    previous_hash = (self.chain[len(self.chain)-1]).hash # we need the previos hash value for new hash value and -1 for length bcoz at 0 there will be genisis block
    new_block = Block(transactions, previous_hash)   #this is the block object from Block class in different .py file
    new_block.generate_hash()                          # new hash is generated
    proof = self.proof_of_work(new_block)           # now whenever we need to add a new block we need proof of work 
    self.chain.append(new_block)
    return proof, new_block

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if(current.hash != current.generate_hash()):          #now this is tricky, well this comes into picture when we feel that someone has tampered with the block and we need to check it, so we again call the generate hash function and compare it with the current or existing hash so if it is tampered the hash value will change
        print("The current hash of the block does not equal the generated hash of the block.")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("The previous block's hash does not equal the previous hash value stored in the current block.")
        return False
    return True
  
  def proof_of_work(self,block, difficulty=2):
    proof = block.generate_hash()
    while proof[:difficulty] != '0'*difficulty: # slice is used which tells the end till we need to check for 0 
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0                             # we need to set it to 0 for other blocks
    return proof
