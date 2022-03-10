import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pylab
import pandas as pd

#global Variables
Ratio=0
Ports=0
spine_sw=0
Server_number=0
log='l'
array = []
presentation='1'
type='0'


#Firs function to get data from user
def ask():
 global Ratio
 global Ports
 global Server_number
 global log
 global presentation
 global type #to pick in range or just specific number
 print("Give me number of Ratio for serwer(?:1): ")
 Ratio=int(input())# "integer given number":1 =>Ratio
 print("Give me number of servers: ")
 Server_number=int(input())
 print("Give me number of PORTS for switches: ")
 Ports=int(input())
 print ("Would you like calculaition for range |OR| only for yor NUMBERS?[1 or 2?]")
 #option 1 will display plot with results(TOR OR SPINE OR cables) for your number of servers
 #2 -> will display only results for your specific amount of servers 
 type=(input())


 if(type=='1'):
  print("Give me letter(l-logarytmic, n ->normal): ")
  # decision over very huge range numbers of servers or normal (server's number+1000) 
  log=input()
 
 two_layer_DC()
 #we have numbers of ratio for computation
 

#2 layer D.C
def two_layer_DC():
    #ports for spine
    if(float(Ports/(Ratio+1))>1):
        #it means we have enough ports to build it
        computation()     
    else:
         print("Port's number is too low for ratio: ",Ratio,":1")
         #sth went wrong, impossible to build dc
  
def computation():
    #ports for spine
    global array
    spine_ports=int(Ports/(Ratio+1))                   #rounding up               
    TOR_number=int(Server_number/(Ports-spine_ports))  #serwers devided by possible connections 
    spine_switches=int(TOR_number/spine_ports)
    cables= Server_number+spine_ports*TOR_number
    print("Server number:",Server_number,"Spine switches:",spine_switches,", TOR: ",TOR_number, ", cables: ",cables)

    array.clear()
    array.append(spine_switches)
    array.append(TOR_number)
    array.append(cables)
    set_values(array)



def set_values(tab):
    #function to assigne to global variables values from array in function computation()
    global spine_sw,tor,cab
    spine_sw=tab[0]
    tor=tab[1]
    cab=tab[2]
   

def plot():
    if(log=='l'):
     end =40 # if we have logarytmic step, it is unnecessary to iterate so much
    else:
     end=1000
        
    i=0
    x=[]
    y=[]
    z=[]
    f=[]
    global Server_number
    global array
    
    while(i<end):
     x.append(Server_number)
     y.append(spine_sw)#diffrent arrays for unassociated variables
     z.append(tor)
     f.append(cab)
     i=i+1
     if(log=='n'):
      Server_number=Server_number+1
     elif(log=='l'):
      Server_number=Server_number+10**i
     else:
      break
     computation()
    # server_increment=server_increment+1
    # ++server_increment
    # Server_number=Server_number+10**i
 
   #ratio still the same
    plt.figure()

    #spine switches number
    plt.plot(x,y,'x',color='orange',linestyle='solid',label="Spine")#this now active
    
    #top of reck->server
    #plt.plot(x,z,'p',linestyle='solid',label="TOR")
 
    #amount of cables
    #plt.plot(x,f,'o',color='green',label="CAB")
   
    if(log=='l'):
     plt.xscale('log')
     plt.yscale('log')
    else:
     plt.yscale('log')

    
    plt.grid(True)
    plt.xlabel('Numbers of server')
    plt.legend()

    plt.show()
    

def graph():
        
    end_tor ='TOR-'+str(array[1])#add number of last TOR
    end_spine='Spine-'+str(array[0])#add number of last Spine
    #fig = plt.plot(figsize=(15, 8))

    relationships = pd.DataFrame({'from': ['TOR',end_tor, 'TOR',end_tor], 
                              'to':       ['Spine',end_spine, end_spine, 'Spine']})
    #connections

    charac = pd.DataFrame({'ID':['TOR',end_tor, 'Spine',end_spine,'n-TOR','n-Spine'], 
                      'type':['T','T', 'S', 'S','T','S']})


    fig = plt.figure()
    G = nx.from_pandas_edgelist(relationships, 'from', 'to', create_using=nx.Graph())

    G.add_node('TOR',pos=(1,1))
    G.add_node('n-TOR',pos=(1,2))
    G.add_node(end_tor,pos=(1,3))
    G.add_node('Spine',pos=(2,0))
    G.add_node('n-Spine',pos=(2,1))
    G.add_node(end_spine,pos=(2,2))

    cnt=0
    for ele in charac.type:
     if ele=='S':#Spine switch should be connected to all TORs
          G.add_edge('n-TOR',charac.ID[cnt])
     elif ele=='T':
          G.add_edge('n-Spine',charac.ID[cnt])
     cnt=cnt+1

    pos=nx.get_node_attributes(G,'pos')

    charac = charac.set_index('ID')
    charac = charac.reindex(G.nodes())

    charac['type'] = pd.Categorical(charac['type'])
    charac['type'].cat.codes

    # Specify colors
    cmap = matplotlib.colors.ListedColormap(['blue', 'darkorange'])
 # Set node sizes
    node_sizes = [3000 if entry != 'T' else 1000 for entry in charac.type]
# Set edgecolors and node_color and node_size for better visibility
    #nx.draw(G, with_labels=True, edgecolors='red', node_color='lightgray', node_size=2000)
    nx.draw(G, pos,with_labels=True, node_color=charac['type'].cat.codes, cmap=cmap, 
     node_size=node_sizes)
    plt.show()


#main
ask()
if(type=='1'):#depends what user chose
 plot()#plot what we need for range in 1000 servers 
else:
 graph()#concrete number from user, only this purpose

