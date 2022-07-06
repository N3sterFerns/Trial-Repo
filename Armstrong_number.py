# Armstrong Number

num = int(input("Enter the number: "))

sum = 0
order = len(str(num))

copy_n = num

while(num > 0):
    digit = num%10
    sum += digit**order
    num = num//10

if(sum == copy_n):
    print(f'{copy_n} is an Arm strong number...')
else:
    print(f'{copy_n} is not an Arm strong number...')



