# Opening file stream

r = requests.get(link_to_file, stream = True)

# writing file data in chunks.
# for examples, A file of 10 MB written in
# chunk size of 8096 Bytes.
with open(file_name, 'wb') as f:
    for chunk in r.iter_content(chunk_size):
        f.write(chunk)
