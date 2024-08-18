import json
n=int(input('---ENTER YOUR CHOICE---\n- Choose 1 for SignUp\n- Choose 2 for SignIn\n->'))
try:
    with open('details_up.json','r') as f:
        dict_var = json.load(f)
except:
    dict_var={
        'username':[],
        'password':[],
        'number':[]
    }
if n==1:
    uname=input('Enter Username')
    pword=input('Enter Password')
    numb=int(input('Enter Number'))
    dict_var['username'].append(uname)
    dict_var['password'].append(pword)
    dict_var['number'].append(numb)
    with open('details_up.json','w') as f:
            json.dump(dict_var,f)
elif n==2:
    uname=input('Enter Username')
    pword=input('Enter Password')
    try:
        index1=dict_var['username'].index(uname)
        if pword==dict_var['password'][index1]:
            print(dict_var['number'][index1])
        else:
            print('----Your credentials are wrong ----')
    except:
        print("Invalid username or password\n Please sign up first")
else:
    print("Enter correct choice")
        

