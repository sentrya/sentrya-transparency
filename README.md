# Sentrya Transparency Repo

This repository provides a transparent look at how Sentrya(https://sentrya.net) handles user registration, password security, and automated data deletion requests. The mission is to help users take back control of their personal data — without compromising their privacy or trust.

---

## User Registration (Security + Data Collected)

The app collects **minimal personal information** when a user signs up:

| Field           | Purpose                             | Optional? |
|----------------|--------------------------------------|-----------|
| First Name     | Display in dashboard                 | No        |
| Last Name      | Display in dashboard                 | No        |
| Email          | Account ID / communication           | No        |
| Password       | Hashed & salted via PBKDF2           | No        |
| Promo Code     | For discounts                        | Yes       |
| Google Token   | Connection                           | No        |

Passwords are not stored in plaintext. Here’s the hashing logic used:

```python
hashed_password = generate_password_hash(
    register_form.password.data,
    method="pbkdf2:sha256",
    salt_length=12
)
```

📮 Data Deletion Requests (GDPR/CCPA)
Sentrya allows users to automatically send GDPR/CCPA data deletion requests to companies and data brokers via email. These requests are sent from the user's Gmail account using their explicit consent and OAuth.

The only personal information included is:

Full name

Email address

Here’s a sample of the message body used:

Dear Data Protection Officer,
I am writing to request the deletion of my personal information from your database under the General Data Protection Regulation (GDPR) and California Consumer Privacy Act (CCPA).
...
Powered by Sentrya.net

📝 See send_deletion_request.py for the code that constructs and sends this email.


🔎 Why I Made This Repo
I believe transparency is essential for privacy tools. While Sentrya is not fully open source, this repository gives users and privacy advocates a clear view of the data collected, how it is protected, and how I help you fight data misuse.


🔗 Learn More
Visit sentrya.net to explore the full app or try sending your first data deletion request.
