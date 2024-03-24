x=5
y=10
z=11
#print(id(x))
#print(id(y))
#help()
#my_name="Abhi"
#name = input("please enter your name: ")
#age = input("please enter your age: ")
#print("my name is ",name, " and age is ",age)

#support for formatted string
#print(f"my name is {name} and age is {age}")

'''print(x,y,z,sep=",")
print("Hello", end=" ")
print("terminal", end="")
print("!")
print(type(x))
num = 3e6
print(num)
print(type(num))
z=4+6j
print(z)
print(type(z))
print(abs(-10))
print(round(num))
print(round(2.5))
nums = [1,3,5,7,9,11]
print(min(nums))
print(max(nums))
print(sum(nums))
message = 
hello my dear friends
welcome to my vscode terminal
print(message)
name = 'abhi'
#print(name[5])
print(name[-1])
f_name = 'Abhinav'
l_name = 'Mansani'
complete_name = f_name +" "+ l_name
print(complete_name)
print(len(complete_name))
str='  Abhinav Mansani'
print(str[2:8])
print(str[2:])
print(str[:8])
print(str[-9:9])
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.strip())
str="hello dear, i am very good, i am nice and i am wow"
print(str.replace('i am','we are',2))
print("hello \n abhi")
print('abhi\tnav')
print("Abhinav \"Mansani\"")
students = ["Abhinav", "Mansani", "Shivani", "Sakshi"]
print(students)
print(type(students))
list2=list(students)
print(list2)
print(id(students))
print(id(list2))

list3=list("Abhinav")
print(list3)

list4= list((1,2,"Abhi"))
print(list4)


l1=[1,3,9,2,5,6,7,-1]
print(l1[-3])
l1.reverse()
print(l1)
print(l1[::-1])
print(min(l1))
arr = [3,2,1,5,9]
arr.append(11)
#arr.sort()
arr.insert(3,43)
print(arr)
arr2=[4,6,"abhi",True]
arr.extend(arr2)
print(arr)
arr.remove(True)
print(arr)
arr = [1,2,1,1,4,6,7]
arr.count(1)
print(arr.pop())
print(arr)
chars=['a','b','c','d','e']
chars[3]='f'
print(chars)
chars[1:4]='m','n','o'
print(chars)
chars_2=chars.copy()
print(id(chars_2),id(chars))
l1=[5,4,3,2,1]
l1.sort()
print(l1)

tup1=(3,6,1,9,10)
print(type(tup1))
print(tup1)

t1=tuple([1,2,4])
print(t1)
t2=tuple("abhi")
print(t2)
t3=tuple(tup1)
print(t2,t3)
t=(31,)
print(type(t))
fruits = ('apple','mango','orange','apple','mango','kiwi','apple')
print(fruits.count('apple'))
print(fruits.index('mango'))
print(len(fruits))
print(fruits[4])
print(fruits[-4])
print(fruits[::-1])
print(fruits[2:7])

print(True)
print(False)

#Dictionary
student_details = {'name': 'bantu', 'age': 21,'city': 'hyderabad'}
print(student_details)
print(type(student_details))

dict1 = {3:"Abhi", 2:"Mansani",True:"Love"}
print(dict1)

#Dictionary using constructor method
dict2=dict(name='abhi',age=31)
print(dict2)
print(type(dict2))
print(student_details['name'])
print(student_details.get('age'))
print(student_details.keys())
print(student_details.values())
print(student_details.items())

#adding elements to dictionary
student_details = {'name': 'bantu', 'age': 21,'city': 'hyderabad'}
student_details['country'] = 'India'
print(student_details)
marks_details = {'English': 100, 'Maths': 82, 'Science': 86}
student_details.update(marks_details)
print(student_details)
print(student_details.popitem())
print(student_details)
del student_details['age']
print(student_details)
student_details.clear()
print(student_details)

#Sets
myset = {1,3,5,6}
print(myset)
print(type(myset))
s1={1,2,3,1,1,4,6,4}
print(s1)
s2=set()
print(s2)
s3=set({1,2,3,1})
print("s3 =",s3)
l1=[1,2,2,1]
s4=set(l1)
print("s4 =",s4)
#add elements in sets
s2.add(8)
s2.add(10)
s2.add(1)
s2.add(17)
s2.add(10)
print(s2)
print(s2.discard(10))
#s2.remove(14)
print(s2)
print(s2.difference(s3))

#frozenset = immutable set
fs1 = frozenset([1,2,3])
print(fs1)
print(type(fs1))
fs2=frozenset({1,2,3,4})
print(fs2)
dict2={fs2:"abhi"}
print(dict2)

y='10'
print(type(y))
y=int(y)
print(type(y))

l1=[0,1,2,3,4,True]
l1.pop(True)
print(l1)
l1.remove(True)
print(l1)

empty_list = []
print(empty_list)

list = list(range(10))
print(list[2:])

import array
new_arr = array.array('i', [1,2,3,4])
print(new_arr)
new_arr[0]=0
new_arr.reverse()
print(new_arr)

def find_sum(lst, k):
    res = []
    # Replace this placeholder return statement with your code
    i=1
    while i < len(lst):
        j=i+1
        while j < len(lst):
            if (lst[i]+lst[j]) == k:
                res[0] = lst[i]
                res[1] = lst[j]
                break
            j += 1
        if((lst[i]+lst[j]) == k):
            break
        i += 1
    return res

find_sum([2,7,11,15],9)

def find_sum(lst, k):
    idx1,idx2,sum = 0, len(lst)-1,0
    lst.sort()
    res=[]
    while(idx1 != idx2):
        sum = lst[idx1]+lst[idx2]
        if sum<k:
            idx1 += 1
        elif sum>k:
            idx2 -=1
        else:
            res.append(lst[idx1])
            res.append(lst[idx2])
            return res
    return []

print(find_sum([2,7,9,11],9))

def find_fst_uniq(lst):
    res=[]
    for i,j in Counter(lst).items():
        if j==1:
            res.append(i)
    return res

find_fst_uniq([2,7,2,11])

lst=[2,3,9,9]
lst.sort()
res=set(lst)
res=list(res)
res.sort()
print(res[-2])

def rearrange(lst):
    leftMostPosEle=0
    for curr in range(len(lst)):
        if lst[curr]<0:
            if curr != leftMostPosEle:
                lst[curr],lst[leftMostPosEle]=lst[leftMostPosEle],lst[curr]
            leftMostPosEle+=1
    print(lst)
    return lst

rearrange([1,20,31,-9,0])

def max_min(lst):
    s=0
    e=len(lst)
    mid=(s+e)//2
    print(mid)
    lst.sort()
    maxi=lst[mid:]
    maxi.reverse()
    mini=lst[:mid]
    res=[]
    i=0
    while i < len(maxi) and i < len(mini):
        res.append(maxi[i])
        res.append(mini[i])
        i+=1
    while i<len(maxi):
        res.append(maxi[i])
        i+=1
    while i<len(mini):
        res.append(mini[i])
        i+=1
    print(res)
max_min([8,2,4,6,5])

def find_max_sum_sublist(lst):
    if len(lst)<1:
        return 0
    curr_max=lst[0]
    global_max=lst[0]

    for i in range(1, len(lst)):
        if curr_max < 0:
            curr_max=lst[i]
        else:
            curr_max += lst[i]
        if global_max<curr_max:
            global_max=curr_max
    return global_max

lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
print("Sum of largest subarray: ", find_max_sum_sublist(lst))
x=23
x //=3
print(x)

x = int(input("Enter the number: "))
if x>15:
    print("the number is greater than 15")
elif x == 15:
    print("The number is equal to 15")
else:
    print("the number is less than or equal to 15")

marks = 82
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("study more")

#ternary operator
num = 5
res="positive" if num > 0 else "negative"
print(res)

day_num=4
match day_num:
    case 1:
        print("Today is Sunday")
    case 2:
        print("Today is Monday")
    case 3:
        print("Today is Tuesday")
    case 4:
        print("Today is Wednesday")
    case 5:
        print("Today is Thursday")
    case 6:
        print("Today is Friday")
    case 7:
        print("Today is Saturday")
    case _:
        print("Invalid day_num")
fruits = ["apple","banana","cherry","dragon fruit"]
for fruit in range(len(fruits)):
    print(fruit)

name = "Abhinav Mansani"
for ch in name:
    print(ch, end="")

for i in range(12,2,-3):
    print(i)

d = dict({True: "Ram"})
print(d)'''

for i in range(4):
    for j in range(1,12):
        if j%4==0:
            break
        print(j)