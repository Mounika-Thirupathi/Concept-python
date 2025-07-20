1. Print numbers from 1 to 10 using a loop.
def fun(num):
    for i in range(1,num+1):
        print(i)
num=int(input("enter a number:"))
fun(num)

2. Print even numbers from 1 to 20.
def fun(num):
    for i in range(1,num+1):
        if i%2==0:
            print(i)
num=int(input("enter a number:"))
fun(num)

3. Print odd numbers from 1 to 20.
def fun(num):
    for i in range(1,num+1):
        if i%2!=0:
            print(i)
num=int(input("enter a number:"))
fun(num)

4. Calculate the sum of numbers from 1 to 100.
def fun(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum
num=int(input("enter a number:"))
print(fun(num))

5. Print multiplication table of 5.
def fun(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
n=int(input("enter a number:"))
fun(n)

6. Print all numbers divisible by 3 up to 50
def fun(n):
    for i in range(1,n+1):
        if i%3==0:
            print(i)
n=int(input("enter a number:"))
fun(n)

7. Calculate the factorial of a number using a loop.
def fun(n,fact=1):
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter a number:"))
print(fun(n))

8. Reverse the digits of a number using a loop.  
def fun(n):
    count=[]
    while n>0:
        digit=n%10
        count.append(digit)
        n=n//10
    return count
n=int(input("enter a number:"))
print(fun(n))

9. Print squares of numbers from 1 to 10.
def fun(n):
    for i in range(1,n+1):
        print(i**2)
n=int(input("enter a number:"))
fun(n)

10. Count the number of digits in an integer.
def fun(n):
    c=0
    while n>0:
        digit=n%10
        c+=1
        n=n//10   
    return c
n=int(input("enter a number:"))
print(fun(n))

11. Find the sum of digits of a number.
def fun(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    return sum
n=int(input("enter a number:"))
print(fun(n))

12. Print powers of 2 up to 2^10.
def fun(n):
    for i in range(1,n+1):
        print(2**i)
n=int(input("enter a number:"))
fun(n)

13. Check if a number is prime using a loop.
def fun(n):
    if n<=1:
        return "not prime"
    for i in range(2,n):
        if n%i==0:
            return "not prime"
    return "prime"
n=int(input("enter a number:"))
print(fun(n))

14. Print first 10 natural numbers using while loop.
def fun(n):
    i=0
    while i<=n:
        print(i)
        i+=1
n=int(input("enter a number:"))
fun(n)

15. Count down from 10 to 1 using a loop.
def fun(n):
    for i in range(n,0,-1):
        print(i)
n=int(input("enter a number:"))
fun(n)

16. Find product of all numbers from 1 to 10.
def fun(n):
    product=1
    for i in range(1,n+1):
        product*=i
    return product
n=int(input("enter a number:"))
print(fun(n))

17. Print numbers from 1 to 100 in steps of 5
def fun(n):
    for i in range(1,n+1):
        print(i)
n=int(input("enter a number:"))
fun(n)

18. Find numbers between 1–50 divisible by both 3 and 5.
def fun(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print(i)
n=int(input("enter a number:"))
fun(n)

19. Display the reverse of an integer.
def fun(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
n=int(input("enter a number:"))
print(fun(n))

20. Find the smallest digit in a number.
def fun(n):
    small=n%10
    while n>0:
        digit=n%10
        if digit<small:
            small=digit
        n=n//10
    return small
n=int(input("enter a number:"))
print(fun(n))

22. Find the largest digit in a number.
def fun(n):
    largest=n%10
    while n>0:
        digit=n%10
        if digit>largest:
            largest=digit
        n=n//10
    return largest
n=int(input("enter a number:"))
print(fun(n))

23. Print pattern: 1 2 3, 4 5 6, 7 8 9
def fun(n,num=1):
    for i in range(1,n+1):
        res=""
        for j in range(1,n+1):
            res+=str(num)+" "
            num+=1
        print(res)
n=int(input("enter a number:"))
fun(n)

24. Print pattern of stars in triangle format.
def fun(n):
    for i in range(1,n+1):
        res=""
        for j in range(1,i+1):
            res+="*"+" "
        print(res)
n=int(input("enter a number:"))
fun(n)

25.Print sum of even digits in a number.
def fun(n):
    sum=0
    while n>0:
        digit=n%10
        if digit%2==0:
            sum+=digit
        n=n//10
    return sum
n=int(input("enter a number:"))
print(fun(n))

26. Print sum of odd digits in a number.
def fun(n):
    sum=0
    while n>0:
        digit=n%10
        if digit%2!=0:
            sum+=digit
        n=n//10
    return sum
n=int(input("enter a number:"))
print(fun(n))

27. Print table of a given number.
def fun(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
n=int(input("enter a number:"))
fun(n)

28. Count how many times a digit occurs in a number.
def fun(n,target,count=0):
    while n>0:
        digit=n%10
        if digit==target:
            count+=1
        n=n//10
    return count
n=int(input("enter a number:"))
target=int(input("enter a number:"))
print(fun(n,target))

29. Sum of squares of digits of a number.
def fun(n,sum=0):
    while n>0:
        digit=n%10
        sum+=digit**2
        n=n//10
    return sum
n=int(input("enter a number:"))
print(fun(n))

30.Sum of cubes of digits of a number.
def fun(n,sum=0):
    while n>0:
        digit=n%10
        sum+=digit**3
        n=n//10
    return sum
n=int(input("enter a number:"))
print(fun(n))

31. Count multiples of 3 between 1 and 100.
def fun(n,count=0):
    for i in range(1,n+1):
        if i%3==0:
            count+=1
    return count
n=int(input("enter a number:"))
print(fun(n))

32. Print 10, 20, 30... up to 100.
def fun():
    for i in range(10,101,10):
        print(i)
fun()

33. Print reverse of a number using while loop.
def fun(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
n=int(input("enter a number:"))
print(fun(n))

34. Find if number is Armstrong number (3-digit only).
def fun(n):
    temp=n
    power=0
    while temp>0:
        power+=(temp%10)**3
        temp=temp//10
    if power==n:
        return "True"
    else:
        return "False"
n=int(input("enter a number:"))
print(fun(n))

36. Print GCD of two numbers using loop.
def fun(a,b):
    while b!=0:
        a,b=b,a%b
    return a
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(fun(a,b))

37. Print LCM of two numbers using loop.
def fun(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def fun1(a,b):
    g=fun(a,b)
    return a*b//g
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(fun1(a,b))

38. Display all even digits in a number.
def fun(n):
    while n>0:
        digit=n%10
        if digit%2==0:
            print(digit)
        n=n//10
n=int(input("enter a number:"))
fun(n)

39. Display all odd digits in a number.
def fun(n):
    while n>0:
        digit=n%10
        if digit%2!=0:
            print(digit)
        n=n//10
n=int(input("enter a number:"))
fun(n)

40. Print the ASCII values from 65 to 90.
def fun(n):
    for i in range(65,n+1):
        print(chr(i))
        i+=1
n=int(input("enter a number:"))
fun(n)

35. Print Fibonacci series up to n terms.
def fun(n):
    a,b=0,1
    for i in range(1,n+1):
        print(a)
        a,b=b,a+b
n=int(input("enter a number:"))
fun(n)
        