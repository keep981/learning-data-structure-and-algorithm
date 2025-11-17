n = 5

totalPairsCount = ((n-1) * n ) // 2

slowPointer = 0
fastPointer = 0

pairSet = set()
lastPair = None
totalLoopCount = 1

while len( pairSet ) < totalPairsCount:
    if(totalLoopCount == 1000000):
        break
    # print( len(pairSet)  )
    a, b = min( slowPointer, fastPointer ), max( slowPointer, fastPointer )

    pairSet.add( (a, b) )
    
    lastPair = (a, b)
    totalLoopCount+=1
    slowPointer = (slowPointer + 1) % n
    fastPointer = (fastPointer + 2) % n




print(f"totalPairsCount={totalPairsCount}", f"lastPair={lastPair}", f"totalLoopCount={totalLoopCount}"
      , f"pairSet={pairSet}",sep= "\n" )