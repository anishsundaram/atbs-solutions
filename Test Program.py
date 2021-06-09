
print("enter a number")
number = int(input())
def collatz(number):
    if(number % 2 ==0):
        print(str(number // 2))
        return number // 2
    else:
        print(str(3*number+1))

        
collatz(number)

        
