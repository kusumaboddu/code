# input function

##a =  input("enter a number")
##print(a)
##print(type(a))

##print(10 , end = "")
##print(20)

# strings
##tech = "python"
##print(tech[2])
##print(tech[5])
##print(tech[-3])
##print(tech[-1])

##tech = "Python and Django"
##print(tech[1:8])
##print(tech[3:20:1])
##print(tech[3:20:2])
##print(tech[3:])
##print(tech[:15])

##print(tech[20:3:-1])
##print(tech[:3:-1])
##print(tech[20::-1])
##print(tech[::-1])

# immutable
# XX   change XX deletion XX addition 

##print(tech)
##del tech
##print(tech)

##special chars
##-------------
##\n newline  \t  tabspace

##name = "python \n Lync \t digital"
##print(name)

##escape chars
##------------
##\ %

##stmt = "i'm in a python class"
##print(stmt)
##
##stmt = 'i\'m in a python class'
##print(stmt)
##
##path = "c\programs\python\code\\new\\technology"
##print(path)

##raw strings
##-----------
##path = r"c\programs\python\code\new\technology"
##print(path)

##unicode strings
##---------------
##<docs>

##string literals
##---------------

##%d integer , %s string , %f float
##-> dynamic data  , queries in DB
##
##name = "khan"
##marks = 60

##print("khan has secured 60 marks")
##print("%s has secured %d marks  " %(name , marks))
##
##print("khan has secured 60 % marks")
##print("%s has secured %d %% marks  " %(name , marks))


##name = "khan"
##marks = 60

##newvar = name + marks
##newvar2 = name , marks
##print(name , marks)
##
##newvar3 = name + str(marks)
##print(newvar3)

##membership identity

##in ,not in
##is ,is not


##name = "python is an easy language"
##print("i" in name)
##print("in" in name)
##print("python" not in name)
##print("python is an easy language" in name)
##

##name = "python"
##print(name is "python")
##print(name is not "Python")

##book = "first \n second \n third "
##print(book)

##multi line strings
##<strname> = '''
##<data> 
##'''

##book = ''' first
##second
##third
##fourth
##'''
##print(book)


#comments
#--------
#skip execution
##a = 10
#print(a)

'''
<multi line comments>

'''

##functions in strings
##--------------------

##-> attribute fetching (.)
##-> parameterised (<something>)

##-> case based
##   lower()
##   upper()
##   swapcase()
##   capitalize()
##   title()
##   
##-> checking
##   startswith
##   endswith 
##-> operational
##   len()
##   index()
##   find()
##   count()
##   strip() , lstrip() , rstrip()
##   join()
##   split()
##   replace()
##   zfill()

##name = "python is an Easy Language"
##print(name.lower())
##print(name.upper())
##print(name.swapcase())
##print(name.capitalize())
##print(name.title())
##print(name)

##print(name.startswith("p"))
##print(name.startswith("python"))
##print(name.startswith("p"))
##
##print(name.endswith("Language"))
##print(name.endswith("e"))
##print(name.endswith("z"))


##print(len(name))
##<strname>.count(<char / substring>)
##print(name.count("a"))
##print(name.count("is"))
##print(name.count("and"))

##print(name.index("a"))
##print(name.index("a" , 11))
##print(name.index("a" , 15))
##print(name.index("is"))
##print(name.index("and"))

##print(name.find("a"))
##print(name.find("a" , 11))
##print(name.find("a" , 15))
##print(name.find("is"))
##print(name.find("and"))

##name = "  in india we do live  "
##print(name)
##print(name.strip())
##print(name.strip(" i"))
##print(name.strip(" in"))
##print(name.lstrip())
##print(name.rstrip())

##stmt  = "python is easy and is used is devops is IT "
##print(stmt.replace("is" , "out"))
####stmt = stmt.replace("is" , "out")
##print(stmt.replace("is" , "out"),2)
##print(stmt)

##join and split 
##<strname>.split(<delimiter>)
##print(stmt.split()) # default delimiter = " "
##print(stmt.split("a")) # delimiter = "a"
##words = stmt.split()
##print(words)
##
####<delimiter>.join(<collection>)
##newstmt = "-".join(words)
##print(newstmt)

##zfill() --> zero fill --> only str

##0  0  0
##1  1  1
##2  4  8
##3  9  27
##4  16 64
##5  25 125 

##<strname>.zfill(<charlen>)
##a = "python"
##print(a.zfill(10))
##a = 100
##print(str(a).zfill(10))


##conditional statements
##----------------------

##descision trees
##   --> condition ---> T/f 
##   --> statement

