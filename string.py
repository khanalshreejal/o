def birthday(s):
    if 'birthday' in s:
        return True
    else:
        return False

a = birthday('happy birthday') 
if a:
    print('happy birthday')
else:
    print('no birthday Today')