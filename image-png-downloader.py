import requests
import json
import os
# Directory to save the images
save_directory = "/content/drive/MyDrive/<collection_name>/"

# Create the directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# File containing the display_image_url links
input_file = "/content/drive/MyDrive/unique_<collection_name>.txt"

# Function to download images and save them with consecutive filenames
def download_images():
    with open(input_file, "r") as file:
        for idx, line in enumerate(file, start=1):
            image_url = line.strip()  # Remove any surrounding whitespace or newline characters
            if image_url:
                try:
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        # Generate a filename with consecutive numbering
                        filename = f"<collection_name>_{idx}.png"
                        filepath = os.path.join(save_directory, filename)

                        # Save the image
                        with open(filepath, "wb") as img_file:
                            img_file.write(response.content)

                        print(f"Downloaded and saved: {filename}")
                    else:
                        print(f"Failed to download: {image_url} (Status code: {response.status_code})")
                except Exception as e:
                    print(f"An error occurred while downloading {image_url}: {e}")

# Run the function
download_images()
