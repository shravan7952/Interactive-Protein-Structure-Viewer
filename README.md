# Interactive Protein Structure Viewer

This is a Python application that allows users to fetch and visualize protein structures from the Protein Data Bank (PDB) using the PyMOL visualization software. The graphical user interface (GUI) is built using the `tkinter` library.

---

## Features

- Fetches protein structure data by PDB ID from the RCSB PDB database.
- Saves the protein structure in `.pdb` format.
- Opens the structure in PyMOL for visualization.

---

## Requirements

1. **Python**: Version 3.6 or later.
2. **PyMOL**: Installed on your system (ensure the correct path to the PyMOL executable is provided in the script).
3. **Python Libraries**:
   - `tkinter`: Built-in with Python (for GUI).
   - `requests`: For fetching PDB data from the internet.

To install the `requests` library if it’s not already installed, run the following command:

```bash
pip install requests
```

---

## Setting Up PyMOL for Visualization

To use PyMOL to visualize protein structures, follow these steps to set it up correctly:

### Step 1: Download PyMOL

1. Go to the official PyMOL website: [Download PyMOL](https://www.pymol.org/).
2. Download the **portable version** (ZIP file) of PyMOL for Windows.

### Step 2: Extract the ZIP File

1. Once the ZIP file is downloaded, unzip it to the folder where your `interactive_protein_viewer.py` script is located.

### Step 3: Locate the `PyMOLWin.exe` File

1. After extracting the files, navigate to the folder where you unzipped PyMOL.
2. Find the file named `PyMOLWin.exe`—this is the executable used to run PyMOL.

### Step 4: Update the Path in the Script

1. Open the `interactive_protein_viewer.py` file in a text editor.
2. Locate the line where `pymol_path` is defined:
   ```python
   pymol_path = r"C:\Users\shrav\Desktop\PYTHON\shravan7952\Project\PyMOL-3.1.3_appveyor1638-Win64-portable-py310\PyMOL\PyMOLWin.exe"  # Adjust this path as necessary
   ```
3. Change the `pymol_path` to the exact location of `PyMOLWin.exe` on your machine. For example, if you unzipped PyMOL to `C:\PyMOL`, you would modify the line to:
   ```python
   pymol_path = r"C:\PyMOL\PyMOLWin.exe"
   ```
   Ensure that the path points directly to the `PyMOLWin.exe` file.

---

## Usage

1. **Clone or Download the Script**:
   - Clone the repository or copy the `interactive_protein_viewer.py` script to your local machine.

2. **Set Up PyMOL**:
   - Follow the steps above to set up PyMOL on your system and make sure the path to `PyMOLWin.exe` is correct in the script.

3. **Run the Script**:
   - Open a terminal or command prompt and navigate to the directory containing the `interactive_protein_viewer.py` file.
   - Run the script using the following command:
     ```bash
     python interactive_protein_viewer.py
     ```

4. **Enter PDB ID**:
   - When the GUI opens, enter a valid Protein Data Bank (PDB) ID (e.g., `1A8M`) into the input field and click the **"Visualize Protein"** button.
   - The script will fetch the corresponding protein structure from the RCSB PDB database and open it in PyMOL for visualization.

---

## Notes

- Ensure you have an active internet connection to fetch PDB files.
- Verify that the PDB ID you enter is valid. You can search for valid PDB IDs on the [RCSB PDB website](https://www.rcsb.org/).
- If PyMOL does not open, double-check that the path to the PyMOL executable is correct in the script.
- The path to `PyMOLWin.exe` must be updated in the script to match where you have unzipped the PyMOL files on your machine.

---

## Error Handling

- **Invalid PDB ID**: If the entered PDB ID is invalid or the structure cannot be fetched, an error message will be displayed in the GUI.
- **PyMOL Not Found**: If PyMOL cannot be found or executed, a corresponding error message will appear. This is often due to an incorrect path to `PyMOLWin.exe`.

---

## License

This project is open-source and available under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- **RCSB PDB** for providing protein structure data.
- **PyMOL** for their powerful visualization tools.
```

### Summary of Changes:
- The README now includes **detailed instructions** for downloading and setting up PyMOL.
- **Instructions for locating the `PyMOLWin.exe` file** and updating the script path have been added.
- Clear, step-by-step guidance on how to set up the software and run the script has been provided.

This should now be a fully functional README that covers all aspects of using the interactive protein structure viewer with PyMOL!
