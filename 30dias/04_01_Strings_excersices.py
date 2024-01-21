
# 1.- Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

p1 = 'Thirty'
p2 = 'Days'
p3 = 'of'
p4 = 'Python'
space = ' '
full_name = p1 + space + p2 + space + p3 + space + p4
print ('#1', full_name) 

# 2.- Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

qu = str ( ' " ' )
spc= str ( '  ')
w1= str ( 'Coding' )
w2 = str ('for')
w3 ='ALL'
phrase = qu + spc + w1 + spc + w2 + spc + w3 + spc + qu

print('#2' ,phrase)

# 3.- Declare a variable named company and assign it to an initial value "Coding For All".

qu = str ( ' " ' )
spc= str ( '  ')
w1= str ( 'Coding' )
w2 = str ('for')
w3 ='ALL'
phrase = qu + spc + w1 + spc + w2 + spc + w3 + spc + qu

w4 = 'COMPANY : '
print('#3', w4, phrase)

# 4.- Print the variable company using print().

qu = str ( ' " ' )
spc= str ( '  ')
w1= str ( 'Coding' )
w2 = str ('for')
w3 ='ALL'
phrase = qu + spc + w1 + spc + w2 + spc + w3 + spc + qu

w4 = 'COMPANY : '
comp= w4 + spc + phrase + spc

print ('#4', comp)

# 5.- Print the length of the company string using len() method and print().

qu = str ( ' " ' )
spc= str ( '  ')
w1= str ( 'Coding' )
w2 = str ('for')
w3 ='ALL'
phrase = qu + spc + w1 + spc + w2 + spc + w3 + spc + qu
w4 = 'COMPANY : '
comp= w4 + spc + phrase + spc

long = int(len (comp) )
print ('#5', 'La cantidad de palabras es : ', long, 'Palabras')

# 6.- Change all the characters to uppercase letters using upper() method.

qu = str ( ' " ' )
spc= str ( '  ')
w1= str ( 'Coding' )
w2 = str ('for')
w3 ='ALL'
phrase = qu + spc + w1 + spc + w2 + spc + w3 + spc + qu
w4 = 'COMPANY : '
comp= w4 + spc + phrase + spc
#long = int(len (comp) )
UPcomp=comp.upper()

print ('#6', UPcomp)

# 7.- Change all the characters to lowercase letters using lower() method.

qu = str ( ' " ' )
spc= str ( '  ')
w1= str ( 'Coding' )
w2 = str ('for')
w3 ='All'
phrase = qu + spc + w1 + spc + w2 + spc + w3 + spc + qu
w4 = 'COMPANY : '
comp= w4 + spc + phrase + spc
#long = int(len (comp) )
UPcomp=comp.upper()
print ('#7-1', UPcomp)
upcomp=UPcomp.lower()
print('#7-2', upcomp)

# 8.- Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.


ph1= 'Coding For All'
cap=ph1.capitalize()
tit=ph1.title()
swc=ph1.swapcase()
print('#8', cap, spc, tit, spc, swc)

# 9.- Cut(slice) out the first word of Coding For All string.


opt1= ph1[0:6]
opt2=ph1[7:14]


print('#9', 'Caso 1: ', opt1, spc, 'Caso 2: ', opt2)


# 10 .- Check if Coding For All string contains a word Coding using the method index, find or other methods.


#ph1= 'coding for all'    -------> la string 'coding for all' ya esta definida previamente
substring = 'Coding'

substrcontained = substring in ph1

print('#10', 'The word "Coding" is in cadena ph1 ? : ' , substrcontained)


try:
  #encuentra la palabra coding en el string ph1

  index=ph1.index(substring)
  print('#10-1', f"palabra' {substring} ' encontrada con indice {index} ")
except ValueError:
  print(f"palabra '{substring} no encontrada en el texto ")


print('#10-3',f"palabra' {substring} ' encontrada con indice {index} ")

# 11 .- Replace the word coding in the string 'Coding For All' to Python.

print('#11', ph1.replace('coding','pyhton'))

# 12 .- Change Python for Everyone to Python for All using the replace method or other methods.

ph2= str('Python For Everyone')
print('#12-1', 'Se reemplaza "Everyone" por "All" en la frase :',ph2)
print('#12-2', 'Se hace el cambio : ', ph2.replace('Python for Everyone','Python for All'))

# 13 .- Split the string 'Coding For All' using space as the separator (split()) .

print('#13', ph1.split(   ))

# 14 .-  "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

