import random

amino_acid_three_letter_codes = {
    'A': 'Ala',
    'C': 'Cys',
    'D': 'Asp',
    'E': 'Glu',
    'F': 'Phe',
    'G': 'Gly',
    'H': 'His',
    'I': 'Ile',
    'K': 'Lys',
    'L': 'Leu',
    'M': 'Met',
    'N': 'Asn',
    'P': 'Pro',
    'Q': 'Gln',
    'R': 'Arg',
    'S': 'Ser',
    'T': 'Thr',
    'V': 'Val',
    'W': 'Trp',
    'Y': 'Tyr'
}


def generate_random_sequence(sequence_length, excluded_amino_acids=[]):
    amino_acids = list(amino_acid_three_letter_codes.keys())
    random_sequence = ""

    rib_content = "title RIBOSOME\n\n"
    rib_content += "default helix\n\n"

    for _ in range(sequence_length):
        filtered_amino_acids = [acid for acid in amino_acids if acid not in excluded_amino_acids]
        random_amino_acid = random.choice(filtered_amino_acids).upper()
        random_sequence += random_amino_acid

        three_letter_code = amino_acid_three_letter_codes[random_amino_acid]
        code = three_letter_code.lower()

        phi_angle = random.uniform(-90, 90)
        chi_angle = random.uniform(-90, 90)

        rib_content += f"res {code}   phi  {phi_angle:.1f}  psi {chi_angle:.1f}\n\n"

sequence_length = int(input("Enter the peptide length: "))
number_of_sequences = int(input("Enter the number of sequences you want: "))

def generate_rib(rib_file_path):
    random_sequence = generate_random_sequence(sequence_length)
    with open(rib_file_path, 'w') as file:
        for rib_content in random_sequence:
            #rib_content = sequence_data['rib_content']
            file.write(rib_content)

for i in range(1,(number_of_sequences+1)):
    generate_rib(f'output{i}.rib')