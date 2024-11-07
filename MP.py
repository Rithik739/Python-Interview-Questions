                      ## Single inheritance
##class Parent:
##    def fun1(self):
##        print("this is function1")
##class Child(Parent):
##    def fun2(self):
##        print("this is function2")
##
##obj =Child()
##obj.fun1()
##obj.fun2C
                    ## Multiple inheritance
##class Parent1:
##    def car1(self):
##        print('this is car')
##class Parent2:
##    def van(self):
##        print('this is van')
##class Child(Parent1,Parent2):
##    def fun(self):
##        print('this is function')
##
##ob =Child()
##ob.car1()
##ob.van()
##ob.fun()
                      ##  Multilevel inheritance                    
##class Parent:
##    def fun1(self):
##        print('this is parent class')
##class Child(Parent):
##    def fun2(self):
##        print('this is child1 class')
##class Child2(Child):
##    def fun3(self):
##        print('this is child2 class')
##
##ob =Child2()
##ob.fun1()
##ob.fun2()
##ob.fun3()

                     ## Hierachical inheritance

##class Parent:
##    def fun(self):
##        print('this is parent class')
##
##class Child1(Parent):
##    def fun2(self):
##        print('this is child class')
##class Child2(Child1):
##    def fun3(self):
##        print('this is chil2 class')
##class Child3(Child2):
##    def fun4(self):
##        print('this is child3 class')
##
##obj1 =Child1()
##obj1.fun()
##obj1.fun2()
##
##obj2 =Child2()
##obj2.fun()
##obj2.fun3()
##
##obj3 =Child3()
##obj3.fun()
##obj3.fun4()

                       ## Hybrid inheritance
##class Parent:
##    def fun_info(self):
##        print('this is hybrid inheritance')
##class Child1(Parent):
##    def fun2_info(self):
##        print('this is child class')
##class Child2(Parent):
##    def fun3_info(self):
##        print('this is child2 class')
##class Child3(Child1,Parent):
##    def fun4_fun2_info(self):
##        print('this is child4 class')
##
##ob =Child3()
##ob.fun_info()
##ob.fun2_info()
##ob.fun4_fun2_info()
##
#### Count the characters in string
##
s =input("enter the string:")
total =0
for i in s:
    total =total+1
print(total)


##string="hello how are you"
##new_string="" 
##for i in range(len(string)): 
##   if i==0: 
##        new_string+=string[i].upper() 
##   else: 
##        new_string+=string[i] 
##print(new_string) 

##s ='programming'
##x =''
##for i in s:
##    if i.islower():
##        i =i.upper()
##    else:
##        i =i.lower()
##    x +="".join(i)
##print(x)


##people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
##          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
##print(people[1].get('name'))
##for k,v in people.items():
##   for k1,v1 in v.items():
##      print(k1)
      


##Liverpool = {
##    'Keepers': {'Loris Karius': 1, 'Simon Mignolet': 2, 'Alex Manninger': 3},
##    'Defenders': {'Nathaniel Clyne': 3, 'Dejan Lovren': 4, 'Joel Matip': 5, 'Alberto Moreno': 6, 'Ragnar Klavan': 7,
##                  'Joe Gomez': 8, 'Mamadou Sakho': 9}
##}
##
##
##for k, v in Liverpool.items():
##    for k1, v1 in v.items():
##        print(v1)
##

s =12345
n =0
for i in str(s):
   n=n+int(i)
print(n)


def findsum(num):
   if num ==0:
      return 0
   return int(num%10)+findsum(num/10)
num =12345
print(findsum(num))

##Reverse number
s=12345
n =""
for i in str(s):
   n =i+n
print(n)

Pickling: The process of converting a Python object (like lists, dictionaries,
etc.) into a byte stream so that it can be saved to a file or transferred over
a network.
Unpickling: The inverse process, where the byte stream is converted back into
the original Python object.

##
s ='python learn'
v =''
for i in range(len(s)):
   if  not i%2:
      v =v+s[i].upper()
   else:
      v=v+s[i].lower()
print(v)

