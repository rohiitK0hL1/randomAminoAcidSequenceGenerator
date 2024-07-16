import random

#List of amino acids with three letter codes:
aminoAcids = {'A': 'Ala','C': 'Cys','D': 'Asp','E': 'Glu','F': 'Phe','G': 'Gly','H': 'His','I': 'Ile','K': 'Lys','L': 'Leu','M': 'Met','N': 'Asn','P': 'Pro','Q': 'Gln','R': 'Arg','S': 'Ser','T': 'Thr','V': 'Val','W': 'Trp','Y': 'Tyr'}

def gen_random_seq(seqLength, numbofSeq, not_aminoAcids=[]):
    randomSeq = []

    for _ in range(numbofSeq):
        RandSeq = randomSequenceGenerate(seqLength, not_aminoAcids)
        randomSeq.append(RandSeq)

    return randomSeq

def randomSequenceGenerate(seqLength, not_aminoAcids=[]):
    amino_acids = list(aminoAcids.keys())
    RandSeq = ""
    CompleteSeq = ""

    rib = "title RIBOSOME\n\n"
    rib += "default helix\n\n"

    for _ in range(seqLength):
        filtered_amino_acids = [acid for acid in amino_acids if acid not in not_aminoAcids]
        random_amino_acid = random.choice(filtered_amino_acids).upper()
        RandSeq += random_amino_acid

        threeLetterAACode = aminoAcids[random_amino_acid]
        code = threeLetterAACode.lower()

        phi_angle = random.uniform(-90, 90)
        chi_angle = random.uniform(-90, 90)

        rib += f"res {code}  phi  {phi_angle:.1f}  psi {chi_angle:.1f}\n\n"

    CompleteSeq = {
        'id': random.randint(0, 10000),
        'sequence': RandSeq,
        'rib': rib,
    }

    return CompleteSeq

def generate_rib(seqLength, numbofSeq, output_file):
    randomSeq = gen_random_seq(seqLength, numbofSeq)
    with open(output_file, 'w') as file:
        for sequence_data in randomSeq:
            rib = sequence_data['rib']
        file.write(rib)

def main():
    seqLength = int(input("Enter the peptide length: "))
    numbofSeq = int(input("Enter the number of sequences you want: "))
    
    for i in range(1, numbofSeq + 1):
        generate_rib(seqLength, numbofSeq, f'output{i}.rib')

if __name__ == "__main__":
    main()
