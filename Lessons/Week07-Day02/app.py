

x = input("Print: " + "")
print ("Print: " + x)


ad = input("Ad: ")
soyad = input("Soyad: ")
tam_ad = (ad.capitalize()) + " " + (soyad.capitalize())
print("Salam, " +  tam_ad + ".")



x = int(input("Number: " ))
y = int(input("Power: " ))
z= (x)**(y)
print(z)

k = pow(int(input("Number1: ")), int(input("Power1: ")))
print(k)

a = "4.92"
b = int(float(a))
print(type(b))

print('Hava neçə dərəcədir?: ') 
x = int(input(' '))
if x <= 10:
    print('Hava soyuqdur')
elif 10 < x < 30:
    print('Hava normaldir')
else :
    print('Hava istidir')


string = 'Proqramlaşdırma'
x = string.find(input("Herf axtar: "))
if x < 0:
    print("Yoxdur")
else :
    print( "Var")

a = 'Visual'
b = 'Studio'
c = (a) + ' ' + (b)
print(c)
    