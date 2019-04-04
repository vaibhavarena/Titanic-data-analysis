import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# READING THE DATA SET #

pd.set_option('display.max_columns', None)
data = pd.read_csv('titanic_data.csv')
print(data.head())


counts_mf = [len(data[data['Sex'] == 'male']), len(data[data['Sex'] == 'female'])]

criteria_male = (data['Sex'] == 'male') & (data['Survived'] == 1)
criteria_female = (data['Sex'] == 'female') & (data['Survived'] == 1)
criteria_male_n = (data['Sex'] == 'male') & (data['Survived'] == 0)
criteria_female_n = (data['Sex'] == 'female') & (data['Survived'] == 0)
criteria_total = (criteria_male | criteria_female)
criteria_total_n = (criteria_male_n | criteria_female_n)

males_survived = len(data[criteria_male])
females_survived = len(data[criteria_female])

sizes = np.array([counts_mf[0], counts_mf[1]])
size_sur = np.array([males_survived, counts_mf[0]-males_survived, females_survived, counts_mf[1]-females_survived])

survived_patch = mpatches.Patch(color='#3CB371', label='Survived')
n_survived_patch = mpatches.Patch(color='#F08080', label='Not Survived')

missing_age = data[data['Age'].isnull()]['PassengerId']


# DISTRIBUTION OF PASSENGERS ON BASIS OF AGE GROUP #

range_age = np.arange(0, max(data['Age'])+1, 10)
plt.hist(data['Age'], range_age, histtype='bar', rwidth=0.5, alpha=0.5, color='#F08080', label='Total')
plt.hist(data[criteria_total]['Age'], range_age, histtype='bar', rwidth=0.5, alpha=0.7, label='Survived')
plt.legend()
plt.grid(True, color='#4169E1')
plt.xlabel('Age Groups', fontweight='bold')
plt.ylabel('No. of people', fontweight='bold')
plt.show()

survived_age = []
for i in range_age[:-1]:
    a = data[(data['Age'] > i) & (data['Age'] <= (i+10)) & (data['Survived'] == 1)]
    survived_age.append(len(a['Survived']))


# PIE CHART FOR PROPORTION OF MALES AND FEMALES #


label_mf = ['Males', 'Females']
label_sur = ['Survived', 'Not Survived', 'Survived', 'Not Survived']
color = ['#c2c2f0', '#ffb3e6']
color_sur = ['#3CB371', '#F08080', '#3CB371', '#F08080']

centre_circle = plt.Circle((0, 0), 0.4, color='black', fc='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.pie(counts_mf, labels=label_mf,  colors=color, startangle=90, radius=.85)

plt.pie(size_sur, colors=color_sur, explode=(0.02, 0., 0.02, 0), startangle=90, radius=0.65)
plt.legend(handles=[survived_patch, n_survived_patch])


plt.axis('equal')
plt.tight_layout()
plt.show()


# -->  Try like the above code TRAVELLING CLASS TO SURVIVAL RATE #

class1 = len(data[data['Pclass'] == 1])
class2 = len(data[data['Pclass'] == 2])
class3 = len(data[data['Pclass'] == 3])
c1_sur1 = len(data[(data['Pclass'] == 1) & (data['Survived'] == 1)])
c1_sur2 = len(data[(data['Pclass'] == 2) & (data['Survived'] == 1)])
c1_sur3 = len(data[(data['Pclass'] == 3) & (data['Survived'] == 1)])
c1_sur1_n = len(data[(data['Pclass'] == 1) & (data['Survived'] == 0)])
c1_sur2_n = len(data[(data['Pclass'] == 2) & (data['Survived'] == 0)])
c1_sur3_n = len(data[(data['Pclass'] == 3) & (data['Survived'] == 0)])

labels_sur_class = ['Survived', 'Not Survived']
fig1 = plt.figure(figsize=(13, 5))
ax_1 = fig1.add_subplot(131)
ax_1.pie([c1_sur1, c1_sur1_n], colors=['#3CB371', '#F08080'], radius=1.2)
ax_1.set_title('Class 1')
ax_2 = fig1.add_subplot(132)
ax_2.pie([c1_sur2, c1_sur2_n], colors=['#3CB371', '#F08080'], radius=1.2)
ax_2.set_title('Class 2')
ax_3 = fig1.add_subplot(133)
ax_3.pie([c1_sur3, c1_sur3_n], colors=['#3CB371', '#F08080'], radius=1.2)
ax_3.set_title('Class 3')
fig1.legend(labels_sur_class, loc='lower center')
fig1.show()


# FARE PAID TO AGE TO SURVIVAL RATE #

s_patch = mpatches.Patch(color='#006400', label='Survived', alpha=0.5)
n_patch = mpatches.Patch(color='#DC143C', label='Not Survived', alpha=0.5)
fig = plt.figure(figsize=(15, 7))

ax1 = fig.add_subplot(122)
ax1.scatter(data[criteria_total]['Fare'], data[criteria_total]['Age'], color='#006400', s=5, alpha=0.5)
ax1.legend(handles=[s_patch])
ax1.set_xlabel('Fare ->', fontweight='bold')
ax1.set_ylabel('Age ->', fontweight='bold')

ax2 = fig.add_subplot(121, sharex=ax1, sharey=ax1)
ax2.scatter(data[criteria_total_n]['Fare'], data[criteria_total_n]['Age'], color='#DC143C', s=5, alpha=0.5)
ax2.legend(handles=[n_patch])
ax2.set_xlabel('Fare ->', fontweight='bold')#
ax2.set_ylabel('Age ->', fontweight='bold')
plt.show()
