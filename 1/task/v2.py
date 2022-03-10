import sys
from math import *

if __name__ == '__main__':

    #N and M are the total size of the network and p is the size of the basic building block
    #network_type is the type of netowrk (SNB or REAR)
    N=int(sys.argv[1])
    M=int(sys.argv[2])
    p=int(sys.argv[3])
    network_type=sys.argv[4]
    # my graph is a dictionnary
    network={}

    #here I calcul the number of module of the first and the third column
    r1= ceil(N/p)
    r3= ceil(M/p)

    #here I put on my dictionnary all the module of the first and third column (a is the first one and c the third one)
    # the list is for all the node who will be connect after
    for i in range (r1):
        network.update({'a'+ str(i+1):[]})
    for j in range (r3):
        network.update({'c'+str(j+1):[]})

    # I have made two scenario, one if you want a rearangable network et one if you want a SNB network
    if network_type == 'REAR':
        #here i calcul the lenght of the central column for a rearangeable network
        r2= p
        for k in range(r2):
            # here I put the module of my second column(b) in my dictionnary
            network.update({'b'+str(k+1): []})
            #here I put the module who are connected to the current module on the list associated to it
            for test in range (r1):
                network['a'+str(test+1)].append('b'+str(k+1))
                network['b' + str(k+1)].append('a' + str(test+1))
            for test1 in range (r3):
                network['c'+str(test1+1)].append('b'+str(k+1))
                network['b' + str(k+ 1)].append('c' + str(test1+1))


    elif network_type == 'SNB':
        # here i calcul the lenght of the central column for an SNB network
        r2= 2*p-1
        for l in range(r2):
            network.update({'b'+ str(l+1): []})

            for test2 in range(r1):
                network['a' + str(test2+1)].append('b' + str(l+1))
                network['b' + str(l+1)].append('a' + str(test2+1))

            for test3 in range(r3):
                network['c' + str(test3+1)].append('b' + str(l+1))
                network['b' + str(l+1)].append('c' + str(test3+1))
    else:
        print('error of network type ')
    print(network)
    #the number of module of my clos network correspond to the lenght of my dictionnary (graph)
    number_of_modules= len(network)
    print('number of modules: ' + str(number_of_modules))

