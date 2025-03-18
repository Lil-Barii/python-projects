user_input = input()
s1 , s2 = user_input.split()

def word_game(s1, s2):
    while s1 and s2: 
        if s1[0] < s2[0]:
            s1 = s1[1:] 
        elif s2[0] < s1[0]: 
            s2 = s2[1:] 
        else: 
            s1 = s1[1:] 
            s2 = s2[1:] 
        s1 = s1[::-1] 
        s2 = s2[::-1] 
    if not s1 and not s2: 
        return "Both strings are empty!"
    elif not s1:
        return s2[::-1] 
    else: 
        return s1[::-1]


result = word_game(s1, s2)
print(result)
