import pandas as pd
import matplotlib.pyplot as plt
import math

data= pd.read_csv(r"monthly_salary_brazil.csv")

averagePrice = data['AveragePrice']
plt.title('Histogram of Avocado Prize Distribution')
number_of_classes = int(round(math.log(averagePrice.size) / math.log(2)))
freq, bins, patches = plt.hist(averagePrice, bins=number_of_classes, edgecolor="black")
plt.show()


