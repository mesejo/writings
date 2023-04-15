import re

res = re.split(r'(\W)', 'foo-bar/spam.eggs')
print(res)  # ['foo', '-', 'bar', '/', 'spam', '.', 'eggs']
