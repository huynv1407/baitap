import os

def main(inputs):
    filenames = [x for x in os.listdir(inputs) if x.endswith(".txt")]
    for filename in filenames:
        # print(filename)
        file_path = os.path.join(inputs, filename)
        read_files = open(file_path, 'r').read().replace(" ","")
        reads_files = open(file_path, 'r').readlines()
        # count character
        count_character = len(read_files)
        #count line min and max

        sum_characters = 0
        max_line = len(reads_files[0])
        min_line = len(reads_files[0])
        # for line in reads_files:
        #     sum_characters += len(line)
        #     if len(line) > max_line:
        #         max_line = len(line)
        #     if len(line) < min_line:
        #         min_line = len(line)
        # # maxs_line = max(reads_files, key=len)
        # # mins_line = min(reads_files, key=len)
        # # print('So dong dai nhat: ', len(maxs_line), '\n', 'so dong ngan nhat ', len(mins_line))
        # print('So dong dai nhat: ', max_line, '\n','so dong ngan nhat', min_line)
        # # #so ki tu xuat hien nhieu va it nhat
        # dct = {}
        # for i in read_files:
        #     if i in dct:
        #         dct[i] += 1
        #     else:
        #         dct[i] = 1
        # print(dct)


if __name__== '__main__':
    inputs = r'C:\Users\HuyNV27\Desktop\python\Excise\Tan Senpai\ProcessTXT'
    main(inputs)
