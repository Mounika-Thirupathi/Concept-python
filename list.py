1.#create a list of 5 integers
def fun():
    l=[]
    for i in range(1,6):
        l.append(i)
    return l
print(fun())

#2. Acsess the 3 element in a list
def fun(l,p):
    for i in range(len(l)):
        if i==p:
            return l[i]
l=list(map(int,input("enter a list:").split()))
p=int(input("enter a number:"))
print(fun(l,p))

#3. change value at index specified
def fun(l,p,v):
    if p<len(l):
        l[p]=v
    return l
l=list(map(int,input("enter a list:").split()))
p=int(input("enter a number:"))
v=int(input("enter a value:"))
print(fun(l,p,v))

#4. Append an element to list
def fun(l,e):
    l.append(e)
    return l
l=list(map(int,input("enter a list:").split()))
e=int(input("enter a value:"))
print(fun(l,e))

#5. insert an element at index
def fun(l,p,e):
    l.insert(p,e)
    return l
l=list(map(int,input("enter a list:").split()))
p=int(input("enter a value:"))
e=int(input("enter a value:"))
print(fun(l,p,e))

#6. remove an element by value
def fun(l,e):
    l.remove(e)
    return l
l=list(map(int,input("enter a list:").split()))
e=int(input("enter a value:"))
print(fun(l,e))

#7. remove an element by index
def fun(l,e):
    l.remove(l[e])
    return l
l=list(map(int,input("enter a list:").split()))
e=int(input("enter a value:"))
print(fun(l,e))

#8. length of list
def fun(l):
    return len(l)
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#9.find element present in list
def fun(l,e):
    for i in l:
        if l==e:
            return "exist"
    return "not exist"
l=list(map(int,input("entre a list:").split()))
e=int(input("enter a number:"))
print(fun(l,e))

#10. Loop through a list and print each item.
def fun(l):
    res=[]
    for i in l:
        res.append(i)
    return res
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#11. Sort a list in ascending order.       
def fun(l):
    l.sort()
    return l
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#12. Sort a list in descending order
def fun(l):
    l.sort(reverse=True)
    return l
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#13. Reverse a list using reverse()
def fun(l):
    res=list(reversed(l))
    return res
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#14. Reverse a list using slicing
def fun(l):
    return l[::-1]
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#115. Copy a list using slicing
def fun(l):
    res=l[:]
    return res
l=list(map(int,input("enter a list:").split()))
print(fun(l))
        
#16. Copy a list using the copy() method
def fun(l):
    res=l.copy()
    return res
l=list(map(int,input("enter a list:").split()))
print(fun(l))
        
#17. Clear all elements in a list
def fun(l):
    l.clear()
    return l
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#18. Count occurrences of a number
def fun(l,n):
    count=0
    for i in l:
        if i==n:
            count+=1
    return count
l=list(map(int,input("enter a list:").split()))
n=int(input("enter a number:"))
print(fun(l,n))
        
#19. Find the index of a number.
def fun(l,n):
    for i in range(len(l)):
        if l[i]==n:
            return i
l=list(map(int,input("enter a list:").split()))
n=int(input("enter a number:"))
print(fun(l,n))
        
#20. Concatenate two lists
def fun(l1,l2):
    return l1+l2
l1=list(map(int,input("enter a list:").split()))
l2=list(map(int,input("enter a list:").split()))
print(fun(l1,l2))
        
#21. Repeat a list 3 times
def fun(l):
    return l*3
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#22. Print every second element.
def fun(l):
    for i in range(1,len(l),2):
        print(l[i])
l=list(map(int,input("enter a list:").split()))
fun(l)

#23. Print elements from index 2 to 5.
def fun(l):
    for i in range(2,5):
        print(l[i])
l=list(map(int,input("enter a list:").split()))
fun(l)
        
#24. Check if all elements are positive.
def fun(l):
    count=0
    for i in l:
        if i>0:
            count+=1

    if len(l)==count:
        return "positive"
    return "negative"
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#25. Convert list to a string with commas
def fun(m):
    l = ""
    for i in m:
        l = str(i) + l  
    return l
l = list(map(int, input("enter a list: ").split()))
print(fun(l))

#26. Find the max element
def fun(l):
    m=l[0]
    for i in l:
        if i>m:
            m=i
    return m
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#27. Find the min element
def fun(l):
    min=l[0]
    for i in l:
        if i<min:
            min=i
    return min
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#28. Sum all numbers in a list
def fun(l):
    sum=0
    for i in l:
        sum+=i
    return sum
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#29. Square every number in a list
def fun(l):
    s=[]
    for i in l:
        s.append(i*i)
    return s
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#30. Filter even numbers from a list
def fun(l):
    s=[]
    for i in l:
        if i%2==0:
            s.append(i)
    return s
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#31. Filter odd numbers from a list
def fun(l):
    s=[]
    for i in l:
        if i%2!=0:
            s.append(i)
    return s
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#32. Find duplicates in a list
def fun(l):
    s=[]
    o=[]
    for i in l:
        if i not in s:
            s.append(i)
        else:
            o.append(i)
    return o
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#33. Remove duplicates from a list.
def fun(l):
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
    return s
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#34. Get unique elements using set()
def fun(l):
    res=set(l)
    return res
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#35. Check if a list is empty.
def fun(l):
    if len(l)==0:
        return "empty"
    else:
        return "not empty"
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#36. Initialize a list of n zero
def fun(n):
    res=[]
    for i in range(n):
        res.append(0)
    return res
n=int(input("enter a number:"))
print(fun(n))

#37. Swap two elements in a list.
def fun(l,a,b):
    l[a],l[b]=l[b],l[a]
    return l
l=list(map(int,input("enter a list:").split()))
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(fun(l,a,b))

#38. Get last element of a list
def fun(l):
    return l[len(l)-1]
l=list(map(int,input("enter a list:").split()))
print(fun(l))

#39 Convert a string to a list of chars
def fun(str):
    l=[]
    for i in str:
        l.append(i)
    return l
str=input("enter a string:")
print(fun(str))
    
