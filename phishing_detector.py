import csv
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. TRAINING DATA (The "Brain" of your AI)
# These examples teach the AI what is Safe vs. Phishing
training_emails = [
    "Your account is locked, click here to reset now!",
    "Urgent: Unauthorised login detected. Verify identity.",
    "Hey, are we still meeting for lunch at 12?",
    "Attached is the project report for Q3 review.",
    "WINNER! You won a $1000 gift card, claim now!",
    "Can you send me the notes from today's class?"
]
# 1 = Phishing, 0 = Safe
labels = [1, 1, 0, 0, 1, 0]

# 2. INITIALIZE AI TOOLS
# We must 'fit' the vectorizer to our training data first
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_emails)
model = MultinomialNB()
model.fit(X_train, labels)


def analyze_and_log(email_text):
    """
    Main function to analyze emails and save results for Power BI.
    Uses 'try-except' for professional error handling.
    """
    try:
        # Step A: Transform the new email into numbers the AI understands
        email_vector = vectorizer.transform([email_text])

        # Step B: Make a prediction (1 or 0)
        prediction = model.predict(email_vector)[0]

        # Step C: Log result to CSV for your Portfolio Dashboard
        log_to_csv(email_text, prediction)

        return "⚠️ PHISHING" if prediction == 1 else "✅ SAFE"

    except Exception as e:
        return f"Error: {e}"


def log_to_csv(text, result):
    """Saves the data using a simple, clear list variable."""
    file_path = 'security_logs.csv'
    file_exists = os.path.isfile(file_path)

    try:
        with open(file_path, 'a', newline='') as f:
            writer = csv.writer(f)

            # Write header if file is new
            if not file_exists:
                header = ["Email_Text", "Label"]
                writer.writerow(header)

            # THE ALTERNATIVE: Create the row first
            # This avoids the syntax error you were seeing
            clean_text = text[:40]
            row_to_save = [clean_text, result]

            # Now save the row variable
            writer.writerow(row_to_save)

    except Exception as e:
        print(f"Logging Error: {e}")

# 3. TEST THE SYSTEM
# Run these to generate data for your CSV file!
print(f"Test 1: {analyze_and_log('Meeting rescheduled to tomorrow morning.')}")
print(f"Test 2: {analyze_and_log('Verify your account to avoid suspension now!')}")
