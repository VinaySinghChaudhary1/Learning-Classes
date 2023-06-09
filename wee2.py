#...........week 02..............
#.........lectrue 2.2....variable representation...and put comment (#) for good coding and in future editing will take help to edit your code

ram_bank_balance=100000
ram_loan=500000
lakshman_bank_balance=2000000
lakshman_loan=1000000
net_income=ram_bank_balance+lakshman_bank_balance
net_laibility=ram_loan+lakshman_loan
final_value=net_income-net_laibility
print('so,the family has', final_value)

#........
ram_bank_balance=100000
ram_loan=500000
lakshman_bank_balance=2000000
lakshman_loan=10000000
net_income=ram_bank_balance+lakshman_bank_balance
net_laibility=ram_loan+lakshman_loan
final_value=net_income-net_laibility
print('so,the family has', final_value)


#.........lectrue 2.3....variable revisited: Dynamic typing

n=10
print(type(n))
n=n/2
print(type(n))

print(n)
n=n/1
print(type(n))
print(n)

b='india'
print(type(b))

a=10
print(a)
print(type(a))


#.........lectrue 2.4....More on variable, Operators and Expressions

##  we can not use pre-define key word such as and,or,if,while,else,elif etc

a1_=5
print(a1_)

# numeric number not in frrist place as variable such as "1a"

roll=5
ROLL=15
Roll=10
print(roll,ROLL,Roll)

# multiply assignment (position is matter in this type of assiging)
x,y,z=1,23,44
print(x,y,z)
print(y,x,z)
print(z,x,y)


#sort hand operators (athematic operator)

count = 12
count=count+1
count=count+1
count=count+1
count=count+1
count=count+1
print(count)

count = 12
count+= 1
count+=1
count+=1
count+=1
count+=1
print(count)

count = 12
count+= 1
count=count+1
print(count)

count = 12
count-= 1
count=count-1
print(count)

count = 12
count*= 1
count=count*1
print(count)

count = 12
count/= 2
count=count/2
print(count)

#in operator.....(in operator give alway booling value)
print('alpha' in 'A variable anme can only contain alpha-numeric characters and underscores')
print('alpha' in 'a variable name must start with a latter or the underscore character')

# chaining operator....(using multiple logical opeator in single line or coding)
x=5
print(1<x<10)
print(10<x<20)
print(x<10<x*10<100)
print(10>x<=9)
print(5==x>4)

#deleting a variable
x=10
print(x)
del x
print(x)  # error give because x delete



#.........lectrue 2.5....Escape characters and types of quotes


#...escape

print('It\'s beautiful day')   #issue resolved of it's by it\'s  where '\'(backscase) is refer as escape character
print('It is beautiful day')

print("we are from \"IIT\" Madras")   #issue resolved of "IIT" by \"IIT\"  where '\'(backscase) is refer as escape character

print('My name is Viany. I am from kanpur.') # space b/w 2 sentence by Tap button 
print('My name is Viany.\tI am from kanpur.')
# space b/w 2 sentence by \t operator
print('My name is Viany.\nI am from kanpur.')
# break b/w 2 sentence by \n operator

print("It's beautiful day")
print("we are from \'IIT\' Madras") 

#...Python support '', "", ''' code break
x='This is my class'
y="This is my class"
z='''first line
second line
third line'''
print(x,y,z)    # code complete in multiple line by adding ''' in both end


#....adding of #(computer not show outcome this code line)...........# is use comment
#x='This is my class'
#y="This is my class"
z='''first line
second line
third line'''
print(x,y,z)    # code complete in multiple line by adding ''' in both end

# what we do if we coment in multiple line
 '''simple use three commas 
 for multiple comment line'''

'''

print('It's beautiful day')   #give error

print("we are from "IIT" Madras")    # give error

z='first line
second line
third line'
print(z)     

'''


#.......lectrue 2.6....String Methods

''' we know function of string in pyhton
such as lower, upper, capitalize, title, swapcase, islower, isupper, istitle, isdigit, isapha, isalnum, strip, lstrip, rstrip, startswith, endswith, count, index, replace'''


#.........lectrue 2.7....An interesting cipher: more on Strings

alpha="abcdefghijklmnopqrstuvwxyz"
j=0
print(len(alpha))
print(alpha[j])
print(alpha[j+1])
print(alpha[j+3])
print(alpha[j+5])

i=23
print(alpha[i%26])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26])

