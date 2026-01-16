def isPalindrome(s: str) -> bool:
        stra = "".join(char for char in s.lower() if char.isalnum())
        print(stra)
        if stra[::-1] == stra:
            return True
        return False
        
    
# print(isPalindrome("A man, a plan, a canal: Panama"))

def prime_factors(n):
    factors = []
    i = 2
    while n > 1 :
        if n%i == 0:
            n //= i
            factors.append(i)
        else:
            i+=1
    return factors

print(prime_factors(124))