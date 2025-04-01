#pseudocode activities: 2 in 1

#take your pick
programme = input('Pick which program; a or b. ')
if programme == 1:

    romannumeral = int(input("Number? "))
    evenodd = romannumeral % 2
    if evenodd == 1:
        print('Odd number')
    else:
        print('Even number')

elif programme == 2:
    print("I ain't codin that")
else:
    print('You had ONE JOB!!!!!!!')