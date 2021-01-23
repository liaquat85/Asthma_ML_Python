
import pandas as pd

dataset = pd.read_csv('asthma_data.csv')
dataset.shape
data = dataset.sample(frac=0.9, random_state=786)
data_unseen = dataset.drop(data.index)

data.reset_index(drop=True, inplace=True)
data_unseen.reset_index(drop=True, inplace=True)

print('Data for Modeling: ' + str(data.shape))
print('Unseen Data For Predictions: ' + str(data_unseen.shape))
from pycaret.classification import *
exp_mclf101 = setup(data = data, target = 'asthma_severity', session_id=123, normalize = True,polynomial_features = True, trigonometry_features = True, feature_interaction=True)


lr = create_model('lr')
tuned_lr = tune_model(lr)

final_lr = finalize_model(tuned_lr)
unseen_predictions = predict_model(final_lr, data=data_unseen)
unseen_predictions.head()

save_model(final_lr,'Finallrmodel20Jan2021')
saved_final_lr = load_model('Finallrmodel20Jan2021')

data_unseen1 = ['3','M','normal','53','none','mild','wheezing','123']
cols = ['age', 'sex', 'color_of_skin','respiratory_rate','use_of_accessory_muscles','lung_auscultation','brain_function','heart_rate']
df_data_unseen_single = pd.DataFrame([data_unseen1],columns=cols)

new_prediction = predict_model(saved_final_lr, data=df_data_unseen_single, round=0)
print(new_prediction.Label[0])