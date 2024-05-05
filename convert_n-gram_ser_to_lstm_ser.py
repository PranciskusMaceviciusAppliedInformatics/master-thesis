def merge_files(file1_path, file2_path, output_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_path, 'w') as output:
        for line1, line2 in zip(file1, file2):
            line1 = line1.split('\t')[-1].strip() + '\t'
            line2 = line2.split('\t')[-1].strip()
            output.write(line1 + line2 + '\n')
            
file1_path = 'lit_test.tsv'
file2_path = '3lit.txt'
output_path = 'neural_like_3.txt'
merge_files(file1_path, file2_path, output_path)
file2_path = '4lit.txt'
output_path = 'neural_like_4.txt'
merge_files(file1_path, file2_path, output_path)
file2_path = '5lit.txt'
output_path = 'neural_like_5.txt'
merge_files(file1_path, file2_path, output_path)
file2_path = '6lit.txt'
output_path = 'neural_like_6.txt'
merge_files(file1_path, file2_path, output_path)
file2_path = '7lit.txt'
output_path = 'neural_like_7.txt'
merge_files(file1_path, file2_path, output_path)
file2_path = '8lit.txt'
output_path = 'neural_like_8.txt'
merge_files(file1_path, file2_path, output_path)
file2_path = '9lit.txt'
output_path = 'neural_like_9.txt'
merge_files(file1_path, file2_path, output_path)
