
mi_age=int(52)
mi_height=float(80.45)
#almacenar numero complejo
complex_numb=complex(2+5j)

#Area triangulo

constante=float(0.5)
base= float(input('Ingresa la base del triangulo : '))
Altura= float(input('Ingresa la altura del triangulo : '))

Area=float(constante*base*Altura)
print('El area es : ', Area)

#Perimetro del Triangulo
a=float(input('Ingresa el valor del lado a del triangulo : '))
b=float(input('Ingresa el valor del lado b del triangulo : '))
c=float(input('Ingresa el valor del lado c del triangulo : '))

Perimetro=float(a+b+c)
print('El perimetro es : ', Perimetro)        

#Area yperimetro del Rectangulo

length=float(input('Ingresa el valor de longitud : '))
width=float(input('Ingresa el valor del ancho : '))

area=float(length*width)
Perimetro=float(2*(length+width))

print('El area es : ',area, 'mts^2')
print('El perimetro es : ',Perimetro, 'mts')

#Calculo de area y circunferencia

radio=(float(input('Ingrese el radio del circulo en cms')))
pi=float(3.141596)
area=(pi*radio**2)
Perimetro=(2*pi*radio)
print('El area de la circunferencia es : ', area, 'cms^2')
print('El perimetro de la circunferencia es : ', Perimetro, 'cms')














