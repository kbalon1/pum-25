import pandas as pd
import pickle
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from Featurizer import Featurizer

df = pd.read_csv(r"C:\Users\kbalo\Documents\Chemia medyczna\V rok\Machine Learning\pum-25\data\aqsol.csv")

# featurizer
featurizer = Featurizer(df['SMILES'])

X = featurizer.featurize(df['SMILES'])
y = df['Solubility']

# model
svr = SVR()
svr.fit(X, y)

# save
with open('featurizer.pkl', 'wb') as f:
    pickle.dump(featurizer, f)

with open('model.pkl', 'wb') as f:
    pickle.dump(svr, f)