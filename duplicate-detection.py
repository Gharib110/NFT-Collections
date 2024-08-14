# File containing the URLs or lines
input_file = "/content/drive/MyDrive/<collection_name>.txt"
output_file = "/content/drive/MyDrive/unique_<collection_name>.txt"

# Function to remove duplicates
def remove_duplicates():
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Remove duplicates by converting the list to a set, then back to a list
    unique_lines = list(set(lines))

    # Sort lines to maintain order (optional)
    unique_lines.sort()

    # Write the unique lines back to a new file
    with open(output_file, "w") as file:
        file.writelines(unique_lines)

    print(f"Removed duplicates. Unique lines saved to {output_file}")

# Run the function
remove_duplicates()
