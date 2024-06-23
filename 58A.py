def can_say_hello(s: str) -> str:
    word = "hello"
    wordLength = len(word)
    i = 0  

    for char in s:
        if char == word[i]:
            i+=1
        if i == wordLength:
            return "YES"
    
    return "NO"

s = input().strip()
print(can_say_hello(s))

