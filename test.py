import math

pkts = [12,16,9,10,31,52]
powers = []
toAdd = 0
toAddList = []

for pkt in pkts:
    pkt += toAdd
    power = math.floor(math.log2(pkt))
    powers.append(power)
    toAdd = pkt - 2 ** power
    toAddList.append(toAdd)
    
print(powers, toAddList)
