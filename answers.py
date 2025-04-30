def modify_content(line):
    # Example modification: convert to uppercase
    return line.upper()

# Ask the user for the filename
filename = input("Enter the filename to read: ")

try:
    # Try to open the file for reading
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Modify each line
    modified_lines = [modify_content(line) for line in lines]

    # Prepare new filename
    new_filename = f"modified_{filename}"

    # Write to a new file
    with open(new_filename, 'w') as new_file:
        new_file.writelines(modified_lines)

    print(f"Modified content written to '{new_filename}'.")

except FileNotFoundError:
    print("Error: The file was not found.")
except IOError:
    print("Error: Could not read or write to the file.")
