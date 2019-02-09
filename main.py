# Javier Mondragon Martin del Campo A01365137
# Alfredo Salazar Peralta A01366438

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bkPDF
import numpy as np
import math

data= pd.read_csv(r"avocado.csv")
averagePrice = data['AveragePrice']
sold = data['Total Bags']
Total_bags = data['Total Bags']
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

#b

fig_b = plt.figure(figsize=(8, 30))

#b1

plt.title("Cumulative histogram of Avocado prize distribution")

cumfreq,trash1,trash2=plt.hist(averagePrice,bins=number_of_classes,edgecolor="black",cumulative=True)

#b2

plt.ylabel('Cumulative frequency of sold Avocados')
plt.xlabel('Avocado Price')
pdf.savefig(fig_b)
plt.show()
plt.close()

#b3

print('\n There are 6 classes, which cumulative frequency is lower than 15000')

#d.4
figure=plt.figure(figsize=(8,30))
n=7

ax=figure.add_subplot(n,1,1)
ax.boxplot(averagePrice,vert=False)
p_25=round(np.percentile(averagePrice,25),2)
p_50=round(np.percentile(averagePrice,50),2)
p_75=round(np.percentile(averagePrice,75),2)
plt.text(p_25, 0.85, "$Q_{1}=$"+ str(p_25), fontsize=12)
plt.text(p_50, 0.75, "$Q_{2}=$"+ str(p_50), fontsize=12)
plt.text(p_75, 0.65, "$Q_{3}=$"+ str(p_75), fontsize=12)

iqr = (p_75) - (p_25)

lower = (p_25) - (1.5 * (iqr))
upper = (p_75) + (1.5 * (iqr))

plt.title("Boxplot of Avocado Price Distribution")
plt.xlabel("Avocado Price")

print("The lower fence is lw:", lower)
print("The uper fence is up:", upper)

plt.show()

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

# 2
pdf.close()

# 3
soi=sold
number_of_classes=int(round(math.log(soi.size)/math.log(2)))
freq,bins,patches=plt.hist(soi,bins=number_of_classes,edgecolor="black")
rel_freq=freq/soi.size
class_range=[]
upper_class=[]
middle_class=[]
for i in range(int(bins.size)-1):
    lower=bins[1]
    upper=bins[i+1]
    upper_class.append(upper)
    middle_class.append((upper+lower)/2)
    class_range.append("{:0.3f}".format(lower)+"-"+"{:0.3f}".format(upper))
cumFreq, trash1, trash2 = plt.hist(soi,bins=number_of_classes,edgecolor="black",cumulative=True)

table = pd.DataFrame({"Number of avocado sold":sold, "Relative frequency": rel_freq, "Cumulative frequency of sold avocados": cumFreq, "Mark of class": middle_class}, index=class_range)

#4
table.to_excel("Quizz_Python_Probability_and_Statistics_FDT.xlsx", float_format="%.3f")

#5
# figure2=plt.figure(figsize=(20,20))
#
#
# sector_counts = data["region"].value_counts()
#
# allplaces=sector_counts[sector_counts>=2000]
#
# less_common=sector_counts[sector_counts<2000]
#
# rare=less_common[less_common<150]
#
# less_common=less_common[less_common>150]
#
# other=pd.Series([less_common.sum()],index=["Less Common places"])
# allplaces=allplaces.append(other)
# vul=pd.Series([rare.sum()],index=["Very Unlikely places"])
# less_common=less_common.append(vul)
# alabels_final=[allplaces.index[i]+" "+"{:0.3f}".format(allplaces[i]/data["region"].size*100)+ "%"for i in range (allplaces.size)]
# alabels_lscommon=[less_common.index[i]+" "+"{:0.3f}".format(less_common[i]/data["region"].size*100)+ "%"for i in range(less_common.size)]
# alabels_vul=[rare.index[i]+" "+"{:0.4f}".format(rare[i]/data["region"].size*100)+ "%"for i in range(rare.size)]
#
# cmap=plt.get_cmap('RdYlBu')
# acolors=[cmap(i) for i in np.linspace(0,1,8)]
# explode_1=np.zeros(allplaces.size)
# for i in range (1,10):
#     explode_1[-i]=2.5-i*0.13
# explode_2=np.zeros(less_common.size)
# for i in range (1,22):
#     explode_2[-i]=3-i*0.13
# explode_3=np.zeros(rare.size)
# explode_3[-1]=4
# explode_3[-2]=2.8
# explode_3[-3]=1.6
# explode_3[-4]=0.4
#
#
# ax2=figure2.add_subplot(3,1,1)
# ax2.set_title("All places",x=-0.2,fontsize=25)
# ax2.pie(allplaces,colors=acolors,
# labels=alabels_final,explode=explode_1,rotatelabels=True)
# ax2=figure2.add_subplot(3,1,2)
# ax2.set_title("Less Common places ",x=1.7,fontsize=25)
# ax2.pie(less_common,colors=acolors,
# labels=alabels_lscommon,explode=explode_2,rotatelabels=True)
# ax2=figure2.add_subplot(3,1,3)
# ax2.set_title("Rare places ",x=1.7,fontsize=25)
# ax2.pie(rare,colors=acolors,
# labels=alabels_vul,explode=explode_3,rotatelabels=True)
# print(rare)
#
# print('The region that sold more avocado was(', allplaces, ') ')
# print('The region that sold more avocado was(',less_common , ') ')

