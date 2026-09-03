str=input("Enter a string:").strip()
l=len(str)
# print(l)
vowel="aeiou"
count=0
count2=0
for ch in str:
    if ch.isalpha():
        if ch.lower() in vowel:
            count += 1
        else:
            count2 += 1
print("Vowels:",count)
print("Consonants:",count2)
