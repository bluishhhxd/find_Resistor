while True:
    name= input("Enter your username, sir? ")
    list_parallel=[]
    Total_parallel=[]
    Sum=0
    name=name.replace(" ",'').lower()
    
    if not name:
        
        print("Name can't be empty")
        continue
    
    elif len(name)<=3:
        
        print("Name must have more than 3 characters")
        continue
    
    elif len(name)>=10:
        
        print("Name can't have 10 or more than 10 characters")
        continue
    
    else:
        pass
    
    print(f"Your username is {name}")

    
    while True:
        
        ask=input(f"What would you like to do today sir {name}, find parallel or series?: ")

        try:

            if ask.lower()== "parallel":

                number_resistor=int(input(f"How many resistors are there,SIR {name}? "))

                for i in range(1,number_resistor+1):
                    i=float(input(f"Resistor {i}= "))
                    list_parallel.append(1/i)

                Sum=sum(list_parallel)
                print(f"Your answer is {1/Sum}")
                break
                
                                        
            elif ask.lower()=="series":

                number_resistor=int(input(f"How many resistors are there,SIR {name}? "))

                for j in range(1,number_resistor+1):
                    j=float(input(f"Resistor {j}= "))
                    Sum+=j

                print(f'Your answer is {Sum}')
                break
            
            else:

                print("Please try again")
                continue
            
            
        except(ValueError,NameError,ZeroDivisionError):
            print("Invalid input: Please choose again")

            
         

    choice=input("Do you want to do it again? (Yes/no): ")

    if choice.lower()=="yes":
        continue

    else:
        print("Okay")
        break
                
             
