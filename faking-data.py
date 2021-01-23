from faker import Faker
from datetime import datetime
import random
import pandas as pd
fake = Faker()
# Asthma types = Mild, Moderate, Severe 

def data_random():
	d=dict()
	d['age'] = lambda: random.randint(1,85)
	d['sex'] = lambda: 'M' if random.randint(0,1) == 0 else 'F'
	d['color_of_skin'] = lambda: random.choice(['normal', 'pale','cyanotic'])
	d['respiratory_rate'] = lambda: random.randint(20,60)
	
	d['respiratory_rate'] = lambda: random.randint(20,60)
	d['use_of_accessory_muscles'] = lambda: random.choice(['none','mild','intense'])
	d['lung_auscultation'] = lambda: random.choice(['wheezing_end_expiration','wheezing_inspiratory_expiration','wheezing_loud'])
	d['brain_function'] = lambda: random.choice(['Normal','Depressed','Comatose'])
	d['heart_rate'] = lambda: random.randint(110,165)
	d['asthma_severity'] = lambda: random.choice(['Mild','Moderate','Severe'])
	data = []
	for _ in range(10):
		r=[d[k]() for k in d.keys()]
		data.append(r)
		#print(r)
	return data
		

def data_catogerize(agemin, agemax,color_of_skin,respiratory_ratemin\
	,respiratory_ratemax,use_of_accessory_muscles,lung_auscultation,\
	brain_function,heart_ratemin, heart_ratemax,asthma_severity):
	d = dict()
	d['age'] = lambda: random.randint(agemin,agemax)
	d['sex'] = lambda: 'M' if random.randint(0,1) == 0 else 'F'
	d['color_of_skin'] = lambda: random.choice([color_of_skin])
	d['respiratory_rate'] = lambda: random.randint(respiratory_ratemin,respiratory_ratemax)
	d['use_of_accessory_muscles'] = lambda: random.choice([use_of_accessory_muscles])
	d['lung_auscultation'] = lambda: random.choice([lung_auscultation])
	d['brain_function'] = lambda: random.choice([brain_function])
	d['heart_rate'] = lambda: random.randint(heart_ratemin, heart_ratemax)
	d['asthma_severity'] = lambda: random.choice([asthma_severity])
	data = []
	for _ in range(50):
		r=[d[k]() for k in d.keys()]
		data.append(r)
		#print(r)
	return data
	


data = []
#Age 1-2 - Mild
data = data + data_catogerize(1, 2,'normal',25,30,'none','wheezing_end_expiration','Normal',110,160,'Mild')
#random data
data = data + data_random()
#Age 2-5 - Severe
data = data + data_catogerize(2, 5,'cyanotic',50,90,'intense','wheezing_loud','Comatose',160,175,'Severe')
#random data
data = data + data_random()
#Age 2-5 Mild
data = data + data_catogerize(2, 5,'normal',20,25,'none','wheezing_end_expiration','Normal',110,140,'Mild')
#random data
data = data + data_random()
#Age 5-90 - Moderate
data = data + data_catogerize(5, 90,'pale',21,40,'mild','wheezing_inspiratory_expiration','Depressed',111,130,'Moderate')
#random data
data = data + data_random()
#Age 5-90 - Severe
data = data + data_catogerize(5, 90,'cyanotic',40,60,'intense','wheezing_loud','Comatose',130,175,'Severe')
#random data
data = data + data_random()
#Age 1-2 - Moderate
data = data + data_catogerize(1, 2,'pale',31,60,'mild','wheezing_inspiratory_expiration','Depressed',160,165,'Moderate')
#random data
data = data + data_random()
#Age 5-90 - Mild
data = data + data_catogerize(5, 90,'normal',15,20,'none','wheezing_end_expiration','Normal',90,110,'Mild')
#random data
data = data + data_random()
#Age 2-5 - Moderate
data = data + data_catogerize(2, 5,'pale',26,50,'mild','wheezing_inspiratory_expiration','Depressed',140,160,'Moderate')
#random data
data = data + data_random()
#Age 1-2 - Severe
data = data + data_catogerize(1, 2,'cyanotic',60,90,'intense','wheezing_loud','Comatose',165,175,'Severe')



