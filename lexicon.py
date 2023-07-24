
file_1 = 'positive-words.txt'

with open(file_1, 'r') as file:
    positive_words = [line.strip() for line in file]



for line in positive_words:
    print(line)