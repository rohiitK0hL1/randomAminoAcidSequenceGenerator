import nglview

def visualize_structure(pdb_file_path, html_file_path):
    view = nglview.show_file(pdb_file_path)
    view.render_image()
    view._display_image()
    view.display()
    view._set_notebook_class()
    view._display_notebook()
    view.save(html_file_path)

# Example usage
visualize_structure("PDBgenerated.pdb", "visualization.html")
