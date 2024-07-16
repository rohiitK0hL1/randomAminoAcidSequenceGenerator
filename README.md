# Generate Random Sequence and Visualise its Structure

This project is designed to generate random sequences of amino acids and visualize their structures using the provis library in Python.

## Install the required dependencies using pip:
This Project is done on a Windows system, using WSL.
Make sure ribosome is installed in your system.
Also, install provis library. (pip install provis)

## Getting Started

To run this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Open terminal on your IDE.
4. Run "python main.py".
5. Give input to the following output- for example: choose- peptide length: 100; no. of sequence: 10 
6. There you have it! 10 output.rib files are created.
7. Now run "python convert.py". You have to again give input of the no. of sequence, keep it same.
8. 10 .pdb files are made from those .rib files (PDBgenerated.pdb)
9. To visualize these .pdb files run "python generateStructure.py".

## Project Structure

This project is made on python as it has multiple libraries, you are able to see the structures of your random sequence of Amino Acids from various libraries. 
- **main.py**: generates random sequences, in .rib format.
- **convert.py**: converts .rib into .pdb
- **generateStructure.py**: Generates visual structure of your .pdb files.

## Development Environment

This project was developed using Visual Studio Code using WSL.

## Author

- **[Rohit Kohli]**
- **[210106055]**
