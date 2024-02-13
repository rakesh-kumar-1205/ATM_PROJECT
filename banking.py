from bankexcep import DepositeError,WithdrawError,InsufficientFundError
bal=500.00 #Global variable

def Deposite():
    Deposite_Amount=float(input("Enter how much amount you want to deposite: "))
    if (Deposite_Amount<=0):
        raise DepositeError
    else:
        global bal
        bal=bal+Deposite_Amount
        print("\nYour Acount xxxxxxxx587 Credited with INR:RS.{}".format(Deposite_Amount))
        print("\nNow Current Balance INR:RS.{}".format(bal))
       
    
def Withdraw():
    global bal
    Withdraw_Amount=float(input("Enter how much amount you want to withdraw: "))
    if (Withdraw_Amount<=0):
        raise WithdrawError
    elif((Withdraw_Amount + 500)>bal):
        raise InsufficientFundError
    else:
        bal=bal-Withdraw_Amount
        print("\nYour Acount xxxxxxxx587 Debited with INR:RS.{}".format(Withdraw_Amount))
        print("\nNow Current Balance INR:RS.{}".format(bal))
              
def Balance_Enquery():
    print("\nNow Your Current Balance is INR RS.{}".format(bal))
    #return bal
    