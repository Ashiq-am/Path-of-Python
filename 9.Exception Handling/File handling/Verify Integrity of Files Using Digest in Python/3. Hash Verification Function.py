def verify_hash(downloaded_file, expected_hash):
    calculated_hash = calculate_hash(downloaded_file)
    return calculated_hash == expected_hash