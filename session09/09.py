# function repeats 10 times. Each:roll 100dice and print the sum
import random
# def roll():
#     result=0
#     for i in range (10):
#         for i in range(100):
#             d=random.randint(1,6)
#             result += d
#     return result

# print (roll())

import random
def roll():
    for i in range (10):
        result=0
        for i in range(100):
            d=random.randint(1,6)
            result += d
    return result

print (roll())

# r+=i
# r= oldr +i


# if __name=='__main__':
#     main()
# result=0
# def stimulate():
#     for i in range(100):
#             d=random.randint(0,6)
#             result =+ d
#     return result

# def repeat():
#     for i in range(10):
#         stimulate()



        
