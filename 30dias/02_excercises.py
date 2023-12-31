
first_name = 'Pedro'
last_name = 'Fuentes'
#full_name = ['Pedro' ' ' 'Fuentes']
full_name = first_name,last_name
country = 'Chile'
City = 'Santiago'
age = 26
year = 2023
is_married = True
is_light_on = False

#Variable multiple  ---->
#first_name, last_name, full_name, country, City, age, year, is_married, is_light_on, = 'Pedro', 'Fuentes', ['first_name','last name'], 'Chile', 'Santiago', 26, 2023, True, False

print(first_name)
print(last_name)
print('Nombre Completo : ', full_name)
print('El pais es:', country)
print('La ciudad es:', City)
print('Edad', age)
print(year)
print('esta casado? :', is_married)
print('Esta prendida la lampara ? :', is_light_on)

print(type (first_name))
print(type (last_name))
print(type (full_name))

print(type (country))
print(type (City))
print(type (age))
print(type (is_married))
print(type (year))
print(type (is_light_on))


a=len(first_name)
b=len(last_name)
print('La longitud de mi nombre es : ', a)
print('La longitud de mi apellido es : ',b)
print('el valor de la diferencia entre ambos valores (b - a) es :' ,b-a)

num_one = 5
num_two = 4
suma=(num_one+num_two)
diff=(num_two-num_one)
multi=(num_one*num_two)
division=(num_one/num_two)
remainder=(num_two%num_one)
expo=(num_one**num_two)
floor_div=num_one//num_two

print('El primer numero es :',num_one)
print('El segundo numero es :', num_two)
print('La suma es: ',suma)
print('La diferencia es : ', diff)
print('La multiplicacion es :', multi)
print('La division es :', division)
print('La resto es :', remainder)
print('La potencia 5^4 es :', expo)
print('floor es :', floor_div)

pi=3.141596
radio=40
area_circulo=(3.141596*radio**2)
circunferencia_circ= (2*pi*radio)

print('El area del circulo es : ', area_circulo, 'mts2')
print('La circunferencia del circulo es : ', circunferencia_circ, 'metros')


nombre=input('Ingrese el nombre : ')
apellido=input('ingrese el apellido : ')
pais=input('Ingrese el pais de origen : ')
edad=input('Ingrese la edad : ')

print(nombre,apellido,pais,edad)