##syntax
##------
##if <condition>:
##   <statement>
##   
##if (<condition>):
##   <statement>
##else:
##   <statement2>
##
##
##if (<condition1>):
##   <statement1>
##elif <condition2>:
##   <statement2>
##elif (<condition3>):
##   <statement3>
##elif <condition4>:
##   <statement4>
##else:
##   <statement5>

##if <condition>:
##   if <condition2>:
##      <statement1>
##      <statement11>
##   else:
##      <statement2>
##else:
##   <statement3>

##a = 2
##
##if a >5 :
##   print("5")
##elif a>7 :
##   print(7)
##elif a==10:
##   print(10)
##else:
##   print("no")

##if a== 10 :
##   pass
##else:
##   print("not equals")


##isdigit() isnumeric()
##even odd
##num = input("enter a number : ")
##
##if num.isdigit():
##   num = int(num)
##   if num%2 == 0 :
##      print("%d is a %s number" %(num, "even"))
##   else:
##      print("%d is a %s number" %(num, "odd"))
##else:
##   print("enter only numbers")
##
##user --> n
##n is multiple of 3 only
##n is multiple of 5 only
##n is multiple of 3 and 5 
##
##3
##3 is multiple of 3 only
##5
##5 is multiple of 5 only
##30
##30 is multiple of 3 and 5  
##4
##not a multiple of 3 and 5
##
##
##


##num = input("enter a number : ")
##
##if num.isdigit():
##   num = int(num)
##   if num%3 == 0 and num%5 == 0  :
##      print("%d is a %s number" %(num, "both"))
##   elif num%5 == 0 :
##      print("%d is a %s number" %(num, "5 mul"))
##   elif num%3 == 0  :
##      print("%d is a %s number" %(num, "3 mul"))
##   else:
##      print("none")
##else:
##   print("enter only numbers")


##stmt = input("enter your smt ")
##stmt = stmt.lower()
##if ( "a" in stmt )or 


## looping structures
##--> reduce repititions
##--> minimal coding 
##
##--> finite (for while) vs infinite (while for(collections))
##
##--> for , while
##   --> numbers
##   --> strings
##   --> collections
##
##-> initilisation
##-> limit / condition
##-> statement
##-> inc /dec
##
##for (i = 0 ; i <=10 ; i ++){
##
##<statements >
##
##   }
##
##
##for with numbers 
##-> range()
##range(<end>) ---> 0 ----  end -1
##range(<start> , <end>) ---> start----  end -1
##range(<start> , <end> , <step>) ---> start , start + step----  end -1
##
##
##syntax:
##-------
##for <dummy> in range(<end>):
##   <statements>

##for i in range(10): # 0 ...... 9 i = 0  ; i<10 ; i++
##   print(i)
##print("-------------------")
##
##for i in range(5,30): # 5...... 29 i = 5  ; i<30 ; i++
##   print(i)
##
##print("-------------------")
##for i in range(5,100 , 5): # 5 ...... 95 i = 5  ; i<100 ; i = i+5
##   print(i)
##
##print("-------------------")

##for i in range(10,1, -1): # i = 10 i>1 i--
##   print(i)

# empty loop using pass
##for i in range(10,1, -1): 
##   pass   

##while with numbers
##syntax
##------
##<initialisation>
##while <condition>:
##   <statements>
##   <inc/dec>

##i = 0
##while i<10:
##   print(i)
##   i = i + 1

##i = 10
##while i>=1:
##   print(i)
##   i = i - 1

##i = 10
##while i == 10:
##   print(i)

##while True:
##   print("hello")

##patterns
##--------
##for
##n ---> 4
##
##*
##**
##***
##****

##print("*" * 1 )
##print("*" * 2 )
##print("*" * 3 )
##print("*" * 4 )
##
##n = int(input("enter number : "))
##for i in range(1,n+1):
##   print("*" * i)

##1
##22
##333
##4444
##55555
##

##for i in range(1,5):
##   print(str(i) * i)
##   
##    *
##   **
##  ***
## ****
##*****
##print((" " * 4)+ ("*" * 1))
##print((" " * 3)+ ("*" * 2))
##print((" " * 2)+ ("*" * 3))
##print((" " * 1)+ ("*" * 4))
##print((" " * 0)+ ("*" * 5))

##for i in range(5,1,-1):
##   print((" " * i ) + ("*" ) * (5-i)) 

##n -- 5
##a
##bb
##ccc
##dddd
##eeeee
##
##n -- 5
##a
##ab
##abc
##abcd
##abcde
##n-->4
##1
##12
##123
##1234
##
##for i in range(1,1):
##   print(i , end = "")
##print()
##for i in range(1,2):
##   print(i , end = "")
##print()
##for i in range(1,3):
##   print(i , end = "")
##print()
##for i in range(1,4):
##   print(i , end = "")
##print()
##for i in range(1,5):
##   print(i , end = "")

