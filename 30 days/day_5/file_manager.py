import os

absolute_path=os.path.abspath("__file__")
base_dir=os.path.dirname(absolute_path)
email_tx=os.path.join(base_dir,"templates","email.txt")
content=""

with open(email_tx) as file:
    content=file.read()

print(content.format(name="Raghavendra"))

