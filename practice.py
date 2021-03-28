list1=[1,2,3,4,1,2,3,4,7,8,2,4,4,5,5,5]
for i in list1:
    if list1.count(i) > 1:
        for j in range(list1.count(i)-1):
            list1.remove(i)
print(list1) 