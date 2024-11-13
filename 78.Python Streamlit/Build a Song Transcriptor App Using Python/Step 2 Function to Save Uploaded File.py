def save_uploaded_file(uploaded_file, save_path):
    with open(os.path.join(save_path, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
