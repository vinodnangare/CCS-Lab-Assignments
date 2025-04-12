import hashlib                
m=input("Enter A Message :")
result=hashlib.md5(m.encode())
print(result)