##for j in range(1,6):
##   for i in range(1,j):
##      print(i , end = "")
##   print()

##n --> 5
##5 X 1 = 5
##5 X 2 = 10
##5 X 3 = 15
##5 X 4 = 20
##5 X 5 = 25
##5 X 6 = 30
##5 X 7 = 35
##.
##.
##5 X 10 = 50
##n = 5

##for i in range(1,11):
##   print(" %d X %d = %d" %(n,i,n*i))

##n = 5
##000 000 000
##001 001 001
##002 004 008
##003 009 027
##004 016 064
##005 025 125

##s = 6
##e = 50
##
##6 --> even
##7 --> odd
##8 --> even
##.
##.
##.
##..
##50 --> even

##n = 5
##54321
##4321
##321
##21
##1

##n = 5
##
##for i in range(97 , 97+n ):
##   print(chr(i) * ((i-97)+1))

##s = "abcdefgh"
##n= 7
##for i in range(0,n+1):
##   print(s[i] * (i+1))
##   
   
##a
##ab
##abc
##abcd

##control stamts

##pass break continue
##pass --> everywhere
##break , continue --> loops 
##
##condition
##break --> exit loop at condition ==true 
##
##continue --> pause loop at condition ==true and resumes the execution 

##for i in range(20):
##   if i == 5:
##      break
##   print(i)
##
##for i in range(20):
##   print(i)
##   if i == 5:
##      break
##   

##
##for i in range(20):
##   if i == 5:
##      continue
##   print(i)


##for with strings
##----------------

##tech = "python and data"
##for i in range(len(tech)):
##   print(tech[i])

##for ch in tech:
##   print(ch)

##stmt = "iam in a python session"
##iam in a pyt
##iam in a pyton session

##for i in stmt:
##   if i is "h":
##      break
##   print(i , end="")
##
##print()
##for i in stmt:
##   if i is "h":
##      continue
##   print(i , end="")

##dia = "i have secured 7 marks 8 perc "
##i have secured 
##i have secured marks 

##for ch in dia:
##   if ch.isdigit():
##      break
##   print(ch , end="")
##   
##print()
##for ch in dia:
##   if ch.isdigit():
##      continue
##   print(ch , end="")
##
##
##prime composite -->
##
##n = 13 ---> prime 1, 13
##n= 12 --> composite 1 2 3 4 6 12
##n= 19 --> prime 1 19
##n = "abc" --> wrong input 

##12 % 1 == 0
##12 % 2 == 0
##12 % 3 == 0
##12 % 4 == 0
##12 % 5 == 2
##12 % 6 == 0
##.
##.
##.
##.
##12 % 12 == 0
##n = 12
##count = 0 
##for i in range(1,n+1):
##   if(n%i == 0 ):
##      count = count + 1
##      print(i)
##print("total factors : " + str(count))
##
##if count == 2 :
##   print("prime")
##else:
##   print("composite")

##10 - composite 1,2,5,10
##11 - prime 1,11
##.
##.
##.
##.
##30 - composite 1,2,3,5,6,10,15,30
##st = 10
##en = 20
##for j in range(st,en+1):
##   count = 0 
##   for i in range(1,j+1):
##      if(j%i == 0 ):
##         count = count + 1
##         print(i , end = " ")
##   print("total factors : " + str(count))
##
##   if count == 2 :
##      print(str(j) +" is prime")
##   else:
##      print(str(j) +" is composite")

##n = 5
##000 000 000
##001 001 001
##002 004 008
##003 009 027
##004 016 064
##005 025 125


##zfill()

##n= 8
##l = len(str(n**3))
##for i in range(1,n+1):
##   print("%s %s %s" %(str(i).zfill(l) , str(i**2).zfill(l) , str(i**3).zfill(l)))

##   *
##  ***
## *****
##*******
##
##dia = "iam in a python class"
##a --> 3
##a --> 1 , 7 , 18

##c = 0 
##for i in dia:
##   if dia.count(i) > c:
##      c = dia.count(i)
##      print(i)


##collections / sequences
##------------------------
##lists
##tuples
##dictionaries
##
##
##sets
##frozensets
##
##
##
##lists
##-----
##--> MUTABlE
##--> duplicate
##--> i c i s
##--> <class list>
##--> nested lists
##
##
##syntax
##------
##<listname> = [<ele> , <ele2> , <ele3>]
##nums = [1,2,3,4,5,6]
##print(nums)
##print(type(nums))
##
##chars = ["a" , "python"]
##print(chars)
##print(type(chars))
##
##ml = [2,3,4,"a" , "python"]
##print(ml)
##print(type(ml))

