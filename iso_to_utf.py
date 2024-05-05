input_file_path = 'initial_data_with_spaces.txt'
output_file_path = 'initial_data_in_utf.txt'

with open(input_file_path, 'r', encoding='iso-8859-1') as input_file:
    content = input_file.read()

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(content)
