l1 =[10,20,30,40,50]
l2 = ["mohamed",35,"ali",40]
l3 = list()
l4 = ([12,14,16])
l5 = list("python")

print(l5[3])
print(l5[-2])
print(l5[0])
print(l5[0:3])
print(l5[3:])
#print(len(l4),max(l4),min(l2),sum(l4))
print (l1.count(30))
l1.extend([20,33,56,66])
print(l1)
print(l1.index(30))
print(l1.pop(7))
l1.reverse()
print(l1)
l1.remove(20)
print(l1)

t1 = (10,20,30,40,50,80,90 )
t2 = tuple ([50,60,70,80])
t3 = tuple()
t4 = tuple("puthon")
print(t1)
print(t1[0])
print(t1[2:])
print(t1[:4])
print(t1[2:])
print(max(t2),min(t1),len(t1),sum(t1))
print(60 in t2)
t7 = ((1,2,3),(4,5,6),"hello")
print(t7[0])
print(t7[0][2])
for i in t1:
    print(i ,end="\n")