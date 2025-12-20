import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import Crippen
from rdkit import RDLogger

RDLogger.DisableLog('rdApp.*')  # Disabling rdkit warnings
from sklearn.preprocessing import StandardScaler


class Featurizer:
    def __init__(self, smiles_list):
        self.scaler = StandardScaler()
        self.smiles_list = smiles_list
        X_train = self.get_descriptors(smiles_list)
        self.scaler.fit(X_train)

    def get_descriptors(self, smiles_list):
        df = pd.DataFrame({'SMILES': smiles_list})
        df['mol'] = df['SMILES'].apply(Chem.MolFromSmiles)

        df['mol_wt'] = df['mol'].apply(rdMolDescriptors.CalcExactMolWt)
        df['logp'] = df['mol'].apply(Crippen.MolLogP)
        df['num_heavy_atoms'] = df['mol'].apply(rdMolDescriptors.CalcNumHeavyAtoms)
        df['num_HBD'] = df['mol'].apply(rdMolDescriptors.CalcNumHBD)
        df['num_HBA'] = df['mol'].apply(rdMolDescriptors.CalcNumHBA)
        df['aromatic_rings'] = df['mol'].apply(rdMolDescriptors.CalcNumAromaticRings)

        df = df[['mol_wt', 'logp', 'num_heavy_atoms', 'num_HBD', 'num_HBA', 'aromatic_rings']]
        return df

    def featurize(self, smiles_list):
        X = self.get_descriptors(smiles_list)
        X_scaled = self.scaler.transform(X)
        return pd.DataFrame(X_scaled, columns=X.columns)