import csv
import re
import json
import os

SUSPICIOUS_WORDS = [
    "urgent", "verify", "password", "click here", "login",
    "account", "bank", "confirm", "reset", "suspend", "prize",
    "locked", "compromised", "security alert", "identity"
]

def has_link(text):
    return bool(re.search(r"http[s]?://|www\.", text.lower()))

def excessive_caps(text):
    return sum(1 for c in text if c.isupper()) > len(text) * 0.35

def contains_suspicious_words(text):
    text = text.lower()
    return any(word in text for word in SUSPICIOUS_WORDS)

def classify_email(text):
    if contains_suspicious_words(text):
        return "Likely Phishing"
    if has_link(text):
        return "Likely Phishing"
    if excessive_caps(text):
        return "Likely Phishing"
    return "Safe"

# Correct file path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "emails.csv")

emails = []
phishing_count = 0

with open(CSV_PATH, newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        result = classify_email(row["email"])
        emails.append({
            "email": row["email"],
            "result": result
        })
        if result == "Likely Phishing":
            phishing_count += 1

summary = {
    "total_emails": len(emails),
    "phishing_detected": phishing_count,
    "emails": emails
}

with open("results.json", "w") as f:
    json.dump(summary, f, indent=4)

print("Total Emails:", summary["total_emails"])
print("Phishing Detected:", summary["phishing_detected"])

