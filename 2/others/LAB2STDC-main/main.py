# A Program to design a data center with leaf and spine topology takes as an input
# oversubscribtion ratio and size of Tor and Spine switches which are symmetric
import matplotlib.pyplot as plt
import numpy as np

# oversubscription ratio is between network capacity and server capacity
a, b = input("Input oversubscription ratio in form a b: ").split()
c, d = input("Input number of ports of leaf switches and of spine switches in form a b: ").split()
# convert all values to integer
a = int(a)
b = int(b)
c = int(c)
d = int(d)
# n/N=b/a provided above where I considered all interfaces have same speed that is 1gb/s
# so n= N*b/a and we know that n+N=c where c is size for switch
# so (1+b/a)N=c so N=c/(1+b/a) but we round it
insw = b / a
# round to get nearest value insw is port toward spine
insw = round(c / (insw + 1))
# inss is number of ports toward server
inss = c - insw
# numla is number of ports of spine switch equal to number of leaf switches
numLa = d
# tot is total number of spine and leaf switches
tot = numLa + insw
# tots is total number of server
tots = d * c
print("Number of switches in total is: " + str(tot))
print("Number of spine switches is: " + str(insw))
print("Number of leaf switches is: " + str(numLa))
a = input("press 1 to print total number of switches as function of number of servers: ")
a = int(a)
if a:
    fig, ax = plt.subplots()
    s = np.linspace(2, 10000, 10)
    L = (2 + np.log2(inss) - np.log2(numLa) - np.log2(s)) / (1 - np.log2(numLa))
    Cs = ((numLa ** (L - 1)) + (2 * L - 3) * insw * (numLa ** (L - 2))) / (2 ** (L - 2))
    Css = (insw * (numLa ** (L - 2))) / (2 ** (L - 2))
    Csl = Cs-Css
    ax.plot(s, Cs)
    ax.plot(s, Css)
    ax.plot(s, Csl)
    ax.legend(['total switches', 'Spine switches', 'leaf switches'])
    plt.xlabel("Number of Servers 'S'")
    plt.ylabel("Number of switches")
    plt.show()
else:
    print("Finished!")
