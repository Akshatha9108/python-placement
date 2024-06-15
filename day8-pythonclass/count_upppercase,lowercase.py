import string
sentence=input("Enter a sentence:")
wordlist=sentence.strip().split(' ')
print(f'this sentence has{len(wordlist)}words',end='\n\n')
digit_count=upppercase_count=lowercase_count=0
for char in sentence:
    if char in string.digits:
        digit_count+=1
    elif char in string.ascii_uppercase:
        upppercase_count+=1
    elif char in string.ascii_lowercase:
        lowercase_count+=1
print(f'this sentence has: {digit_count} digits',f'{upppercase_count}:upper case letters',f'{lowercase_count} :lowercase letters',sep='\n')
