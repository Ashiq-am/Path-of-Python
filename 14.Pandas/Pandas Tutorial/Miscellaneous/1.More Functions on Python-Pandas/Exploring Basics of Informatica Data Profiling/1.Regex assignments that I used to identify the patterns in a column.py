pattern_url = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
pattern_date = r'\d{4}-\d{2}-\d{2}|[0-3]?[0-9]/[0-3]?[0-9]/\d{4}'
pattern_credit_card = r'\b(?:\d{4}-?){3}\d{4}\b'
pattern_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b'
pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
pattern_phone = r'(?:(?:\+|0{0,2})(91-?)?)[7-9]\d{9}'
pattern_aadhar = r'\b\d{4}\s\d{4}\s\d{4}\b'
pattern_ssn = r'\b\d{3}-\d{2}-\d{4}\b'

pattern_list = [pattern_url , pattern_date, pattern_credit_card, pattern_ip , pattern_email , pattern_phone , pattern_aadhar , pattern_ssn]
