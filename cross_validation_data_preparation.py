import random

def scramble_lines(lines):
    random.shuffle(lines)
    return lines

def split_and_scramble_data(input_file, output_prefix, chunk_size, dev_size, num_iterations):
    with open(input_file, 'r') as f:
        all_lines = f.readlines()
    start_offset = 4800
    previous_start_offset = 0

    for i in range(1, num_iterations + 1):
        test_lines = all_lines[previous_start_offset:start_offset]
        train_lines = all_lines[:previous_start_offset]
        train_lines.extend(all_lines[start_offset:])
        train_lines = scramble_lines(train_lines)
        dev_lines = train_lines[dev_start_offset:]
        train_lines = train_lines[:-1000]            
        
        test_file = f'transliteration_with_stress/5_cross_validation_data_preparation/{output_prefix}_test_{i}.tsv'
        train_file = f'transliteration_with_stress/5_cross_validation_data_preparation/{output_prefix}_train_{i}.tsv'
        dev_file = f'transliteration_with_stress/5_cross_validation_data_preparation/{output_prefix}_dev_{i}.tsv'
        
        with open(test_file, 'w') as f:
            f.writelines(test_lines)
        
        with open(train_file, 'w') as f:
            f.writelines(train_lines)
        
        with open(dev_file, 'w') as f:
            f.writelines(dev_lines)
        previous_start_offset = start_offset
        start_offset = start_offset + chunk_size    

if __name__ == '__main__':
    input_file = 'transliteration_with_stress/4_cut_to_last_previous_thousand.txt'
    output_prefix = 'lit'
    chunk_size = 4800
    dev_size = 200
    dev_start_offset = 42200
    num_iterations = 10
    
    split_and_scramble_data(input_file, output_prefix, chunk_size, dev_size, num_iterations)
