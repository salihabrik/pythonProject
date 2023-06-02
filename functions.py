def sum(start,end):
    result =0
    if (start>end):
        print("end must be greater than staet")
        return

    for i in range(start,end):
        result = result+i
    return result
s= int(input("enter start num"))
p =int(input("enter end num"))
output = sum(s,p)
print(output)

#############################
def bigger(a,b):
    if a>b:
        return a,b
    else:
        return b,a
result = bigger(10,30)
print (result,type(result))
