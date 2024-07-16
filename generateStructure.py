import os
import provis
from provis.src.processing.protein import Protein
from provis.src.processing.residue import Residue
from provis.src.plotting.plotter import Plotter
#from provis.src.plotting.plotter import DynamicPlotter

density = 3.0
plot_solvent = False
msms = True
notebook = False

numb = int(input("Enter the number of sequences, once again: "))
for i in range(1,numb+1):
    name = f"PDBgenerated{i}.pdb"
prot = Protein(name, base_path=None, density=density)
prot2 = Protein(name, base_path=None, density=density, model_id=30)

#temporoary directory
temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "tmp")
os.makedirs(temp_dir, exist_ok=True)

#prot = Protein(name, base_path=None, density=3.0)
#prot2 = Protein(name, model_id=30)

# Create a Plotter instance
plotter = Plotter(prot, prot2, msms=msms, notebook=notebook, plot_solvent=plot_solvent)

# Call the plot_backbone() method on the Plotter instance
plotter.plot_backbone()


plot = Plotter(prot, prot2, msms=msms, notebook=notebook, plot_solvent=plot_solvent)
plot = Plotter(prot, prot2, msms=msms, notebook=notebook)
plot.plot_bonds()


plotter.plot_backbone()
plotter.plot_atoms()
plotter.plot_bonds()
plotter.plot_vw()
plotter.plot_stick_point()
plotter.plot_residues()
r = Residue(1)
r.add_residue(3)
r. add_residue(1, 1)
r.remove_residue(1, 1)
plotter.plot_structure(atoms=1, box=1, bonds=1, vw=0, residues=0, res=r, bb=0)

plotter.plot_surface()
plotter.plot_hydrophob()
plotter.plot_shape()
plotter.plot_charge()

'''
class DynamicPlotter:
    dp = DynamicPlotter(prot, msms=msms, notebook=notebook, plot_solvent=plot_solvent)
    dp.plot_backbone()
    dp.plot_atoms()
    dp.plot_bonds()
    dp.plot_vw()
    dp.plot_stick_point()
    dp.plot_residues()
    dp.plot_structure(atoms=1, box=1, bonds=1, vw=0, residues=0, res=r, bb=0)
    dp.plot_surface()
    dp.plot_hydrophob()
    dp.plot_shape()
    dp.plot_charge()
'''

prot.file_converter.cleanup()
