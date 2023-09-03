import sys

if len(sys.argv) == 2:
    string = sys.argv[1]
else:
    string = "Kate got a job offer from invest Tinkoff team"

def countWord(string):
    target_word = "tinkoff"
    string = string.lower()
    count = 0
    letter_count = {}
    for char in string:
        if char.isalpha() and char in letter_count:
            letter_count[char] += 1
        elif char.isalpha():
            letter_count[char] = 1
   
    while True:
        for char in target_word:
            if char in letter_count and letter_count[char] > 0:
                letter_count[char] -= 1
            else:
                print(f'Tinkoff word was found {count} times')
                return count
        count += 1

countWord(string)
