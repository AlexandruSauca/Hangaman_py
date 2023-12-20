import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

df = pd.read_csv('data.csv',nrows = 5)

df.plot()

plt.show()

df = pd.read_csv('data.csv', skiprows = 155)

df.plot()

plt.show()
