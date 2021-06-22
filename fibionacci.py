n = int(input("How many numbers? :"))
num1 = 0
num2 = 1
count = 0
#Loop for fibionacci series
while count<n :
    print(num1)
    #updating values
    num = num1+num2
    num1=num2
    num2=num
    count =count+1
