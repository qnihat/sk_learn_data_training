import pandas as pd
import pickle

with open('angle_model.pkl', 'rb') as f:
    model = pickle.load(f)

angles_by_index=[8,150,92,0,2,37.6,0.191,39]

X = pd.DataFrame([angles_by_index])
body_language_class = model.predict(X)[0]
body_language_prob = model.predict_proba(X)[0]

print(f'class: {body_language_class}, prob: {max(body_language_prob)}')