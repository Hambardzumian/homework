# Json to Text

import json
with open("sample_json.json","r") as file:
	data = json.load(file)
with open("json_to_text.txt","w") as file:
	file.write(str(data))
print("The json to text is saved as   json_to_text.txt  ")

# # Yaml to text

with open("sample.yaml","r") as file:
	data = yaml.load(file)
with open("yaml_to_text.txt","w") as file:
	file.write(str(data))
print("The yaml to text is saved as   yaml_to_text.txt  ")

# Yaml to Json

with open("sample.yaml","r") as file:
	data = yaml.load(file)
new = json.dumps(data)
with open("yaml_to_json.txt","w") as file:
	file.write(str(new))
print("The Yaml to Json is saved as   yaml_to_json.txt  ")

# Json to Yaml

import yaml
with open("sample.json","r") as file:
	data = json.load(file)
new = yaml.dump(data)
with open("json_to_yaml.txt","w") as file:
	file.write(str(new))
print("The json to yaml is saved as   json_to_yaml.txt  ")