##ll = [100,200,300, "abc" , [2,3,4,"a" , "python"] , 1000, 11, 100]
##print(ll)
##print(ll[2])
##print(ll[4][3])
##
##il = [[[[[[[[[[[[[[[10]]]]]]]]]]]]]]]
##print(il[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0])

##print(type(ll))

##accessing / modifying elemets
##-----------------------------
##<listname>[<index>]

##print(ll[0])
##print(ll[3])
##print(ll[4])
##print(ll[6])

##print(ll[0:3]) # 100 200 300 
##print(ll[1:6]) 
##
##print(ll[:4])
##print(ll[2:])

##<listname>[<index>] = <newvalue>
##print(ll)
##ll[3] = "java"
##print(ll)
##ll[0:3] = "ab" , "abcD" , "def"
##print(ll)

##print(ll)

##deleting of elements
##--------------------
##del 

##del <listname>[<index>]
##del ll[3]
##del ll[0]
##del ll[0:5]
##print(ll)
##
##del ll
##print(ll)

##for with collections(lits)
##--------------------------
##for <dummy> in <listname>:
##   <statements>
   
##for elems in ll:
##   print(elems)

##for i in range(8):
##   print(ll[i])
##
##print(100 in ll)
##print(3000 in ll)
##print("python" not in ll)


##functions
##----------

##print(len(ll))
##print(ll.count(100))
##print(ll.count(1))
##print(ll.index("abc"))
##newll = ll.copy()
##print(newll)
##ll.clear()
##print(ll)

##append() --> add elemems at last 

##ll.append("java" )
##print(ll)
##ll.append(1319 )
##print(ll)

##ll.insert(3,"java")
##print(ll)

##ll.pop()
##print(ll)
##ll.pop()
##print(ll)
##ll.pop()
##print(ll)
##ll.pop()
##print(ll)

##ll.remove(100)
##print(ll)
##ll.remove("abc")
##print(ll)

##.sort() ---> asc
##   homogeneous
##   

##l1 = [5,7,3,4,5,7,8,23,34,2,3,43,545,17]
##l1.sort()
##print(l1)
##l1.sort(reverse = True)
##print(l1)
##
##ch =["python" ,"java" , "c" , "php" , "angular"]
##ch.sort()
##print(ch)
##ch.sort(reverse = True)
##print(ch)


##nums = [1,2,3,5,1,4,2,34,45,7,3,4,5,7,8,23,34,2,3,43,545,17]
##uni = []

##print(1 in nums)
##print(1 not in uni)

##for i in nums:
##   if i not in uni:
##      uni.append(i)
##print(uni)
##uni.sort(reverse = True)
##print(uni[1])

##dia = "iam in a python session"
##lw = []
##words = dia.split()
##print(words)
##for i in words:
##   lw.append(len(i))
##print(lw)

##bigwords = []
##for i in words:
##   if len(i) > 5:
##      bigwords.append(i)
##print(bigwords)



##range(1,10)
##sq --> [1,4,9,16,. . . . 100]

##sq =[]
##for i in range(1,11):
##   sq.append(i**2)
##print(sq)

##range(1,30)
##[4,16,36,64,100 ......900]

##esq = []
##for i in range(1,31): # 1 2 3 4 5 30
##   if i%2 == 0 :
##      esq.append(i**2)
##print(esq)


##esq = []
##for i in range(0,31,2): # 0 2 4 6 8
##      esq.append(i**2)
##print(esq)

##l = [6,8,9,[100,200,400,"abc"],1000,"python",[1,2,3]] # int , str , list
##
####o = [6,8,9,100,200,400,"abc",1000,"python",1,2,3] # int , str 
##o = []
##for i in l:
##   if type(i) is not list  : #  6 8 9 1000 python 
##      o.append(i)
##   else:
##      for j in i: # [100,200,400,"abc"]
##         o.append(j)
##print(o)
##


##l1 = [1,2,3]
##l2 = [10,20,30]
##ol = []
##
##if len(l1) == len(l2):
##   for i in range(len(l1)): # 0, 1, 2
##      ol.append(l1[i] + l2[i])
##   print(ol)  
##else:
##   print("not equal lists")

##[11,22,33]

##for i,j in l1,l2: # XX python XX
   
##for i in l1:
##   for j in l2:
##      ol.append(i+j)
##print(ol)

##tech =["c","c++","python" , "java" , "php" , "angular" , "node"] # elements 
##n = [0,2,5] # indices 

##ol ---> ["c" , "python" , "angular"] # elements 

##ol =[]
##for i in n:
##   ol.append(tech[i])
##print(ol)

##making of a list 

mylist =[]
##enter no of elements 
##4
##
##enter your element
##100
##enter your element
##200
##enter your element
##300
##enter your element
##4000
##
##[100,200,300,4000]

