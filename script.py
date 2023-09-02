import sys

if len(sys.argv) == 2:
    string = sys.argv[1]
else:
    string = "Kate got a job offer from invest Tinkoff team TiNkoFf"

def countWord(string, count = 0):
    sanitized_string = string.lower().replace(" ","")
    search_word = "Tinkoff".lower()
    for i in range(len(search_word)):
        for j in range(len(sanitized_string)):
            if sanitized_string[j] == search_word[i]:
                sanitized_string = sanitized_string[:j]+sanitized_string[j+1:]
                if i == len(search_word)-1:
                    return countWord(sanitized_string, count + 1)
                break
    print(f'Tinkoff word was found {count} times')
    return count
countWord(string)
