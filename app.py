from flask import Flask, render_template, request, send_file
import pandas as pd
import imapclient
import pyzmail
import pickle
import os

app = Flask(__name__)

# === Load trained model and vectorizer ===
with open('model/model.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

# === Function to fetch and classify emails ===
def fetch_and_classify_emails(email, password):
    with imapclient.IMAPClient('imap.gmail.com') as client:
        client.login(email, password)
        client.select_folder('INBOX', readonly=True)

        UIDs = client.search(['UNSEEN'])[:250]
        results = []

        for uid in UIDs:
            raw_message = client.fetch([uid], ['BODY[]'])
            message = pyzmail.PyzMessage.factory(raw_message[uid][b'BODY[]'])

            subject = message.get_subject() or ""
            if message.text_part:
                body = message.text_part.get_payload().decode(message.text_part.charset or 'utf-8', errors='ignore')
            elif message.html_part:
                body = message.html_part.get_payload().decode(message.html_part.charset or 'utf-8', errors='ignore')
            else:
                body = ""

            full_text = subject + " " + body
            vect_text = vectorizer.transform([full_text])

            probs = model.predict_proba(vect_text)[0]
            max_prob = max(probs)
            predicted = model.classes_[probs.argmax()]

            if max_prob < 0.6:
                predicted = "Unknown"

            results.append({
                "UID": uid,
                "Subject": subject,
                "Category": predicted,
                "Confidence": round(max_prob, 2)
            })

        return results

# === Home route ===
@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error = None

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            results = fetch_and_classify_emails(email, password)
            df = pd.DataFrame(results)
            df.to_csv("classified_emails.csv", index=False)
        except Exception as e:
            error = str(e)

    return render_template('index.html', results=results, error=error)

# === CSV download route ===
@app.route('/download')
def download_csv():
    path = "classified_emails.csv"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "CSV file not found", 404

# === Run the server ===
if __name__ == '__main__':
    app.run(debug=True)
