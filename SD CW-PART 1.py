#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution
#Student ID 20221106/ w1953808
#27/11/2022


def credit_input_and_check(credit):
    ''' Gets inputs and checks for errors in range and value errors. If there are no errors returns the credit value'''
    while True:
        try:
        
            credit_input= int(input("Please enter your credits at "+ credit +": "))
            if credit_input not in range (0,121,20):
                print("Out of range.")
                continue
            
            else:
                return credit_input
        except ValueError:
            print("Integer Required: ")
            continue

        

def another_set():
    '''Asks whether user wants to input another set of data, loops until user inputs a valid input. When a correct input is given, returns the value as a string'''
    while True:
    
        anotherset=input("\nWould you like to enter another set of data? \nEnter \'y\' for yes or \'q\' to quit and view results: ")
        anotherset=anotherset.lower()   #turns anotherset into lowercase to include upper case correct inputs as well

        if anotherset=="y":
            return anotherset
        elif anotherset=="q":
            return anotherset
           
        else:
            print("\nInvalid input , try again")
            continue
            


progress= 0
trailer= 0
exclude= 0
retriver= 0

                  
while True:   #calls credit_input_and_check function for each credit input and assigns returned value to respective variables
     
    passcredits=credit_input_and_check("pass")
    defercredits=credit_input_and_check("defer")
    failcredits=credit_input_and_check("fail")
    

    total = passcredits + defercredits + failcredits
    
        
    if total !=120:
        print("Total Incorrect, try again\n")
        continue
    
    elif(passcredits==120):
        print ("Outcome: Progress")
        progress+=1
       
    elif (passcredits==100):
        print ("Outcome: Progress (Module Trailer)")
        trailer+=1
        
    elif (failcredits>=80):
        print ("Outcome: Exclude")
        exclude+=1
        

    else:
        print ("Outcome: Do not progress (Module Retriever)")
        retriver+=1


        
    y_or_q=another_set() #another_set funtion is called, which returns the user's input, either y or q,and assigns it to y_or_q variable
    
        
    if y_or_q=='y':
        print("\n")
        continue          #iterates through the while loop again

    
    elif y_or_q=="q":
        print('\n')
        print('-'*80)
        
        print("HISTOGRAM")
        print("Progress ",progress,":",progress*"*")
        print("Trailer ",trailer," :",trailer*"*")
        print("Retriver ",retriver,":",retriver*"*")
        print("Excluded ",exclude,":",exclude*"*")
        tot_outcomes= progress+trailer+retriver+exclude

        if tot_outcomes==1:     #for when only one set of data is entered
             print('\n')
             print(tot_outcomes," outcome in total.")
             print('-'*80)

             
        else:                   #for when multiple sets of data are entered
            print('\n')
            print(tot_outcomes," outcomes in total.")
            print('-'*80)

            
          
        break












        
       
        
        
















        
    

        
