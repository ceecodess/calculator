# This is a simple student calculator
# to simply get total and average score.

student_name=input("what is your name? ")
scoreinmaths=input("score in maths? ")
scoreinenglish=input("score in english? ")
total=int(scoreinmaths) + int(scoreinenglish)
average=total/2
print(f' hello {student_name} your total score is {total}')
print(f' your total average is {average}')


# retry of building cal
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

#second retry
numb1=float (input('what is your first no:  '))
operation=input('choose bet add,sub,mult.div')
numb2=float (input('what is your second no:  '))

if operation=='add':
    print(numb1 + numb2)
elif operation=='sub':
    print(numb1 - numb2)
elif operation=='mult':
    print(numb1*numb2)
elif operation=='div':
    print(numb1/numb2)
else:
    ('printinvalid')
