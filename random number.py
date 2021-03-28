l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
def closest(l, n): 
      
    return l[min(range(len(l)), key = lambda i: abs(l[i]-n))] 
      
n = int(input("Enter a number "))
list1 = []
for i in range(0,10):
    a = (((((((i+n)/5)*9)*7)/10+1)/13)*6*5)/n+n**i
    b = closest(l,a)
    list1.append(b)
    l.remove(b)


print(list1[1])


    