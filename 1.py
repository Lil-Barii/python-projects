while True :
    user_input = int(input())
    if user_input>99 or user_input<10 :
        continue
    else :
        tens_input = user_input//10
        ones_input = user_input % 10
        break
if tens_input>ones_input :
    print(tens_input-ones_input)
else :
    print(ones_input-tens_input)
