import random

input_file_path = 'transliteration_with_stress/2_space_to_tab.txt'
output_file_path = 'transliteration_with_stress/3_scrambled_lines.txt'

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
    
random.shuffle(lines)

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(lines)
