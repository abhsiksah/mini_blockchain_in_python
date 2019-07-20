# mini_blockchain_in_python
with sha256 hashing and proof of work

regarding line 36 on file blockchain.py
an example to understand better:-

 hash is an instance variable that is created at when the block is instantiated. 
 The method “generate_hash” is called during the comparison and we would expect that 
 these two would not be equivalent, as for one thing the timestamp would be different.