##mylist =[] # making an empty list 
##l = int(input("enter length of list you need: "))
##
##for i in range(l):
##   ele = int(input("enter your element "))
##   mylist.append(ele)
##
##print(mylist)


##stmt = "i have secured  7 marks in 3 techs"
##ol --> [7,3]
##
##tech = "abcde"
##ol --> ["a" , "ab" , "abc" , "abcd" , "abcde"] 
##
##
##list comprehensions
##-------------------
##
##--> l1 = [1,2,3,4,. . .. 10]
##--> l2 = [1,4,9,16 . . .100]
##--> l3 = [2,4,6,8]
##--> l4 = [4,16,36,64]

##l1 = [] # initialisation
##for i in range(1,11): # iteration 
##   l1.append(i) # assignment
##print(l1)
##
##l2 = [] #initialisation
##for i in range(1,11): # iteration
##   l2.append(i**2) # assignment + operation
##print(l2)
##
##l3 = [] #initialisation
##for i in range(1,11): # iteration
##   if i % 2 == 0 : # condition
##      l3.append(i) # assignment 
##print(l3)
##
##l4 = [] #initialisation
##for i in range(1,11): # iteration
##   if i % 2 == 0 : # condition
##      l4.append(i**2) # assignment + operation
##print(l4)


##
####<listname> = [<dummy> <iteration>]
##l1 = [ x  for x in range(1,11)]
##print(l1)
##
####<listname> = [<dummy + operation> <iteration>]
##l2 = [i**2  for i in range(1,11)]
##print(l2)
##
####<listname> = [<dummy> <iteration> <condition>]
##l3 = [i for i in range(1,11) if i%2==0]
##print(l3)
##
####<listname> = [<dummy + operation> <iteration> <condition>]
##l4 = [i**2 for i in range(1,11) if i%2 == 0 ]
##print(l4)

##tuples
##------
##-> heterogeneous
##-> I S I C
##-> duplicate
##-> infinite
##-> 1XN
##-> default collections
##-> IMMUTABLE
##-> <class tuple>
##
##syntax
##------
##<tuplename> = (<ele1> ,<ele2> , <ele3> , <ele4>)
##nums = (1,2,3,4,5,90)
##print(nums)
##print(type(nums))

##
##a , b , c = 100,200,1319
##print(a)
##print(b)
##print(c)


##a = 100
##b = 200
##print(a)
##print(b)


##a = 100,200,300, 
##print(a)
##print(type(a))

##mt = (100,400,23,"java","python" , 900)
##print(mt[0])
##print(mt[3])
##print(mt[5])
##print(mt[2])
##
##print(mt[0:3])
##print(mt[:4])
##print(mt[4:])

##tt = (100,[400,23],120,("java","python" ,1200,400) , 900)
##
##1200
##java
##23
##900

##print(tt[3][2])
##print(tt[3][0])
##print(tt[1][1])
##print(tt[4])

##for i in tt:
##   print(i)

##t1 = (10,20,30)
##t2 = (200,400,900,100)
####print(t1+t2)
##t3 = t1 + t2
##print(t3)

##tt = (100,[400,23],120,("java","python" ,1200,400) , 900)
# int list tuple 
##[100,400,23,120,"java","python" ,1200,400 , 900]
# int str 
##op =[]
##for i in tt:
##   if type(i) is int or type(i) is str: # int str 
##      op.append(i)
##   else: # list tuple
##      for j in i:
##         op.append(j)
##         
##print(op)

##tt[0] = "1000"
##print(tt)

##del tt[0]
##print(tt)

##del tt
##print(tt)

##len()  , count() , index()
##
##len(<tuplename>) --> total element count 
##<tuplename>.count(<elemnet>) --> frequency of element 
##<tuplename>.index(<elemnet>) --> index value

##print(len(tt))
##print(tt.count(100))
##print(tt.index(900))
##


##tuple ---> list --> list()
##modify
##list --> tuple  --> tuple()

##fees = (20 , 30 ,40 ,50)
##
##print(fees)
####print(type(fees))
##fees = list(fees)
####print(fees)
####print(type(fees))
##fees[1] = 35
##fees = tuple(fees)
##print(fees)
##print(type(fees))

##stmt = input("enter your statement ")
## # iam here for python
####(3 , 4 , 3 ,6)
##op = []
##words = stmt.split()
##for i in words:
##   op.append(len(i))   
##op = tuple(op)
##print(op)

##ip = (10,20,304,5,7,8,5,3,2,121,13) 
##
##l= [10,304,7,5,2,13]
##t= (20,5,8,3,121)
##
##ip = (100,400,"python" , "java" , 500,"700" , 200)
##ol = [100,400,500,200]
##ot = ("python" , "java" ,"700")

