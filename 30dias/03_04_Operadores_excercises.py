# para ecuacion : y = x^2 + 6x + 9
#averiguar valor para y=0

x=float(input('Ingrese el valor de x para la ecuacion : y=x^2+6x+9  '  ))
sol_y=float(x**2+6*x+9)
print('El valor de y para la ecuacion anterior es : ', sol_y)
eq=(sol_y== 0)
print('para el valor dado de x, es y = 0  ? :  ', eq)

#Encuentre la longitud de next words: python and dragon, and compare:

w1='python'
w2='dragon'
longw1=len(w1)
longw2=len(w2)
print('La longitud de la palabra "python es" : ',longw1)
print('La longitud de la palabra "dragon" es : ', longw2)
lx=longw1==longw2
print('tienen la misma longitud ? : ',lx)

# Verificar que ambas palabras tengan los carateres "on"

w11= 'on' in w1
w12= 'on' in w2

print ('Ambas palabras tienen los caracteres "on" ?? :' , w11 and w12)

# Verificar si la palabra "jargon aparece en la string "I hope this course is not full of jargon"

jar= str('I hope this course is not full of jargon')
jarst= 'jargon' in jar
print('Dentro de la cadena aparece eñ string "jargon" ?? ' , jarst)

#Negar la igualdad de w11 y w12
notON=not(w11 and w12)
print('negacion de string on', notON)

#longitud del texto "python", convertir a float next a string

print('La longitd de la string "python es" : ', longw1)

longw1float=float(longw1)
longw1str=str(longw1float)
print('La longitud del string "python" en float es : ',longw1float)
print('La longitud del string "python" en string es : ',longw1str)

#comprobar si numero es par (considerar remainder =0)


numerador=int (input( 'Ingrese el numero: '))
print(' Si el numero es divisible por 2 el resultado es TRUE')
denominador= int (2)
divisionh=(numerador%denominador)
print('el resultado de la division modulo es : ', divisionh)
result= (0 == divisionh)
if result is True:
     print('El numero es divisible por 2')
else:
     print('El numero no es divisible por 2')

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
     
fdiv=7//3
numb=int(2.7)
z=fdiv == numb

print('usando tipo int seran iguales?? : ',z)

#Check if type of '10' is equal to type of 10

t1=type('10')
t2=type(int(10))
comp=t1==t2
print('El tipo de elemento de "10" y int(10) son iguales ??? : ',comp)

#Check if int('9.8') is equal to 10

t11=type(float(9.8))
t12=type(int(10))
comp= t11==t12
print(comp)

t111=type(int(9.8))
t122=type(int(10))
compe= t111==t122
print(compe)


# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120

horas= float(input('Ingrese la cantidad de horas : '))
pphoras=float(input('Ingrese su pago por hora : '))
psemanal=float(horas*pphoras)
print('su pago semanal correspondiente es : ', psemanal, 'dolares')

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

años=float(input('Ingrese su edad en años : '))
x=float(60*60*24*30*12)
seconds=float(años*x)

print('Los segundos que tu has vivido son : ', seconds)

#write a matrix 5x5

print ('1 1 1 1 1 ', end='\n')
print ('2 1 2 4 8 ', end='\n')
print ('3 1 3 9 27', end='\n')
print ('4 1 4 16 64', end='\n')
print ('5 1 5 25 125', end='\n')







