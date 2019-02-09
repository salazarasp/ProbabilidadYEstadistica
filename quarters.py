import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv(r"monthly_salary_brazil.csv")
salaries = data["total_salary"]
array = np.array([1,2,3,4])
std = np.std(salaries)
mean = np.mean(salaries)
q1 = np.percentile(salaries, 25)
q2 = np.percentile(salaries, 50)
q3 = np.percentile(salaries, 75)

IR = q3 - q1
upperFence = q3 + 1.5 * IR
upperOutliers = salaries[salaries > upperFence]
lowerDownliers = salaries[salaries > upperFence]

def printQ():
    print("Standard Derivation: ", std)
    print("Mean: ", mean)
    print("Quartile 1", q1)
    print("Quartile 2", q2)
    print("Quartile 3", q3)
    print("Upper Outliers: \n", upperOutliers, " \nLower Downliers: \n", lowerDownliers)

realSalaries = salaries[salaries>0]
realSalaries = realSalaries[realSalaries<5000]
numberClasses = math.log(realSalaries.size)/math.log(2)
numberClasses2 = math.sqrt(realSalaries.size)

meanRealSalaries = np.mean(realSalaries)
stdRealSalaries = np.std(realSalaries)

plt.hist(realSalaries, edgecolor='Black', bins=int(numberClasses))
plt.show()

# zValues = (upperOutliers-meanRealSalaries)/stdRealSalaries

# print("Starting plot box...")
# plt.boxplot(zValues)
# plt.show()
# print("Finished")

