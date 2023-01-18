n=int(input())
add=0
pro=1

while(n>0):
    rem=n%10
    add=add+rem
    pro=pro*rem
    n=n//10
    
if add==pro:
    print("Spy Number")
else:
    print("Not Spy Number")
    