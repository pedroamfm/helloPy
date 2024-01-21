#1 .- Declare an empty list
listvacio=[ ]
print('#1' ,'El listado vacio es: ', listvacio)

#2 .- Declare a list with more than 5 items

list1=['Frutas', 'Verduras', 'Motores', 'Herramientas', 'Libros', 'Discos', 'Monitores']
print('#2' ,list1)


#3 .- Find the length of your list

print('#3', 'Los items contenidos en el listado son : ', len(list1))

#4.- Get the first item, the middle item and the last item of the list

fml_list1= list1[0:1], list1[3:4],list1[ -2:-1] 


#print(firstlist2,midlist2, lastlist2)
print('#4.1' ,'El primer elemento es :', fml_list1[0])
print('#4.1' ,'El segundo elemento es :', fml_list1[1])
print('#4.1' ,'El tercer elemento es : ', fml_list1[2])

#5.- Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

list2=['Pedro', '52', '80', 'Single', 'Maitenes23']
print('#5', list2)

#6.- Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

list3=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM' ,'Oracle', 'Amazon']
print('#6', list3)

#7 .- Print the list using print()

print('#7' ,list3)

#8 .- Print the number of companies in the list

print('#8', 'La cantidad de compañias es : ', len(list3))

#9 .-Print the first, middle and last company

print('#9.1', ' The 1st Company is: ', list3[0])
print('#9.1',' The middle Company is: ', list3[4])
print('#9.1',' The last Company is: ', list3[-1])


#10 .-Print the list after modifying one of the companies

#print('Se borra el listado completo' ,list4.clear())
del list3[0:2]
print('#10','Deleted from list 4 item 0 y 1 :remains 5 items ' ,list3)

#11 .-Add an IT company to it_companies

list3.insert(0,'Google')
list3.insert(0,'Facebook')
print('#11' ,'Add the items removed form previous excercise. .\n list3 remains in the original order', list3)

#12 .-Insert an IT company in the middle of the companies list

list3.insert(3, 'Samsung')
print ('#12' ,list3, 'La cantidad de items es ahora : ',len(list3))

#13 .-Change one of the it_companies names to uppercase (IBM excluded!)

del list3[5]
upp_list3 = list(map(str.upper, list3))

print('#13', 'the elements of the list are changed to uppercase, .\n (except IBM)', upp_list3)

list3.insert( 5, 'IBM')
print('Re-add item IBM',list3)

#14 .-Join the it_companies with a string '#;  '

list2.extend(list3)
print ('#14.- ','Se agregan items usando metodo extend() ' , '# #',list2)

listextend=list2+list3
print('#14.1' , 'usando operado +' ,listextend)


#15 .-Check if a certain company exists in the it_companies list.

itemin=input('Insert the company name  :')

if itemin in listextend:
 print('The company is founded in list : ', itemin)

else:
   print ('#15' , 'The company is not in list : ', itemin)

#16 .-Sort the list using sort() method

upp_list3.sort()
print('#16' , upp_list3)

#17 .-Reverse the list in descending order using reverse() method

upp_list3.sort(reverse=True)
print('#17' , upp_list3)



