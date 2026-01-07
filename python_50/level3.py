#1
def largest_num(li):
    li.sort()
    return li[-1]
#1.1
def largest_num2(li):
    num = 0
    for i in range(len(li)):
        if num < li[i]:
            num = li[i]
    return num

li = [4,-5,-6,-7,-4,-2]
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
    first = li[0]
    sec = li[0]
    for i in range(len(li)):
        if first < li[i]:
            sec = first
            first = li[i]
        elif sec < li[i]:
            sec = li[i]

    return sec
print(sec_largest2(li))