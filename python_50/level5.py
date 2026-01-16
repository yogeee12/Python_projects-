#1
def non_repating_element(s):
    dic = {}
    for idx,char in enumerate(s):
        if char not in dic.keys():
            dic[char] = [1,idx]
        else:
            dic[char][0] += 1
    
    li = list(dic.values())
    li.sort()
    if li[0][0] > 1:
        return "Not char found!"
    for key,value in dic.items():
        if value == li[0]:
            return key

# print(non_repating_element("swwiissn"))
#2
def pair_match(arr,k):
    if k<1:
        return "Value is smaller!!"
    pair = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i] + arr[j]) == k:
                pair.append((arr[i],arr[j]))
            else:
                continue 
    if pair:
        return pair
    return "Nothing found"

# print(pair_match([1,4,5,3,2],8))
#3
def zero_collector(arr):
    len_arr1 = len(arr)
    arr = [k for k in arr if k != 0]
    for i in range(len_arr1-len(arr)):
        arr.append(0)
    return arr

# print(zero_collector([1,0,1,4,0,3]))
#4
def longest_word(s):
    s_list = s.split(" ")
    long_word = s_list[0]
    for word in s_list:
        if len(word) > len(long_word):
            long_word = word
    return long_word

# print(longest_word("I love artificil intelligence"))             
#5
def str_comp(s):
    if len(s) <= 0:
        return "Empty string found! "
    count = 1
    compressed_str = ''
    for idx,char in enumerate(s):
        if idx != len(s)-1:
            if char == s[idx+1]:
                count += 1
            else:
                compressed_str += f"{char}{count}"
                count = 1
        else:
            compressed_str += f"{char}{count}"
    return compressed_str

# print(str_comp("aaannjjj"))
#6
def rotation_check(arr1,arr2):
    a = arr1+arr1
    first_n = a.index(arr2[0])
    for i in range(len(arr2)):
        if arr2[i] != a[first_n+i]:
            return False
    return True


# a=[1,2,3,4,5]
# b=[2,3,4,5,1]
# print(rotation_check(a,b))
#7
class Queue:
    def __init__(self) -> None:
        self.li = []

    def enaqueue(self,num):
        self.li.append(num)

    def deaqueue(self):
        self.li.pop(0)

    def display(self):
        return self.li

# q1 = Queue()
# q1.enaqueue(5)
# q1.enaqueue(8)
# q1.enaqueue(7)
# print(q1.display())
# q1.deaqueue()
# print(q1.display())
#8
class Stack:
    def __init__(self) -> None:
        self.li = []

    def push(self, num):
        self.li.append(num)

    def pop(self):
        self.li.pop()

    def display(self):
        return self.li

# s1 = Stack()
# s1.push(8)
# s1.push(5)
# s1.push(9)
# print(s1.display())
# s1.pop()
# print(s1.display())

#9
def bianry_search(li,v,l,r):
    if l > r:
        return False
    
    mid = (l+r)//2
    if (v == li[mid]):
        return True
    
    if (v < li[mid]):
        return bianry_search(li,v,l,mid-1)
    else:
        return bianry_search(li,v,mid+1,r)

# li=[1,2,3,4,5]
# print(bianry_search(li,2,0,len(li)-1))

#10
class Business:
    def __init__(self) -> None:
        self.menu = {
            "items" : ["burger","pizaa","maggie"],
            "prices" : [30,80,50]
        }

    def add_item(self,item,price):
        if item.lower() not in self.menu["items"]:
            self.menu["items"].append(item)
            self.menu["prices"].append(price)
        else: 
            return f"{item} already exists in menu"
    
    def delet_item(self,item):
        if item in self.menu["items"]:
            idx = self.menu["items"].index(item)
            self.menu["items"].remove(item)
            self.menu["prices"].pop(idx)
        else:
            return "Item not in menu"
    
    def view_menu(self):
        headers = list(self.menu.keys())
        rows = list(zip(*self.menu.values()))

            # calculate width of each column
        widths = []
        for i, h in enumerate(headers):
            col = [str(h)] + [str(row[i]) for row in rows]
            widths.append(max(len(x) for x in col))

        # print header
        for i, h in enumerate(headers):
            print(h.ljust(widths[i]), end=" | ")
        print()
        print("-" * (sum(widths) + 3 * len(widths)))

        # print rows
        for row in rows:
            for i, val in enumerate(row):
                print(str(val).ljust(widths[i]), end=" | ")
            print()

if __name__ == "__main__":
     b1 = Business()
     b1.add_item("momo's",120)
     b1.delet_item("pizaa")
     b1.view_menu()
