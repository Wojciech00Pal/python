import random

N=5 #number of inputs and outputs
r, c = N, N #C column, r-rows
output_reserved=[0 for x in range(N)]
VOQ = [[random.randint(0, 1) for x in range(c)] for y in range(r)] #input data structure
match=[-1 for x in range(N)]


print("VOQ")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in VOQ]))

print("match:")

print('\n'.join(['{:4}'.format(item) for item in match]))

for i in range(N):#row
    for j in range(N):
        if((VOQ[i][j]>0) & (output_reserved[j]==0)):
            match[i]=j
            output_reserved[j]=1
            break

print("match:")
print('\n'.join(['{:4}'.format(item) for item in match]))        

#probbabiliyty P , arrival element in row