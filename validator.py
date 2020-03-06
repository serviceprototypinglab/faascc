# Validates a (simplified) file for relative completeness

import yaml

cc = yaml.load(open("faascc.simplified.yaml").read())

def validate(cc):
	for entry in cc[0]:
		for ccrel in cc[1:]:
			if not entry in ccrel:
				print("Entry", entry, "missing in", ccrel["name"])

validate(cc)
