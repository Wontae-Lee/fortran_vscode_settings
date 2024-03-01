import os

def add_tab_to_lines_in_directory(directory_path):
    # Iterate over all files and subdirectories in the specified directory
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            # Combine the root path with the current file name
            file_path = os.path.join(root, file_name)

            # Process only text files (you can modify the condition based on your needs)
            if file_name.endswith(".h") or file_name.endswith(".inl") or file_name.endswith(".cpp"):
                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # Add a tab to the beginning of each line
                lines_with_tab = ['\t' + line for line in lines]

                # Write the modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(lines_with_tab)

                print(f"Processed: {file_path}")

# Specify the directory path you want to process
directory_to_process = '../src'

# Call the function to add tabs to lines in all files in the specified directory
add_tab_to_lines_in_directory(directory_to_process)
