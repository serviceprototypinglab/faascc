# Calculates & visualises the cost of running a cloud function

import yaml
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def calculate(entry, ax, color):
	x = np.zeros([9, 9])
	y = np.zeros([9, 9])
	z = np.zeros([9, 9])
	for i, monthlycalls in enumerate(range(500000, 10*500000, 500000)):
		for j, monthlyload in enumerate(range(100000, 10*100000, 100000)):
			priceload = max((monthlyload - entry["contingentload"]) * entry["priceload"], 0)
			pricecalls = max((monthlycalls - entry["contingentcalls"]) * entry["pricecall"], 0)
			price = round(priceload + pricecalls, 2)
			#print(price)
			x[i, j] = monthlycalls
			y[i, j] = monthlyload
			z[i, j] = price
	frame = ax.plot_wireframe(x, y, z, colors=(color + (0.9,)))
	frame.set_label(entry["name"])
	ax.legend()

cc = yaml.load(open("faascc.simplified.yaml").read())

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

colors = (
	(0.2, 0.2, 0.7),
	(0.3, 0.9, 0.3),
	(0.6, 0.2, 0.1),
	(0.8, 0.7, 0.2)
)

for entry, color in zip(cc, colors):
	calculate(entry, ax, color)

plt.title("Pricing comparison across FaaS providers (in USD per month)")
plt.xlabel("calls")
plt.ylabel("load")
#plt.zlabel("USD")
plt.show()
