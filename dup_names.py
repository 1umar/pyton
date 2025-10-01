
import os
from collections import defaultdict
from tinytag import TinyTag as tt

# name: dup_names.py
""" Pentru ca folosesc modulul tinytag, instalat in virtual environment,
    programul trebuie pornit din acel mediu:
    1. source pyvir/bin/activate
		in Ubuntu:	source pythVirt/bin/activate
    2. python /home/lu/Muzici/find_duplicates.py
		in Ubuntu:	python /home/luch/pythProj/Muzici/duplicate_names.py
    3. ca sa parasesti mediul virtual, dupa rularea programului:
        $ deactivate
"""

#folder = "/home/lu/Music/2Pac_Keyshia Cole/A Different Me"
#folder = "/home/lu/Music"
folder = "/media/lu/HD6"	# pe RPi 4, iar in Ubuntu:
#folder = "/media/luch/DATA/BM-Share/Music/Music"

good_ext = ['.mp3','.m4a','.flac','.wav','.wma']

def find_duplicate_files(directory):
    """
    Find duplicate files in the given directory.
    
    :param directory: Directory to search for duplicates
    :param follow_symlinks: Whether to follow symbolic links
    :return: Dictionary of duplicate file groups
    """
    duplicate_groups = defaultdict(list)
    
    # Walk through directory
    for root, _, files in os.walk(directory):
        name_groups = defaultdict(list)
        for filename in files:
            if os.path.splitext(filename)[1].lower() in good_ext:
                filepath = os.path.join(root, filename)
            
                try:
                    # Get file name
                    file_name = tt.get(filepath).title
                    name_groups[file_name].append(filepath)
                except (PermissionError, FileNotFoundError):
                    continue
                    
#    Find potential duplicates (files with the same name)                    
        for name, files in name_groups.items():
            # Only process groups with more than one file
            if len(files) > 1:
                # Group files by their content hash
                duplicate_groups[name].append(files)
                               
            # Add hash groups with more than one file to duplicate groups
            # for nume_val, nume_files in name_groups.items():
                # if len(nume_files) > 1:
                    # duplicate_groups[nume_val] = nume_files
    
    return duplicate_groups

def print_duplicate_groups(duplicate_groups):
    """
    Print out the groups of duplicate files.
    
    :param duplicate_groups: Dictionary of duplicate file groups
    """
    if not duplicate_groups:
        print("No duplicates found.")
        return
    
    print(f"\nFound {len(duplicate_groups)} groups of duplicate files:\n")
#    for i, (hash_val, files) in enumerate(duplicate_groups.items(), 1):
    for nume, files in duplicate_groups.items():
        for file in files:  # aici 'file' e o lista, de fapt
            for num_fis in file:
                print(num_fis)
        print()
            
    # print("\n\nFisiere de sters:\n\n")
    # nr_fis_de_sters = 0
    # size_fis_de_sters = 0
    # for i, (hash_val, files) in enumerate(duplicate_groups.items(), 1):
 # #       print(f"\nDuplicate Group {i}:")
        # for file in files:
            # if file[-6]==' ' and file[-5].isdigit():
                # nr_fis_de_sters = nr_fis_de_sters + 1
                # size_fis_de_sters = size_fis_de_sters + os.path.getsize(file)
                # print(f"{file} ")
# #                os.remove(file)
    # print("Nr. fisiere de sters:\t", nr_fis_de_sters)
    # print("Total bytes to delete:\t", size_fis_de_sters)
    
    

def main():
    os.system("sync")
    duplicate_groups = find_duplicate_files(folder)
    print_duplicate_groups(duplicate_groups)

if __name__ == '__main__':
    main()
# Initial	39.022 files, 840,5GB
# Final		38.117 files, 817,8GB
