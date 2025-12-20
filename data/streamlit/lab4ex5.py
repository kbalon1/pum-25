import streamlit as st
import pandas as pd
import pickle

st.title('Solubility predictor')
st.write('### This is a model predicting solubility when SMILES provided.')
st.write('Based on SMILES this model counts basic descriptors and predicts solubility of a molecule.')
st.write('Paste one or more SMILES (one per line)')

molecule = st.text_area('Enter **SMILES** of your molecule here')

with open('featurizer.pkl', 'rb') as f:
    featurizer = pickle.load(f)

with open('model.pkl', 'rb') as f:
    svr = pickle.load(f)

smiles_list = [s.strip() for s in molecule.split('\n') if s.strip()]

if st.button('**Predict**'):
    if not molecule:
        st.write(':red[Enter a correct SMILES]')
        st.stop()

    X = featurizer.featurize(smiles_list)
    y_pred = svr.predict(X)

    tab = pd.DataFrame({
        'SMILES': smiles_list,
        'Predicted solubility': y_pred
    })

    st.table(tab)