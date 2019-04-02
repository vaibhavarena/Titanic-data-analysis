import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# READING THE DATA SET #

pd.set_option('display.max_columns', None)
data = pd.read_csv('titanic_data.csv')
print(data.head())


# DISTRIBUTION OF PASSENGERS ON BASIS OF AGE GROUP #

range_age = np.arange(0, max(data['Age'])+1, 10)
### plt.hist(data['Age'], range_age, histtype='bar', rwidth=0.8)
### plt.grid(True, color='#4169E1')
### plt.xlabel('Age Groups', fontweight='bold')
### plt.ylabel('No. of people', fontweight='bold')
### plt.show()


# PIE CHART FOR PROPORTION OF MALES AND FEMALES #

counts_mf = [len(data[data['Sex'] == 'male']), len(data[data['Sex'] == 'female'])]

criteria_male = (data['Sex'] == 'male') & (data['Survived'] == 1)
criteria_female = (data['Sex'] == 'female') & (data['Survived'] == 1)

males_survived = len(data[criteria_male])
females_survived = len(data[criteria_female])

sizes = np.array([counts_mf[0], counts_mf[1]])
size_sur = np.array([males_survived, counts_mf[0]-males_survived, females_survived, counts_mf[1]-females_survived])


#def val_total(val):
#    a = np.round(val/100.*sizes.sum(), 0)
#    return int(a)
#
#
#def val_sur(val):
#    a = np.round((val/100)*size_sur.sum(), 0)
#    return int(a)


### label_mf = ['Males', 'Females']
### label_sur = ['Survived', 'Not Survived', 'Survived', 'Not Survived']
### color = ['#c2c2f0', '#ffb3e6']
### color_sur = ['#3CB371', '#F08080', '#3CB371', '#F08080']
###
### centre_circle = plt.Circle((0, 0), 0.4, color='black', fc='white', linewidth=0)
###
### plt.pie(counts_mf, labels=label_mf, explode=(0.01, 0.01), colors=color, startangle=90, radius=.85)
### plt.legend()
###
###
### plt.pie(size_sur, colors=color_sur, explode=(0.05, 0.01, 0.05, 0.01), startangle=90, radius=0.6)
###
### fig = plt.gcf()
### fig.gca().add_artist(centre_circle)
### plt.axis('equal')
### plt.tight_layout()
### plt.show()


# -->  Try like the above code TRAVELLING CLASS TO SURVIVAL RATE #

class1 = len(data[data['Pclass'] == 1])
class2 = len(data[data['Pclass'] == 2])
class3 = len(data[data['Pclass'] == 3])

c1_sur1 = len(data[(data['Pclass'] == 1) & (data['Survived'] == 1)])
c1_sur2 = len(data[(data['Pclass'] == 2) & (data['Survived'] == 1)])
c1_sur3 = len(data[(data['Pclass'] == 3) & (data['Survived'] == 1)])


# FARE PAID TO AGE TO SURVIVAL RATE #

