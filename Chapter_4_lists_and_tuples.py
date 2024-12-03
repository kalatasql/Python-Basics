
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

