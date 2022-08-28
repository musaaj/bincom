from random import randint

binary = ""

for i in range(4):
    binary += str(randint(0,1))


decimal = int(binary,2)

print("{0} in binary is {1} in decimal".format(binary, decimal))
