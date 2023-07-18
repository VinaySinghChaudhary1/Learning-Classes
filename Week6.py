#..........Week 05 ..........
#..........Lecture 6.1...... (Lists and Sets)

l = list(range(10))
print(l)

l[5]

l[9]

l.append('Vinay')
l.append('2.344')

print(l)

print(5 in l)

print(-1 in l)

print('vinay' in l)

print('Vinay' in l)

l=list(range(1000000))
print(l)

print(l[0])

print(l[0]==100)

print(l[9990])

print(l(len(l)-1))
print("vinay" in  l)

x=[1,2,3,6,7,6,3,95,23]
y={1,2,4,7,5,3,5,8}
print(type(x))
print(type(y))

l=list(range(1000000000))
s=set(range(10))
print(s)

x=list(range(10))
print(x)

s=set(range(10000000000))
print(0 in l)
print(1 in l )
print(-1 in l)

'''
Lists take longer time than Sets to search for elements in it.

'''

import random
import math
import numpy
import sys

l=[]
l1=[0]
l2=[0,1]

sys.getsizeof(l)
sys.getsizeof(l1)
sys.getsizeof(l2)

x=list(range(100))
s=set(range(10))

sys.getsizeof(x)
print(x)

sys.getsizeof(y)
print(y)

'''
set have no perator s[2] to find particular element from set.

'''
# set operator (in) perator to give booling answer True?False.(present or not)

# you can add element in set
y.add('Ravi')

print(y)




#..........Lecture 6.2...... (Dictionaries)

d={}
d['vinay'] = 2944543
d['ramya'] = 9434231
d['ravi'] = 3848039
print(d)
print(d['ravi'])

malgudi = ['It', 'was', 'Monday','morning', 'Swaminathan', 'was','reluctant', 'to','open', 'his', 'eyes','he','considered','Monday','specially','unpleasant','in','the', 'calendar', 'After', 'the', 'delicious', 'freedom', 'of', 'Saturday', 'and', 'Sunday', 'it','was', 'difficult', 'to', 'get', 'into', 'the', 'Monday', 'mood','of', 'work','and','discipline','he','shuddered','at', 'the','very',"thought", 'of',' school:', 'the', 'dismal','yellow', 'building;','the','fire','eyed’, ‘Vedanayagam', 'his','class',
'teacher!', 'and','headmaster','with', 'his','thin','long','cane']

print(malgudi)
print(len(malgudi))

l=[1,2,3,5,78,8]
for i in range (len(l)):
  print(i)

for x in l:
  print(x)

s=set(malgudi)
print(s)
print(len(s))

print(malgudi[10])
print(malgudi[4])

d={}
for x in s:
  d[x]=0

print(d)

print(d['get'])

for x in malgudi:
  d[x]=d[x]+1

print(d)

max =0
d={}
for x in s:
  d[x]=0

print(d)

for x in malgudi:
  d[x]=d[x]+1
  if d[x]>max:
    max=d[x]

print(max)

max=0
answer_word=''
for x in malgudi:
  d[x]=d[x]+1
  if d[x]>max:
    max=d[x]
    answer_word=x

print(d)

print(max)
print(answer_word)


print(malgudi)

d={}
d['vinay']=[23,45,34]
d['vivek']=[43,45,46]
d['vikash']=[30,41,42]
print(d)

print(d['vinay'])
print(d['vinay'][2])

d['vinay']=[23,45,34,'easy23@gmail.com']
print(d['vinay'][3])


#..........Lecture 6.3...... (Tuples)

l=[1,2,34,55,67]
l.append(100)
print(l)
l.remove(34)
print(l)

'''
# A tuple is unchangeable
# list is changeable
# Tuples are like strings we can use indexing and slicing in tuples.
# in tuple append and remove not work
'''


l=list(range(10))
t=tuple(range(10))

# l is flexiable, but t isn't
# In lists we can update the values but once a tuple is created we can not change its values.


import string

string.ascii_uppercase

string.ascii_letters

string.ascii_lowercase

s=string.ascii_letters
p=set(s)
print(p)

alpha=tuple(s)
print(alpha)

s=string.ascii_letters
alpha=tuple(list(s))
print(list(s))
print(alpha)

# Let’s write a program to remove all the unwanted symbols from the string :-
x='vinay#shingh^75%$^indiachennai*32,tamil Naidu()karnatka'
l=list(x)
print(l)

r=[]

for p in l:
  if p in alpha:
    r.append(p)

print(r)

print(alpha)

l=list(range(10))
t=tuple(range(10))

print(l)
print(t)

print(l._size_())

print(t._size_())

# Tuples have less size than lists.

# When we are sure  of the list that we are handling and we are also sure that it never changes, then use a tuple
    

#..........Lecture 6.4 ..... ( More on Lists)


# Operations on lists-

# Addition :
l1 = [1,2,3]
l2=[10,30,32]
l12 = l1+l2
l21 = l2+l1
print(l12,l21)

l22=[0,0,0,0,0,0,0,0]
print(l22)

# Replication :
l11=[0]*10
print(l11)


# Logical operators :
l1 = [1,2,3]
l2= [1,2,3]
l3 = [1,3,2]

print(l1==l2)
print(l2==l3)

print(l2<l3)

print([1,2]<[2,1])


# Mutability :
l=[1,2,4]  #mutable
print(l)
l[2]=3
print(l)

# Integers are immutable -
x=5
y=x
x=10
print(x,y)

