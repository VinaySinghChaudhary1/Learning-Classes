#..........Week 03 ..........
#..........Lecture 3.2...... ( Introduction to while loop )
print("when did India get ints independence (year)?")
Year=int(input())

if (yesr==1947):
  print("Hip hip Hurrayl. You got that right!")
else:
  print("Comen dont you know even this?")
  print("that ok , I will let you attempt this once more")
  print('when did India get its Independence?')
  year=int(input())
  if (yesr==1947):
    print("You got it?")
  else:
    print('Failed i  your second attempt too/ grrr...')

#.......write above answer untill wrtie coorect.....

print("when did India get ints independence (year)?")
Year=int(input())

while(year!=1947):
  print("you got this wrong. Enter once again.")
  year=int(input())

print("woowwwwwwwww....you got it right!1947")

''' # While works like thats:
    # write wjatever you want here
    # write wjatever you want here
    # write wjatever you want here
    
    '''

#..........Lecture 3.3: While to Compute Factorial

#let us find the factorial of a number

print('Enter a number')
n=int(input())

'''n=5
1*2*3*4*5
'''
answer=1
answer=answer*2      #in this code you need to type code for every number
answer=answer*3
answer=answer*4
answer=answer*5
print(answer)

'''  '''
i=1
answer=1
while(i<=n):            #....less than or equal to.......
  answer=answer*i
  i=i+1

print(answer)


#..........Lecture 3.4: Tutorial on while loop

#......Q1 Find The factorial of the given Number
num=int(input('Enter a number: '))
fact = 1
if (num <0):
  print('Not define')
else:
    while(num>0):
        fact = fact*num
        num= num -1
    print(fact) 

#......Q2 Find The number of digits in the given Number

num = abs(int(input('Enter a number: ')))
digits= 1
while(num>9):
  num=num//10
  digits= digits+1
print(digits)  


#......Q3 reverse the digits in the given number

num = int(input('Enter a number: '))
absNum = abs(num)
if (num>=0):
  rev= num%10    # remender part
  num = num//10    # excatly divide
  while(num>0):
    r = num%10
    num= num//10
    rev= rev*10+r
  print(rev) 
else:
  rev = absNum%10
  absNum= absNum//10
  while(absNum>0):
    r = abdNum%10
    abdNum= abdNum//10
    rev= rev*10+r
  print(rev -2*rev)

#........OR

num = int(input('Enter a number: '))
absNum = abs(num)
rev= num%10    # remender part
absNum = num//10    # excatly divide
while(absNum>0):
  r = absNum%10
  absNum= absNum//10
  rev= rev*10+r
if(num>=0):
  print(rev)
else:
  print(rev - 2*rev)

#......Q4 Find whether the entered number is palindrome or not

num = int(input('Enter a number: '))
absNum = abs(num)
rev= num%10    # remender part
absNum = num//10    # excatly divide
while(absNum>0):
  r = absNum%10
  absNum= absNum//10
  rev= rev*10+r
if (num<0):
  rev = rev - 2*rev
if(num==rev):
  print("palindrome")
else:
  print('Not a palindrome')


#..........Lecture 3.5: Introduction to for loop

print("hello India")      # type code manually
print("hello India")
print("hello India")
print("hello India")
print("hello India")
print("hello India")
print("hello India")
print("hello India")


#...... FOR LOOP.....

for i in range(12):
  print(i, "Hello India")


for i in range(12):
  print(i, "Hello India")
  print("*******")


#...... FOR LOOP.....
print("Enter a numebr")
n=int(input())

for i in range(n):
  if (i%2==0):
    print(i,"Hello India")
  else:
    print(i, "Hii world")

#..........Lecture 3.6: for loop to add the first n numbers

#Sums the first 10 integers

an=0+1+2+3+4+5+6+7+8+9
print(an)

#.............

print("Enter a number")
n=int(input())

ans=0
for i in range(n):
  ans=ans+i

print("the answer is: ", ans)


#..........Lecture 3.7: for loop for multiplication tables

print("2x1=2")
print("2x1=4")
print("2x1=6")
print("2x1=8")
print("2x1=10")
print("2x1=12")
print("2x1=14")
print("2x1=16")
print("2x1=18")
print("2x1=20")


#.............
print("Enter a number")
n=int(input())

for i in range(1,11):
  print("2X",i, "=", 2*i)


#..........Lecture 3.8: More on range and for loop without range

for x in range(10):
  print(x)


for x in range(1,11):
  print(x)

for x in range(1,11):
  if (x%2!=0):
    print(x)
  
for x in range(1,11, 2):    #...range(start, end(not included 11), jump)
  print(x)


for x in range(9,-1, 1):    #.  reverse order..range(start, end(not included 11), jump)
  print(x)


country = "India"
for letter in country:
  print(letter)


print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])


#..........Lecture 3.9: Formatted Printing

for x in range(10):
  print(x)


for x in range(10):
  print(x, end= ' ')    # print number in one line


d=10
m=5
y=2021
print('Today\'s date is', end= ' ')
print(d,m,y, sep='-')


