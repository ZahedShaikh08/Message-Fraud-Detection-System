import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ─── 1) DATA ───────────────────────────────────────────────────────────────────────
messages = [
    "Congratulations! You've won a lottery of $1000.",
    "Hello, how are you?",
    "Claim your free gift card now!",
    "Meeting at 10 AM tomorrow in the office.",
    "Urgent! Update your account details to avoid suspension.",
    "Lunch at 1 PM?"
]
labels = [1, 0, 1, 0, 1, 0]   # 1 = Fraudulent, 0 = Non‑Fraudulent

# ─── 2) PIPELINE ───────────────────────────────────────────────────────────────────
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb',   MultinomialNB())
])

# Train the pipeline
pipeline.fit(messages, labels)

# Save the entire pipeline
joblib.dump(pipeline, 'fraud_pipeline.joblib')
print("✅ Saved pipeline as fraud_pipeline.joblib")


# ─── 3) OPTIONAL: standalone CountVectorizer ──────────────────────────────────────
# If you need to use a separate vectorizer (e.g. for custom pre‑ or post‑processing),
# you can fit and save it too:
vectorizer = CountVectorizer()
vectorizer.fit(messages)
joblib.dump(vectorizer, 'vectorizer.joblib')
print("✅ Saved standalone vectorizer as vectorizer.joblib")
