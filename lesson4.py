names = ['ben', 'suzy','dray', 'akua'] #[] is used for making a list in python
print(names[1])
names.append('aku') add quotaions marks else it will treat it as number. esp when appendn a string.
scores = []
scores.append(98) #adds a new item at the end of the list scores.
scores.insert(0,500) #this option inserts 500 as the 1st item in the list cos of the 0. 1 will insert in 2nd place.
print(names)
print(scores)
print(scores[1]) #prints the 2nd item in the score collection. 0 prints 1st. 1 prints 2nd, 2 prints 3rd. etc.
print(len(names)) #prints the number of items in the name list.
names.sort()
print(names)
#ARRAYS - same as a list but only conatins one data type. example numbers
#LIST - it can contain diff types of data type
#from array import array  #always say this before usimg arrays.
scores = array('d')
scores.append(98)
scores.append(99)
print(scores)
print(scores[1])
presenters = names[1:3] #this used to get smaller list from the universal list. so 1:3 means names from index 1 to 3
#indexes in a list are e.g [0 ben 1 akua 2 aku 3 kojo 4] these are the indexex. so 0:3 will be .
print(presenters)
#DICTIONARY how to create it
full_name = {} #it has been created.an empty one here
full_name = {'first': 'adwoa' } #another e.g. a dictionray is a list of key value pairs. a key value pair consist
#of two related data pair. e.g brand:apple. price:100,colour:black. so brand will be key and apple will be the value
full_name['last'] = 'bayor' #this how u add item(key value pairs) in a dictionary.
print(full_name)
print(full_name['last'])
name = []
name.append('koska')
name.append(full_name) #adding a dictionary inside of a list.
name.append(98)
print(name)
#LOOPS
people = ['ben', 'ken', 'joe','cat']
for name in people:   #for loop suitable for working on  items in a list
    print(name)

index = 0
while index < len(people):
    print(people[index]) #WHILE LOOP suitable when a condition changes e.g flipping thru pages
    index = index + 1

first_name = 'Susan'
fni = first_name[0:1] #how u get a particular string in a group of strings to be displayed.
print(fni)
for x in range(1,10): #range is same as for loop but instead of looping thru a list, it auto creates a list of numbrs
#where 1 will be strting no. and 10 will be the lenght of list.(no. of items in the list)
  print(x)

#FUNCTIONS

from datetime import datetime
def print_time():             #here we define print_time fuction and all the codes that we put under this code on
    print('task completed ')   #line 54 bcomes part of the fxn. so anytime we call the fxn anywhr in our code, it
    print(datetime.now())     #executes all the codes included in it.always 4spaces before writn codes on the next
    print()                    #line after defining the fxn.
    
firstname = 'benny'
print_time()
    
def print_time(taskname):   #here u add a parameter(here taskname is our parameter) to the fxn to modify it so it can do diff things anytime u use
    print(taskname)          #the fxn somewher n u associate a value/string to the parameter. e.g
    print(datetime.now())
    print() 
    
first_name = "benny"
print_time('display first name')

for x in range(0,5):
    print(x)       
print_time('loop completed')

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('pls enter first name? ')
firstname_initial = get_initial(first_name)

last_name = input('pls enter last name? ')
lastname_initial = get_initial(last_name)
print('your initials are  ' + firstname_initial + lastname_initial )

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()   #this means if user input in upper case, u get uppercase 
    else:                              #else u get lower case.
        initial = name[0:1]
    return initial

first_name = input('pls enter first name? ')
firstname_initial = get_initial(first_name,False)  #u set force_uppercase to false here also. 

print('your initials are  ' + firstname_initial)

 #OR
 
def get_initial(name, force_uppercase=True): #u can set the booleon value to true here. it becomes default.
    if force_uppercase:                   #so it wont be compulsory to set it later when callin the fxn(line 108).
        initial = name[0:1].upper()       
    else:
        initial = name[0:1]
    return initial

first_name = input('pls enter first name? ')
firstname_initial = get_initial(name=first_name, force_uppercase=False) #u can also set it here manually. this means it wont have to follow any order.
                                                                    #if u are not assigning values manually, it has to be in order. like code in line 100 
print('your initials are  ' + firstname_initial)







  
    
 

