import hashlib

class CoinBlock:
    def __init__(self, previousBlockHash, transactionList):
        self.previousBlockHash = previousBlockHash
        self.transactionList = transactionList

        self.blockData = "-".join(transactionList) + "-" + previousBlockHash
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()

# list of transactions: in this code example, strings are used instead of real transactional values
t1 = "A sends 2 coins to B"
t2 = "C sends 4.1 coins to B"
t3 = "B sends 3.2 coins to C"
t4 = "D sends 0.3 coins to E"
t5 = "B sends 1 coins to F"
t6 = "B sends 5.4 coins to D"

# testing the blockchain by creating blocks and hashes

initialBlock = CoinBlock("Initial String", [t1, t2]) #taking two transactions per block

print(initialBlock.blockData)
print(initialBlock.blockHash)

secondBlock = CoinBlock(initialBlock.blockHash, [t3,t4])

print(secondBlock.blockData)
print(secondBlock.blockHash)

thirdBlock = CoinBlock(secondBlock.blockHash, [t5,t6])

print(thirdBlock.blockData)
print(thirdBlock.blockHash)