import hashlib

class isacaCoinBlock:
    def __init__(self, previousBlockHash, transactionList):
        self.previousBlockHash = previousBlockHash
        self.transactionList = transactionList

        self.blockData = "-".join(transactionList) + "-" + previousBlockHash
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()

t1 = "Shamik sends 1 IC to Jacob"
t2 = "Bryce sends 1.5 IC to Paige"
t3 = "Paige sends 9.3 IC to Jake"
t4 = "Jake sends 0.2 IC to Shamik"
t5 = "Jacob sends 1.12 IC to Paige"
t6 = "Shamik sends 13.2 IC to Bryce"

initialBlock = isacaCoinBlock("Initial String", [t1, t2])

print(initialBlock.blockData)
print(initialBlock.blockHash)

secondBlock = isacaCoinBlock(initialBlock.blockHash, [t3, t4])

print(secondBlock.blockData)
print(secondBlock.blockHash)

thirdBlock = isacaCoinBlock(secondBlock.blockHash, [t5, t6])

print(thirdBlock.blockData)
print(thirdBlock.blockHash)