"""
Beginner Streamlit demo for class capstones.
Run:  streamlit run Deploy/app.py
"""
from pathlib import Path

import joblib
import numpy as np
import streamlit as st
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="ML Capstone Demo", layout="centered")
st.title("ML Capstone Demo")
st.write("Beginner template — replace with your capstone features and model.")

ART = Path(__file__).resolve().parent / "artifacts"
ART.mkdir(exist_ok=True)
MODEL_PATH = ART / "demo_rf.joblib"


@st.cache_resource
def load_or_train_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH), load_breast_cancer()

    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42, stratify=data.target
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    return model, data


model, data = load_or_train_model()

st.subheader("Enter a few features (demo uses first 5)")
values = []
for i, name in enumerate(data.feature_names[:5]):
    col_min = float(np.min(data.data[:, i]))
    col_max = float(np.max(data.data[:, i]))
    col_mean = float(np.mean(data.data[:, i]))
    values.append(st.slider(name, col_min, col_max, col_mean))

# pad remaining features with training means for this simple demo
full = data.data.mean(axis=0).copy()
full[:5] = np.array(values)

if st.button("Predict"):
    pred = int(model.predict(full.reshape(1, -1))[0])
    proba = model.predict_proba(full.reshape(1, -1))[0]
    label = data.target_names[pred]
    st.success(f"Prediction: **{label}**")
    st.write({data.target_names[i]: round(float(proba[i]), 3) for i in range(len(proba))})

st.caption("Replace this demo with your capstone pipeline + real input form.")
