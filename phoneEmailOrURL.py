# find all the emails and phone numbers from the clipboard

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# 222|(222) |-|.222 |-|.2222 opcjonalnie  ext|x|ext. {2-5 cyfr}
# phoneRegexPL = re.compile(r'''(
#     (\+\d{2})?
#     (\s)?
#     (\d{2,3})
#     (\s)
#     (\d{3})
#     (\s)
#     (\d{2,3})
#     (\s)?
#     (\d{2})?
#     )''', re.VERBOSE)

urlRegex = re.compile(r'''(
    (http://|https://)
    [a-zA-Z0-9$._+!*'(),-]+
    (\.[a-zA-Z]{2,4})
    /
    ([a-zA-Z0-9$._+!*'(),-/?=]+)?
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

text = str(pyperclip.paste())               # get all text that u copied

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

for groups in urlRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Coppied to clipboard:")
    print('\n'.join(matches))
else:
    print("There was no phone number, email or URL found found")
