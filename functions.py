def sum(start,end):
    result =0
    for i in range(start,end):
        result = result+i
    return result
s= int(input("enter start num"))
p =int(input("enter end num"))
output = sum(s,p)
print(output)