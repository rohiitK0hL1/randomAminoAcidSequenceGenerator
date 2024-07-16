import os
from main import generate_random_sequences

def generate_data_to_file(sequence_length, number_of_sequences, rib_file_path):
    excluded_amino_acids = ['X', 'Z', 'J', 'B', 'U']
    random_sequences = generate_random_sequences(sequence_length, number_of_sequences, excluded_amino_acids)
    write_data_to_file(rib_file_path, random_sequences)

def write_data_to_file(file_path, random_sequences):
    with open(file_path, 'w') as file:
        for sequence_data in random_sequences:
            rib_content = sequence_data['rib_content']
            sequence = sequence_data['sequence']
            # Remove content within parentheses if present
            sequence_cleaned = sequence.split('(')[0].strip()  # Get content before '(' and remove leading/trailing spaces
            combined_data = rib_content.rstrip() + '\n' + sequence_cleaned + '\n\n'  # Add an extra newline
            file.write(combined_data)

    # Remove the last two characters from the file to remove the last line
    with open(file_path, 'rb+') as file:
        file.seek(0, os.SEEK_END)
        pos = file.tell() - 2
        while pos > 0 and file.read(1) != b'\n':
            pos -= 1
            file.seek(pos, os.SEEK_SET)
        file.truncate(pos)

def main():
    sequence_length = int(input("Enter the Sequence length of Aminoacid: "))
    number_of_sequences = int(input("Enter the number of sequences you want: "))
    rib_file_path = input("Enter the file path to save the RIB file: ")
    generate_data_to_file(sequence_length, number_of_sequences, rib_file_path)
if __name__ == "__main__":
    main()