#6

std = np.std(averagePrice)
mean = np.mean(averagePrice)
var = np.var(averagePrice)
med = np.median(averagePrice)

print("The mean price of Avocado is: ",mean)
print("The variance is: ",var)
print("The median price of Avocado is: ",med)
print("The standard deviation of the price of the Avocado is: ",std)

#7

fig_x = plt.figure(figsize=(8, 30))
plt.title('Histogram of Avocado Prize Distribution')

totalbags = data['AveragePrice']
sold = data['Total Bags']
Total_bags = data['Total Bags']
pdf = bkPDF.PdfPages('Quiz_Python_Probability_and_Statistics_Plots.pdf')

# 7.1
number_of_classes = int(round(math.log(totalbags.size) / math.log(2)))
freq, bins, patches = plt.hist(totalbags, bins=number_of_classes, edgecolor="black")

# a.3
print('Number of classes n=', number_of_classes)

# a.4
plt.ylabel('Number of bags sold')
plt.xlabel('Total Bags Sold')
pdf.savefig(fig_x)
plt.show()
plt.close()
print('Yes, it is bell shaped visually')

# a.5
mean = np.mean(totalbags)
std = np.std(totalbags)

print('The n1% of the data lies in the range(', (mean-std), ',', (mean+std), ') according to the Empirical rule')
print('The n2% of the data lies in the range(', (mean-2*std), ',', (mean+2*std), ') according to the Empirical rule')
print('The n3% of the data lies in the range(', (mean-3*std), ',', (mean+3*std), ') according to the Empirical rule')

#b

fig_y = plt.figure(figsize=(8, 30))

#b1

plt.title("Cumulative histogram of total bags distribution")

cumfreq,trash1,trash2=plt.hist(totalbags,bins=number_of_classes,edgecolor="black",cumulative=True)

#b2

plt.ylabel('Cumulative frequency of sold bags')
plt.xlabel('Total bags')
pdf.savefig(fig_y)
plt.show()
plt.close()

#b3

print('\n There are 6 classes, which cumulative frequency is lower than 15000')

figure=plt.figure(figsize=(8,30))
n=7

ax=figure.add_subplot(n,1,1)
ax.boxplot(totalbags,vert=False)
p_25=round(np.percentile(totalbags,25),2)
p_50=round(np.percentile(totalbags,50),2)
p_75=round(np.percentile(totalbags,75),2)
Q1="$Q_{1}=$"+ str(p_25)
plt.text(p_25, 0.85, "$Q_{1}=$"+ str(p_25), fontsize=12)
plt.text(p_50, 0.75, "$Q_{2}=$"+ str(p_50), fontsize=12)
plt.text(p_75, 0.65, "$Q_{3}=$"+ str(p_75), fontsize=12)
plt.title("Boxplot of Total Bags Distribution")
plt.xlabel("Sold BAgs")
plt.show()
plt.close()

#e

middle_class=[]
upper_class=[]
fig_z = plt.figure(figsize=(8,30))

for i in range(int(bins.size)-1):
    lower=bins[1]
    upper=bins[i+1]
    upper_class.append(upper)
    middle_class.append((upper+lower)/2)

R_class=bins[1]-bins[0]
mcfp=middle_class
mcfp.insert(int(len(middle_class)),middle_class[-1]+R_class)
mcfp.insert(0,middle_class[0]-R_class)

ffp=freq.tolist()
ffp.append(0)
ffp.insert(0,0)
plt.plot(mcfp,ffp,"-ro")

# e.1
plt.title('Polygon of frequencies of the total bags distribution')

# e.2
plt.xlabel('Sold Bags')
plt.ylabel('Number of sold bags')
pdf.savefig(fig_z)
plt.show()
plt.close()

# 2
pdf.close()

# 3
soi=sold
number_of_classes=int(round(math.log(soi.size)/math.log(2)))
freq,bins,patches=plt.hist(soi,bins=number_of_classes,edgecolor="black")
rel_freq=freq/soi.size
class_range=[]
upper_class=[]
middle_class=[]
for i in range(int(bins.size)-1):
    lower=bins[1]
    upper=bins[i+1]
    upper_class.append(upper)
    middle_class.append((upper+lower)/2)
    class_range.append("{:0.3f}".format(lower)+"-"+"{:0.3f}".format(upper))
cumFreq, trash1, trash2 = plt.hist(soi,bins=number_of_classes,edgecolor="black",cumulative=True)

table = pd.DataFrame({"Number of bags sold":sold, "Relative frequency": rel_freq, "Cumulative frequency of sold bags": cumFreq, "Mark of class": middle_class}, index=class_range)

#4
table.to_excel("Quizz_Python_Probability_and_Statistics_FDT2.xlsx", float_format="%.3f")

#5




stdt = np.std(Total_bags)
meant = np.mean(Total_bags)
vart = np.var(Total_bags)
medt = np.median(Total_bags)

print("\nThe mean price of Total Bags is: ",meant)
print("The variance is: ",vart)
print("The median price of Total Bags is: ",medt)
print("The standard deviation of the price of the Total Bags is: ",stdt)