Method Resolution order is used in inheritance concepts
where class is inheriting multiple class and in all the parent class, same
method is defined. Child class is confused which method to call during run time.
So the MRO helps to resolve the issue.

l =["apple","Google","msft"]
def has_unique_chars(word):
    return len(set(word.lower()))== len(word)
unique_words =[word for word in l if has_unique_chars(word)]
print(unique_words)

##Find minimum of 3 numbers using lambda function
mini_of_three =lambda a,b,c:min(a,b,c)
result =mini_of_three(4,3,2)
print(result)

##Find all the elements that appears more than once.
##find all duplicates in an arrayii
arr = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 1, 9, 1]
d ={}
for i in arr:
    d[i]=d.get(i,0)+1
print(d)
duplicate =[i for i,v in d.items() if v > 1]
print(duplicate)

##Write a function to check if two strings are rotations
##of each other str="abcd",str2="cdab"
def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    concatenated = str1 + str2
    return str2 in concatenated
str1 = "abcd"
str2 = "cdab"
if are_rotations(str1, str2):
    print(f"'{str1}' and '{str2}' are rotations of each other.")
else:
    print(f"'{str1}' and '{str2}' are not rotations of each other.")
    
##l =[1,2,3,4,5]
##x =0
##y =-1
##l[x],l[y] =l[y],l[x]
##print(l)
##

##s ="PYThon"
##v =s.swapcase()
##print(v)

##  Missing elements
l =[1,3,4,6,7,9,11,15]
n =[i for i in range(max(l)+1) if i not in l]
print(n)

missing_element = [x for x in range(l[0], l[-1]+1) if x not in l]
print(missing_element)

## Missing elements
def find_missing_element(lst):
    n =len(lst)+1
    expected =n * (n+1)//2
    actual =sum(lst)
    missing =expected - actual
    return missing
my_list =[1,2,3,4,5,6,8,9,10]
result =find_missing_element(my_list)
print(result)

l =[1,2,3,4]
res =[(l[i],l[i+1]) for i in range(len(l)-1)]
print(res)
n =[(l[i],l[i+1],l[i+2]) for i in range(len(l)-2)]
print(n)

d1 ={"a":100, "b":200, "c":400}
d2 ={"a":300, "b":200, "d":400}
d3 ={}
for key in d1.keys() | d2.keys():
    d3[key] =d1.get(key,0) + d2.get(key,0)
print(d3)

l =["apple", 1, "mango", 2]
d ={l[i]:l[i+1] for i in range(0,len(l),2)}
print(d)

def compress_string(s):
    result =[]
    count =1
    for i in range(1,len(s)):
        if s[i] ==s[i -1]:
            count +=1
        else:
            result.append(s[i -1] + str(count))
            count =1
    result.append(s[-1] + str(count))
    return "".join(result)
a ="aaaabbbbbccdddd"
output =compress_string(a)
print(output)

s ="aaaaabbbccccc"
d ={}
for i in s:
    d[i]=d.get(i,0)+1
output = ''.join(f"{key}{value}" for key, value in d.items())
print(output)

input ="mamadsfajsdmalayalamasdsafmadam"
def is_palindrome(s):
    return s == s[::-1]
def find_palindromes(s):
    palindromes = list()
    n = len(s)
    # Check all substrings
    for i in range(n):
        for j in range(i+2, n+1):  # Substrings of at least 3 characters
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.append(substring)
    
    return sorted(palindromes, key=len)

I = "mamadsfajsdmalayalamasdfsafmadam"
output = find_palindromes(I)
print(output)

        

######################################
def count_character(s,char):
    count =0
    for i in s:
        if i ==char:
            count +=1
    return count
s ="programms"
sub_string ="m"
print(count_character(s,sub_string))
####################################
s ="programms"
count =0
for i in s:
    if i =="m":
        count +=1
print(count)

##convert dictionary to list comprehension?
dict ={"red":5, "blue":23, "black":35}
d =[[key,value] for key,value in dict.items()]
print(d)
################################################
source_file ="file1.txt"
destination_file ="file2.text"
with open(source_file,'r') as source_file:
    content =source_file.read()
