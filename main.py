import re

# example: <html><head><title>example</title></head></html>
# output: count of tags (6)

string = input()
expression = re.compile("<[^<>]+>", re.IGNORECASE)
print(len(expression.findall(string)))
