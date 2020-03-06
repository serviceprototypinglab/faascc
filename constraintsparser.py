import yaml

cc = yaml.load(open("faascc.yaml").read())

latest = lambda tsl: max([list(ts.keys())[0] for ts in tsl])
latestvalue = lambda tsl: [list(ts.values())[0] for ts in tsl if list(ts.keys())[0] == latest(tsl)][0]

for service in cc:
	print(service["name"], "runs for up to", latestvalue(service["duration"]), "s")