s='india'
# I expect to output tvebstibo

t=''
r=0
k=1
t=t+(alpha[(((alpha.index(s[r]))+k)%26)])    #if we not add %(mudular) then code giveb error due to out of range  error
t=t+(alpha[(((alpha.index(s[r+1]))+k)%26)])
t=t+(alpha[(((alpha.index(s[r+2]))+k)%26)])
t=t+(alpha[(((alpha.index(s[r+3]))+k)%26)])
t=t+(alpha[(((alpha.index(s[r+4]))+k)%26)])
print(t)


#.........lectrue 2.8......Introduction to the if statement

#if condition
# let us consider the movie "Avengers". This is a 13+ movie.
print('please enter your age of birth')
birth_year=int(input())
current_year=2021
age=current_year-birth_year
if (age<13):
   print('your are under age, you cannot watch this movie')
   print('wait until you are old to watch this movie.')

else:
   print('you are old enough to watch Avengers, enjoy!')
   print('Dont forget to watch the sequels and prequels')
print('Have a nice time')

#.........

print('please enter your age of birth')
birth_year=int(input())
current_year=2021
age=current_year-birth_year
if (age<13):
  print('your are under age, you cannot watch this movie')
  
else:
  print('you are old enough to watch Avengers, enjoy!')
print('Have a nice time')


#.........lectrue 2.9......tutorial on if,else and else-if(elif) conditions

# Find whether the given number is even or odd
num=int(input('enter a number:', ))
if num%2==0:
  print("Number is Even number:", num)
else:
  print(("Number is Odd number:", num))


# Find whether the given number ends with 0 or 5 or any other number
num=int(input('enter a number:', ))
if (num%5==0):
   if (num%10==0):
     print("0")
   else:
     print('5')
else:
  print('Other')

  
#Find the grade of student based on the given marks from 0 to 100.

num=int(input('enter a number:', ))
if 90<=num<100:
   print('A')
elif 80<=num<90:
   print("B")
elif 70<=num<80:
   print("C")
elif 60<=num<70:
   print('D')
elif 0<=num<60:
   print('E')
else:
   print('Invaild input')
  
#..........................
num=int(input('enter a marks:', ))
if num>=90 and num<100: 
   print('A')
elif num>=80 and num<90: 
   print("B")
elif num>=70 and num<80:
   print("C")
elif num>=60 and num<70:
   print('D')
elif num>=0 and num<60:
   print('E')
else:
   print('Invaild input')

#Convert the given flowchart into a python code
print('Travel form city A to city B')
Time=int(input('Enter Time: ')) 
Longer=int(input('Define longer: '))
if (Time>=Longer):
  price=int(input('Enter Price: '))
  Higher= int(input('Define higher: '))
  if (Price>=Higher):
    print('Train')
  else:
    print('Coach')
else:
  price=int(input('Enter Price: '))
  Higher= int(input('Define higher: '))
  if (Price>=Higher):
    print('Daytime Flight')
  else:
    print('Red eye Flight')
print('Arrive City B')



#.........lectrue 2.10......Introduction to "import Library"

import random
# Let us simulate two dice six faced
dice1=(random.randrange(1,7))
dice2=(random.randrange(1,7))
total=dice1+dice2
print('Your pair of dice is:', total)

# Let us simulate a dice six faced
print(random.randrange(1,7))

# Let a simulate a coin toss
a=random.random()
if (a<0.5):
  print("Heads")
else:
  print("Tails")
# any random number
print(random.random())

# math import as calculator
import math
a=int(input('Enter your Number: '))
print(math.log(a))
print(math.sin(a))
print(math.sqrt(a))
print(math.factorial(a))
print(math.pow(10,5))


#.........lectrue 2.11......Different ways to import a library

# import calendar in different way

import calendar as c          # C define by us and save sometime to coding
print(c.month(2021,4))

from calendar import month as m    # m define by us and save sometime to coding
print(m(2023,6))


from calendar import month    #if you requried only specific feature then import like this
print(month(2023,10))


from calendar import month,calendar    #if you requried only specific feature then import like this
print(month(2023,10))
print(calendar(2023))


from calendar import*   #computer bring entire library contain import in this python code due to which we write only month, calendar
print(month(2023,10))

print(calendar(2023))


import calendar  #computer bring entire library of calendar import in this python code due to which we write calendar.()

print(calendar.calendar(2021))

print(calendar.month(2017,7))



























