number = int(input("\nEnter the number: "))

if number == 0:
    print('The number is zero!')
elif number%2 != 0:
    print('The number is an odd number!')
elif number%2 == 0:
    print('The number is an even number!')