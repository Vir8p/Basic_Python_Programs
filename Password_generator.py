import random
a='1234567890'
b='abcdefghijklmnopqrstuvwxyz'
c='!@#$%^&*()'
d='ABCDEFGHIJKLMNOPQRTUVWXYZ'
union=a+b+c+d
length=8
password=''.join(random.sample(union,length))
print('Password : ',password)