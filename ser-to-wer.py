import re

with open("test.tsv", "r") as file:
    text = file.read()
    lines = text.split('\n')
    filtered_lines = [line for line in lines if line.count('_') == 2]
    filtered_text = '\n'.join(filtered_lines)
    words = re.split(r' _ |[\t]|[\n]', filtered_text)
    print(words)
word_amount = 0
first_word_list = []
second_word_list = []
with open("ser_to_wer.txt", "w") as output_file:
    for word in words:
        if word_amount == 0:
            first_word_list.append(word)
            word_amount = word_amount + 1
        elif word_amount == 1:
            second_word_list.append(word)
            word_amount = word_amount + 1
        elif word_amount == 2:
            first_word_list.append(word)
            word_amount = word_amount + 1
        else:
            second_word_list.append(word)
            output_file.write(first_word_list[0] + "\t" + first_word_list[1] + "\n" + second_word_list[0] + "\t" + second_word_list[1] + "\n")
            first_word_list.clear()
            second_word_list.clear()
            word_amount = 0