list= " Facebook -- Google -- Microsoft  Apple  IBM  Oracle  Amazon "
print('#14', list.split(  ))

# 15 .- What is the character at index 0 in the string Coding For All.

ph1List= ['C', 'o', 'd', 'i', 'n', 'g',  'F', 'o', 'r',  'A', 'l', 'l', ]

letter0= ph1List[0]
print('#15-1', letter0)

letter5=ph1List[6]
print('#15-2', letter5)

# 16 .- What is the last index of the string Coding For All.

lastindex = len(ph1List) - 1
print('#16', 'El ultimo indice del string es : ', lastindex)


# 17 .- What character is at index 10 in "Coding For All" string.

index10 = ph1List[10]
print('#17', 'El indice 10 del string es : ', index10)

# 18 .- Create an acronym or an abbreviation for the name 'Python For Everyone'.

ph2List= ['P', 'y', 't', 'h', 'o', 'n',  'F', 'o', 'r',  'E', 'v', 'e', 'r', 'y', 'o', 'n', 'e' ]

indexAcronph2 = print('#18', 'La abreviacion es : ', ph2List[0],ph2List[6], ph2List[9])


# 19 .- Create an acronym or an abbreviation for the name 'Coding for All'.

indexAcronph1 = print('#19', 'La abreviacion es : ', ph1List[0],ph1List[6], ph1List[9])

# 20 .- Use index to determine the position of the first occurrence of C in Coding For All.

indexC=ph1List.index('C')
print('#20', 'El indice de la letra C es : ', indexC)


#21 .- Use index to determine the position of the first occurrence of F in Coding For All.

indexF=ph1List.index('F')
print('#21', 'El indice de la letra F es : ', indexF)

# 22 .- Use rfind to determine the position of the last occurrence of l in Coding For All People.

ph1= 'Coding For All'

Pos_l=print('#22', 'The last pos of "l" es : ', ph1.rfind('l'))


#23.- Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because 
#because is a conjunction'

sentence1= 'You cannot end a sentence with because because, because is a conjunction '
ph3='because'
firstbecause=print('#23', 'La primera posicion de because es : ', sentence1.index(ph3))


#24.- Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

lastbecause=print('#24', 'La ultima posicion de because es : ', sentence1.rindex(ph3))

#25.- Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'


startindex1=sentence1.find("You")
endindex1=sentence1.find("because")
sliced1=sentence1[startindex1:endindex1]

sliced2=sentence1[-17: -1]

print('#25' ,sliced1, '<------', 'because because because is cleared',' ------>',sliced2)


#26.-Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

firstocurr=print( '#26' , 'La ubicacion de la primera aparicion de "because" es : ' , sentence1.find('because'))

#27.-Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('#27', 'La misma respuesta de # 25')

#28 .- Does ''Coding For All' start with a substring Coding?


startStr=ph1.startswith('Coding')
print('#28' , 'El string comienza con la palabra "Coding" : ', startStr)


#29 .- Does 'Coding For All' end with a substring coding?

endStr=ph1.endswith('coding')
print('#29' , 'El string termina con el texto "coding "?  : ' ,endStr)


#30 .- '   Coding For All      '  , remove the left and right trailing spaces in the given string.

ph1remspc= '    -Coding For All-    '
remspc=ph1remspc.strip('    ')
print('#30', remspc)


#31 .- Which one of the following variables return True when we use the method isidentifier():
        #    30DaysOfPython   o    thirty_days_of_python

var1='30DaysOfPython'
var2='thirty_days_of_python'
print(   '  #31'  ' var 1 is a valid name to be a var : ? ' , var1.isidentifier(),'   and   ' , 'var 2 is a valid name to be a var : ? ' , var2.isidentifier())



#32 .- The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

list2=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list2spcstr= '  '.join(list2)

print('#32 ' , 'La lista que de la sgte manera :  ', list2spcstr)

#33.- Use the new line escape sequence to separate the following sentences.

print ('#33', 'I am enjoying this challenge  .\n  I just wonder what is next.' )

#34 .- Use a tab escape sequence to write the following lines.
     #Name      Age     Country   City
     #Asabeneh  250     Finland   Helsinki
print('#34')
print('Name  \t  Age \t Country  \t City  ')
print('Asabeneh  250     Finland   Helsinki' )

#35 .- Use the string formatting method to display the following:
'''radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.'''

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
print('#35', formated_string)


#36 .- Make the following using string formatting methods:

a = 8
b = 6
print('#36')
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))








