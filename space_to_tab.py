input_file_path = 'transliteration_with_stress/1_initial_data.txt'
output_file_path = 'transliteration_with_stress/2_space_to_tab.txt'

with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()
modified_lines = [line.replace(' ', '\t', 1) for line in lines]

with open(output_file_path, 'w') as output_file:
    output_file.writelines(modified_lines)
