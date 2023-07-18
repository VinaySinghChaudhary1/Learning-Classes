#..........Week 05 ..........
#..........Lecture 5.1...... (Introduction to Functions)

def add(a,b):        # example
  ans=a+b
  print(ans)

def sub(a,b):
  ans=a-b
  print(ans)

def discount(cost,d):
  ans=cost-(cost*(d/100))
  print(ans)


def add(a,b):         # main 
  ans=a+b
  return ans
a=23  
b=25
print(ans(a,b))



def add(a,b):
  ans=a+b
  return ans
a=23  
b=25
ans=add(a,b)+10
print(ans)



def add(a,b):
  ans=a+b
  return ans
a=23  
b=25
ans=a+b+10
print(ans)



def discount(cost,d):
  ans=cost - (cost*(d/100))
  return ans
print("Enter the cost price")
c=int(input())
print("Enter the discount")
y=int(input())
print("The final discount is : ", discount(x,y))


#..........Lecture 5.2...... (More Examples of Functions)

# let us write a few functions on lists:

def list_min(l):
  mini=l[0]
  for i in range(len(l)):
    if (l[i]<mini):
      mini=l[i]
  return mini

def list_max(l):
  maxi=l[0]
  for i in range(len(l)):
    if (l[i]>maxi):
      maxi=l[i]
  return maxi

def list_appendbefore(l,z):
  newl=[]
  for i in range(len(z)):
    newl.append(z[i])
  for i in range(len(l)):
    newl.append(l[i])
  return newl  

l=[1,2,34,5,4,36,56,-12,34,100]
print(list_min(l))
print(list_maxi(l))
z=[10,20,30]
print(list.appendbefore(l,z))


def list_appendend(l,z):
  newl=[]
  for i in range(len(l)):
    newl.append(l[i])
  for i in range(len(z)):
    newl.append(z[i])
  return newl  

l=[1,2,34,5,4,36,56,-12,34,100]
print(list_min(l))
print(list_maxi(l))
z=[10,20,30]
print(list.appendend(l,z))


def list_average(l):
  sum=0
  for i in range(len(l)):
    sum = sum+l[i]
  ans = sum/len(l)
  return ans

l=[1,7,8,10]
print(list_average)
print("Enter a list")

#..........Lecture 5.3...... (Sorting using Functions)

# find out the minimum most element in the list l 
#  append that to a new lsit x>
# remove the minimum from the original list l.

def min_list(l):    # it simple to sorting by break big programing into smaller program
  mini=[]
  for i in range(len(l)):
    if (l[i]<mini):
      mini=l[i]
  return  mini    


def obvious_sort1(l):
  x=[]
  while len(l)>0:
    mini=min_list(l)
    x.append(mini)
    l.remove(mini)
  return x

l=[20,30,43,48,56,4,1]
print(obvious_sort1(l))  


def obvious_sort(l):   # little complex
  x=[]
  while(len(l)>0):
    mini=[0]
    for i in range (len(l)):
      if l[i]<mini:
        mini=l[i]
  
    x.append(min)
    l.remove(mini)
  return x

l=[20,30,43,48,56,4,1]
print(obvious_sort(l))

# we just learnt that breaking our problem into smller modules and solving them makes it easy on our mind.


      
#..........Lecture 5.4...... (Matrix Multiplication using Functions)

#initialise C to zero 
#I need to consider two matrices A and B
# I need to find the dot product of two lists.
# I need to pick ith row and jth column in a matrix

def initialize_mat(dim):    # initialize materic C
  c=[]
  for i in range(dim):
    c.append([])
  for i in range(dim):
    for j in range(dim):
      c[i].append(0)
  return c  

def dot_product(u,v):      # find Dot product of matrices A and B
  dim=len(u)
  ans=0
  for i in range(dim):
    ans=ans+(u[i]*v[i])
  return ans

