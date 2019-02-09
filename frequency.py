import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bkPdf
import math

data = pd.read_csv(r"monthly_salary_brazil 2.csv")
salaries = data["total_salary"]

std = np.std(salaries)
mean = np.mean(salaries)

Q_1 = np.percentile(salaries, 25)
Q_2 = np.percentile(salaries, 50)
Q_3 = np.percentile(salaries, 75)

IR = Q_3 - Q_1
upperFence = Q_3 + 1.5 * IR
lowerFence = Q_3 - 1.5 * IR

upperoutliers = salaries[salaries > upperFence]
lowerdownliers = salaries[salaries < lowerFence]

# print("Standard Derivation: ", std)
# print("Mean: ", mean)
# print("Q1: ", Q_1)
# print("Q2: ", Q_2)
# print("Q3: ", Q_3)
# print("upperoutliers", upperoutliers,"\n" ,"lowerdownliers",lowerdownliers,"\n")

real_salaries = salaries[salaries > 0]
soi = real_salaries[real_salaries < 5000]
number_classes = int(round(math.log(soi.size) / math.log(2)))

freq, bins, patches = plt.hist(soi, bins=number_classes, edgecolor="Black")
rel_freq = freq / soi.size

class_range = []
upper_class = []
middle_class = []
for i in range(int(bins.size) - 1):
    lower = bins[i]
    upper = bins[i + 1]
    upper_class.append(upper)
    middle_class.append((upper + lower) / 2)
    class_range.append("{:0.2f}".format(lower) + "-" + "{:0.2f}".format(upper))

cumFreq, trash1, trash2 = plt.hist(soi, bins=number_classes, edgecolor="black", cumulative=True)

table = pd.DataFrame(
    {"Frecuency": freq, "Relative Frecuency": rel_freq, "Mark of Class": middle_class, "Cumulative Freq": cumFreq},
    index=class_range)
pd.set_option('precision', 2)
print(table)

plt.plot(upper_class, cumFreq, 'go-')

# number_classes=int(round(math.log(real_salaries.size)/math.log(2)))
# number_classes2= int(round(math.sqrt(real_salaries.size)))
# plt.hist(real_salaries,edgecolor="Black",bins=number_classes)

# plt.boxplot(salaries)
# plt.show()
pdf = bkPdf.PdfPages("output.pdf")
bkPdf.PdfPages("Hello")
