# youtube-sentiment-analysis
Machine learning–powered YouTube comment sentiment analysis system using Streamlit

📌 **Project Overview**

This project is a Natural Language Processing (NLP) based web application that analyzes YouTube comments and classifies them into three sentiment categories:

✅ Positive 😠 Negative 😐 Neutral

The model extracts real-time user comments from YouTube, processes text, trains a machine learning classifier, and provides predictions through an interactive web interface deployed on Hugging Face Spaces.

🎯 **Objective**

To develop a scalable sentiment analysis system that helps decode public opinion on YouTube content across domains such as:

Emotional storytelling

Service-related discussions

Tech reviews, vlogs and gaming

🛠 **Tech Stack**

Python
pandas, NumPy
scikit-learn
Word2Vec (Text Embeddings)
Logistic Regression
Streamlit
YouTube Data API
Hugging Face Spaces (Deployment)

⚙️ **ML Pipeline**

The project follows a complete NLP workflow:

Extract comments using YouTube Data API

Clean and preprocess text

Generate semantic embeddings using Word2Vec

Train Logistic Regression classifier

Evaluate model performance

Deploy the model using Streamlit

Host application on Hugging Face Spaces

🔍 **Key Features**

Real-time sentiment detection

Multi-domain support

Clean and interactive UI

Scalable and modular design

Fully deployed end-to-end system

📊 **Dataset**

Over 15,000 YouTube comments were collected and used for training and evaluation.

🌐 Live Demo

Try the application below:

🔗 https://lnkd.in/g_ta_S4A

📁 Project Structure
youtube-sentiment-analysis/
│── app.py

│── youtube_sentiment.ipynb

│── youtube_comments.csv

│── requirements.txt

│── README.md

▶ How to Run Locally

Clone the repository:

git clone <repository_url>
cd youtube-comment-sentiment-analysis


Install dependencies:

pip install -r requirements.txt


Run the web application:

streamlit run app.py

🚀 **Future Enhancements**

Integrate deep learning models (LSTM / Transformers)

Add multilingual support

Implement sentiment trend analysis

Enhance frontend visuals

Deploy on cloud platforms

👤 **Author**

Srikanth Gunti
📧 Email: srikanthgunti11@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/srikanth-gunti-

⭐ Support

If you found this project useful, feel free to ⭐ star the repository!
