import time



start_time = time.time()
inputs = open('READ_001.txt', 'r')
# fs = inputs.read().replace(" ", "")
fs1= inputs.read().lower()
words= fs1.split()
with open('READ_001.txt', 'r') as f:
    lines = f.readline()
number_of_characters = len(fs)
sum_characters = 0
max_line = 0
min_line = 21331534532

for line in lines:
    sum_characters += len(line)
    if len(line) > max_line:
        max_line = len(line)
    if len(line) == len(line) :
        min_line = len(line)

count = {}

for i in fs:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
list_count = [(k, v) for k, v in sorted(count.items(), key=lambda item: item[1])]

stopwords = ["is", "am", "are", "and", "the", "i", "we", "you", "they"]
for word in list(words):
    if word in stopwords:
        words.remove(word)
count_word= {}

for word in words:
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1


list_countword = [(k, v) for k, v in sorted(count_word.items(), key=lambda item: item[1])]
print(list_countword[-10:])
print("--- %s seconds ---" % (time.time() - start_time))




print('Số kí tự không có dấu cách: ', number_of_characters)
print('so ki tu: ', sum_characters)
print('so dong: ', len(lines))
print('so dong nhieu ki tu nhat: ' ,max_line)
print('so dong it ki tu nhat: ' ,min_line)
print('10 ki tự xuất hiện nhiều nhất:', list_count[-10:])
print('10 ki tự xuất hiện ít nhất:', list_count[:10])