def row(M,i):          # find row from matrix M
  dim=len(M)
  l=[]
  for k in range(dim):
    l.append(M[i][k])
  return l

def column(M,j):       # find column from matrix M
  dim=len(M)
  l=[]
  for k in range(dim):
    l.append(M[k][j])
  return l  

def mat_mul(A,B):       # Doing Multiplication of matrices A and B
  dim=len(A)
  C=initialize_mat(dim)
  for i in range(dim):
    for j in range(dim):
      #C[i][j]= ith roe of A * jth col of B
      C[i][j]= dot_product(row(A,i), column(B,j))
  return C
  
#..........Lecture 5.5...... (Theoretical Introduction to Recursion)

'''
Compound interest  formula   : f(n) = f(n-1)*(interest)

Sum(n) = Sum(n-1)+n
Fact(n) = [Fact(n-1)]*n

'''

#..........Lecture 5.5...... (Recursion - An Illustration)

# Compute sum of N numbers
n =10
ans=0
for i in range(n):
  print(i+1)
  ans=ans+(i+1)
print(ans)

def sum(n):
  ans=0
  for i in range(n):
    ans=ans+(i+1)
  return ans  

# recursion in python

def sum(n):
  if (n==1):
    return 1
  else:
    return n+sum(n-1)

#Python lets you call the same function within the function.abs

#compute compound interest by assuming the interest to be 10%
def comp(p,n):
  if n==1:
    return p*(1.1)  # for one time
    

def comp(p,n):
  if n==1:
    return p*(1.1)   
  else:  
    return (comp(p,n-1))*1.1     # for multi time

print (comp(2000,3))


# Compute factorial

def fact(n):
  if (n==1):
    return 1
  else:
    return (fact(n-1))*n
print(fact(5))


#..........Lecture 5.6...... (Types of Function Arguments)

def add(a,b,c):    # a,b,c are perimeter
  return (a+b-c)
  
print(add(20,30,40))   # 20,30,40 are argument


def add(c,a,b):    # here position of perimeter are important
  return (a+b-c)
  
print(add(20,30,40)) # positinal argument are called




def add(c,a,b):    
  return (a+b-c)
  
print(add(a=20, b=30, c=40))   # 20,30,40 are argument with position argument  # key word argument



def add(c,a,b):    # here position of perimeter are important
  return (a+b-c)
  
print(add(20,30))   # no of perimeter = no of arguments otherwise error give


def add(c,a=20,b=30):    # deflaut perimeter
  return (a+b-c)
  
print(add(40))   # no of perimeter = no of arguments otherwise error give
print(add(40,10))
print(add(40,b=10,a=50))


#..........Lecture 5.7...... (Scope of Variables)

def myfunction1(x):
  x = x*2     # local variable because x is use for only this def dunction
  print('Value of x in function 1',x)#10


def myfunction2(x):
  x = x*3        # local variable
  print('Value of x in function 2',x)#10


x=5      # Global Variable
print("Value of x before function call",x)#5
myfunction1(x)   # call by value of x for myfunctin1 for variable x
myfunction2(x)   # call by value of x for myfunctin2 for variable x
print("Value of x after function call", x)#10


# call by value study it
# scope of variable

# python now represent X global by function global

def myfunction1(x):
  global x
  x = x*2    
  print('Value of x in function 1',x)#10


def myfunction2(x):
  global x
  x = x*3      
  print('Value of x in function 2',x)#10


x=5      # Global Variable
print("Value of x before function call",x)#5
myfunction1(x)
myfunction2(x)
print("Value of x after function call", x)#10



#..........Lecture 5.8...... (Types of Functions)

#Inbuilt functions
print(), input(), len()

#Library functions
log(), sqrt(), random(), randrange(), calendar(), month()

math.log(), math.sqrt(), random.random()

#String methods (functions)
upper(), lower(), strip(), count(), index(), replace()


#User defined function
def square(x):
  sqr = x** 2
  return sqr

print(square(5))




