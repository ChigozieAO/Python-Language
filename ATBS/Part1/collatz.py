def collatz(number) :
    if number % 2 == 0 :
        print(number // 2) 
        return number // 2
    else :
         print(3 * number + 1)
         return 3 * number + 1

def problem() :
    print('Type in any number')
    yourNum = int(input())
    while True:
        if yourNum != 1:
            yourNum = collatz(yourNum)
        else:
            break

problem()