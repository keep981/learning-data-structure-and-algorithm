# x = [12, 67, 78]

# x[0], x[1] = x[1], x[0]
# print(x)
# print( -7 //2 )

from MyMinHeap import MyMinHeap


mh = MyMinHeap.buildMinHeapFromList( [4,1,2,6,7,8] )
print(mh.data)

# mh  = MyMinHeap()


# mh.insert(4)
# mh.insert(1)
# mh.insert(2)
# mh.insert(6)
# mh.insert(7)
# mh.insert(3)
# mh.insert(8)
# mh.insert(5)
# print("Min value is", mh.getMin(), sep="=" )
# mh.insert(-1)
# print("Min value is", mh.getMin(), sep="=" )
# mh.decreaseKey(3, -2)
# print("Min value is", mh.getMin(), sep="=" )
# mh.extractMin()
# print("Min value is", mh.getMin(), sep="=" )
# mh.delete(0)
# print("Min value is", mh.getMin(), sep="=" )
