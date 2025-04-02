import pandas as pd
import numpy as np
import decorator as dec
import matplotlib.pyplot as plt


    
Crude = pd.read_csv('crude-oil-price.csv')
Brent = pd.read_csv('BrentOilPrices.csv')
print(Crude)
x = Crude['date'].tolist()
y = Crude['price'].tolist()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции')
plt.grid(True)
plt.show()
