#..........Week 04 ..........
#..........Lecture 4.2...... (Warmup with Lists)


l=[1,2,4,34,100]     # Learn List and its function append ,remove,etc
print(l)
l.append(230)
print(l)
l.remove(2)
print(l)
l.append(2)
print(l)
l=[]
l.append(2)
l.append(3)
l.append(4)
print(l)

x=[]
x.append(l)
print(x)

m=[2,4,78]           # list in list
x.append(m)
print(x)

t=[]
t.append(x)
print(t)

t.append([34,678,2334,45])
print(t)
print(t[0])

M=[]           # form a matrix
M.append([11,2,4,])
M.append([27,72,5,])
M.append([34,3,48,])
print(M)
print(M[0])
print(M[0][0])
print(M[0][1])
print(M[0][2])

print(M[0][0])    #element of dialong on matrix
print(M[1][1])
print(M[2][2])


#..........Lecture 4.3...... (Birthday Paradox)

print(random, random)
l=[]
l.append(random.random())
print(l)
l.append(random.random())
print(l)


for i in range(10):
  l.append(random.random())
  
print(l)


for i in range(100):
  l.append(random.randint(1,10))
  
print(l)

# now we Simulate an experiment to verify the birthday paradox.
import random

l=[]

for i in range(50):
  l.append(random.randint(1,365))
  #append random numbers between 1 to 365
  #append 30 of them
l.sort()  
print(l)
i=0
flag=0   # denotes thatthere is no repetition
while(i<=len(l)-1):
  if (l[i]==l[i+1]):
    print("Repeats",l[i], l[i+1])
    flag=1
    break
  i=i+1

if (flag==0):
  print("There is no repeation")


#..........Lecture 4.4...... (Naive Search in a List)


l = [2,234,56,33,97,345]

import random

for i in range(10000):
  l.append(random.randint(1,1000000))
print(l)

#...............
l = []

for i in range (100):
  i.append(random.randint(1,1000000))
print(l)

print(l[0])
print(l[1])
print(len(l)-1)
#...............
import random

l = []

for i in range (100):
  i.append(random.randint(1,1000000))
print(l)
flag=0
for i in range(len(l)):
  if (a==l[i]):
    print("Hip Hip hurray, element found")
    flag=1
    break;
if (flag==0):
  print("Element not found")

#...............

l = [22,23454,68865,2434688,5455,33]
a=2434688

flag=0

for i in range(len(l)):
  if (a==l[i]):
    print("Hip Hip hurray, element found")
    flag=1
    break
if (flag==0):
  print("Element not found")

#...............


import random

a=5674
l=[]

for i in range (10000000):
  i.append(random.randint(1,100000000))

flag=0

for i in range(len(l)):
  if (a==l[i]):
    print("Hip Hip hurray, element found")
    flag=1
    break;
if (flag==0):
  print("Element not found")

#......................

import random

l=[]
for i in range(10000):
  l.append(random.randint(1,100000))

n=0
while (n>-1):
  print("Enter a number, type -1 to exit: ")
  n=int(input())

  flag=0

  for i in range(len(l)):
    if (n==l[i]):
      print("Hip Hip hurray, element found")
    flag=1
    break
  if (flag==0):
    print("Element not found")

#..............

import random

l=[]

l=[2001,1990,1981,2003,19973]

n=0
while (n>-1):
  print("Enter a number, type -1 to exit: ")
  n=int(input())

  flag=0

  for i in range(len(l)):
    if (n==l[i]):
      print("Hip Hip hurray, element found")
    flag=1
    break
  if (flag==0):
    print("Element not found")

#..........Lecture 4.5...... (The Obvious Sort)

l=[12,24,67,5,245,38,6,2343,]
l.sort()
print(l)

#...........

l=[12,24,67,5,245,38,6,2343,23443,3,6534,12,9087,3,2455,33]
#let us write a piece of code for explaination
x=[]  

while(len(l)>0):      #sort element from list and append and remove not by using sort function of list
  min=l[0]
  for i in range(len(l)):
    if l[i]<min:
      min=l[i]
  x.append(min)
  l.remove(min)

print(l)
print(x)


#..........Lecture 4.6...... (Dot Product)

l=[1,3,5,78,33,23,12,78,5,44,8,2]
sum=0
for i in range(len(l)):
  sum+=l[i]

print(sum
     
#...........
      
import random

l=random.sample(list(range(10000)),1000)
sum=0
for i in range(len(l)):
  sum+=l[i]

print(sum)

#...........

# write a picec of code to find the dot product.

x=[1,7,3,4]
y=[2,3,5,2]

dot_product=(1*2)+(7*3)+(3*5)+(4*2)
print(dot_product)

#...........
# write a picec of code to find the dot product.

x=[1,7,3,4,3,44,2,245,67,]
y=[2,3,5,2,35,67,53,35,56]

#for more element  use for loop
sum=0
for i in range(len(x)):
  sum=sum+x[i]*y[i]
  
print(sum)


#..........Lecture 4.7...... (Matrix Addition)

# Matrix addition by first principles(?)

dim=3

r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,3,2]
s3 = [4,2,1]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

B=[]
B.append(s1)
B.append(s2)
B.append(s3)


print(A)
print(B)

# I need to add A and B

C=([0,0,0],[0,0,0],[0,0,0])
for i in range (dim):
  for j in range(dim):
    C[i][j]=A[i][j]+B[i][j]
print(C)

#...............

dim=4        # dimension of matrix 4x4

r1 = [1,2,3,2]
r2 = [4,5,6,3]
r3 = [7,8,9,4]
r4 = [3,4,56,12]

s1 = [1,2,1,4]
s2 = [6,3,2,12]
s3 = [4,2,1,10]
s4 = [3,45,5,32]

A=[]     # make matrix A
A.append(r1)
A.append(r2)
A.append(r3)
A.append(r4)

B=[]      # make matrix B
B.append(s1)
B.append(s2)
B.append(s3)
B.append(s4)

print(A)
print(B)

# I need to add A and B

C=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
for i in range (dim):
  for j in range(dim):
    C[i][j]=A[i][j]+B[i][j]
print(C)

#..........Lecture 4.8...... (Matrix Multiplication - 1)

'''
In python, Matrix row and column start with 0 row and column
matrix C are formed by multiplation of matrix A and B
Matric C element C[0][0] are just a Dot_product of Matric A row 0 and Matrix B row 0
simiplarity other


 now C[3][2] = A[3][0].B[0][2] + A[3][1].B[1][2] + A[3][2].B[2][2] +........
 
'''

#..........Lecture 4.9...... (Matrix Multiplication - 2)


dim=3

r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,3,2]
s3 = [4,2,1]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

B=[]
B.append(s1)
B.append(s2)
B.append(s3)


print(A)
print(B)

# I need to add A and B

C=([0,0,0],[0,0,0],[0,0,0])

# C [i][j] is the dot produt of the ith row A and the jth column of B

# C [2][1] is the dot produt of the 2th row A and the 1th column of B

for i in range(dim):
  for j in range(dim):
    for k in range(dim):
      # C[i][j]=dot_product of A[i][j] and B[i][j]
      # C[i][j]=dot_product of A[i][.... ] and B[i][.... ]
      C[i][j] = C[i][j] + A[i][k] * B[k][j]
    
print(C)
# chekc now
print((1*1) + (2*6) + (3*4))
# chekc by numpy libraris
import numpy
X = numpy.mat(A)
Y = numpy.mat(B)
print(X*Y)
    


































