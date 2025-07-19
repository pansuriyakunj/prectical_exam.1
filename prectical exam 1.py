while True:
    print("Welcome to the Bill Splittert App!")

    bill=float(input("Enter total bill amount:",))
    if bill<0:
        print("bill can't be negetive.")

    
    people=int(input("Enter number of people:",))
    if people<=0:
        print("people must have be more than 0:",)
 
    
    tip = int(input("Enter tip percentage(o/5/10/20):"))
    if tip not in (0,5,10,15,20):
        print("invalide tip percentage")
   

    tip=(tip/100)*bill
    total=bill+tip
    person=total/people

    print("tip:",tip)
    print("total:",total)
    print("per_person:",person)


    again=(input("would you like to calculate another bill?(yes,no):"))
    if again != 'y':
        break
    
'''
Welcome to the Bill Splittert App!
Enter total bill amount:1555.5
Enter number of people:4
Enter tip percentage(o/5/10/20):5
tip: 77.775
total: 1633.275
per_person: 408.31875
would you like to calculate another bill?(yes,no):y
Welcome to the Bill Splittert App!
Enter total bill amount:'''
