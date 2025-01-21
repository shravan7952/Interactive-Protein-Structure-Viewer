import tkinter as tk
from tkinter import messagebox
import requests
import subprocess

def fetch_protein_structure(pdb_id):
    """Fetch the PDB file content from the RCSB PDB API."""
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text  # Return the PDB file content as text
    else:
        messagebox.showerror("Error", f"Could not fetch PDB file for {pdb_id}. Status code: {response.status_code}")
        return None

def visualize_protein():
    """Visualize the protein structure using PyMOL."""
    pdb_id = entry.get().strip()
    pdb_structure = fetch_protein_structure(pdb_id)
    
    if pdb_structure:
        # Save the PDB structure to a temporary file
        pdb_file_path = f"{pdb_id}.pdb"
        with open(pdb_file_path, "w") as f:
            f.write(pdb_structure)
        
        # Specify the full path to the PyMOL executable
        pymol_path = r"C:\Users\shrav\Desktop\PYTHON\shravan7952\Project\PyMOL-3.1.3_appveyor1638-Win64-portable-py310\PyMOL\PyMOLWin.exe"  # Adjust this path as necessary
        try:
            subprocess.run([pymol_path, pdb_file_path])
        except FileNotFoundError:
            messagebox.showerror("Error", "PyMOL executable not found. Please check the path.")
    else:
        messagebox.showerror("Error", "No PDB structure found for the given ID.")

# Create the main window
root = tk.Tk()
root.title("Interactive Protein Structure Viewer")

# Create a title label
title_label = tk.Label(root, text="Interactive Protein Structure Viewer", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create a label for PDB ID input
pdb_label = tk.Label(root, text="Enter Protein Data Bank (PDB) ID:")
pdb_label.pack(pady=5)

# Create an entry widget for user input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Create a button to visualize the protein
visualize_button = tk.Button(root, text="Visualize Protein", command=visualize_protein)
visualize_button.pack(pady=10)

# Start the GUI event loop
root.mainloop() 