cols = ['age', 'sex', 'color_of_skin','respiratory_rate','use_of_accessory_muscles','lung_auscultation','brain_function','heart_rate','asthma_severity']
df = pd.DataFrame(data,columns=cols)
df.to_csv('asthma_data.csv',index=False)
print(df.head())


# d['age'] = lambda: random.randint(1,2)
#d['sex'] = lambda: 'M' if random.randint(0,1) == 0 else 'F'
# d['color_of_skin'] = lambda: random.choice(['Normal'])
# d['respiratory_rate'] = lambda: random.randint(25,30)
# d['use_of_accessory_muscles'] = lambda: random.choice(['None'])
# d['lung_auscultation'] = lambda: random.choice(['wheezing_end_expiration'])
# d['brain_function'] = lambda: random.choice(['Normal'])
# d['heart_rate'] = lambda: random.randint(110,160)
# d['asthma_severity'] = lambda: random.choice(['Mild'])


# #Age 1-2 - Moderate
# d['age'] = lambda: random.randint(1,2)
# d['sex'] = lambda: 'M' if random.randint(0,1) == 0 else 'F'
# d['color_of_skin'] = lambda: random.choice(['Pale'])
# d['respiratory_rate'] = lambda: random.randint(31,60)
# d['use_of_accessory_muscles'] = lambda: random.choice(['Mild'])
# d['lung_auscultation'] = lambda: random.choice(['wheezing_inspiratory_expiratory'])
# d['brain_function'] = lambda: random.choice(['Depressed'])
# d['heart_rate'] = lambda: random.randint(160,165)
# d['asthma_severity'] = lambda: random.choice(['Moderate'])

# data = data + data_generation(d)

# #Age 1-2 - Severe
# d['age'] = lambda: random.randint(1,2)
# d['sex'] = lambda: 'M' if random.randint(0,1) == 0 else 'F'
# d['color_of_skin'] = lambda: random.choice(['cyanotic'])
# d['respiratory_rate'] = lambda: random.randint(60,90)
# d['use_of_accessory_muscles'] = lambda: random.choice(['intense'])
# d['lung_auscultation'] = lambda: random.choice(['wheezing_loud'])
# d['brain_function'] = lambda: random.choice(['Comatose'])
# d['heart_rate'] = lambda: random.randint(165,180)
# d['asthma_severity'] = lambda: random.choice(['Severe'])

# data = data + data_generation(d)



#columns that use faker



#d['birth_date'] = lambda: fake.date_between_dates(date_start=datetime(1960, 1, 1), date_end=datetime(2000, 1, 1))
#d['start_date'] = lambda: fake.date_between_dates(date_start=datetime(1995, 1, 1), date_end=datetime(2019, 1, 1))
#d['office'] = lambda: fake.city()
#d['title'] = lambda: fake.job()
#columns that do not use faker
#d['gender'] = lambda: 'M' if random.randint(0,1) == 0 else 'F'
#d['org'] = lambda: random.choice(['Engineer','Sales','Associate','Manager','VP'])
#d['accrued_holidays'] = lambda: random.randint(0,20)
#d['salary'] = lambda: round(random.randint(90000,120000)/1000)*1000
#d['bonus'] = lambda: round(random.randint(0,5000)/500)*500
# data = []
# for _ in range(1000):
#    r=[d[k]() for k in d.keys()]
#    data.append(r)
#    print(r)
# cols = ['age', 'sex', 'respiratory_rate','heart_rate','peak_flow_meter','FEV','FCV','O2_saturation','use_of_accessory_muscles','lung auscultation','brain_function','asthma_severity']
# df = pd.DataFrame(data,columns=cols)
# df.to_csv('asthma_data.csv',index=False)
# print(df.head())