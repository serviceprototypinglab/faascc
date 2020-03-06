# Generates a simplified file without evolution information and in optimised YAML representation
# Suitable as entry point for software development

import yaml

cc = yaml.load(open("faascc.yaml").read())

latest = lambda tsl: max([list(ts.keys())[0] for ts in tsl])
latestvalue = lambda tsl: [list(ts.values())[0] for ts in tsl if list(ts.keys())[0] == latest(tsl)][0]

def simplifyrecursive(cc):
	for entry in cc:
		origentry = entry
		if type(cc) == dict:
			entry = cc[entry]
		if type(entry) == list:
			simplify = True
			for data in entry:
				if type(data) != dict or type(list(data.keys())[0]) != int:
					simplify = False
			if simplify:
				cc[origentry] = latestvalue(entry)
		if type(entry) in (list, dict):
			simplifyrecursive(entry)

simplifyrecursive(cc)

f = open("faascc.simplified.yaml", "w")
yaml.dump(cc, f)
