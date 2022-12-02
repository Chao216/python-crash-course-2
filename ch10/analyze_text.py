with open('adventure-sherlock.txt') as file_novel:
    lines = file_novel.readlines()

long_text = ''

for line in lines:
    long_text += line

long_list = long_text.split()

for word in long_list:
    print(f"\n\t{word}")
