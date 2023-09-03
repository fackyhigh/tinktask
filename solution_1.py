import sys

if len(sys.argv) == 2:
    string = sys.argv[1]
else:
    string = "Kate got a job offer from invest Tinkoff team"

def countWord(string, count = 0):
    string = ''.join(filter(str.isalpha, string.lower()))
    search_word = "Tinkoff".lower()
    for i in range(len(search_word)):
        for j in range(len(string)):
            if string[j] == search_word[i]:
                string = string[:j]+string[j+1:]
                if i == len(search_word)-1:
                    return countWord(string, count + 1)
                break
            elif j == len(string)-1 and string[j] != search_word[i]:
                print(f'Tinkoff word was found {count} times')
                return count
    print(f'Tinkoff word was found {count} times')
    return count

countWord(string)
