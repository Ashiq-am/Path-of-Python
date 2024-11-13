if not args.downloaded_file or not args.expected_hash:
    print(
        f"{Fore.RED}[-] Please Specify the file in order to validate and its Hash.")
    sys.exit()
if verify_hash(args.downloaded_file, args.expected_hash):
    print(
        f"{Fore.GREEN}[+] Hash verification occurred successfully. The software is original.")
else:
    print(
        f"{Fore.RED}[-] Hash verification has failed, which means the software may have been tampered or is not original.")