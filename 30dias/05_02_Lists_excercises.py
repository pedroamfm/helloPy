list2=['Pedro', '52', '80', 'Single', 'Maitenes23']

list3=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM' ,'Oracle', 'Amazon']

listextend=list2+list3


#17 Reverse the list in descending order using reverse() method

list3.reverse()
print('#17', 'The list in reverse mode ---> ',list3)

#18 Slice out the first 3 companies from the list

slicefirstlist3=list3[3:]
print('#18' , slicefirstlist3)

#19 Slice out the last 3 companies from the list

slicelastlist3=list3[-3:]
print('#19' , slicelastlist3)


#20 Slice out the middle IT company or companies from the list

del list3 [3]
print('#20', 'deleted middle item' , list3)
list3.insert (3,'Apple')


#21 Remove the first IT company from the list

listextend.remove('Facebook')

print('#21 ', 'Deleted firts IT (FB) comp' ,listextend)
listextend.insert (9,'Facebook')

#22 Remove the middle IT company or companies from the list

listextend.pop(6)
print('#22', 'Is removed middle item (item6) ',listextend)
listextend.insert (6,'Microsoft')


#23 Remove the last IT company from the list

listextend.pop(-1)
print('#23', 'Is removed last item (item12) ',listextend)
listextend.insert (12,'Amazon')

#24 Remove all IT companies from the list

del listextend [5:12]
print('#24', 'Is removed all IT comp',' The remains items are : ', listextend)


#25 Destroy the IT companies list

print('#25', ' items about IT comp are no longer exists on listestend : see you  ---->' ,listextend)

#26 Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print('#26', 'The new lists are : ', front_end, 'and' , back_end)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack=front_end+back_end
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print('#27', ' added Python and SQL in the list' ,full_stack)


#28 .- Exercises: Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] #age of students
print(ages)
ages.sort()
print(ages)
minage=min(ages)
maxage=max(ages)
print('#28.1', 'The sort list is :',ages,'The min age is:', minage,'The max age is: ', maxage) # Sort the list and find the min and max age

print('#28.2' ,'The previous result was made with a method min and max \n      Next will remove item min and max with del method and readded with insert method')
del ages [0:2]
del ages [-1]
print('     Removed min and max' , ages)

ages.insert(0,19)
ages.insert(1,19)
ages.insert(9,26)

print('# 28.3', 'Added min and max items in the list ' ,ages)

import statistics
media = statistics.median(ages)   # Find the median age (one middle item or two middle items divided by two)
print( '#28.4' ,"La media is : :", media)  # Output: Media del listado usando statistic module

average = sum(ages) / len(ages)
print('#28.5' , 'The average of the list is : ' ,average)

range = maxage-minage
print('#28.6', 'The range of list is : ' ,range)

comp1=abs((minage-average))
comp2=abs((maxage-average))
print('value 1:' ,comp1)
print('value 2:' ,comp2)

if comp1==comp2:
    print('#28.7' ,'The values are equal')
else:
    print('#28.7' ,'The values are different')


paises= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

longlist = len(paises)
print('#28.8', 'The long of list is : ' ,longlist)
miditem=int((longlist-1)//2)
print('#28.8', 'The middle item in the list is : ', miditem)
miditemtext=paises[miditem]
print('#28.8' , 'This item correspond to : ' , miditemtext )
mitad1=paises[:4]
mitad2=paises[-3:]
print ('#28.9 ' , mitad1 , 'and' , mitad2)


paises= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
p1,p2,p3,*rest = paises

print(p1,p2,p3, 'and Scandic Countries' , rest)


