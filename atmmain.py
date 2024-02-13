from atmmenu import atmmentu
from banking import Withdraw,Deposite,Balance_Enquery
from bankexcep import WithdrawError,DepositeError,InsufficientFundError
import sys
def sbi():
    while(True):
        atmmentu()
        try:
            ch=int(input("Enter your choice:"))
            match(ch):
                case 1:
                    try:
                        Deposite()
                    except ValueError:
                        print("\nDont't Deposite strs/symbols/alpha-numerics in your Account")
                    except DepositeError:
                        print("\nDon't Deposite -ve and Zero Value in your Account")
                    except Exception as e:
                        print("\nOops something went wrong",e)
                                
                case 2:
                    try:
                        Withdraw()
                    except ValueError:
                        print("\nDont't Withdraw strs/symbols/alpha-numerics in your Account")
                    except WithdrawError:
                        print("\nDon't Withdraw -ve and Zero Value in your Account")
                    except InsufficientFundError :
                        print("\nYou don't have sufficient funds for withdraw") 
                    except Exception as e:
                        print("\nOops something went wrong",e)   
                case 3:
                    Balance_Enquery()
                case 4:
                    print("\nThanks for using this ATM App!")
                    sys.exit()
                case _:
                    print("Your Selection of Operation is Wrong Try again..")
        except ValueError:
            print("\n Don't Enter strings/symbols/alpha_numerics for your choice.")
        except Exception as e:
            print("\n Oops Something Went Wrong..",e)
            
    
    
    
    
    
    
    

