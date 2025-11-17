# class A(object):
#     def __init__(self) -> None:
#         self.age = 25
    
#     @classmethod
#     def greetFrom(cls, name):
#         print(f"Hi {name}! how is your day")
    
#     def work(self):
#         print(f"I am working very hard at age {self.age}")
#         self.greetFrom("michael")


# x = A()
# x.greetFrom("gudu")
# x.work()

from functools import cmp_to_key

points = [[3,3],[5,-1],[-2,4]]
print(points)
points.sort(  )

def customComparator(po1, po2):
    if (po1[0]**2 + po1[1]**2) <= (po2[0]**2 + po2[1]**2):
        return -1
    else:
        return 1 

points.sort( key = cmp_to_key(customComparator), reverse=True )

print(points)