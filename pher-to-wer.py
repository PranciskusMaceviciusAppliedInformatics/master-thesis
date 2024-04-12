import re

with open("test.tsv", "r") as file:
    text = file.read()
    words = re.split(r' _ |[\t]|[\n]', text)
print(words)
# with open("output2.txt", "w") as output_file:
#     for word in words:
#         output_file.write(word + "\n")
word_amount = 0
first_word_list = []
second_word_list = []
with open("PhER_to_WER.txt", "w") as output_file:
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
