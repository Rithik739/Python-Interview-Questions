n =int(input("enter the number:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end=" ")  
    print()

## Remove duplicate values
x =[1,5,4,6,1,2]
c =[]
for i in x:
    if i not in c:
        c.append(i)
print(c)

##Remove duplicate values print remaining values
x =[1,4,5,6,4,3,1]
y =[]
for i in x:
    if x.count(i) ==1:
        y.append(i)
print(y)

##sort the values
y =[1,2,4,8,9,7,2,34]
for i in range(len(y)-1):
    for j in range(len(y)-1):
        if y[j] > y[j+1]:
            y[j],y[j+1]=y[j+1],y[j]
print(y)

##write a programme for fibonacci series
n =int(input("enter the number:"))
x =0
y =1
for i in range(n):
    print(x)
    x,y =y,x+y

## write a programme fibonacci in recursive function

def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+ fibonacci(n-2))
n =int(input("enter the number:"))
print("Fibonacci1 sequence using recursion:")
for i in range(n):
    print(fibonacci(i))
    
    
## how to sort the key and values  
d ={'name':'model','python':'course',}
c ={}
for k,v in d.items():
    c[v] =k
print(c)

## dimand shape
n =int(input("enter the number:"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print("",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

l ={'perl:python:10','python:perl:20','python:perl:10'}
d ={}
for i in l:
    l2 =i.split(":")
    d[l2[1]] =d.get(l2[1],0)+int(l2[2])
print(d)

##skip the fibonacci series expected output [0 1 1 2 3 8 13 ]?
n =int(input("enter the number:"))
x =0
y =1
for i in range(n):
    if x !=5 and x !=21:
        print(x)
        x,y =y,x+y
    else:
        x,y =y,x+y
        
##print 100 prime numbers
a =[2]
i =3
while len(a) <=100:
    for p in a:
        if (i % p == 0):
            break

    if i%p != 0:
         a.append(i)
         print (i,end=' ')
    i = i + 2
    
## prime numbers
Lower =int(input("enter lowest value:"))
upper =int(input("enter upper value:"))
for number in range(Lower,upper+1):
    if number >1:
        for i in range(2,number):
            if number %i ==0:
                break
        else:
            print(number)
                
## convert two lists into a dictionary
data =[1,2,3,4]
val =[5,6,7,8]
res =dict(zip(data,val))
print(res)

## convert two lists into a dictionary
listk =["mon","tue","wed","thu"]
listv =[1,2,3,4]
res ={listk[i] :listv[i] for i in range(len(list.k))}
print(res)

## Palindrome number or not
string =input("entet the string:")
if (string ==string[::-1]):
    print("the string is palindrome")
else:
    print("the string not palindrome")
    
l1 = [[1,2],[3,4],[5,[6,7]]]
d1={x[0]:x[1] for x in l1}
print(d1)#Output:{1: 2, 3: 4, 5: [6, 7]}


s ="malayalam"
v =list(s)
v[3] ='b'
print("".join(v))

input_str ="hello world"
i ="l"
j ="x"
results ="".join([ j if char == i else char for char in input_str])
print(results)

v =[i for i in range(0,10) if i%2 ==0]
print(v)
##
##
st ="abcdefg"
st.replace('b','x')
print(st)
print(st.replace('b','x'))

dict ={'chinna':200,'japan':300,'india':600,'eropu':150}
x ={(v,k) for k,v in dict.items()}
print(max(x))
print(min(x))

##How to fetch the 10 digit of ph number
import re
s ="this is my number 9849644691"
req =r'\d{10}'
print(re.findall(req,s))

## Validate phone number
import re
n =input("enter the number:")
m =re.fullmatch("[6-9][0-9]{9}",n)
if m!= None:
    print("valid phone number")
else:
    print("invalid phone number")
    
## Validate email id 
import re
r=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def isValid(email):
    if re.fullmatch(r, email):
      print("Valid email")
    else:
      print("Invalid email")


## second hight value in list
l =[4,5,1,7,8,9]
l.sort()
print(l[-2])

## count the repeted values
v="Regression Testing is nothing but a full or partial selection of already"
d ={}
for i in v:
    d[i] =d.get(i,0)+1
print(d)

strSample ="a@bcd#ef&"
lists =list(strSample)
i =0
j =len(lists)-1
while i<j :
     if not lists[i].isalpha():
         i +=1
     elif not lists[j].isalpha():
        j -=1
     else:
        lists[i],lists[j] =lists[j],lists[i]
        i +=1 
        j -=1
srout ="".join(lists)
print(srout)
        
s="aaaabbbbcccfff"
l =[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in l:
    print('{} occurence {} times'.format(ch,s.count(ch)))
    
##############################################
s ="a4b2c6d7"
output =""
for x in s:
     if x.isalpha():
          output =output+x
          previous =x
     else:
          output =output+previous*(int(x)-1)
print(output)

############################################

s ="welcome to python"
for i in s.split():
    print("".join(i[::-1]),end=" ")
    
############################

s =input("enter the string")
total =0
for i in s:
    total +=1
print(total)

string = "The best of both worlds";  
count = 0  
for i in range(0, len(string)):  
    if(string[i] != ' '):  
        count = count + 1;   
print("Total number of characters in a string: " + str(count));


##   HCL Interview

####write a palindrome progamme using recursion function
def check_palindrome(s):
    if len(s) <= 1 :
        return True
    if s[0] == s[len(s) - 1] :
        return check_palindrome(s[1:len(s) - 1])
    else:
        return False
    
var = input(("Enter a value: "))
if(check_palindrome(var)): 
    print("Palindrome")
else:
    print("Not a Palindrome")


###   1
##  1 2 1
# 1 2 3 2 1

def pyramid():
    odd =1
    space =3
    for i in range(1,5):
        k =0
        for j in range(1,space+1):
            print("",end="")
        for j in range(1,add+1):
            if (j<=i):
                k =k+1
            else:
                k =k-1
            print(k,end="")
        print()
        odd =odd+2
        space =space-1
pyramid()              
##   Globallogic interview

s =[1,'p',2,3,'y','t',4,'h']
l1 =[]
l2 = []
for i in range(len(s)):
   if type(s[i]) == str:
      l1.append(s[i])
   else:
      l2.append(s[i])
        
new =[]
for i in range(len(l2)):
   new.append((l2[i],l1[i]))
print(new)


#### s ='programming' my expected output is s ='pRoGRaMMinG' 
s ='programming' 
new =''
for i in s:
   if s.count(i)==1:
      new +=i
   else:
      new +=i.upper()
print(new)

##v =[1,2,3,4,5,5,2] expexted output {1:1,2:2,3:1,4:1,5:2}?
v =[1,2,2,3,4,5,5]
d ={}
for i in v:
    d[i] =d.get(i,0)+1
print(d)

##[1,2,3,4,5,6,7,8,9]what is output print(a[-1:-5])?
a =[1,2,3,4,5,6,7,8,9]
print(a[-1:-5])

##[1,2,3,4,5] total sum without sum function?
s =[1,2,3,4,5]
s1 =0
for i in s:
    s1 +=i
print(s1)

###### HCL interview
####maximum and minimum numbers in array input:arr[]:{1,2,3,4}
arr =[1,20,5,6,88,3]
max =arr[0]
n =len(arr)
for i in range(1,n):
   if arr[i]>max:
      max =arr[i]
print(max)

min =arr[0]
n =len(arr)
for i in range(1,n):
   if arr[i]<min:
      min =arr[i]
print(min)

####find the sum of digits and find index value of target a =14
num =[4,5,6,8,15]
target =14
for i in range(0,len(num)):
   for j in range(i+1,len(num)):
      if num[i]+num[j] ==target:
         print(num[i],num[j])

s ="abcde" write a program substring ?
s ="ABCDE"
t =[s[i:j] for i in range(len(s)+1) for j in range(i+1,len(s)+1)]
print(t)

         
########## L & T Interview
         
####take a dictionary and write programme space key and values by using for loop
d ={'model':'ford','car':'benz','python':'learn'}
for key,value in d.items():
    print(key," ",value)

####s ='python' print alternative characters
s ='python'
print(s[::2])

four_letter_names = [name for name in students if len(name) == 4]


v =''
for i in range(len(s)):
    if i%2==0:
        v +=s[i]
print(v)

######add two numbers by using lambda function 
v =lambda a,b:a+b
print(v(2,3))

def reverse_middle_word(input_str):
    words =input_str.split()
    if len(words)<3:
        return input_str
    
    middle_index =len(words)//2
    words[middle_index] =words[middle_index][::-1]
    
    result_str =" ".join(words)
    return result_str
orginal_str ="python automation chandra"
output =reverse_middle_word(orginal_str)
print(output)


######################## TCS 

##what is module and packages?
##difference between remove and pop ?
##difference between append and extend?
##count the number of strings in dictionary format?
##l =[1,2,3,1] reverse the list?
##l =[1,2,3,4,5,6] even numbers using list comprahenssion?
##palidrome number or not by using class object?

######Palindrome number or not program by using class
            
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
      
    
####   Globallogic  

##How to check python version
##a =(1,2)
##a[0] +=1 what is the output?
a =(1,2)
a[0] +=1
print(a)

ans:TypeError: 'tuple' object does not support item assignment

##a =(1,2)
##a +=(-2,-1) what is the output?
a =(1,2)
a +=(-2,-1)
print(a)

Ans:(1, 2, -2, -1)

## list =[1,2,3,4,5] print(list(set([1,1,2,3,4,4]))) what is the output?
list =[1,2,3,4,5]
print(list(set([1,1,2,3,4,4])))

ans: TypeError: 'list' object is not callable

##########
class Test:
    def __init__(self):
        self._c =1
        self.__c =2
        self.__c_ =3
        self.__c__ =4

obj =Test()
print(obj._c)
print(obj.__c)
print(obj.__c_)
print(obj.__c__)
AttributeError: 'Test' object has no attribute '__c'. Did you mean: '_c'?

########
a =8.3
b =2
print(a//b)

ans: 4.0
########
a =5
b =2
print(a //b)

ans:2
########
def my_func(l1 =[]):
    l1.append('hi')
    print(l1)
my_func()
my_func()
my_func()

ans: ['hi']
['hi', 'hi']
['hi', 'hi', 'hi']

########
class Parent:
    x =1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
p =Parent()
c1 =Child1()
c2 =Child2()
print(p.x c1.x c2.x)
c1.x =2
print(p.x c1.x c2.x)
Parent.x =3
print(p.x c1.x c2.x)
c2.x =4
print(p.x c1.x c2.x)

ans: 1 1 1
     1 2 1
     3 2 3
     3 2 4

######## WIPRO Interview
what is set?
n =[1,4,5,6,7,9] n[2:16] what is output? and n[-16] what is output ?
what is meaning of .py and .pyc ?
difference between *args and *kwargs ?
how many data types in python?
what is difference between python3 and python2?
difference between floor division and division?
how many methods in request module? what is Put and Post method?
how to merge code in github?can you explain your process?
writre a program third highet value in given list?l =[1,2,4,5,6,8,9]?
can you explain one test case?

########## SmartSocs 
write a program to print 100 prime numbers?
what is black box testing ?
what is agile methdologie?
what is use of fixtures?what is use of conftest.py ?
write a program 123 -> 321  and -123 -> -321 ?

def reve(x):
    x=str(x)
    if x[0]=='-':
        a=x[::-1]
        return f"{x[0]}{a[:-1]}"
    else:
        return x[::-1]

print(reve("abc"))
print(reve(123))
print(reve(-123))

def reverse_integer(input_num):
    if input_num <0:
        value =-1
        input_num =abs(input_num)
    else:
        value = 1
    reverse_str =str(input_num)[::-1]
    reversed_num =int(reverse_str)
    reversed_num *= value
    return reversed_num
input_num1 =123
output_num =reverse_integer(input_num1)
print(output_num)
input_num2 =-123
output2_num =reverse_integer(input_num2)
print(output2_num)
The abs() function returns the absolute value of the specified number.

Q #45) What is the use of Assertions in Python?

Assert statement is used to evaluate the expression attached.
If the expression is false, then python raises an AssertionError Exception.

##### # Emphasis 
what is bitwise operator how many methods?
what is use of rightshift and liftshift operators?
what is ternary operator how many methods?
what is map and reduce?
what is lambda function?
write a program count the vowels in given string?
write a program  input s ="python automation chandra" expexted output is
v ="python noitamotua chandra"?
what is classmethod decorator and static method decorator?
what is method overloading and overriding?
how to convert tuple object to dictionary object it is posible?
what is use of enemurate function?
how to convert json file to string file?
what is fixtures?
what is use of xfail and skip?
how to rerun failed test case in pytest framework?
you create your own modules?


def change_string(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_string('abcd'))
print(change_string('12345'))



## virtusa
what is generator?
what is decorator?
what is list comphression and dictionary comphresion?
what is comphresion?
what is module and packages?
what is shallow copy and deep copy?
what is lamda function?
what is use of pass statement?

write a program to variable length argument?
def func1(*mylist):
    for i in mylist:
        print(i)
    return

func1(20,30,10)
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    return
 
myFun(first='Geeks', mid='for', last='Geeks')

write a program to sequence of numbers?
a = [i for i in range(100)]
print(a)


## capgemini
List1 =["apples","banana","apples","mangos","apples"]
List2 =["apples","banana","mangos"]
List3 =List1 - List2 substract elements in list?

res =[ele for ele in List1]
for a in List2:
    if a in List1:
        res.remove(a)
print(str(res))

l=[1,0,3,0,7,0,9,0,0,0]
l.sort()
print(l)
v =l[l.count(0)::]+l[:l.count(0)]
print(v)

##how to count of words in string?
n ="neelam chandra reddy"
s =len(n.split())
print(s)


#   altimax 
how many data types?
what is  memory management?
what is self keyword?
what is constructor?
what is name space and how many name spaces?
what is scope and how many scopes?
difference between iterators and generators?
what is decorator?
write a program to print 0,100 range values?

write a program for missing elements in given list?
l =[1,3,4,6,7,9,11,15]
n =[i for i in range(max(l)+1) if i not in l]
print(n)

write a program for count the vowels in string but return dictionary format?
def Check_Vow(string, vowels):
    string = string.casefold()
    count = {}.fromkeys(vowels, 0)
    for i in string:
        if i in count:
            count[i] += 1
            return count
vowels = 'aeiou'
string = "Hi, I love eating ice cream and junk food"
print (Check_Vow(string, vowels))

def vowels_count(input_string):
    vowels ="AEIOUaeiou"
    vowel_count=0
    for char in input_string:
        if char in vowels:
            vowel_count +=1
    return vowel_count
input_string ="Hello World"
result =count_vowels(input_string)
print(result)


what is fixture?

## innominds
what is meaning of decorator?
l1=[1,2,3,4,5],l2=['a','b','c','d','e'] return values in dictionary format?
s ="welcomepython" repeted elements return dictionary format?
s ="welcomepython"
d ={}
for i in s:
    d[i]=d.get(i,0)+1
print(d)

what is break,continue,pass statements?

The break statement is used to exit a loop prematurely, Once break is encountered, the
control exits the loop.

The continue statement is used to skip the rest of the current iteration of the
loop and move to the next iteration.

The pass statement is a null operation; it does nothing when executed.


##Harman
##write a program 10 floating numbers randomly?
##what is cat framework?
##what is jarvis foundation?

from random import random
lst =[]
for i in range(10):
    lst.append(random())
print(lst)

string ="audi infotainment com16"
new =string.split()
v =new[2]
print(v)

n =string.split()
print(n[-1])

class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
  
print()

s ="hi chandra welcome to bangalore"
v =s.split()
n =2
for i in range(n):
    v.append(v.pop(0))
##    v.insert(4,v.pop(0))
v.remove("hi")
print(" ".join(v))

##Capgemini
write a programm with out using inbuilt function Decending order in list?
defference between sort and sorted?
difference between iterator and generator?
what is dictionary comprahension write on exemple code?
write a python code with out using in built functions s ="PytHon" lower case letters in string?
write a programm for linear search in index position of value?
defect life cycle?
what is ord?
what is 4 pillar of oops concepts?
what is encapsulation?
what is abstraction?
what is abstract method?
how to search string by using regular expresion?
what is decerator ?
what is compile and search in regular expression?
what is regression and unit and system testing?

##############################################################

def linear_search(arr,target):
   for i in range(len(arr)):
      if arr[i] ==target:
         return i
   return -1
my_list =[1,4,6,8,9,7,10]
target_value =7
result =linear_search(my_list,target_value)
if result !=-1:
   print(f"target value {target_value}found at index{result}.")
else:
   print("target value not found in the list.")

##################################################################
   
def separate_lower_upper(s):
   lower_letter =""
   upper_letter =""
   for char in s:
      if 'a' <= char <='z':
         lower_letter +=char
      elif 'A' <= char <='Z':
         upper_letter +=char
   return lower_letter,upper_letter
s ="pYtHoN"
lowercase,uppercase =separate_lower_upper(s)
print(lowercase)
print(uppercase)


###################################################################

import re
def find_string(text,search_string):
   pattern =re.escape(search_string)
   match =re.search(pattern,text)
   return match
text ="this is a sample string to search in."
search_string ="sample"
result =find_string(text,search_string)
if result:
   print(result.start())
else:
   print(f"{search_string} not found in the text.")

##find string
text ="welcome to python world"
substring ="python"
index =text.find(substring)
if index != -1:
    print(f" '{substring}' found at index {index}")
else:
    print(f" '{substring}' not found")

############## Capgemini 2nd round 

########################################################
import datetime
current_time =datetime.datetime.now()
print(current_time)

##########################################################
##l =[1,2,3,4,5] using list comprehension print the stars in list?

l =[1,2,3,4,5]
v =["*"*i for i in l]
print(v)

##########################################################

l=[1,2,3,4,5]
x =0
y =-1
l[x],l[y] =l[y],l[x]
print(l)

######################################################
l =[1,2,3,1,1,2,4,5]
d ={}
for i in l:
    d[i] =d.get(i,0)+1
print(d)

################################
import re

pat = re.compile("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
test = pat.match(hostIP)
if test:
   print "Acceptable ip address"
else:
   print "Unacceptable ip address"


######reverse number
num =int(input("enter the number:"))
val =0
while num > 0:
     digits=num%10
     val=val*10+digits
     num =num//10
print("reverse number{}".format(val))
     
s=12345
n =""
for i in str(s):
   n =i+n
print(n)


##########globallogic
##reverse string
s ="welcome to python"
y =""
for i in s:
    y =i+y
print(y)

##write a programm common prefix and suffix element in list =["flowers","flow","floor"]
##expected output ="flo"

import os
strings =["flowers","flow","floor"]
common =os.path.commonprefix(strings)
print(common)

##Another method
def common_prefix(strings):
    if not strings:
        return ""
    shortest =min(strings,key =len)
    for i, char in enumerate(shortest):
        for string in strings:
            if string[i] != char:
                return shortest[:i]
    return shortest
strings =["flowers","flow","floor"]
prefix =common_prefix(strings) 
print(prefix)


####happiest minds
s ="hol pol mol lol pol hol nol pol mol"
n =s.split()
d ={}
for i in n:
    if i == 'pol' or i =='mol':
        d[i] =n.count(i)
print(d)

def find_triplets_sum_zero(nums):
    nums.sort()
    triplets =[]
    for i in range(len(nums)-2):
        if i > 0 and nums[i] ==nums[i-1]:
            continue
        left =i+1
        right =len(nums)-1
        while left < right:
            total =nums[i] + nums[left]+nums[right]
            if total ==0:
                triplets.append((nums[i],nums[left],nums[right]))
                while left < right and nums[left]==nums[left+1]:
                    left +=1
                while left < right and nums[left] ==nums[right-1]:
                    right -=1
                left +=1
                right -=1
            elif total <0:
                left +=1
            else:
                right -=1
    return triplets
nums =[-1,0,1,2,-1,-4]
result =find_triplets_sum_zero(nums)
print(result)

what is meaning inheritance?
what is self keyword?
class variable and instance variable?
how to run the testcases in pytest?
what use of skip in pytest?
what is fixture?
what is parameterize?
how many types of locators? which one is the fast in locators?
how to change dynamic xpath?

l =["sun","moon","sun"]
n =[[word,l.count(word)]for word in set(l)]
print(n)

##############maximum of second larget index position 
l =[1,5,4,8,9,7,3]
for i in range(len(l)-1):
     for j in range(len(l)-1):
          if l[j] >l[j+1]:
               l[j],l[j+1]=l[j+1],l[j]
print(l.index(l[-2]))


##what is try,except,finally,else?
####what is the testcases and test case seniors ?
##shallow copy and deep copy ?where it is use shallow copy and deepcopy?
##defect life cycle?
##prime number or not by using class method?

##linearsearch by using class method?
class LinearSearch:
    def __init__(self,data_list):
        self.data_list =data_list
    def search(self,target):
        for index,item in enumerate(self.data_list):
            if item ==target:
                return index
        return -1
data =[1,4,5,6,8,9]
searcher =LinearSearch(data)
target =8
result =searcher.search(target)
if result !=-1:
    print(f"target value {target_value}found at index{result}.")
else:
   print("target value not found in the list.")
 


























                    
                
        
        



































