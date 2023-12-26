#get sentance from the user

origin = input ("Please enter a sentance:").strip().lower()
# Split sentance into words

words =origin.split()
print(words)

#loop through word and convert to pig latin
new_words=[]

for word in words:
    print(word)
    if word[0] in "aeiou":                            #if starts from vowel just add "Yay"

        new_word= word + "yay"
        new_words.append(new_word)
        
    else:                                             #Otherwise , move first consonant cluster to end and add "ay"  
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos=vowel_pos+1
            else:
                break
        conc=word[:vowel_pos]
        rest=word[vowel_pos:]
        new_word= rest+conc+"ay"
        new_words.append(new_word)

print(new_words)

#stick words back together

" ".join(new_words)

#output