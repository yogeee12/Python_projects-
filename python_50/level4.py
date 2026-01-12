#1 Armsrtong number
def armstrong_check(n):
    num=n
    count = 0
    while num != 0:
        num //=10
        count += 1

    num=n
    sum_n = 0
    while num != 0:
        reminder = num%10 
        sum_n += reminder ** count
        num//=10

    if sum_n == n:
        return "Number is Armstrong"
    return "Number is not Armstrong"

# print(armstrong_check(153))

#2 GCD
def gcd(n,k):
    if k<n:
        n,k = k,n
    if (k%n == 0):
        return n
    return gcd(n,k%n)

print(gcd(40,60))

#3
def anagram(st1,st2):
    st1 = st1.lower()
    st2 = st2.lower()

    list_st1 = [item for item in st1]
    list_st2 = [item for item in st2]

    list_st1.sort()
    list_st2.sort()

    if list_st1 == list_st2:
        return "Yes it's anagram"
    return "NO it's not anagram"

# print(anagram("car","acr"))
#4
def frequency_char(st):
    char_dic = {}
    for char in st:
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic

# print(frequency_char("Hello"))

#5 calculater
def calculater(val1,val2):
    operater = ["+","-","*","/","%"]
    for i in operater:
        print(i)
    ask = input("Which operation you want to perform : ")
    print("Answer =",end=' ')
    if ask == '+':
        return val1+val2
    elif ask == '-':
        return val1-val2
    elif ask == '*':
        return val1*val2
    elif ask == '/':
        return val1/val2
    elif ask == '%':
        return val1%val2
    else:
        return "Wrong input!"

# print(calculater(5,8))
#5.1 
def calculater1(val1,val2,op):
    operation = f"{val1} {op} {val2}" 
    return eval(operation)

# print(calculater1(5,8,'/'))

#6
def flatten_list(li):
    flat_list = []
    for n in li:
        try:
            for i in n:
                flat_list.append(i)
        except TypeError:
            flat_list.append(n)
    return flat_list

# print(flatten_list([4,[4,5],[7,8]]))
#7
def find_missing(li):
    sum_of_element = 0
    for i in li:
        sum_of_element += i

    sum_to_n = (li[-1]*(li[-1]+1))/2
    return sum_to_n-sum_of_element

# li = [1,2,3,4,6]
# print(find_missing(li))
    
#8
def password_validation(password):
    min_length = 8
    if len(password) < min_length:
        return "Minimum 8 character!"
    digits = [n for n in password if n.isdigit()]
    if not digits:
        return "Password must contain Numbers"
    password_upper = password.lower()
    if password_upper == password:
        return "Password must contain Uppercase char"

    return "correct password"

# print(password_validation("hel2loooo"))

class atm:
    def __init__(self,account_number,pin) -> None:
        self.account_number = account_number
        self.pin = pin
        self.acc_detail = {
            "account_number" : ["0001","0002","0003"],
            "pin_number" : ["4523","7894","5689"],
            "balance" : [80000,100000,50000]
        }
        self.idx = self.acc_detail["account_number"].index(self.account_number)
        self.auth(self.pin,self.account_number)

    def auth(self,pin,account_number):
        pin_no = self.acc_detail["pin_number"][self.idx]
        account_no = self.acc_detail["account_number"][self.idx]
        if pin_no != pin and account_no != account_number:
            return "No data found !"
        return True        

    def withdraw(self,amount):
        current_balance = self.acc_detail["balance"][self.idx]
        if current_balance < amount:
            return "Not enough balance!"
        self.acc_detail["balance"][self.idx] -= amount
        return "Withdraw succefull..."

    def deposit(self,amount):
        self.acc_detail["balance"][self.idx] += amount
        return "Deposit succefull..."

    def balance(self):
        current_balance = self.acc_detail["balance"][self.idx]
        return f"Current Blanace : {current_balance}"

# if __name__ == "__main__":
    # s1 = atm("0001","4523")
    # print(s1.withdraw(10000))
    # print(s1.balance())
    # print(s1.deposit(25000))
    # print(s1.balance())

def remove_punctuation(s):
    punctuation_marks = ['`',"~","!","@","#","$","%","^","&","*","(",")","/","-","_","<",">",",",".","?",";",":","\\","|","{","}","[","]","\"","\'","+"]
    str1 = ''
    for char in s:
        if char not in punctuation_marks:
            str1 += char
    return str1

# print(remove_punctuation("tf@^jj!h37"))