
import random
from random import choices
import sys, select, os

N=5 #number of inputs and outputs
r, c = N, N #C column, r-rows
output_reserved=[0 for x in range(N)]
VOQ = [[random.randint(0, 3) for x in range(c)] for y in range(r)] #input data structure
match=[-1 for x in range(N)]



print("VOQ")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in VOQ]))


max=0
column=-1

#EACH TIME WITH PROBABILITY ONE ELEMENT PER ROW CAN COME

#choosing columns
columns = [0, 1, 2, 3, 4]
weights_columns = [0.2,0.2, 0.4, 0.2, 0.2]

#packet arrives or no
packet_is_or_no=[0,1]
weight_arrive_per_row=[0.1,1.5]


loop=0
while (loop<30):
    
    print("VOQ before Arriving:")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in VOQ]))
    #ARRIVALS
    for r in range(N):
        y_n=int(*choices(packet_is_or_no,weight_arrive_per_row))
        if(y_n==1):# packet arrive per row
            #select column
            VOQ[r][int(*choices(columns,weights_columns))]+=1    #add packet to queue

    print("VOQ after Arriving:")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in VOQ]))

    #SCHEDULER.........:
    #maximal size matching
    for i in range(N):#row
        for j in range(N):#column
            #find maximal
            if((max<VOQ[i][j]) & (output_reserved[j]==0)):#assign
                max=VOQ[i][j]
                column=j
        if(max>0):
         output_reserved[column]=1
         match[i]=column
        max=0

    #Cleaning output_reserved
    for i in range (N):
        output_reserved[i]=0
    loop+=1
    print("match weight maximal after scheduler:")
    print('\n'.join(['{:4}'.format(item) for item in match]))

    #Departures
    for i in range(N):
        if((match[i]>-1) & (VOQ[i][match[i]]>0)):
            VOQ[i][match[i]]-=1



    print("VOQ after sending:")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in VOQ]))
    print("\n Break,....")

    #max size matching
    #for i in range(N):#row
     #   for j in range(N):
      #      if((VOQ[i][j]>0) & (output_reserved[j]==0)):
       #         match[i]=j
        #        output_reserved[j]=1
         #       break


   

    #print("match size maximum:")
    #print('\n'.join(['{:4}'.format(item) for item in match2]))        

    #probabiliyty P, arrival one element in ROW, CHOoSING COLUMN RANdom
    #arrivals =>Update VOQ =>schedulers => matching=> UPDATe VOQ => arrivals
    #time slot for t=o loop
    #ARRIVALS fun() arrival one element in ROW, CHOoSING COLUMN RANdom
    #schedule
    #departures in VOQ =>choosin in match, decrement one

