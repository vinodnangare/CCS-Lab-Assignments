
p =int(input("Enter Prime Number:"))

q =int(input("Enter primitive root:"))

a=int(input("Enter Private User of User A:"))

b=int(input("Enter Private User of User B:"))

if p==q:
    
    print("Enter Distinct Numbers")
    exit()

c=int(pow(p,a,q))

d=int(pow(p,b,q))
if c==d:
  print("Secreat key of A is :",c)
  print("Secreat key of B is :",d)
  print("Both the secret Key Matches and exchange Successfully!!!")
  exit()



    
