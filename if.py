print(22>5)
print(55>99)
print(22==22)
"""""
num = int(input("enter number to test : " ))

if num %2 ==0 :
    print("even number")
else :
    print("odd number")

mark = int(input("enter your mark : " ))
if mark >=90 :
    print("you got B")
elif mark <=80 :
    print("you got C")
elif mark <= 70:
    print("you got D")
elif mark <= 60:
    print("you got E")
else:
    print("you got A")
"""
a = 50
b = 30
max = a if  (a>b) else b
print(max)
#########################
"""""
no = int(input("enter positive number to test :"))
if no >0:
    if no %2 ==0:
        print("even")
    else:
        print("odd")
else:
    print("invalide input")"""
############################
for i in range(2,20 ,3):
    print(i)
l=[20,30,40,50]
for i in l :
    print(i)

############################

count =0
while count <= 10:
    print(count)
    count +=1
    if count == 5:
        break
print ("outside looop")

