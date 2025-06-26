# Email-Classification
# Email Classification Web App using Flask & Machine Learning

This project is a web-based Gmail email classifier built with **Flask**, using a trained **machine learning model (Naive Bayes)** and **TF-IDF vectorizer**. It fetches **unread emails** from your Gmail inbox using **IMAP**, classifies them into categories like **Spam**, **Promotions**, or **Personal**, and allows you to download the results as a **CSV**.

---

## Features

- Secure Gmail login using App Password
- Fetches unread emails from your inbox
- Classifies emails using a pre-trained ML model
- Displays results with category and confidence score
- Exports classified results as a downloadable CSV
- Runs as a local web app using Flask

---

## Folder Structure

email_classifier_web/
├── app.py # Flask backend application
├── train_model.py # Training script to create model.pkl
├── model/
│ └── model.pkl # Trained TF-IDF vectorizer + Naive Bayes model
├── templates/
│ └── index.html # HTML frontend with Gmail form and results
├── classified_emails.csv # Output CSV generated after classification
└── README.md # Project documentation


---

## Technologies Used

- Python 3
- Flask
- IMAPClient
- Pyzmail36
- Scikit-learn (TF-IDF + Naive Bayes)
- Pandas
- HTML/CSS

---

## Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/email-classifier-web.git
cd email-classifier-web
2. Install required libraries
pip install flask imapclient pyzmail36 pandas scikit-learn
3. Generate Gmail App Password
Visit Google Account Security
Enable 2-Step Verification
Go to App passwords
Generate a password for Mail → Windows Computer
Use this 16-character password in the web form
4. Train the Model (if not already)
python train_model.py
This creates model/model.pkl using your local dataset.
5. Run the Flask App in cmd
python app.py
Open in your browser:
http://127.0.0.1:5000
Sample Dataset (Optional)
You can use any labeled dataset with the following columns:
Subject
Body
Category
Place it inside a /data/ folder if needed during training.

## Developed By
Amar H M 
B.Tech Student 
Department of Artificial Intelligence & Machine Learning
Dayananda Sagar University
Department of Artificial Intelligence & Machine Learning

## Disclaimer
This app is for educational use only. Your Gmail credentials are used only for session access and are never stored. Always use Gmail App Passwords, not your main account password.

## Future Improvements
Host app online using Render or Railway
Add email content preview
Improve UI with dark mode
Add user login and dashboard
Train on larger, more diverse email datasets

## License
This project is licensed under the MIT License. Free to use for academic and personal projects.

**I would like to express my heartfelt gratitude to Prof. Pradeep Kumar for his valuable guidance, encouragement, and continuous supervision throughout the development of this project. His insights and support played a vital role in shaping this work into a successful academic achievement.**


--- THE END ---
