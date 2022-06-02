import hashlib
import time
begin = time.time()
str1=input("Enter String")

gstr="00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"

i=1
j=1
while(i==1):
    strn = str1+str(j)
    strn1=hashlib.sha256(strn.encode())
    strn2=strn1.hexdigest()
    strn2=strn2.upper()
    if(strn2<gstr):
        i=0
        print("The nonce value is",int(j))
    int(j)
    j+=1

end = time.time()
print(f"Total runtime of the program is {end - begin} seconds.")

    


