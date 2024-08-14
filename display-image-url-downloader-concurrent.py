import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Directory to save the images
save_directory = "/content/drive/MyDrive/<collection_name>/"

# Create the directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# File containing the display_image_url links
input_file = "/content/drive/MyDrive/<collection_name>.txt"

# Function to download a single image
def download_image(idx, image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            # Generate a filename with consecutive numbering
            filename = f"babydogearmy_{idx}.png"
            filepath = os.path.join(save_directory, filename)

            # Save the image
            with open(filepath, "wb") as img_file:
                img_file.write(response.content)

            print(f"Downloaded and saved: {filename}")
            return True
        else:
            print(f"Failed to download: {image_url} (Status code: {response.status_code})")
            return False
    except Exception as e:
        print(f"An error occurred while downloading {image_url}: {e}")
        return False

# Function to download images concurrently
def download_images_concurrently():
    with open(input_file, "r") as file:
        image_urls = [line.strip() for line in file if line.strip()]

    # Use ThreadPoolExecutor to download images concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all download tasks
        futures = [executor.submit(download_image, idx, url) for idx, url in enumerate(image_urls, start=1)]

        # Wait for all tasks to complete
        for future in as_completed(futures):
            future.result()

# Run the concurrent downloader function
download_images_concurrently()
