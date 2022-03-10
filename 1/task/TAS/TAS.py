import math 
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
import networkx as nx

#Cost benes network 2x2 modules


def Computaition(a):
    a=int(a)
    if a>2:
       return a/2+2*Computaition(a/2)+a/2
    else:
       return 1

##start, ask for N
def ask():
    print("Give me number of inputs: ")
    insert()
   
##Wrong number N
def ask_if_wrong_number():
    print("Wrong input's number, it should be two to the power N")
    ask()

#Download the number from user
def insert():
    N=int(input())
    Y_N = bool(check_the_power_of_two(N))

    if Y_N==True:
         r=Computaition(N)
         print("Result: ")
         print(r)
         
    else:
        ask_if_wrong_number()
        
def check_the_power_of_two(a):
    return math.log2(a).is_integer()







       
      
def Benes_Network_Plot():

    x = np.arange(9)
    x=[1,2,3,4,5,6,7,8,10]

    x=np.power(2,x)

    y=[]

    for i in x:
        y.append(Computaition(int(i)))
    
    
    plt.figure();
    plt.plot(x,y,'go')
    plt.plot(x,y,'b')
    plt.grid(True)
    plt.ylabel('Number on 2x2 modules')
    plt.xlabel('Number of inputs N')
    plt.show()
 
    
Benes_Network_Plot() 
while True:
    ask()

    print("Close window to shut down progamm, OR")


