#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution
#Student ID 20221106 / w1953808
#7/12/2022


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
            



def progression_dict(studentid_no,progressoutcome,pcredits,dcredits,fcredits):
    '''Adds the credits of each student to a list, then adds that list as a value of a dictionary where the matching student id is the key,
    returns the dictionary'''

    values_list=[progressoutcome,pcredits,dcredits,fcredits]
    progress_dict[studentid_no]=values_list
    
    return progress_dict

  
       



progress= 0
trailer= 0
exclude= 0
retriver= 0
progress_dict={}


                           
       
while True:
    
    student_id=input("Enter student id: ")

    while True:
        #calls credit_input_and_check function for each credit input and assigns returned value to respective variables

        passcredits=credit_input_and_check("pass")
        defercredits=credit_input_and_check("defer")
        failcredits=credit_input_and_check("fail")
        

        total = passcredits + defercredits + failcredits
        
        if total !=120:
            print("Total Incorrect, try again\n")
            continue   #loops to ask for credits from the start without asking for student id again
        else: 
            
            break        
    

                    

    if(passcredits==120):
        print ("Outcome: Progress")
        progress+=1
      
        progression_dict(student_id,'progress-',passcredits,defercredits,failcredits) #calls the progression_dict function and passes the values
       

    elif (passcredits==100):
        print ("Outcome: Progress (Module Trailer)")
        trailer+=1
        
        progression_dict(student_id,'Progress(Module Trailer)-',passcredits,defercredits,failcredits)
        

    elif (failcredits>=80):
        print ("Outcome: Exclude")
        exclude+=1
       
        progression_dict(student_id,'Exclude -',passcredits,defercredits,failcredits)
       
    else:
        print ("Outcome: Do not progress (Module Retriever)")
        retriver+=1
       
        progression_dict(student_id,'Module Retriever -',passcredits,defercredits,failcredits)
        

  
    y_or_q=another_set()  #another_set funtion is called, which returns the user's input, either y or q, and assigns it to y_or_q variable
         
    if y_or_q=='y':
        print("\n")
        continue        #iterates through the while loop again

    
    elif y_or_q=="q":
        print('\n')
        print('-'*80)
        
        print("HISTOGRAM")
        print("Progress ",progress,":",progress*"*")
        print("Trailer ",trailer," :",trailer*"*")
        print("Retriver ",retriver,":",retriver*"*")
        print("Excluded ",exclude,":",exclude*"*")
        tot_outcomes= progress+trailer+retriver+exclude

        if tot_outcomes==1: #for when only one set of data is entered
             print('\n')
             print(tot_outcomes," outcome in total.")
             print('-'*80)

             
        else:               #for when multiple sets of data are entered
            print('\n')
            print(tot_outcomes," outcomes in total.")
            print('-'*80)
        
       
       
       

        print("Part 4")
        finaldict=progress_dict    #the dictionary returned by the progression_dict function is assigned to a new dictionary called finaldict
       
        
        for a,b,in finaldict.items():
            print(a,':',b[0],b[1],',',b[2],',',b[3],' ',end='')

 
        break












        
       
        
        
















        
    

        