with open(destination_file,'w') as destination_file:
    destination_file.write(content)
print(f"contents from {source_file) have been copied to {destination_file}")
########################################
import re
def search_pattern_in_file(file_path,pattern):
    try:
        with open(file_path,'r') as file:
            content =file.readlines()
        if re.search(pattern,content):
            return True
        else:
            return False
    except FileNotFoundError:
        print(f"the file {file_path} does not exist.")
        return False
file_path ="example.txt"
pattern =r'interview_word_in_file_path"
if search_pattern_in_file(file_path,pattern):
    print(f"the pattern '{pattern}' was found in the file '{file_path}'.")
else:
    print(f"the pattern '{pattern}' was not found in the file '{file_path}'.")

######################################################    
def hamming_distance(s1,s2):
    if len(s1) != len(s2):
        raise ValueError ("string must be same length")
    distance =sum(1 for a,b in zip(s1,s2) if a != b)
    return distance
s1 ="hello world"
s2 ="hello world"
difference =hamming_distance(s1,s2)
print(difference)

#######################################
def check_all_vowels_present(s):
    vowels =set('aeiou')
    s =s.lower()
    present_vowels ={char for char in s if char in vowels}
    if vowels <= present_vowels:
        return "all the vowels are present"
    else:
        return "not all vowels are presents"
n ="this are flour"
output =check_all_vowels_presents(n)
print(output)

############################################
n =int(input("enter the number"))
x =[]
for i in range(n):
   x.append(i)
print(x,end=" ")

l=[0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81,
 82, 83, 84, 85, 87, 88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100]
n =[i for i in range(max(l)+1) if i not in l]
print(n)


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


s ="ABCDE"
t =[s[i:j] for i in range(len(s)+1) for j in range(i+1,len(s)+1)]
print(t)

l1 =[1,2,3,4,5]
l2 =['a','b','c','d','e']
l3 ={key:value for key,value in zip(l2,l1)}
print(l3)

sample =[('A',76),('B',77),('c',70),('d',80)]
sample.sort(key=lambda a:a[1])
print(sample)

d ={"telugu":75,"english":80,"maths":90,"social":82}
n =[key for key,value in d.items() if value == max(d.values())]
print(n)

new_string = "Germany26China47Australia88"
emp_str = ""
for m in new_string:
    if m.isdigit():
        emp_str = emp_str + m
print("Find numbers from string:",(emp_str))
print(new_string.split()[1::2])

from itertools import zip_longest
l1=[1,2,3,4,5,6,7]
l2=['a','b','c','d']
d1=zip_longest(l1,l2,fillvalue='x')
print (d1)#Output:<itertools.zip_longest object at 0x00993C08>
#Converting zip object to dict using dict() contructor.
print (dict(d1))
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'x', 6: 'x', 7: 'x'}


##reversing string in recursive function

def reverse_string(text):
    if len(text) ==1:
        return text
    return reverse_string(text[1:])+text[:1]

print(reverse_string("welcome world"))


s ="python"
y =""
for i in s:
    y =i+y
print(y)

v =[1,2,3,4]
y =[]
for i in v:
    y =[i]+y
print(y)

l =[1,2,3,4,5]
reve_list =[]
for i in reversed(l):
    reve_list.append(i)
print(reve_list)


def reverseword(sentence):
    return (" ".join(word[::-1] for word in sentence.split()))
sentence ="welcome to python world"
print(reverseword(sentence))

sentence ="welcome to python world"
v =sentence.split()[::-1]
n =[]
for i in v:
    n.append(i)
print(n)


for i in sentence.split():
    print("".join(i[::-1]),end=" ")


string ="hello 12 hi 899 howdy 345"
print(string.split()[1::2])

li =["apple","mango","bananas","kiwi","orange"]
##li.sort(key=len)
print(li)

##remove repeted values in list
def remove_all_occurence(list_obj,value):
    while value in list_obj:
        l.remove(value)
        
l =[1,2,2,4,5,6,4,5,2,2,3]
remove_all_occurence(l,2)
print(l)

##l =[1,2,2,4,5,6,4,5,2,2,3]
##n =2
##for i in l:
##    if i != n:
##        print(i,end=" ")

