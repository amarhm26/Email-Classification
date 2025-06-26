import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# === Load your dataset ===
df = pd.read_csv(r"C:\Users\amarh\OneDrive\Desktop\My College\Projects\e-mail\Data sets\email_classification_dataset_1M.csv")
df = df.dropna(subset=['Subject', 'Body', 'Category'])

df["text"] = df["Subject"] + " " + df["Body"]

X = df["text"]
y = df["Category"]

vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vect = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vect, y)

os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Model trained and saved as 'model/model.pkl'")
