import pandas as pd
import numpy as np
import decorator as dec
import matplotlib.pyplot as plt
from decorator import Oil
Crude = pd.read_csv('crude-oil-price.csv')
Brent = pd.read_csv('BrentOilPrices.csv')
oil = Oil(Crude, Brent)
Oil.main(oil)
