bank=1000000

def pin(): 
    pin_number=int(input("Enter your pin: "))
    if pin_number==1234:
        return True
    else:
        print("Invalid pin!")
        return False    

def dashboard():
    print(f'1. withdraw  2.deposit\n3.checkbalance 4.quickteller\n5. tranfer  6.change pin')
    dash=int(input("select to proceed: "))
    if dash==1:
        wit=int(input(f" 1.500  2.1000\n 3.1500  4.2000\nselect amount: "))
        if wit==1:
            print(f"withdraw successful")
        elif wit==2:
            print(f"withdraw successful")
        elif wit==3:
            print(f"withdraw successful")
        elif wit==4:
            print(f"withdraw successful")
    else:
        print("invalid selection")

    if dash==2:
        deposit=int(input(f"1. ahmad bank  2.other banks\nselect bank name: "))
        if deposit==1:
            print(f"welcome\nenter account number:")
        elif deposit==2:
            otherbank=int(input(f"1. gt bank  2.polaris bank\n3. first bank  4.nji bank\nselect bank"))
            if otherbank==1:
                print(f"welcome\nenter account number")
            elif otherbank==2:
                print(f"welcome\nenter account number") 
            elif otherbank==3:
                print(f"welcome\nenter account number")
            elif otherbank==4:
                print(f"welcome\nenter account number")       
        else:
            print("invalid selection")

    elif dash==3:
        checkbalance=int(input(f"1. ahmad bank  2.other banks\nselect bank name: "))
        if checkbalance==1:
            print(f"welcome\nenter account number:")
        elif otherbank==2:
            otherbank=int(input(f"1. gt bank  2.polaris bank\n3. first bank  4.nji bank\nselect bank"))
            if otherbank==1:
                print(f"welcome\nenter account number")
            elif otherbank==2:
                print(f"welcome\nenter account number") 
            elif otherbank==3:
                print(f"welcome\nenter account number")
            elif otherbank==4:
                print(f"welcome\nenter account number")       
        else:
          print("invalid selection")

    


    elif dash==5:
        pin()
        transfer=int(input(f'1. ahmad bank  2.other banks\n3. beneficiaries' ))
        if transfer==1:
            print(f"welcome\nenter account number:")
        elif transfer==2:
            otherbank=int(input(f"1. gt bank  2.polaris bank\n3. first bank  4.nji bank\nselect bank"))
            if otherbank==1:
                print(f"welcome\nenter account number")
            elif otherbank==2:
                print(f"welcome\nenter account number") 
            elif otherbank==3:
                print(f"welcome\nenter account number")
            elif otherbank==4:
                print(f"welcome\nenter account number")
            else:
                print("transfer successful")       
                    
        elif transfer==3:
         beneficiaries=int(input(f"1. rakiya makama 21xxx22 opay  2.abdul 32xxx22 palmpay"))
        if beneficiaries==1:
            print(f"welcome\nenter amount")
        elif beneficiaries==2:
            print(f"welcome\nenter amount")
        else:
            print("insufficient fund")

    
    
        

    
                  

    elif dash==6:
        pin()
        changepin=int(input("enter old pin"))
        if changepin==1234:
            newpin=int(input("enter new pin"))
            if newpin==12345:
                print("change of pin successful")
            else:
                print("change failed")
        else:
            print("incorrect pin")
    
    elif dash==4:
        pin()
        quickteller=int(input("1.airtime  2.electricity"))
        if quickteller==1:
            airtime=int(input("1.self  2.others"))
            if airtime==1:
                print("recharge successful")
            elif airtime==2:
                network=int(input("1.MTN  2.airtel\n3.glo"))
            if network==1:
                 print("welcome\nenter amount")
            elif network==2:
                print("welcome\nenter amount")
            elif network==3:
                print("welcome\nenter amount")
            else:
                print("recharge successful")
        
            

        elif quickteller==2:
            
            electricity=int(input("1.prepaid 2.postpaid"))
            if electricity==1:
                prepaidnumber=int(input("input prepaid number"))
                int(input("enter amount"))
                pin()
                print("recharge successful")

            if electricity==2:
                postpaidnumber=int(input("input postpaid number"))
                int(input("enter amount"))
                pin()
                print("recharge successful")


              
                           
pin()        
dashboard()
   