##tuple comprehensions --> No chance
##--------------------
##<tuplename> = (<dummy> <iteration>)
##t1 = ( x  for x in range(1,11))
##print(t1)

##-> keyboard inputs --> input()
##-> CLI inputs

##import sys
##sys.argv --> list --> filename , input values 
##0 index --> filename
##1 index --> 1st input
##.
##.
##.
##.
##n index --> nth input


##import sys
##print(sys.argv)
##a = int(sys.argv[1])
##b = int(sys.argv[2])
##c = int(sys.argv[3])
##d = int(sys.argv[4])
##e = int(sys.argv[5])
##
##print(a+b+c+d+e)
##s = int(sys.argv[1]) + int(sys.argv[2])+int(sys.argv[3])+int(sys.argv[4])+int(sys.argv[5])
##print(s)
##
##ans = 0
##for i in range(1,len(sys.argv)):
##   ans = ans+ int(sys.argv[i])
##print(ans)   


##c:/>python task.py 10
##sys.argv --> [task.py , 10 ]

##n = int(sys.argv[1]) + 1
##l1 = [x for x in range(1,n)]
##print(l1)

##dictionaries
##-------------
##-->mutable
##--><class dict>
##-->hetero
##-->indexed , concat
##--> XXX sliced XX
##
##--> keys --> unique , immuatable --> int , str , tuple
##--> values --> anything , repetitive 
## arbitary

##syntax
##------
##<dictname> = {<k1>:<v1> , <k2>:<v2> , <k3>:<v3> , <k4>:<v4>}
##keys --> k1 k2 k3 k4
##values --> v1 v2 v3 v4

##empdict ={}
##print(empdict)
##print(type(empdict))


##nums = {1:10 , 2:"python" , "tech" :"python" , "version" : 3.6 }
##print(nums)
##print(type(nums))
##accesing
##---------
##<dictname>[<key>]

##print(nums["tech"])
##print(nums["version"])
##print(nums[2])

##modifying
##---------
##<dictname>[<key>] = <newvalue> --> key is available 

##nums[2] = "java"
##print(nums)
##
##nums[3] = 3000 #--> key is not available --> added item
##print(nums)

##deleting
##--------
##del <dictname>[<key>]
##del nums[2]
##print(nums)
##del nums["version"]
##print(nums)
##
##del nums
##print(nums)

##nums[(1,2,3)] = 4000
##print(nums)
##nums[[1,2,3]] = 4000
##print(nums)


##l1 = [2 ,3 ,4 , 5 , 6 , "tech"]
##l2 =[20,30,40,50,60 , "java"]
##d = {}
##
##if len(l1) == len(l2):
##   for i in range(len(l1)):
##      d[l1[i]] = l2[i]
##else:
##   print("lengths are unequal")
##print(d)

##zip() --> dict out of lists 

##l1 = [2 ,3 ,4 , 5 , 6 , 7]
##l2 =[20,30,40,50,60 , 70,80]

##zobj = zip(l1,l2)
##print(zobj)
##d = dict(zobj)
##print(d)

##d = dict(zip(l1,l2))
##print(d)


##.keys()
##.values()
##.items()

##print(nums.keys())
##print(nums.values())
##print(nums.items())


##c:/>python dtask.py 10
##{1:1 , 2:4, 3:9 . . . . .10:100}
##
##stmt = "iam in a class of python "
##{"iam" : 3 , "in" :2  .. . . "python":6}


##functions
##---------
##pop() 
##popitem()
##update()
##copy()
##clear()
##
##
##<dictname>.pop(<key>) --> removes the item
##<dictname>.popitem() --> removes any arbitary item
##
##<dict1> + <dict2> --> is not possible
##XXXX newdict = d1 + d2 XXXXX
##
##<dict1>.update(<dict2>)

##nums.pop(2)
##print(nums)
##
##nums.popitem()
##print(nums)
##
##copied = nums.copy()
##print(copied)
##
##nums.clear()
##print(nums)

##
##nums2 = dict(zip(l1,l2))
##print(nums2)
##
####print(nums+nums2) # error on +
##
##nums2.update(nums)
##print("----------------")
##print(nums)
##print(nums2)
##
##
##c:/>python task.py
##enter no of elements
##3
##enter the key
##name
##enter the value
##khan
##enter the key
##tech
##enter the value
##python
##enter the key
##org
##enter the value
##lync
##
##{name:khan , tech:python , org:lync}

##d ={}
##l = int(input("enter no of elements  "))
##for i in range(l):
##   k = input("enter your key ")
##   v = input("enter your value ")
##   d[k] = v 
##print(d)

##c:/>python task.py
##enter no of keys
##3

##enter the key
##10

##enter the key
##tech

##enter the key
##20

