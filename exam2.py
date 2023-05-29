
# First Project
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


path = f'/Users/narek/Downloads/mtcars.csv.xls'
x = pd.read_csv(path)

figure = plt.figure(figsize=(20, 15))
gs = gridspec.GridSpec(4, 4, figure=figure)

axis1 = figure.add_subplot(gs[:2, :2])
axis3 = figure.add_subplot(gs[0, 2])       
axis6 = figure.add_subplot(gs[1, 2])       
axis7 = figure.add_subplot(gs[2, 0])       
axis8 = figure.add_subplot(gs[2, 1])       
axis9 = figure.add_subplot(gs[2, 2])

mask = np.tril(x.corr(numeric_only=True), k=-1)


sns.heatmap(x.corr(numeric_only=True)[::-1], mask=mask[::-1], ax=axis1, cmap="coolwarm",
            linewidth=.5, center=0, cbar_kws={'shrink': 0.5}, vmax=1, vmin=-1)
cbar = axis1.collections[0].colorbar
cbar.set_label("Pearson correlation", rotation=90)
axis1.set_xlabel('Var1')
axis1.set_ylabel('Var2')
axis1.tick_params(axis='x', rotation=45)
axis1.tick_params(axis='y', rotation=0)

sns.histplot(data=x, x='wt', ax=axis3, hue='am', multiple='stack', bins=10)
sns.move_legend(axis3, "upper left", bbox_to_anchor=(1, 1), frameon=False, title='Transmission')
axis3.set_title('Weight and automatic/manual proportions on the plot', size=8)
axis3.set_xlabel('Ib')
axis3.set_ylabel('# of cars')
axis3.spines['right'].set_visible(False)
axis3.spines['top'].set_visible(False)
axis3.set_xticks([2, 3, 4, 5])


sns.boxplot(data=x, x="carb", y='mpg', ax=axis6)
axis6.set_xlabel('# of carburetors')
axis6.set_ylabel('mpg')

sns.scatterplot(data=x, x='hp', y='drat', hue='gear', size='cyl', ax=axis7, palette="bright")
axis7.set_xlabel('Gross horsepower')
axis7.set_ylabel('Rear axle ratio')
sns.move_legend(axis7, "upper left", bbox_to_anchor=(1, 1), frameon=False)

sns.histplot(data=x, x='am', ax=axis8, hue='carb', palette="ch:start=.2,rot=-.3",
             edgecolor=None, discrete=True, shrink=0.8)
sns.move_legend(axis8, "upper left", bbox_to_anchor=(1, 1), frameon=False)
axis8.set_xlabel('Transmission')
axis8.set_xticks([0, 1])

sns.kdeplot(data=x, x='mpg', hue='am', multiple='stack', ax=axis9)

figure.tight_layout()

figure
plt.show()

# Second Project

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create(num1=50, num2=0.5):
    return np.random.choice([0, 1], size=(num1, num1), num2=[1-num2, num2])

def animate(universe, img):
    newUniverse = np.zeros((num1+2, num1+2))
    newUniverse[1:-1, 1:-1] = universe
    for i in range(1, num1+1):
        for j in range(1, num1+1):
            n = (newUniverse[i+1][j] + newUniverse[i-1][j]
                 + newUniverse[i][j+1] + newUniverse[i][j-1]
                 + newUniverse[i+1][j+1] + newUniverse[i-1][j-1]
                 + newUniverse[i+1][j-1] + newUniverse[i-1][j+1])
            if newUniverse[i][j] == 0 and n == 3:
                universe[i-1][j-1] = 1
            elif newUniverse[i][j] == 1 and (n < 2 or n > 3):
                universe[i-1][j-1] = 0
            else:
                universe[i-1][j-1] = newUniverse[i][j]
    img.set_data(universe)
    return img

num1 = 50
num2 = 0.5
universe = create(num1, num2)
figure = plt.figure(figsize=(8, 8))
axis = plt.axes()
image = axis.imshow(universe, interpolation='nearest')
animation = FuncAnimation(figure, animate, fargs=(universe, image),
                    frames=None, interval=500, save_count=50)

plt.show() 