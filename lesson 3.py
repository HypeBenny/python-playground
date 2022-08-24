x = 42
y = 2
try:
print(x / y)
except ZeroDivisionError:
print('fuck u')
else: 
 print('holy win') 
finally: 
 print('watsasssssspppp')  
 price = 3
if price >= 2.00: #when using conditions(if) always leave 4spaces in the next line before u put your code.
    tax = .05     #note signs  <> - less n greater than  >=(greater or equal to)
    print(tax)            # == (is equal to)   != (not equal to)
else:
    tax = 0
    print(tax)
country = input( 'please state your country: ')
if country == 'Ghana':      #use if country.lower() == 'ghana'
    print('oh Ghnana bwoy')
else:
   print ('sorry bro')
#above line will not run if user changes any of the alphabet cases in line 17 cos strings is case sensitive.
#so we chnge it. 
price = input('please how much did u pay? ')
price = float(price)
if price >= 1.00:
    tax =  0.07
    print('tax is 7 percent')  #note since these line 27 n 28 are indentted, it only runs if the if statement is true 
else: 
   tax = 0
   print('tax rate is 0 ')
country = input('please tell us your country? ')
province = input('please enter province? ')
if province == 'alberta':
    tax = 0.05
elif province == 'yukon':   #u can use elif or if but elif is more appropriate.
    tax = 0.05
elif province == 'ontario': 
    tax = 0.07
else:
    tax = 0.10
print(tax)
 #or u can use this instead of the above.
#nesting if staements withn if statements. 
if country.lower() == 'canada': #here code ask for yur country in line 32. if country is canada, then ask for yur province or else it wont and tax = 0.
   province = input('please enter province? ') 
   if province.lower() == 'yukon':
       tax = 0.05
   elif province.lower() == 'ontario':
       tax = 0.07
   else:
       tax = 0.10
else:
    tax = 0
print('tax is ' + str(tax)) 
#you can lso use and to combine 2 if statements.add()
#adv of nesting if statements instead of using and:
#if u have 2 conditions n u need both to be met, suitable to use next 'if statements' if one of the variables
#involves difficult calculations. in this case, if staement to test the easy variable, if condition is met, before
#u proceed to test the next difficult variable so as not to waste your time(video24) 
if country == 'canada' and province == 'yukon': 
    tax =0.32
    print(tax)
#you can use bulleon variable to rep a long if statement. example
if country == 'canada' and province == 'yukon':
   honour_roll = True
else:
   honour_roll = False
if honour_roll:
   print('congratulations')
#in this case, as we dont want to type the whole line 64 later in the code, we can use a bulleon variable.
#we used honour_roll as our bulleon variable.So if the condition is true, we set the variable to true else false
#so later in line 68, instead of typing the whole condition, we just used the bulleon variable.



    
