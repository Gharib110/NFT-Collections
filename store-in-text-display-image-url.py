import requests
import json

# OpenSea API base URL and initial query parameters
base_url = "https://api.opensea.io/api/v2/collection/<collection_name>/nfts"
params = {
    "limit": 200  # Set the limit per page (adjust as needed) 1 to maximum 200
}

# Headers with the API key
headers = {
    "accept": "application/json",
    "x-api-key": "xxxxxx"
}

# File to save the display_image_url values
output_file = "/content/drive/MyDrive/<collection_name>.txt"

# Function to fetch NFTs and save display_image_urls
def fetch_and_save_nfts():
    with open(output_file, "a") as file:
        while True:
            response = requests.get(base_url, headers=headers, params=params)
            data = response.json()

            # Extract and save display_image_url from each NFT
            for nft in data.get("nfts", []):
                display_image_url = nft.get("display_image_url")
                if display_image_url:
                    file.write(display_image_url + "\n")

            # Check if there is a next page
            next_page = data.get("next")
            #print(response)
            if next_page:
                #print("next ...")
                # Update the params to use the next page token
                params["next"] = next_page
            else:
                # No more pages, break the loop
                break

    print(f"Display image URLs have been saved to {output_file}")

# Run the function
fetch_and_save_nfts()
