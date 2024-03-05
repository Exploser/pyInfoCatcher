#! python3

import re, pyperclip

phoneRegex = re.compile(r''' 
                (((\+)                        # country code   
                (\d+)       
                (\s|-)?)?                      # seprator
                ((\d\d\d)|(\(\d\d\d\)))?      # area code (op)
                (\s|-)                        # first separator
                \d\d\d                        # first 3 digits
                (\s|-)                        # separator
                \d\d\d\d                      # last 4 digits
                (((ext(\.)?\s)|x)             # extension word (op)
                 (\d{2,5}))?)                 # extension number (op)
                ''', re.VERBOSE)

emailRegex = re.compile(r'''
                        ([a-zA-Z0-9_.+]+    # name 
                        @                   # @
                        [a-zA-Z0-9_.+]+     # domain
                        .                   # .
                        [a-zA-Z0-9_.+]+)    # TLD
                        ''', re.VERBOSE)

text = pyperclip.paste() 

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)