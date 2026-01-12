#1
def largest_num(li):
    li.sort()
    return li[-1]
#1.1
def largest_num2(li):
    if len(li) < 1:
        try:
            return li[0]
        except IndexError as e:
            return "Empty list",e
    num = li[0]
    for i in range(len(li)):
        if num < li[i]:
            num = li[i]
    return num

li = [-10,-5,-3]
# print(largest_num(li))
# print(largest_num2(li))

#2 
def sec_largest(li):
    li = set(li)
    li = list(li)
    li.sort()
    return li[-2]

# print(sec_largest(li))
#2.1
def sec_largest2(li):
    if len(li) <= 1:
        try:
            return "Single value found in list",li[0]
        except IndexError as e:
            return "Empty list",e
    first = float('-inf')
    sec = float('-inf')
    for i in range(len(li)):
        if first < li[i]:
            sec = first
            first = li[i]
        elif sec < li[i] and first > li[i] :
            sec = li[i]

    return sec
li = [1,5,6,6,4]
print(sec_largest2(li))

#3
def count_element(li):
    dic = {}
    for element in li:
        if element in dic.keys():
            dic[element] += 1
        else:
            dic[element] = 1

    return dic

# print(count_element(li))

#4
def remove_duplicates(li):
    new_li = []
    for item in li:
        if item not in new_li:
            new_li.append(item)
    return new_li

# print(remove_duplicates(li))
#5 
def check_sort(li):
    if len(li) < 1:
        return "No values"
    li_len = 0
    temp = li[0]
    while li_len != len(li):
        if temp <= li[li_len]:
            temp = li[li_len]
            li_len += 1
        else:
            return "Not sorted"
    return "Sorted"

#5.1
def check_sort2(li):
    if len(li) < 1:
        return "No value"
    temp = li[0]
    for element in li:
        if temp <= element:
            temp = element
        else:
            return "Not sorted"
    return "Sorted"

# li = [1,2,3,5,8]
# print(check_sort(li))

#6
def merge_sort(li_1,li_2):
    new_li = li_1+li_2
    new_li.sort()
    return new_li

# li1=[1,7,3,4]
# li2=[5,7,8,4]
# print(merge_sort(li1,li2))
#7
def comman_element(li_1,li_2):
    comman_element = []
    for element in li_1:
        if element in li_2 and element not in comman_element:
            comman_element.append(element)

    if comman_element:
        return comman_element,"comman element in both lists"
    return "No comman element found"

# li1=[1,1,7,3,4]
# li2=[1,5,7,8,4]
# print(comman_element(li1,li2))

#8
def rotate_list(li,k):
    k = k % len(li)
    print(k)
    rotated_list = li[-k:]+ li[:-k]
    return rotated_list

li=[1,2,3,4,7]
# print(rotate_list(li,3))
#9
def even_indices(li):
    sum = 0
    for idx, ele in enumerate(li):
        if idx%2 == 0:
            sum += li[idx]
    return sum

# li = [2,1,2,1,2]
# print(even_indices(li))

#10
def split_list(li):
    k=len(li)//2
    first_li = li[:k]
    sec_li = li[k:]
    return first_li,sec_li

li=[1,2,3,4,5,6]
# print(split_list(li))