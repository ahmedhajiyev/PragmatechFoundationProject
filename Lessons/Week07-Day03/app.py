x = int(input('Dairənin diametri: '))
p = 3.14
y = p*((x/2)**2)
print(y)


x = """Sweep through the days Like children that can't stay awake"""
z = int(input('Reqem: '))
if 0 <= 1 <= len(x): 
    print(x[:z])
if z > len(x):
    print("Error")
if z < 0:
    print('False')


import random
name = input('Adiniz: ')
surname = input('Soyadiniz: ')
number = random.randint(0, 1000)
randommail = (name) + (surname) + (str(number)) + '@gmail.com'
print(randommail)


x = int(input('1ci reqem: '))
y = int(input('2ci reqem: '))
z = input('Riyazi emel: ')
if z == "+":
    print(f"{x}+{y}={x+y}")
if z == "-":
    print(f"{x}-{y}={x-y}")
if z == "*":
    print(f"{x}*{y}={x*y}")
if z == "/":
    print(f"{x}/{y}={x/y}")


n = int(input('Reqem daxil edin: '))
if n % 2 == 0:
    print('EVEN')
else:
    print('ODD')


n = int(input('Reqem daxil edin: '))
a = int(input('Bolunen daxil edin: '))
b = int(input('2ci Bolunen daxil edin: '))
if n / a and n / b and n % a == 0 and n % b == 0:
    print('YES')
else:
    print('NO')

n = int(input('Reqem daxil edin: '))
if n < 0:
    print('Negative')
elif n > 0:
    print('Positive')
else:
    print('Zero')


a = int(input('1ci teref: '))
b = int(input('2ci teref: '))
c = int(input('3ci teref: '))
if a+b > c and a+c > b and b+c > a:
    print('YES')
else:
    print('NO')


x = int(input('Shagirdin nealiyyeti: '))
if 1 <= x <= 3:
    print('Inital')
if 4 <= x <= 6:
    print('Average')
if 7 <= x <= 9:
    print('Sufficent')
if 10 <= x <= 12:
    print('High')


x = int(input('Reqem daxil edin: '))
y = x-1
print(y)


a = int(input('Bolunen: '))
b = int(input('Bolen: '))
c = str(a%b)
d = str(int(a/b))
print("Tam:" + (d))
print("Qaliq:" + (c))


x = int(input('Reqem daxil edin: '))
y = x*(-1)
print(y)


x = input('Reqem daxil edin: ')
y = 0
for z in x:
    y += int(z)
j = y**2
print(j)


x = input('Adiniz: ')
if 3 <=  len(x) <= 11: 
    y = input('Soyadiniz: ')
    if 5 <= len(y) <=15:
        z = input('Dogum iliniz: ')
        if len(z) == 4:
            a = input('Emailiniz: ')
            b = "@gmail.com"
            if 10 <= len(a) <= 22: #and a in "@gmail.com":
                c = input('Sifre: ')
                if 6 <= len(c) <= 13:
                    d = input('Sifreni tesdiq edin: ')
                    if c == d:
                        print('Qeydiyyat Tamamlandi')
