# 1
def check_even_odd(num):
    if (num//2)*2 == num:
        return "Even"
    else :
        return "Odd"
    
print(check_even_odd(7))
# 2
def largest_3(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

# print(largest_3(0,5,2))
# 3
def reverse_int(num):
    revrsed_num = 0
    while num != 0:
        reminder = num % 10
        revrsed_num = revrsed_num * 10 + reminder
        num //= 10
    return revrsed_num

# print(reverse_int(123))
# 4
def count_digit(num):
    count = 0
    while num != 0:
        num //=10
        count += 1
    return count

# print(count_digit(456115))
# 5
def num_palindrome(num):
    if num == reverse_int(num):
        return "Palindrome"
    return "Not Palindrome"

# print(num_palindrome(412214))
# 6
def swap(a,b):
    a,b = b,a
    return f"a:{a} , b:{b}"

# print(swap(5,6))
# 7
def natural_num(num):
    if num <= 0:
        return "Num is not natural number"
    for i in range(1,num+1):
        print(i)
        
# natural_num(5)
# 8
def sum_num(num):
    sum = 0
    while num != 0:
        sum += num%10
        num //= 10

    return sum
# print(sum_num(451))

# 9
def pos_neg_zero(num):
    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive"
    else:
        return "Negative"
    
# print(pos_neg_zero(-56))
# 10
def cel_fahrenheit(cel):
    fahrenheit = (cel * (9/5))+32
    return fahrenheit

# print(cel_fahrenheit(16))

