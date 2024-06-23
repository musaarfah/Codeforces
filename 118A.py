def del_vowel_string(string):
    lower_string=string.lower()
    vowels=['a','e','i','o','u','y']

    new_string=''

    for i in range(len(string)):
        if lower_string[i] not in vowels:
            new_string+=f'.{lower_string[i]}'

    return new_string



string=input().strip()

print(del_vowel_string(string))