#..........Lecture 5.8...... (Tutorial on functions)

#............Question 1............
# write a python code using function which calculates the number of upper case letters, lower case letters, total number of characters and number of words.


def upper(s):
  upper = 0
  for c in s:
    if (c.isupper()):
      upper += 1
  return (upper)


def lower(s):
  lower = 0
  for c in s:
    if (c.islower()):
      lower += 1
  return (lower)

def characters(s):
  chars = 0
  for c in s:
      chars += 1
  return (chars)


def words(s):
  words = 1
  for c in s:
      if (c == ' '):
        words += 1
  return (words)


sentence = input("Enter the sentence: ")
uLetters = upper(sentence)
print(f'\nTotal number of upper case characters: {uLetters}')

lLetters = lower(sentence)
print(f'\nTotal number of lower case characters: {lLetters}')

chars = characters(sentence)
print(f'\nTotal number of characters: {chars}')

words = words(sentence)
print(f'\nTotal number of words: {words}')

'''
Function could have no parameters
'''


#............Question 2............
# Write a python code using functions to calculate area and perimenter of circle and rectangle.

PI = 22/7
def circle_area(r):
  return (PI *r*r)

def circle_perimeter(r):
  return (2*PI*r)

def rectangle_area(l,b):
  return (l*b)

def rectangle_perimeter(l,b):
  return ( 2* (l+b))

r = float(input('\n Enter the radius of the circle: '))
cArea = circle_area(r)
print(f'\nArea of circle with radius {r} = {cArea} sq.units')
cPerimeter = circle_perimeter(r)
print(f'\nPerimeter of circle with radius {r} = {cPerimeter} units')
l= float(input('\nEnter the length of the ractangle: '))
b= float(input('\nEnter the breadth of the ractangle: '))
rArea = rectangle_area(l,b)
print(f'\nArea of rectangle with length {l} and breadth {b} = {rArea} sq.units')
rPerimeter = rectangle_perimeter(l,b)
print(f'\nPerimeter of rectangle with length {l} and breadth {b} = {rPerimeter} units')

#.................

import math

PI = math.pi
def circle_area(r):
  return (PI *r*r)

def circle_perimeter(r):
  return (2*PI*r)

def rectangle_area(l,b):
  return (l*b)

def rectangle_perimeter(l,b):
  return ( 2* (l+b))

polygon = ''
while (polygon != "exit"):
  print('\nPOLYGONS\ncircle\nrectangle\nexit')
  polygon = input('\nChooose the polygon type or exit:')
  property=''
  if(polygon == 'circle'):
    r =float(input('\nEnter the radius of circle: '))
    while (property == ''):
      print('\nCIRCLE PROPERTIES\narea\nperimeter\nback')
      property = input('\nchoose the circle property or go back: ')
      if (property == "area"):
        cArea = circle_area(r)
        print(f'\nArea of circle with radius {r} = {cArea} sq.units')
        property = ''
      elif (property == "perimeter"):
        cPerimeter = circle_perimeter(r)
        print(f'\nPerimeter of circle with radius {r} = {cPerimeter} units')
        property = ''
      elif (property == "back"):
        break
      else:
        print('please select the correct polygon property')
        property = ''
    
  elif(polygon == 'rectangle'):
    l= float(input('\nEnter the length of the ractangle: '))
    b= float(input('\nEnter the breadth of the ractangle: '))
    while (property == ''):
      print('\nRECTANGLE PROPERTIES\narea\nperimeter\nback')
      property = input('\nchoose the rectangle property or go back: ')
      if (property == "area"):
        rArea = rectangle_area(l,b)
        print(f'\nArea of rectangle with length {l} and breadth {b} = {rArea} sq.units')
        property = ''
      elif (property == "perimeter"):
        rPerimeter = rectangle_perimeter(l,b)
        print(f'\nPerimeter of rectangle with length {l} and breadth {b} = {rPerimeter} units')
        property = ''
      elif (property == "back"):
        break
      else:
        print('please select the correct polygon property')
        property = ''
  elif(polygon == 'exit'):
    break
  else:
    print('Please select the correct polygon type or exit')


