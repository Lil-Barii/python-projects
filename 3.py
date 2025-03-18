def separate_numbers(numbers):
    ali_numbers = []
    reza_numbers = []
   
    for i in numbers:
        if i % 2 == 0: 
            ali_numbers.append(i)
        else: 
            reza_numbers.append(i)
   
    return ali_numbers, reza_numbers

user_input=input()
numbers_list = user_input.split()
numbers = [int(i) for i in numbers_list]
ali_numbers, reza_numbers = separate_numbers(numbers)

if ali_numbers:
    print(*ali_numbers)
else:
    print("[]")

if reza_numbers:
    print(*reza_numbers)
else:
    print("[]")
