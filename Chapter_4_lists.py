import random


spam = ['cat', 'horse', 'elephant', 'lion'] # create list stored in 'spam' variable

print(spam[0]) # shows the first element from list



invoices = [ ['invoice1', 'invoice2' ], [20.55, 50.99] ] #multiple lists in list

print(f'Invoice: {invoices[0][0]}  Amount: ${invoices[1][0]}') #shows elements


print(spam[-1]) #shows the last element from 'spam' list
print(spam[-2]) #shows the element before the last element from 'spam' list


print(spam[1:3]) #shows the second and third elements from the 'spam' list
                 #['horse', 'elephant']

print(spam[0:-1]) #starts from the first element and stops before the last 
                  #['cat', 'horse', 'elephant']

# shortcuts

print(spam[:3]) #from the first element to third element 

print(spam[1:]) #starts from second element to last

print(spam[:]) #show all elements

print(len(spam)) #total length of the 'spam' list

#End first commit
#---------------------------------------------------------------

cars = ['Mercedes', 'Audi', 'Lada', 'Porsche']

carsSecond = ['BMW', 'Toyota']

cars[-1] = 'Varburg' #change the last element value

print(cars[:]) #show all elements from cars

carsAll = cars + carsSecond #concatenate both lists

print(carsAll) 

del(carsAll[-1]) #delete last element from carsAll

print(carsAll) 

catNames = []

while True :
    
    print(f'Please enter a cat name for cat number (Or enter nothing to stop) {len(catNames) + 1} : ', end='')
    catName = input()

    if(catName == '') :
    
        break
    

    catNames = catNames + [catName] #list concatenation

for catName in catNames : #loop for list
    print(catName + ' ')

for i in range(len(catNames)) : #simple loop with list len
    print(str(i + 1) + '. ' + catName) #shows number of cat and cat name

for i in ['zero', 1, 2, 'three']: #loop for list
    print(i)


car = 'Mercedes'

if car in carsAll :
    print(f'{car} remain in all cars')
else :
    print(f'{car} not remain in all cars')

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat #upack values from list to variables 

print(color)

for index, carMark in enumerate(carsAll) : #with enumareate in for we can get index and item 
    print(index + 1, carMark)

print(random.choice(carsAll)) #random index from list

print(carsAll) #['Mercedes', 'Audi', 'Lada', 'Varburg', 'BMW']
#random.shuffle(carsAll) #random shuffle of list
print(carsAll) #['Lada', 'Mercedes', 'BMW', 'Varburg', 'Audi']

print(carsAll.index('BMW')) #get index of BMW value

carsAll.append('Porsche') #method for adding value in list

print(carsAll)

carsAll.insert(3, 'Opel') #add opel on index 3 in list carsAll

print(carsAll)

carsAll.remove('Opel') #remove Opel from carsAll list

print(carsAll) 

try :
    carsAll.remove('Tesla')
except ValueError :
    print('This value dont remain in carsAll list ')

carsAll.sort() #sorting carsAll

print(carsAll)

carsAll.sort(reverse=True) #reverse sorting carsAll

print(carsAll)

carsAll.sort(key=str.lower) #sorting by lower letter ['a', 'A', 'z', 'Z']

carsAll.reverse() #reverse list

print(carsAll)

#---------------------------------------------------------------------  

print('Four score and seven ' + \
'years ago...') #two lines print

myList = ['listItem1',
          'listitem2',      
          'listitem3']

print(myList)

#8 MAGIC BALL GAME

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(random.choice(messages))
print(messages[random.randint(0, len(messages) - 1)])

name = 'kalatasql'

for i in name :
    print('* * * * * * * ' + i + ' * * * * * * *')

message = 'Hello Python'

newMessage = message[0:6] + 'kalatasql' #from first letter to first space in message variable and conncatenate

print(newMessage)

eggs = [1, 2, 3]
eggs = [4, 5]

print(eggs)
