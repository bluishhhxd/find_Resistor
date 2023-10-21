def username():
    while True:
        name=input("Please enter your username: ").replace(" ",'').lower()
        if not name:
            print("Name can't be empty")
        elif len(name)<3:
            print("Name must be 3 or greater than 3 characters, Please try again")
        elif len(name)>15:
            print("Name can't be greater than 15 characters, Pleas try again")
        else:
            return name

def parallel():
    while True:
        try:
            num_resistors=int(input("Number of resistors= "))
            inverse_resistors=[]
            for i in range(1,num_resistors+1):
                i=float(input(f"Resistor {i} = "))
                if i==0:
                    pass
                inverse_resistors.append(1/i)
                    
            Sum=sum(inverse_resistors)
            R_eq=1/Sum
            print(f"Equivalent resistor= {R_eq}")
            return
        except ValueError:
            print("Please enter a Numerical digit")

def series():
    while True:
        try:
            num_resistors=int(input("Number of resistors= "))
            Sum=0
            for i in range(1,num_resistors+1):
                i=float(input(f"Resistor {i} = "))
                Sum+=i
            print(f"Equivalent resistor= {Sum}")
            return
        except ValueError:
            print("Please enter a Numerical digit")

while True:
    name=username()
    while True:
        try:
            ask=input("Choose one you wanna apply (parallel/series): ")
            if ask.lower() == "parallel":
                parallel()
                break
            elif ask.lower() == "series":
                series()
                break
            else:
                print("Try Again")
                continue
    
        except (NameError, ValueError, ZeroDivisionError):
            print("Choose again, Value of resistor is always positive")
            
    choice=input("Do you want to try again (Yes/No): ").lower()
    if choice!='yes':
        print("okay")
        break
