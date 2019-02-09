import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bkPDF
import numpy as np
import math

data= pd.read_csv(r"avocado.csv")
averagePrice = data['AveragePrice']
pdf = bkPDF.PdfPages('Quiz_Python_Probability_and_Statistics_Plots.pdf')

# a.1
fig_a = plt.figure(figsize=(8, 30))
plt.title('Histogram of Avocado Prize Distribution')

# a.2
number_of_classes = int(round(math.log(averagePrice.size) / math.log(2)))
freq, bins, patches = plt.hist(averagePrice, bins=number_of_classes, edgecolor="black")

# a.3
print('Number of classes n=', number_of_classes)

# a.4
plt.ylabel('Number of sold avocados')
plt.xlabel('Avocado Price')
pdf.savefig(fig_a)
plt.show()
plt.close()
print('Yes, it is bell shaped visually')

# a.5
mean = np.mean(averagePrice)
std = np.std(averagePrice)

print('The n1% of the data lies in the range(', (mean-std), ',', (mean+std), ') according to the Empirical rule')
print('The n2% of the data lies in the range(', (mean-2*std), ',', (mean+2*std), ') according to the Empirical rule')
print('The n3% of the data lies in the range(', (mean-3*std), ',', (mean+3*std), ') according to the Empirical rule')

#e

middle_class=[]
upper_class=[]
fig_e = plt.figure(figsize=(8,30))

for i in range(int(bins.size)-1):
    lower=bins[1]
    upper=bins[i+1]
    upper_class.append(upper)
    middle_class.append((upper+lower)/2)

R_class=bins[1]-bins[0]
mcfp=middle_class
print(middle_class[-1])
print(R_class)
mcfp.insert(int(len(middle_class)),middle_class[-1]+R_class)
mcfp.insert(0,middle_class[0]-R_class)

ffp=freq.tolist()
ffp.append(0)
ffp.insert(0,0)
plt.plot(mcfp,ffp,"-ro")

# e.1
plt.title('Polygon of frequencies of the avocado prize distribution')

# e.2
plt.xlabel('Avocado prize')
plt.ylabel('Number of sold avocados')
pdf.savefig(fig_e)
plt.show()
plt.close()

pdf.close()
