import re

text = "My email is test123@gmail.com"

pattern = r"\w+@\w+\.\w+"

match_result = re.match(pattern, text)
search_result = re.search(pattern, text)

print(match_result)
print(search_result.group())
