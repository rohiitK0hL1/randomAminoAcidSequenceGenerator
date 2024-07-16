import subprocess

def convert_rib_to_pdb(rib_file_path, pdb_file_path, ribosome_path, res_zmat):
    command = f'"{ribosome_path}" "{rib_file_path}" "{pdb_file_path}" {res_zmat}'
    subprocess.run(command, shell=True)

numb = int(input("Enter the number of sequences, once again: "))

if __name__ == "__main__":
    for i in range(1, numb + 1):
        #generate_rib(seqLength, numbofSeq, f'output{i}.rib')
        rib_file_path = f'output{i}.rib'
        pdb_file_path = f'PDBgenerated{i}.pdb'
        ribosome_path = './ribosome'  # Specify the full path to Ribosome executable
        res_zmat = 'res.zmat'
        convert_rib_to_pdb(rib_file_path, pdb_file_path, ribosome_path, res_zmat)