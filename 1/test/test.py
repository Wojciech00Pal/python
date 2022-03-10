import numpy as nmp
import matplotlib.pyplot as plt

# Building block has same number of inputs and outputs
m = int(input("Give size of basic building block:"))
# possible to be nonsymetric
N, M = input("Give size of clos network provide two numbers:").split()
G = int(N)
srlist = [int(N)]
yallist = []


listed = range(30, 1000, 50)
srlist.extend(listed)
srlist = sorted(srlist)
for N in srlist:
    # Convert to integer
    N = int(N)
    M = int(M)
    # define an empty list
    mist = []
    # q1 and q2 used for iteration they store size of new clos network to build replace N and M variables
    q1 = N
    q2 = M
    # summa a variable to store final number of basic unit start from zero
    summa = 0
    # keep iterating
    while True:
        # check if input and output of new clos network is smaller than size of basic block
        if q1 <= m and q2 <= m:
            # for last clos network from iteration divide a whole module by taking
            # max size between input and output of clos network and divide by m size of basic block
            # eg. C(4,5) and m=10 => q1=(max(4,5)/10)=1/2
            q1 = float(max(q1, q2) / m)
            # add value to list and break because it will be the last clos network
            mist.append(q1)
            break
        else:
            # q1 and q2 if greater one or both from m we divide both by m and take whole number
            # not fraction considering whole network at start at end a fraction
            # eg. C(10,10) and m=3 => q1=4 and q2=4
            q1 = int(nmp.ceil(q1 / m))
            q2 = int(nmp.ceil(q2 / m))
            # add both values to list
            mist.append(q1)
            mist.append(q2)

    # Getting length of list
    length = len(mist)
    i = int(0)
    # Iterating using while loop till value before last because has diff form
    while i < length - 1:
        # formula C(N)=N/m*C(m)+M/m*C(m)+mC(N/m,M/m)
        # C(q1,q2)=q1/m*C(m)+q2/m*C(m)+mC(q1/m,q2/m)
        # mist[i] and mist[i+1] are q1 and q2 multiply by m power i/2 by formula
        summa = summa + (int(mist[i]) + int(mist[i + 1])) * m ** (i / 2)
        # move two steps
        i += 2
    # for last we have one value only multiplied by power of base m
    summa = summa + mist[length - 1] * m ** ((length - 1) / 2)
    yallist.append(summa)
    # Only print output of input value
    if N == G:
        print("number of modules of your input  is:" + str(summa))
plt.plot(srlist, yallist, 'b+')
plt.ylabel("Number of modules")
plt.xlabel("Input size of Clos Network")
plt.title("Number of modules as function of input of Clos Network")
plt.show()
