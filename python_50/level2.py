#1
def right_triangle(num):
    for i in range(1,num+1):
        print('*'*i)

#2
def pyramid(num):
    for i in range(1,num+1):
        print(" "*(num-i),"*"*(2*i-1))

# pyramid(5)
#3
def fibonacci(num):
    first = 0
    sec = 1
    fib_list = []
    for i in range(num):
        a = first+sec
        fib_list.append(first)
        first = sec    
        sec = a 
    print(fib_list)
    

# fibonacci(4)
#4
def prime_no(num):
    if num <= 0:
        return "Invalide number"
    count = 0
    for i in range(2,num+1):
        if num%i == 0 :
            count += 1
            if count > 1:
                return False
            
    return True

# print(prime_no(7))
#5  
def upto_n_prime(n):
    if n <= 0:
        return "Invalide Number"
    for i in range(1,n+1):
        if prime_no(i):
            print(i)

# upto_n_prime(15)
#6
def fact(n):
    if n <= 0:
        return "Invalid Input"
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac

# print(fact(6))
#7
def vowels_count(s):
    vowels = ['a','e','i','o','u']
    s = s.lower()
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

# print(vowels_count("Heiiillo"))
#8
def reverse_str(s):
    st = ''
    for i in range(len(s)):
        st += s[((len(s)-1) - i)]
    return st

# reverse_str("Yogesh")
#9
def palindrome(s):
    if s == reverse_str(s):
        return "Yes It's Palindrome"
    return "No it's not palindrome"

# print(palindrome("OHO"))
#10
def even_num_sum(n):
    sum = 0
    for i in range(1,n+1):
        if i%2 == 0:
            sum+=i
    return sum

# print(even_num_sum(5))