##
##{10:100 , tech:4 , 20:400}

##d = {}
##l = int(input("enter no of keys  "))
##for i in range(l):
##        k = input("enter your key ")
##        if k.isnumeric():
##           k = int(k)
##           v = k**2
##           d[k] = v
##        else:
##           v = len(k)
##           d[k] = v
##print(d)
##   
##dictionary comprehensions
##-------------------------

##num and sq

##d = {}
##for i in range(11):
##   d[i] = i**2
##print(d)
##
##
##d = {}
##for i in range(11):
##   if i % 2 == 0:
##      d[i] = i**2
##print(d)
##
##
##ns = { x:x**2 for x in range(11)} 
##print(ns)
##
##ens = { x:x**2 for x in range(11) if x%2==0} 
##print(ens)
##
##stmt = "iam in a python session at lync"
##
##wl = { word:len(word) for word in stmt.split()}
##print(wl)
##
##wl = { word:len(word) for word in stmt.split() if len(word) >= 5 }
##print(wl)
##
##wl = { word:len(word) for word in stmt.split() if len(word) >= 5 }
##print(wl)
##
##wl = { word:word.split() for word in stmt.split()  }
##print(wl)

##sets and frozensets
##--> Ver 2.4 +
##--> XX repetition XX
##--> mutable
##--> XXX index Sliced XXX
##--> iterations
##--> <class set>
##--> arbitary
##
##nums = {1,2,3,4,5,6,7}
##print(nums)
##print(type(nums))
##
##empset = set(())
##print(empset)
##print(type(empset))
##
##nums = set((1,2,3,4,5,6,7))
##print(nums)
##print(type(nums))
##mset = {100,20,"python" , "hyd",900,100,"python"}
##print(mset[2])
##print(mset[2:4])

##for i in mset:
##   print(i)

##print(mset)

##l1 = [1,2,43,8,6,8,6,54,3,1,3,2,3,4,5,6]
##print(l1)
##l1 = set(l1)
##print(l1)
##l1 = list(l1)
##print(l1)

##mset.add(200)
##print(mset)
##
##mset.pop()
##print(mset)

##mset.remove("python")
##print(mset)
##
##mset.remove("java")
##print(mset)


##mset.discard("python")
##print(mset)
##
##mset.discard("java")
##print(mset)
##

##numsset = {1,2,3,4}
##print(numsset)
##
##
##numsset.update(mset)
##print("--------------")
##print(numsset)
##print(mset)
##
##print("--------------")
##
##mset.update(numsset)
##print("--------------")
##print(numsset)
##print(mset)
##s1 = {10,20,30,40,50}
##s2 = {30,40,50,60,70}
##s3 = {100}

##union
##intersection
##differeence
##issubset
##issuperset
##isdisjoint

##print(s1.union(s2)) # |
##print(s1.intersection(s2)) # &
##print(s2.intersection(s1))
##print(s1.difference(s2)) # -
##print(s2.difference(s1))
##print(s1.issubset(s3)) # >
##print(s3.issubset(s1))
##print(s1.issuperset(s3)) # <
##print(s1.isdisjoint(s3))

##print(s1 | s2 | s3)
##print(s1 & s2)
##print(s1 - s2)
##print(s2 - s1)
##print(s1 > s3)
##print(s1 < s3)
##print(s3 > s1)
##print(s3 < s1)

##frozensets
##----------
##--> Ver 2.4 +
##--> XX repetition XX
##--> IMMUTABLE
##--> XXX index Sliced XXX
##--> iterations
##--> <class frozenset>
##--> arbitary

##fsetnums = frozenset((1,2,3,4))
##print(fsetnums)
##print(type(fsetnums))

##task file
##docx for m1 , m2 

