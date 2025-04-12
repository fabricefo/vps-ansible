from jinja2 import Template
import os

with open("inventory.ini.j2") as f:
    template = Template(f.read())

output = template.render()
with open("inventory.ini", "w") as f:
    f.write(output)
