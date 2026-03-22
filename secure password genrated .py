"""import random

se= []

num= "1234567890"
cap= "QWERTYUIOPASDFGHJKLZXCVBNM"
sm= "qwertyuiopasdfghjklzxcvbnm"
spe= "`~!@#$%^&*()_-+=*/?><[]\:'/.,"

length= int(input("Length of your password: "))

for i in range(length):
    n= random.choice(num)
    se.append(n)
    ca= random.choice(cap)
    se.append(ca)
    s= random.choice(sm)
    se.append(s)
    sp= random.choice(spe)
    se.append(sp)
    
print(se)"""

import random

num = "1234567890"
cap = "QWERTYUIOPASDFGHJKLZXCVBNM"
sm = "qwertyuiopasdfghjklzxcvbnm"
spe = "`~!@#$%^&*()_-+=*/?><[]\\:'/.,"

all_chars = num + cap + sm + spe

length = int(input("Length of your password: "))

password = []

for i in range(length):
    password.append(random.choice(all_chars))

print("".join(password))