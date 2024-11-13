import requests

file_path = '/path/to/your/audio/file.mp3'
upload_url = 'http://localhost:5000/upload'

files = {'file': open(file_path, 'rb')}
response = requests.post(upload_url, files=files)

if response.status_code == 200:
	print('File uploaded and processed successfully')
	processed_filename = response.json()['filename']
	download_url = f'http://localhost:5000/download/{processed_filename}'
	# Use download_url to download the processed file
else:
	print('Error:', response.json()['error'])