##functional programming
##----------------------
##---->usage of functions
##----->procedure of tasks.
##---->snipest of code to solve atleast one task
##----->functions are also called as first class object.
##--><class function>
##--->function are classified based on the return type and parameter
##return type 0 1 1 0
##parameter 0 1 0 1
##functions are two types
##--->predefined ex:len(),append(),copy() everything that ends with'()'
##---->user defined
##3 components
##----------
##->definition---->naming a function
##->implementation--->logic
##->call----->o/p from function
##syntax:
##--------
##def <functionName>():##definition
##    ________________
##    _________________##implementation should have a tab space
##    <statements>
##    ______________
##    ______________
##    <functionName>()--->call
##function types:
##    parameters are inputto the function
##    these are of 4 kinds
##    ->positional parameters
##    ->default
##    ->variable
##    ->key warded parameter
####def printme():
####print ("hello")
##    the definition and implementation of a function ideally is written only
##one call can be done multiple  times
## if the same function name has multiple implementation the latest implementation is considered
####def hey():
####    print("hi")
##hey()
##def empty():
##    pass
##empty()
##def printme(name): ## formal parameter
##    print("name is"+name)
##printme("kusuma") ##actual parameter
##parameters are written in def and function call
##the parameter in def is called as formal parameter
##the parameter in call is called as actual parameter
##def addnums(a,b):
##    ans=a+b
##    print(ans)
##addnums(20,10)
##def arith(x,y):
##    sans=x+y
##    print("sum of %d and %d is %d"%(x,y,sans)
##    dans=x-y
##    print("diff of %d and %d is %d"%(x,y,dans))
##    mans=x*y
##    print("mul of %d and %d is %d"%(x,y,mans))
##    vans=x/y
##    print("div of %d and %d is %f"%(x,y,vans))
##arith(10,20
##def average(w,x,y,z):
##    ans=(w+x+y+z)/4
##    print(ans)
##average(10,20,30,40)
##def printme():
##    print("lync")
##### function name
##print(printme) ### location / address
##print(type(printme)) ### function
###### function call
##print(printme()) ### location / address
##print(type(printme()))  ### function
##return type
##------------
##1.return type is the output of the function given by the user.
##2.a function can have only one return type
##3. the return value is stored in the function call
##4. a function can return values, variables,function name and function call
##def avg(a,b):
##    ans=(a+b)//2
##    print(ans)
#### return<component>
##    return "hello"
##avg(10,20) ##---> 15
##print(avg(10,20)) #---> none+15
##when a function doesnt return anything caled prints none
##return of values
##------------------
##def avg(a,b):
##    ans=(a+b)//2
##    print(ans)
#### return<component>
##    return "1000"
##avg(10,20) ##---> 15
##print(avg(10,20)) #---> none+15
##return of variables
##-------------------
##def avg(a,b):
##    ans=(a+b)//2
##    print(ans)
#### return<component>
##    return ans
##    return a
##    return b
##avg(10,20) ##---> +15
##print(avg(10,20)) #---> 15+15
##print(type(avg(10,20))) ## int+15
####if we have multiple return statements in a single function,it will return the first return value
##def avg(a,b):
##    ans=(a+b)//2
##    return ans
##print(avg(100,200))
##res=avg(100,200)
##print(res)
##task:
##    ---------
##words=[]
##words.append(s[0:n])
##n=n+3
##splitter("iam in a python class",3)
##["iam","in","a","pyt","hon"]
## anagram---->"iam in a python class",2
##["iam in","in a","a python","python class"]
##nested  function
##--------------
##def one():
##    def two():
##        print("hello")
##    two()
##one()
##docstring
##---------
##->meta data of the function
##->it gives the description of the function if it is written
##->it is stored a variable"_doc_"
##print(<functionname>._doc_)
##->a docstring is returned just after the definition as a multi line comment
##def docdemo():
##    ''' this function prints lync '''
##    print("lync")
##    
##docdemo()
##print(docdemo._doc_)
##
##print(len._doc_)
##print(list.sort._doc_)
##print(print._doc_)
##def addnums(a,b):
##    ans=a+b
##    print("adding output "+str(ans))
##    return ans
##address = addnums(10,20)
##def diffnums(a,b):
##    ans=a-b
##    print("difference output "+str(ans))
##    return ans
##subres=diffnums(address,20)
##def mulnums(a,b):
##    ans=a*b
##    print("product output "+str(ans))
##    return ans
##mulres=mulnums(subres,20)
##def divnums(a,b):
##    ans=a/b
##    print("division output "+str(ans))
##    return ans
##divres=divnums(mulres,20)
##x=int(input("enter first number"))
##y=int(input("enter second number"))
##def addnums(a,b):
##    ans=a+b
##    print("adding output "+str(ans))
##    return ans
##def diffnums(a,b):
##    ans=a-b
##    print("difference output "+str(ans))
##    return ans
##def mulnums(a,b):
##    ans=a*b
##    print("product output "+str(ans))
##    return ans
##def divnums(a,b):
##    ans=a/b
##    print("division output "+str(ans))
##    return ans
####address = addnums(10,20)
####subres=diffnums(address,20)
####mulres=mulnums(subres,20)
####divres=divnums(mulres,20)
##divnums(mulnums(diffnums(addnums(x,y),y),y),y)
c:/>python functask.py
1.arith
2.logic
3.comp
enter your category 1
1.add
2.sub
3.mul
4.div
enter your option 3
3
enter your number
20
enter your number
50
100
def task():
    print("\n 1.arith \n 2.logic \n3.comp")
    print("enter your category:")
    print("\n 1.add \n 2.sub \n 3.mul \n 4.div")
    print("enter your option")
    print("enter your number")
    return
task()



