# Rule-Based Phishing Email Detection System

## Overview
This project implements a simple rule-based phishing email detection system using Python. The system analyzes email messages and classifies them as **Likely Phishing** or **Safe** based on predefined rules.

## Detection Rules
1. Presence of suspicious keywords such as:
   - urgent, verify, password, click here, login, reset
2. Presence of links (http, https, www)
3. Excessive use of capital letters

If two or more rules are triggered, the email is flagged as phishing.

## Limitation
This system relies on fixed rules and keywords, so it may fail to detect new phishing styles or generate false positives for legitimate urgent emails.

## Future Improvement (Using ML)
A machine learning model trained on real-world phishing datasets could learn contextual patterns and improve detection accuracy and adaptability.

## How to Run
```bash
python src/detector.py
```


