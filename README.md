
# 🛡️ Message Fraud Detection System

The **Message Fraud Detection System** is an AI-powered project built to identify fraudulent or spam messages from legitimate ones using machine learning and natural language processing (NLP). This tool processes user-input messages and accurately classifies them as **Spam** or **Ham (Not Spam)**. It's ideal for SMS filtering, email spam detection, and similar use cases.


---

## 🚀 Features

- 🔍 Real-time message spam detection
- 📊 Text preprocessing with NLP (tokenization, stemming, stopword removal)
- 📁 SMS Spam Collection dataset used for model training
- 🧠 ML model trained using Naive Bayes / SVM
- 🎯 High accuracy with performance metrics
- 📈 Confusion matrix, classification report & visualizations

---

## 🧰 Technologies Used

- **Programming Language:** Python
- **Libraries & Tools:**
  - `pandas` – data handling
  - `numpy` – numerical computations
  - `scikit-learn` – ML algorithms & vectorization
  - `nltk` – text preprocessing
  - `matplotlib` & `seaborn` – data visualization
- **Model Used:** Multinomial Naive Bayes (or equivalent classifier)
- **Dataset:** [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

---

## 📦 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/ZahedShaikh08/Message-Fraud-Detection-System.git
   cd Message-Fraud-Detection-System
   ```

2. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**
   ```bash
   python main.py
   ```

> Make sure you have Python 3.7+ installed.

---

## 🧪 How It Works

1. **Data Preprocessing**
   - Convert text to lowercase
   - Remove stopwords and punctuation
   - Apply stemming
   - Vectorize text using TF-IDF or CountVectorizer

2. **Model Training**
   - Train on labeled dataset with "spam" and "ham"
   - Fit the model using classification algorithms (e.g., Naive Bayes)

3. **Prediction**
   - Input a new message
   - Model outputs `Spam` or `Ham`

4. **Evaluation**
   - Use accuracy, precision, recall, F1-score
   - Confusion matrix for visual metrics

---

## 📷 Screenshots

![Screenshot (81)](https://github.com/user-attachments/assets/c1f8f50a-a906-4f1d-ae82-8c6688ab56c0)

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute.

---

## 🙋‍♂️ Author

**Zahed Shaikh**  
🔗 [GitHub](https://github.com/ZahedShaikh08)  
🔗 [LinkedIn](https://linkedin.com/in/zahedshaikh08)
