parser = argparse.ArgumentParser(
    description="Verify the hash of a file that is downloaded.")
parser.add_argument("-f", "--file", dest="downloaded_file",
                    required=True, help="path for the file downloaded")
parser.add_argument("--hash", dest="expected_hash",
                    required=True, help="Expected hash value is")
args = parser.parse_args()