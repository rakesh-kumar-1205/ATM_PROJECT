import getpass
import sys
from atmmain import sbi
def runatm():
    ctr=0
    while(True):
        pin=getpass.getpass(prompt="Enter Your Pin:")
        if(pin=="7116"):
            sbi()
        else:
            print("\nYour pin is invalid ,Try again..")
            ctr=ctr+1
            if(ctr==3):
                print("Your Card Is Blocked")
                sys.exit()