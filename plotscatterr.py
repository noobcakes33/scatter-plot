import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter
import pandas as pd
import numpy

x = pd.read_excel('example_power_curve.xlsx')

a = x.iloc[:, 0].values
y = x.iloc[:, 2].values

y = [str(i).replace(';', ' ') for i in y]

cleaned_a = a[:15]
cleaned_y = y[:15]

f = [] #input
g = [] #label

for i in range(len(cleaned_a)):
    if len(cleaned_y[i].split()):
        data = cleaned_y[i].split()
        if data[0] == 'nan':
            data[0] = 0
        for k in data:
            g.append(int(k))
            f.append(cleaned_a[i])

print(f)
print(g)


fig = plt.figure()
scatter(f, g)
plt.xticks(rotation=90)
plt.title('Individual Value Plot of No of lasers available')
plt.ylabel('No of lasers available')
fig.tight_layout()
plt.show()
fig.savefig('foo.png')
