import ezgmail

# searching emails
# with attachments
results = ezgmail.search('has:attachment')

# list of attached filenames
files_attached = results[0].messages[0].attachments

# downloading the first file
# in the list
print('Downloading '+files_attached[0])
results[0].messages[0].downloadAttachment(files_attached[0])
