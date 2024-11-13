import requests
import shutil

def download_large_file(url, destination):
    try:
        response = requests.get(url, stream=True)
        with open(destination, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        print("File downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print("Error downloading the file:", e)

# Example usage
url = 'https://releases.ubuntu.com/20.04.4/ubuntu-20.04.4-desktop-amd64.iso'
save_path = 'ubuntu-20.04.4-desktop-amd64.iso'
download_large_file(url, save_path)
