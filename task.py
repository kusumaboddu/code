1. Make the following patterns by taking inputs from user :

c:/>python task.py “python”
##str=input("enter the string")
##length=len(str)
##for i in range(length):
##    for j in range(i+1):
##        print(str[j],end="")
##    print()
enter the stringpython
p
py
pyt
pyth
pytho
python
4. Get the mean(average) and central value of all the numbers
in a list
lst=[10,20,30,40,50]
c:/>python task.py
##def mean(lst):
##    return sum(lst) / len(lst)
##L1 = [10,20,30,40,50]
##print("mean: " +str(mean(L1)))
mean: 30.0
##def median(lst):
##    lst.sort()
##    print(lst)
##    if len(lst) % 2 ==0:
##        return(lst[int(len(lst) /2)] + lst[int(len(lst) /2)-1]) /2
##    else:
##        return lst[int(len(lst)/2)]
##L1 = [10,20,30,40,50]
##print("median:" +str(median(L1)))
[10, 20, 30, 40, 50]
median:30
L1 = [10,20,30,40,50,70]
c:/>python task.py
##def mean(lst):
##    return sum(lst) / len(lst)
##L1 = [10,20,30,40,50,70]
##print("mean: " +str(mean(L1)))
mean: 36.666666666666664
##def median(lst):
##    lst.sort()
##    print(lst)
##    if len(lst) % 2 ==0:
##       return(lst[int(len(lst) /2)] + lst[int(len(lst) /2)-1]) /2
##    else:
##        return lst[int(len(lst)/2)]
##L1 = [10,20,30,40,50,70]
##print("median:" +str(median(L1)))
[10, 20, 30, 40, 50, 70]
8.Split a word into characters and store them in a list
c:/>python mytask.py “python”
##str="python"
##lst=list(str)
##print(lst)
['p', 'y', 't', 'h', 'o', 'n']
5.Make a dictionary of repeated strings (more than once , non
case sensitive) from a list
Input_list = [“python” , “java” , “php” , “python” ,“c” , “Python” , “PHP” , “c++” ,“PYTHON”]
##list = [“python” , “java” , “php” , “python” ,“c” , “Python” , “PHP” , “c++” ,“PYTHON”]
##count={}
##for x in list:
##  if x in count.keys():
##        count[x]+=1
##  else:
##       count[x]=1
##print(count)
##for x in count.keys():
##    print(x, "occurs for",count[x],"times")
count={“python” :4 , “php”:2}
6. Make a list of cumulative sum of elements in list of
numbers
##values = [3,4,5,6,7,8]
##total  = 0
##sums   = []
##
##for v in values:
##  total = total + v
##  sums.append(total)
##
##print ('Values: ', values)
##print ('Sums:   ', sums)
Values:  [3, 4, 5, 6, 7, 8]
Sums:    [3, 7, 12, 18, 25, 33]
7.Get the common elements from two lists into a tuple
list1 = [10,20,30,40,50]
list2 = [30,40,70,80]
##list1= [10,20,30,40,50]
##list2 = [30,40,70,80]
##final_list=[]
##for i in list1:
##    for j in list2:
##        if i==j:
##            final_list.append(i)
##print(final_list)
##final_list=[30,40]
##tup=tuple(final_list)
##print(tup)
(30, 40)
3. Make a dictionary from two lists made by user inputs

c:/>python task.py 4
##l1 = []
##l2 = []
##l1_size = int(input("Enter total elements for the first list : "))
##l2_size = int(input("Enter total elements for the second list : "))
##for i in range(l1_size):
##    l1.append(input("Enter value for the first list : "))
##for i in range(l2_size):
##    l2.append(input("Enter value for the second list : "))
##print("Your first list : ",l1)
##print("Your second list : ",l2)
##combined_dict = dict(zip(l1,l2))
##print("Final dictionary : ",combined_dict)
Enter total elements for the first list : 4
Enter total elements for the second list : 4
Enter value for the first list : 10
Enter value for the first list : 100
Enter value for the first list : 20
Enter value for the first list : 200
Enter value for the second list : "Aa"
Enter value for the second list : "Bb"
Enter value for the second list : "Cc"
Enter value for the second list : "Dd"
Your first list :  ['10', '100', '20', '200']
Your second list :  ['"Aa"', '"Bb"', '"Cc"', '"Dd"']
Final dictionary :  {'10': '"Aa"', '100': '"Bb"', '20': '"Cc"', '200': '"Dd"'}


