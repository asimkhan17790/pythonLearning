#
# To learn more about Regular Expressions Go to Website:
# https://regexr.com/
#
#


import re  # built in package for regular expressions

text = "The quick brown fox jumps over the the lazy dog. fuck"

# returns first occurence for the match only
match = re.search("brown", text, re.IGNORECASE)

print(match)
if (match):
    print("Match found!")
    print("Start index : ", match.start())
    print("End index : ", match.end())


# Find all occurences
matches = re.findall("the", text, re.IGNORECASE)

print("Matches:", matches)


# Replace something in the text

new_text = re.sub("[f]+", "*", text)
print(text)
print(new_text)
