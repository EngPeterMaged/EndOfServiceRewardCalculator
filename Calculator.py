import sys
# Global Parameters
Duration_Type = 0
reason = 0
Salary = 0
Period_Years = 0
Period_Months = 0
Period_Days = 0
Reward = 0

# Main Function
def main():
   # First Set Inputs 
   Set_Inputs()
   # Calculate Reward
   Calculate_Total_reward()




    



def Set_Inputs ():
     # get the duration type as user choise
    global Duration_Type 
    global reason 
    global Salary 
    global Period_Years 
    global Period_Months 
    global Period_Days
    global Reward

    Duration_Type = 0
    reason = 0
    Salary = 0
    Period_Years = 0
    Period_Months = 0
    Period_Days = 0
    Reward = 0

    while 1:
        try:
            Duration_Type = int(input("""Enter a Duration Type Choise number: 
            \n1.Fixed Time 
            \n2.Unimited Period 
            \n"""))

            if (Duration_Type > 0 and Duration_Type < 3):
                break
            else :    
                print("Please input Choise Number only...") 
                continue
        except ValueError:
                print("Please input Choise Number only...") 

    # get the Reason as user choise
    while 1:
        if (Duration_Type == 1) :

                    try:
                        reason = int(input("""Enter a Resaon Choise number: 
                        \n1.Expiration of contract terms, or the parties have agreed to terminate the contract 
                        \n2.Termination of the contract by the employer
                        \n3.Termination of the contract by the employer for one of the terms and conditions stated in Article (80).
                        \n4.Leaving work as a result of force majeure.
                        \n5.The worker terminates the labor contract within six months into the marriage contract or three months into birth.
                        \n6.The worker leaves work for one of the conditions stated in Article (81)
                        \n7.Termination of the contract by the worker, or the worker has quit work for other reasons not stated and in Article (81). 
                        \n"""))

                        if (reason > 0 and reason < 8):
                            break
                        else :    
                            print("Please input Choise Number only...") 
                            continue
                    except ValueError:
                            print("Please input Choise Number only...")


        if (Duration_Type == 2 ):

                    try:
                        reason = int(input("""Enter a Resaon Choise number: 
                        \n1.Expiration of contract terms, or the parties have agreed to terminate the contract 
                        \n2.Termination of the contract by the employer
                        \n3.Termination of the contract by the employer for one of the terms and conditions stated in Article (80).
                        \n4.Leaving work as a result of force majeure.
                        \n5.The worker terminates the labor contract within six months into the marriage contract or three months into birth.
                        \n6.The worker leaves work for one of the conditions stated in Article (81)
                        \n7.Termination of the contract by the worker, or the worker has quit work for other reasons not stated and in Article (81). 
                        \n8.The resignation of a worker.
                        \n"""))

                        if (reason > 0 and reason < 9):
                            break
                        else :    
                            print("Please input Choise Number only...") 
                            continue
                    except ValueError:
                            print("Please input Choise Number only...") 
    # get the Salary value
    while 1:
        try:
            Salary = float(input("""Enter a Your Salary Please 
            \n"""))

            if (Salary > 0):
                break
            else :    
                print("Salary Cannot be 0") 
                continue
        except ValueError:
                print("Please input Valid Salary") 

    # get the Period in years value
    while 1:
        try:
            Period_Years = int(input("""Enter a working Period in Years
            \n"""))

            if (Period_Years > 0):
                break
            else :    
                print("Period_Years Cannot be 0") 
                continue
        except ValueError:
                print("Please input Valid Period Years")


    # get the Period in months value
    while 1 :
            try:
                    Period_Months = int(input("""Enter a working Period in Months (Optional) \n"""))
                    if (Period_Months > 0 and Period_Months < 12):
                        break  
                    print("Period Months must be between 1 and 11 ") 
            except ValueError:
                        Period_Months = 0
                        break

    # get the Period in Days value
    while 1 :
            try:
                    Period_Days = int(input("""Enter a working Period in Days (Optional) \n """))
                    if (Period_Days > 0 and Period_Days < 30):
                            break
                    print("Period Months must be between 1 and 29 ")
                        
            except ValueError:
                        Period_Days = 0
                        break



def Calculate_Initial_reward():
        global Reward 
    # if years less than 5 years ca
        if (Period_Years <= 5):
            Reward = Period_Years * (Salary/2)
            
            if (Period_Years == 5):
                Reward += Salary * (Period_Months / 12)
                Reward += Salary * (Period_Days / 365)

            else :    

                Reward += (Salary/2) * (Period_Months / 12)
                Reward += (Salary/2) * (Period_Days / 365)

        else :

            Reward = (5) * (Salary/2)
            Reward += (Period_Years-5) * (Salary)
            Reward += Salary * (Period_Months / 12)
            Reward += Salary * (Period_Days / 365)

def Calcualte_Reward_for_Special_Cases():
    global  Reward
    """ 
1.Expiration of contract terms, or the parties have agreed to terminate the contract 
2.Termination of the contract by the employer
3.Termination of the contract by the employer for one of the terms and conditions stated in Article (80).
4.Leaving work as a result of force majeure.
5.The worker terminates the labor contract within six months into the marriage contract or three months into birth.
6.The worker leaves work for one of the conditions stated in Article (81)
7.Termination of the contract by the worker, or the worker has quit work for other reasons not stated and in Article (81). 
8.The resignation of a worker.
    """


# 1.Expiration of contract terms, or the parties have agreed to terminate the contract 
    if (reason == 1):
        # Full Reward
        pass
#2.Termination of the contract by the employer
    if (reason == 2):
        # Full Reward
        pass
#3.Termination of the contract by the employer for one of the terms and conditions stated in Article (80).
    if (reason == 3):
        # No Reward
        Reward = 0 

#4.Leaving work as a result of force majeure.
    if (reason == 4):
        # Full Reward
        pass

#5.The worker terminates the labor contract within six months into the marriage contract or three months into birth.      
    if (reason == 5):
        # Full Reward
        pass

#6.The worker leaves work for one of the conditions stated in Article (81)
    if (reason == 6):
        # Full Reward
        pass
#7.Termination of the contract by the worker, or the worker has quit work for other reasons not stated and in Article (81). 
    if (reason == 7):
        # No Reward
        Reward = 0   

#8.The resignation of a worker. 
    if (reason == 8):
        # Case when less than 2 years No Reward
        if (Period_Years < 2):           
                    Reward =  0
               
             
# Case when between 2 and 5 years
        elif (Period_Years <= 5):
            # case when 5 years with months and days
            if ((Period_Years == 5 and (Period_Months > 0 or Period_Days > 0))):
                    # 2/3 Reward
                    Reward *= (2/3)
            else :     
                    # 1/3 Reward      
                    Reward *=  (1/3)
               
            
# Case when between more than 5  and 10 years
        elif (Period_Years <= 10):
            # case when 10 years with months and days
            if (not (Period_Years == 10 and (Period_Months > 0 or Period_Days > 0))):
                    # 2/3 Reward
                    Reward *= (2/3) 
            # else Full Reward        
        # Case when more than 10 years in full reward            
        return     
                     




def Calculate_Total_reward():
    Calculate_Initial_reward()
    Calcualte_Reward_for_Special_Cases()
    print ("Your Reward : " + str("{:.3f}".format(Reward)) + " \n\n\n")



   

# Program Start
if __name__ == "__main__":
    while 1:
            main()
