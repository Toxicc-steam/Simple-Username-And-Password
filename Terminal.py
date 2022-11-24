import time
import random

def terminal():
  print("Example Code")

pswa=0
while True:
  usrn=input("Enter Username: ").lower()
  if usrn=="user":
    print("Valid User")
    while True:
      usrp=input("Enter Password: ").lower()
      if usrp=="1234":
        terminal()
        break
      else:
        pswa+=1
        if pswa==4:
          print("Quiting...")
          quit()
        print("You Have "+str(4-pswa)+" Attemp(s) Left")

  else:
    print("Invalid User")