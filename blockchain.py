#Module 1 - Create a blockchain 
import datetime
import hashlib
import json
from flask import Flask, jsonify

#create a blockchain
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, prev_hash= '0')
        
    def create_block(self, proof, prev_hash):
        block = {'index' : len(self.chain) + 1,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'prev_hash' : prev_hash
                 }
        self.chain.append(block)
        return block
    
    def get_prev_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, prev_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str((new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
     
        
    def is_chain_valid(self, chain):
        prev_block = chain[-1]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['prev_hash' ] !=  self.hash(previous_hash):
                return False
            prev_proof = prev_block['proof']
            proof = block['proof'] 
            hash_operation = hashlib.sha256(str((proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            prev_block = block
            block += 1
        return True
        
        
#mine a blockchain

#Create a web app
app = Flask(__name__)

#Create a blockchain











