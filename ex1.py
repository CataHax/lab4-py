# The smallest and largest of the inputs.
n= 0
lst= []

for e in range(10):
    x= int(input("Enter a number:"))
    t= max(x,n)
    lst.append(t)
    n= t
print(lst)

# END

# The number of even and odd inputs.

lst= []
lys= []


for e in range(6):
    x= int(input("Enter a few numbers:"))

    if x%2== 0:
        lst.append(x)

    else:
        lys.append(x)


print("Cift:",lst)
print("Tek:",lys)

# END

# Cumulative  totals.  For  example,  if  the  input  is  1  7  2  9,  the  program  should  print 1 8 10 19.

lst = []
t = 0

for e in range(4):
    c = int(input("Enter a number:"))
    t = t + c
    lst.append(t)

print("Lista:",lst)

# END

# All  adjacent  duplicates.  For  example,  if  the  input  is  1  3  3  4  5  5  6  6  6  2,
# the program should print 3 5 6

ele= []
l= []
for e in range(10):
    x= int(input("Enter a number:"))
    ele.append(x)

# from stackoverflow:
# t= set([y for y in ele if ele.count(y) > 1])
# print(t)

# my way:
for z in range(10):
    n = 0
    for i in range(10):
        if z != i:
            if ele[z] == ele[i]:
                n= n+1
        elif 2 > n >= 1:
            l.append(ele[z])

print(f"All of the numbers: {ele}")
print(f"Numbers written more than once: {l}")

# END
