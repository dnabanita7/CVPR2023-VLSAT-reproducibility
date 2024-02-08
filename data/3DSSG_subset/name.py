import os

def write_folder_names_to_txt(folder_path):
    # Get the list of all folders inside the main folder
    folders = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

    # Write folder names to a text file
    with open(os.path.join(folder_path, 'rescans.txt'), 'w') as file:
        for folder in folders:
            file.write(folder + '\n')

    print("Folder names written to 'rescans.txt' in the main folder.")

# Specify the folder path where you want to write the folder names
folder_path = '.'

# Call the function to write folder names to a text file
write_folder_names_to_txt(folder_path)
