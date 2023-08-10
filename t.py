from replit import clear

print('''

 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

'''
)


def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2
def start_again():
  n1 = float(input("put ur first number: "))
  opreation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
  }
  for symbol in opreation:
    print(symbol)
  while True:  
  
    n2 = float(input("put ur next number: "))
    choosing_symbol= input("Pick an opreation: ")
    calculation_symbol= opreation[choosing_symbol]
    ans= float(calculation_symbol(n1,n2))
    print(f"{n1} {choosing_symbol} {n2} = {ans} ")  
    repet = input(f"Type 'y' to continue calculation with {ans}, or type 'n' to start again: ")
    if repet=='y':
      n1=ans
    elif repet=='n':
      clear()
      start_again()
  
start_again()
