
userInfo = {'username' : 'kalatasql', 
            'email' : 'kalata.sql@gmail.com', 
            'password' : 'hashed_pass'}

while True :
    print('Search by username: (blank to quit) ')
    
    inpUser = input()

    if(inpUser == '') :
        break

    if inpUser == userInfo['username'] :
        print(userInfo)

