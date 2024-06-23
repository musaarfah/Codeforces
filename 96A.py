def football_dangerous(string):
    if '0000000'in string or '1111111' in string:
        return 'YES'
    else:
        return 'NO'

string = input().strip()
print(football_dangerous(string))

