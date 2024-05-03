# \d - any decemal digit
# \D - any not num
# \s - any whitespace
# \S - any non whitespace
# \w - alphanumeric  любая цифра буква или нижний прочерк
# \W - not
# \b - mach paterns in beginin word
# \B - at the end

import re

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""
print(re.findall("\bip", text))
print(re.findall("[^a-g]", text))