word1 = input()
word2 = input()

# How many letters does the longest word contain?
if len(word1) < len(word2):
    print(len(word2))
else:
    print(len(word1))