# This is how we change the values of integer variables.

l1 = [1,2,3]   #computer change l1 and l1 first position on both
l2 =l1
l1[0]=100
print(l1,l2)

''' How to create a separate copy?
There are three ways -  '''

l1=[1,2,3]
l2 = list(l1)
l3=l1[:]
l4=l1.copy()
l5 =l1

# How do we know if two lists have the same memory location?
print(l1 is l2)
print(l1 is l3)
print(l1 is l4)
print(l1 is l5)

# If function type is mutable it is called by reference otherwise it is called by value
def add(x):
  x=x+1
  return x


def add(x):
  x.append(1)
  return x
  
x=[5]
print(add(x))
print(x)


l1 = [1,2,3]  
print(l)

l.append(4)
print(l

# List methods :
''' append() (inserts the element in the last)
remove() (this will remove element from list) '''
      
l.remove(2)
print(l)

x= l.copy()
print(x,l)

l.insert(2,9)
print(l)


d=x.pop(0)
print(l)


l = [1,45,4,75,2,9,7]  
l.sort()
print(l)


l = [1,45,4,75,2,9,7]  
l.reverse()
print(l)



#..........Lecture 6.5 ..... (More on Tuples)

# More on tuples :-
'''  Tuples are immutable.   '''

t = 1,2,3
print(t,type(t))

x,y,z =t
print(x,y,z)

x=5
y=10
x,y = y,x
print(x,y)

l=[10]
print(l, type(l))

t=(10)
print(t,type(t))

t = ([1,2],['a','b'])  # tuple is not modify
t[0] = 10
print(t)

t = ([1,2],['a','b'])  # list under tuple can be modify
t[0][0] = 10
print(t)


t1 = (1,2,3)    # not hashable (inmutable inside tuple)
t2 = ([1,2,3],)  # hashable (mutable inside tuple)




#..........Lecture 6.5 ..... ( More on Dictionaries)



d ={'key':'value'}

# key have unique value,
# in dictionary "key" have inmutable things but "value " mutable things have
# duplication is allowed for values.

'''
So, the next question is apart from this what all things we can use as a dictionary key.
Can we use an integer, as a dictionary key?
Yes, we can use integer as a dictionary key, float, yes, Boolean, yes, string, yes, list,
no, because list is mutable.

Another dictionary once again, no, because dictionary is also mutable.

Then what about tuples?
Can we use tuple as a dictionary key?
And the answer is yes and no.

Yes, because tuple is immutable, hence, it can be used as a dictionary key, but at the
same time, no, because tuple allows you to have mutable values inside it.
We have seen such an example in previous lecture and that time I asked you to remember one
term called hashable.

So, in other words, a dictionary key has to be immutable hashable, which means all such
tuples, which do not have any mutable entity inside are allowed at dictionary keys.

'''

'''

Then what about values?
What all things we can use as value.
Integer, float, Boolean, string, list, tuple, dictionary, anything else and the answer is
all of the above.
Dictionary value can be anything.
There is no restriction on it and as it is a mutable entity all the different properties,


'''

# How to iterate over a dictionary :

d ={0:0, 1:1, 2:4, 3:9, 4:16}
print(d)
for key in d:
  print(key, d[key])

# Three most imp methods related to dictionaries -

d ={0:0, 1:1, 2:4, 3:9, 4:16}
print(d.keys())
print(d.vaules())
print(d.items())


#..........Lecture 6.6 .....(More on Sets)

#  Set methods -

st = { 1,2,3,4,5}
print(st)

st = { 1,2,3,4,5,1,2,3,4}
print(st)


a ={1,2,5}
b = {1,2,3,4,5}
print(a.issuperset(b))


A ={1,2,3}
B = {3,4,5}
C1 = A.union(B)
C2 = A|B
print(C1, C2)



A ={1,2,3}
B = {3,4,5}
C1 = A.difference(B)
C2 = A - B
print(C1, C2)

'''

Set is an unordered entity; we can not say that 1 is at zeroth index or is the first element in the set.

Set itself is mutable but values inside set have to be immutable and hashable , hence, we cannot add a dictionary or list or tuple containing a list or dict to a set.

'''


'''

sets are curly brackets, which are similar  to dictionary, whereas values inside follow  
a pattern, which is like a list or a tuple. So, the question is what is different about  

set as compared to other three components?  

First, set does not allow duplicate values.  
For example, if we add these duplicate  values and try to print the set  
still, we will get only the unique values in that  set and all the duplicates will be discarded.  

Second, set is an unordered entity, which means we  cannot say that this element 1 is at zeroth index  
or it is the first element in set and because  of that, if we try to execute something like  
this a computer will give us an error, set  object is not subscriptable. As I mentioned,  
sets do not have a notion of order. Set  is simply a collection of values.  

Third, with respect to mutability set is peculiar.  Set itself is mutable, but every value inside set  
has to be immutable and hashable, which  means you can add values into a set,  
but whatever values which we add,  those values has to be immutable.  

Hence, we cannot add a list or a dictionary or a  tuple containing a list or a dictionary to a set,  
because then it will not be  immutable as well as hashable.  

Apart from this, we can iterate over a set. Moving  to next point, which is set methods. The concept of set in python is derived from mathematical  sets. Therefore, Python set also support  
all those operations, which we usually perform  using mathematical sets like subset, superset,  
union, intersection, difference and so on. All  these mathematical operations can be implemented  

'''



