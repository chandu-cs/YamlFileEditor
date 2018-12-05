import sys
from ruamel.yaml import YAML
#Create a yaml variable
yaml = YAML()
key = input("Please enter a name to replace Jack: ")
#Open file and declare it into a variable and read file
file = open("testyaml.yml").read()
#Load file using yaml variable
details = yaml.load(file)
#Set the parameter to update
details['items'] = key
#Open file in write mode
file = open("testyaml.yml", "w")
#Update file
yaml.dump(details,file)
print(details)
file.close()