n =2
x =[i for i in l if i!= n]
print(x)

## write a program addition in class method
class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def forward(self):
        return self.x+self.y

a =Add(5,6)
print(a.forward())

##################################
class empl:
    def a(*arg):
        print(sum(arg))

def a(*arg):
    print(sum(arg))
a(1,2,3,4)
empl.a(7,8)

string_count ="@hdnlb$r&"
d ={char:string_count.count(char) for char in string_count if char.isalnum()}
for key,value in d.items():
    print(f"Characters '{key}'occurs {value} times.")

## write a program prime number or not

num =int(input("enter the number:"))
if num >1:
   for i in range(2,num):
      if num%i ==0:
         print(num,"is not a prime number")
         break
   else:
      print(num,"is a prime number")
else:
   print(num,"is not a prime number")
   
##write a program
   
l =[1,0,3,0,7,0,9,0,0,0]
l.sort()
print(l)
v =l[l.count(0)::]+l[:l.count(0)]
print(v)

import re
def isvalid(s):
   pattern =re.compile("(0|91)?[6-9][0-9]{9}")
   return (pattern.match(s))
s ="5849644691"
if isvalid(s):
   print("valid number")
else:
   print("invalid number")
   
l =[1,2,3,4,5]
n =2
x =l[-n::]
print(x)

def change_string(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_string('abcd'))
print(change_string([1,2,3,4,5]))

lt1 = [5, 10, 15, 20, 25, 30]  
lt2 = [2, 4, 6, 8, 10, 12]
res_lt = [] 
for x in range (0, len (lt1)):  
    res_lt.append( lt1[x] + lt2[x])    
print ( " Addition of the list lt1 and lt2 is: " + str (res_lt))


    
Software development can be challenging to manage due to changing requirements,
technology upgrades, and cross-functional collaboration. The software
development lifecycle (SDLC) methodology provides a systematic management
framework with specific deliverables at every stage of the software development
process. As a result, all stakeholders agree on software development goals and
requirements upfront and also have a plan to achieve those goals.

Here are some benefits of SDLC:

Increased visibility of the development process for all stakeholders involved
Efficient estimation, planning, and scheduling
Improved risk management and cost estimation
Systematic software delivery and better customer satisfaction
How does SDLC work?
The software development lifecycle (SDLC) outlines several tasks required to
build a software application. The development process goes through several
stages as developers add new features and fix bugs in the software.

The details of the SDLC process vary for different teams. However, we outline
some common SDLC phases below.

Plan
The planning phase typically includes tasks like cost-benefit analysis,
scheduling, resource estimation, and allocation. The development
team collects requirements from several stakeholders such as customers,
internal and external experts, and managers to create a software requirement
specification document.

The document sets expectations and defines common goals that aid in project
planning. The team estimates costs, creates a schedule, and has a detailed
plan to achieve their goals.

Design
In the design phase, software engineers analyze requirements and identify
the best solutions to create the software. For example, they may consider
integrating pre-existing modules, make technology choices, and identify
development tools. They will look at how to best integrate the new software
into any existing IT infrastructure the organization may have.

Implement
In the implementation phase, the development team codes the product.
They analyze the requirements to identify smaller coding tasks they can do
daily to achieve the final result.

Test
The development team combines automation and manual testing to check the
software for bugs. Quality analysis includes testing the software for errors
and checking if it meets customer requirements. Because many teams immediately
test the code they write, the testing phase often runs parallel to the
development phase.

Deploy
When teams develop software, they code and test on a different copy of the
software than the one that the users have access to. The software that
customers use is called production, while other copies are said to be in
the build environment, or testing environment.

Having separate build and production environments ensures that customers can
continue to use the software even while it is being changed or upgraded. The
deployment phase includes several tasks to move the latest build copy to the
production environment, such as packaging, environment configuration, and
installation.

Maintain
In the maintenance phase, among other tasks, the team fixes bugs, resolves
customer issues, and manages software changes. In addition, the team monitors
overall system performance, security, and user experience to identify new ways
to improve the existing software.



