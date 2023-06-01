print("hello ", "my freinds" ,"voue " ,"etes" , "okey ??")
print("hello ", "my freinds" ,"voue " ,"etes" , "okey ??", end= "........\n")

print("hello ", "my freinds" ,"voue " ,"etes" , "okey ??" , sep = ">>>>>")
#f=open("d:\\myoutput.txt","w")
#print("hello ", "my freinds" ,"voue " ,"etes" , "okey ??", sep = ">>>>>",file=f)
h = "my age is "
print(type(h))
h = 22
print(type(h))
i = 30
j= i
print(i,j)
print(id(i),id (j))
i =50
print(id(i),id (j))


######################
"""var1 = input("enter the the first parametr value")
print (var1, type(var1))

var1 = int (input("enter the the first parametr value"))
print (var1, type(var1))

print(3/5,3//2)
print(5**2 , 4**7)
x =20
x+=20
print(x)
x =65
print(bin(x),oct(x),hex(x))"""
str1 = 'hello world'
str2 = "hello world"
str3 = str("hello world")
str4 =""
print (type(str1),type(str2),type(str3),type(str4))
str5 = "he said that \"i am from algeria\""
print (str5)
str6 = """hello ya bib"""
print (str6)
s =("hello ", "my fre","inds" ,"vo","us " ,"etes" , "okey ??")
print("hello ", "my freinds" ,"voue " ,"etes" , "okey ??" )
print(s * 3)
print(s[4])
print(s[2])
print(s[0:3])
print(len(str1),max(str1))
print(len(s))
print ( str3 .isalnum())