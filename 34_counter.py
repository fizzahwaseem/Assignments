#python program which inputs a text and count the occurrences of vowels and consonant
text_ = input("Enter some text: ")
text_ = text_.lower()
vowels_ = "aeiou"
consonant_ = "bcdfghjklmnpqrstvwxyz"
vowel_count = 0
consonant_count = 0
for i in text_:
    if i in vowels_:
        vowel_count += 1
    if i in consonant_:
        consonant_count +=1
print("number of vowels are", vowel_count, " and number of consonents are ", consonant_count)