import random

N=5 #number of inputs and outputs
r, c = N, N #C column, r-rows
output_reserved=[0 for x in range(N)]
output_reserved2=[0 for x in range(N)]
VOQ = [[random.randint(0, 3) for x in range(c)] for y in range(r)] #input data structure
match=[-1 for x in range(N)]
match2=[-1 for x in range(N)]


print("VOQ")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in VOQ]))

print("match:")
print('\n'.join(['{:4}'.format(item) for item in match]))

max=0
column=-1

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
   

#max size matching
for i in range(N):#row
    for j in range(N):
        if((VOQ[i][j]>0) & (output_reserved2[j]==0)):
            match2[i]=j
            output_reserved2[j]=1
            break



print("match weight maximal:")
print('\n'.join(['{:4}'.format(item) for item in match]))        

print("match size maximum:")
print('\n'.join(['{:4}'.format(item) for item in match2]))        

#probabiliyty P, arrival one element in ROW, CHOoSING COLUMN RANdom
#arrivals =>Update VOQ =>schedulers => matching=> UPDATe VOQ => arrivals
#time slot for t=o loop
#ARRIVALS fun() arrival one element in ROW, CHOoSING COLUMN RANdom
#schedule
#departures in VOQ =>choosin in match, decrement one

