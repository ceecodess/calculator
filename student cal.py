
firstno=float(input('what is your first no:  '))
secondno=float(input('what is your second no:  '))
operation=input('choose between add,sub,div,mult  ')

if operation=='add':
    print(firstno+secondno)
elif operation=='sub':
    print(firstno-secondno)
elif operation=='mult':
    print(firstno*secondno)
elif operation=='div':
    print(firstno/secondno)
else:
    ('print invalid')
