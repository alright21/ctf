import string
# import string.ascii_lowercase as alphabet
alphabet = string.ascii_lowercase
input = "ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! mbz cjzg kv iajbo{ndldie_al_aqk_jjrnsxee}. xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj :)."



all_output = []
for i in range (26):
    output = ''
    for letter in input:
        if letter in alphabet:
            
            
            index = alphabet.index(letter)
            # print(str(index) + '\n')
            index = ((index-i)%26)
            # print(index)
            
            output += (alphabet[index])
            
        else:
            output+=letter
        i+=1

    print(output)

