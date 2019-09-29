import re

text = r'{{x1:3}, {y:5}, {x:test}, {y:2, x:1}}'
pattern = r':\d+'
sum_in_text = 0
for match in re.findall(pattern, text):
    sum_in_text += int(match[1:])
print(sum_in_text)
print(sum([int(match[1:]) for match in re.findall(pattern, text)]))
