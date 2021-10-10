def abbreviator(word):
    if len(word) > 10:
        abr = word[0] + str(len(word) -2)   + word[-1]
        return abr
    else : 
        return word

words_count = int(input())
words_list = []  
abbr_list = []

for i in range(words_count):
    words_list.append(input())
    abbr_list.append(abbreviator(words_list[i]))
    
for elem in abbr_list:
    print(elem)

