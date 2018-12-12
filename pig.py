# get sentence from user

original = input("Input a sentence:").lower().strip()

# split sentence into words

words = original.split()

new_words = []

# Loop through words and convert those word into piglatin

#print (new_words)
#print (words)

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)

    else:
        
        vow_pos = 0
        for letter in word:
            if letter not in "aeiou":
                 vow_pos = vow_pos + 1
            else:
                break
        cons = word[:vow_pos]
        print(cons)
        the_rest = word[vow_pos:]
        print(the_rest)
        new_word = cons + the_rest + "ay"
        new_words.append(new_word)

            
                    
        




print (new_words)


# if the word starts with consonent, add the cluster at the end and add a word called "yay"


# if the word starts with vowel, add the alphabet at the end of the word and adds "ay"


# stick words back together


# print the string
