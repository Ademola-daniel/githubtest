password='king'
no_tries=3
tries=0
while tries !=no_tries:
    data=input('> ')
    tries+=1
    if data.lower()==password:
        print('Welcome sir')
        break
    elif tries==no_tries:
        print('Sorry come again in two minutes')
    else:
        print('try again')