#..........Lecture 5.8...... (Tutorial on functions)

#............Question 3............
# Write a python code using functions which checks whether the input coordinates from a triangle or not

''' Approach 1: Using distance between point '''

def distance (xi,yi, xj,yj):
  return ((((xj-xi)**2) + ((yj-yi)**2)) **0.5)

def isTriangle(max,a,b):
  if ((a+b)>max):
    print('\nTriangle')
  else:
    print('\nNot a trinagle')

x1 = float(input('Enter x coordinate of 1st point: '))
y1 = float(input('Enter y coordinate of 1st point: '))
x2 = float(input('\nEnter x coordinate of 2nd point: '))
y2 = float(input('Enter y coordinate of 2nd point: '))
x3 = float(input('\nEnter x coordinate of 3rd point: '))
y3 = float(input('Enter x coordinate of 3rd point: '))

d1 = distance(x1,y1,x2,y2)
print(f'\nDistance between points ({x1},{y1}) and ({x2},{y2}) = {d1}')
d2 = distance(x2,y2,x3,y3)
print(f'\nDistance between points ({x2},{y2}) and ({x3},{y3}) = {d2}')
d3 = distance(x3,y3,x1,y1)
print(f'\nDistance between points ({x3},{y3}) and ({x1},{y1}) = {d3}')

if (d1>d2):
  if(d1>d3):
    isTriangle(d1,d2,d3)
elif (d2>d3):
  isTriangle(d2,d1,d3)
else:
  isTriangle(d3,d1,d2)



''' Approach 2: Using slope method'''

import math

def slope (xi, yi, xj, yj):
  if(xi==xj):
    return (math.inf)
  else:
    return ((yj-yi) / (xj-xi))


x1 = float(input('Enter x coordinate of 1st point: '))
y1 = float(input('Enter y coordinate of 1st point: '))
x2 = float(input('\nEnter x coordinate of 2nd point: '))
y2 = float(input('Enter y coordinate of 2nd point: '))
x3 = float(input('\nEnter x coordinate of 3rd point: '))
y3 = float(input('Enter x coordinate of 3rd point: '))

s1 = slope(x1,y1,x2,y2)
print(f'\nSlope of the line connecting points ({x1},{y1}) and ({x2},{y2}) = {s1}')
s2 = slope(x2,y2,x3,y3)
print(f'\nSlope of the line connecting points ({x2},{y2}) and ({x3},{y3}) = {s2}')

if (s1 != s2):
  print('\nTriangle')
else:
  print('\nNot a Triangle')




#  .................LIVE CLASS..............
def func(a):
  return a**2

vinay = func(5)
print(vinay)

def prime(a):
  flag = True
  for i in range (2,a):
    if a%i == 0:
      flag = False
      break
    return flag

if prime(5):
  print('The number is prime')
else:
  print(' Number is not a prime number')


n= int(input())
for i in range(2,n+1):
  if prime(i):
    print(i)


def Check_even(n):
  if n%2==0:
    return True
  return False  


def coprime(a,b):
  pass    # pass mean leave it or woring on this course later

def cube(a):
  pass
  
for i in range(10):
  if i%2==0:
    continue     # 
  print(i) 
  print(i**2)
  print(i**3)
  print(i**4)


# Recursion
def recur(n):
   if n==1:
     return 1
   return recur(n-1)  

def waterbottles(n):
  if n==1:
    return


def recu_sort(L):    # recursion mean doing operation repeatly untill operation are completed completely
  if len(L) == 1:
    return L
  smallest = L[0]
  for i in range (len(L)):
    if L[i]<smallest:
      smallest = L[i]
  L.remove(smallest)
  return [smallest] + recu_sort(L)

print(recu_sort([2,1,100,99,81]))






















































































