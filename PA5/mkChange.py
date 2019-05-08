import numpy as np
import sys

coins = [1,5,10,25]
calls = 0
reads = 0

''' Making Change recursively using the recurrence in the slides '''
# c == d, n == M, n is amount of change, c is the coins index (coin)


def mkChangeDC(n, c):
    global calls
    calls += 1
    
    if c == 0:
        return 1
    
    coinChoices = n // coins[c]
    
    ways = 0 
    for i in range(coinChoices + 1):
        ways += mkChangeDC(n - coins[c]*i, c - 1)
    return ways
  
''' Making Change recursively avoiding the loop in mkChangeDC 
    Based on a different recurrence
'''
def mkChangeDC1(n, c):
    global calls
    calls += 1
    if c == 0:
        return 1
    if c == -1 or n < 0:
        return 0
    
    take = 0
    dontTake = 0
    if n - coins[c] >= 0:
        take += mkChangeDC1(n - coins[c], c)
    if c >= 0:
        dontTake = mkChangeDC1(n, c - 1)
    return take + dontTake


''' Dynamic Programming version of mkChangeDC '''     
def mkChangeDP(n):
    global reads
    refRow = [0 for x in range(n)]
    curRow = [0 for x in range(n)]
    #print("{:3} {}".format("Coin", [x for x in range(n)]))
    for c in range(1, len(coins)):
        for amount in range(n):
            if amount % coins[c - 1] == 0 and c - 1 == 0:
                refRow[amount] = 1
                curRow[amount] = 1
    
            for remainder in range(amount - coins[c], -1, -coins[c]):
                curRow[amount] += refRow[remainder]
                reads += 1
        
        # Output a Table
        '''
        if c == 1: 
            print("-" * (10*3 + 3 + len("Coin [")))
            print("{:4} {}".format(1, [1 for x in range(n)])) 
        
        print("{:4} {}".format(coins[c], curRow))
        '''
        
        refRow = curRow.copy()
    
    
    return curRow[-1]
        
    '''table = [[0 for x in range(n + 1)] for x in range(len(coins))]
    
    for i in range(len(coins)):
        table[i][0] = 1
    
    for i in range(n + 1):
        if i % coins[0] == 0:
            table[0][i] = 1
    print(" -------- Table ------------")
    for value in table:
        print(value)
    
    for i in range(1, n+1):
        for j in range(len(coins)):
            #coinChoices = n // coins[c]
            for numCoins in range(coinChoices + 1):
                # Take
                #print("i, j:", i, j, "element val:", table[i][j], end = ", ")
                table[j][i] = table[j - coins[i]][i] if j-coins[i] >= 0 else 0
                reads += 1
            print()
    return 0 #table[n][len(coins) - 1]
    '''
    

''' Dynamic Programming version of mkChangeDC1 '''     
def mkChangeDP1(cap):
    global reads
    
    waysOfDoingNcents = [0 for x in range(n + 1)]
    waysOfDoingNcents[0] = 1
    
    for c in range(len(coins)):
        coin = coins[c]
        for higherAmount in range(coin, n+1):
            higherAmountRemainder = higherAmount - coin
            waysOfDoingNcents[higherAmount] += waysOfDoingNcents[higherAmountRemainder]
            reads += 2
    

    return waysOfDoingNcents[n]
    
if __name__ == "__main__":
   c = len(coins)-1
   print()
   print("Making change with coins:", coins)

   # performance data: [[n, complexity], ... ]
   dataDC  = []
   dataDC1 = []
   dataDP  = []
   dataDP1 = []
   
   if True:#for n in range(200,2001,200):
      n = 200
      print()
      print("Amount:",n)
      
      
      calls = 0
      ways = mkChangeDC(n,c)
      print("DC", ways, calls)
      dataDC.append([n,calls])
                    
      calls = 0
      ways = mkChangeDC1(n,c)
      print("DC1", ways, calls)
      dataDC1.append([n,calls])
      
      
      reads = 0
      ways = mkChangeDP(n+1)
      print("DP", ways, reads)
      dataDP.append([n,reads])
      
      reads = 0
      ways = mkChangeDP1(n+1)
      print("DP1", ways, reads)
      dataDP1.append([n,reads])
      
   print("dataDC:", dataDC)
   np.savetxt('dataDC', dataDC, delimiter=',', fmt='%d')
   
   print("dataDC1:",dataDC1)
   np.savetxt('dataDC1', dataDC1, delimiter=',', fmt='%d')
   
   print("dataDP:", dataDP)
   np.savetxt('dataDP', dataDP, delimiter=',', fmt='%d')
   
   print("dataDP1:",dataDP1)
   np.savetxt('dataDP1', dataDP1, delimiter=',', fmt='%d')
   