num =int(input())
for i in range(1,11):
  print(num, 'X',i, '=', num*i)
  print(f'{num} X {i} = {num*i}')
  print('{0} X {1} = {2}'.format(num,i,num*i))
  print('%d X %d = %d' % (num,i,num*i))
  

pi=22/7
print(f'value of PI = {pi}')
print('value of PI {0}'.format(pi))
print('Value of PI = %f' %(pi))


print(f'value of PI = {pi:.2f}')     # .2f upto 2 decimal point
print('value of PI {0:.2f}'.format(pi))
print('Value of PI = %f.2f' %(pi))


print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))


print('{0:5d}'.format(1))      # 5d means tells to computer to use min. five character
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))


#..........Lecture 3.10: Tutorial on for loop and difference between while loop and for loop

#.......Example of FOR LOOP......

#.........Q1 Find the factorial of the given number  ( by FOR LOOP)

num = int (input())
num=int(input('Enter a number: '))
fact = 1
if (num <0):
  print('Not define')
else:
    for i in range(num, 1, -1):
      fact = fact *i
    print(fact) 

#......Q2 Find The number of digits in the given Number

num = abs(int(input('Enter a number: ')))
strNum=str(num)
digits= 1
for c in strNum:
  digits= digits+1
print(digits)  


#......Q3 reverse the digits in the given number


num = int(input('Enter a number: '))
absNum = str(abs(num))
rev= ''   
for c in absStrNUm:
  rev= c + rev
if(num>=0):
  print(rev)
else:
  print('-' + rev)
  

#......Q4 Find whether the entered number is palindrome or not

num = int(input('Enter a number: '))
absStrNum = str(abs(num))
rev= '' 
if c in absStrNum:
  rev = c + rev
if (num<0):
  rev = "-" + rev
if(num==int(rev)):
  print("palindrome")
else:
  print('Not a palindrome')


#..........Lecture 3.11: Nested for loop

s='VIBGYOR'
t='VIBGYOR'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
print(s[6])

# by for loop
for i in range(7):
  print(s[i])

# example of nested loop
g='VIBGYOR'
h='VIBGYOR'
for i in range(7):
  for j in range(7):
    print(s[i],s[j])
    print(i,j,s[i],s[j])



g='VIBGYOR'
h='VIBGYOR'
count=0
for i in range(7):
  for j in range(7):
    print(s[i],s[j])
    print(i,j,s[i],s[j])
    count=count+1
print('The total way in which the two brothers can wear 7 different colours: 'count) 



#..........Lecture 3.12 Tutorial on nested loops

#.......Q1 Find all prime numbers less then the entered number

num = int(input('Enter a number: '))
if (num>2):
  print(2, end=' ')
for i in range(3, num):
  flag = False
  for j in range(2,i):
    if (i%j == 0):
      flag=False
      break
    else:
      flag=True
  if (flag):
    print(i, end = ' ')


#..........Lecture 3.12 Tutorial on nested loops

#.......Q1 Find all prime numbers less then the entered number

num = int(input('Enter a number: '))
if (num>2):
  print(2, end=' ')
for i in range(3, num):
  flag = False
  for j in range(2,i):
    if (i%j == 0):
      flag=False
      break
    else:
      flag=True
  if (flag):
    print(i, end = ' ')



#.......Q2 Find the Total profit/loss of each trader working in trading firm. imformation regarding number of traders and number of trasactions in unknown.

empID = int(input('Enter Emp ID: '))
while (empID !='-1'):
  trade=int(input('Enter the trade amount: '))
  profit_loss = 0
  while(trade!=0):
    profit_loss = profit_loss + trade
    trade = int(input('Enter the trade amount: '))
  print(f'profit/loss for employee {empID} is {profit_loss}')
  empID = input('\nEnter employee ID: ')


#.......Q3 Find the daywise total rainfall for the entered duration of time r.g week, month, etc.

days= int(input('Enter the number of days: '))
for i in range(1, days+1):
  total=0
  rainfall= int(input('Enter the Rainfall: '))
  while (rainfall != -1):
    total = total + rainfall
    rainfall = int(input(' Enter the rainfall: '))
print('Total rainfall for day {0} is {1}'.format(i, total))

#.......Q4 Find the loength of longest word from the set of words entered bu the user

word = input("Enter a word: ")
maxLen = 0
while (word!='-1'):
  count= 0
  for letter in word:
    count = count+1
  if (count> maxLen):
    maxLen = count
  word= input("Enter a word: ")    
print('The length of longest word is  %s'%maxLen)          
    
#..........Lecture 3.13: break, continue and pass
    
# break keyword
email=input()
for c in email:
  if (c=='@'):
    break      # break is also called exit loop
  print(c)


# Continue keyword
email=input()
for c in email:
  if (c=='@'):
    print(' ')
    continue      
  print(c, end=' ')


# Pass keyword
for x in range(11):
  if (x%3 ==0):
    print(x)
  else:        #else is not empty  if empty it give error
    pass       # pass mean do nothings








