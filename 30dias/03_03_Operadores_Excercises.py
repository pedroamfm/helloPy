#Calculo de pendientes m
#donde m = (y2-y1) / (x2-x1)

print('Para determinar la pendiente m la ecuacion de la recta : y=2x-2' , 'Ingrese los siguientes valores')
x1= float(input('Ingrese el valor de x1 para determinar valor de y1 : ' ))
y1=float((2*x1-2))
x2=float(input('Ingrese el valor de x2 para determinar valor de y2 : '))
y2=float((2*x2-2))

m=float((y2-y1)/(x2-x1))
m1=float(m)


print('El valor de la pendiente para los valores agregados es : ' , m)

#Calculo de pendiente y distancia euclidiana.

#donde m = (y2-y1) / (x2-x1)
# y la distancia es d(p,q)^2 = (q1-p1)^2 + (q2-p2)^2
# o tambien d = (a^2 + b^2 )^1/2
#Los puntos dados son (2,2) y (6,10)

q1=float(6)
p1=float(2)
q2=float(10)
p2=float(2)
m=float((q2-p2)/(q1-p1))
m2=float(m)
d=float( ((q1-p1)**2 + (q2-p2)**2)**0.5)

print('La pendiente m de los puntos (2,2) y (6,10) es : ', m)
print('La distancia del triangulo en esos puntos es : ' , d)

#Comparar el valor de las slopes en los casos anteriores

print('m caso 1 es igual a m caso 2', m1==m2)





