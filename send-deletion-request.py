def send_deletion_request(user_full_name, user_email, company_email, service, company_name):
    email_body = (f"Dear Data Protection Officer,\n\n"
                  f"I am writing to request the deletion of my personal information from your database "
                  f"({company_name}), under the General Data Protection Regulation (GDPR) and California Consumer "
                  f"Privacy Act (CCPA).\n\n"
                  f"I include the following information in order to confirm my identity:\n"
                  f"Full name: {user_full_name}\n"
                  f"Email: {user_email}\n\n"
                  f"Please confirm once all my information has been removed from your systems.\n\n"
                  f"If you are not the person responsible for handling these requests, please pass this email to "
                  f"your relevant department.\n\n\n"
                  f"Thank you, and I look forward to hearing from you.\n\n"
                  f"{user_full_name}\n\n\n\n"
                  f"Powered by Sentrya.net")

    message_content = (
        "From: {}\n"
        "To: {}\n"
        "Subject: Data deletion request\n\n"
        "{}".format(user_full_name, company_email, email_body)
    )
    encoded_message = base64.urlsafe_b64encode(message_content.encode()).decode()

    message = {
        "raw": encoded_message
    }
    service.users().messages().send(userId=user_email, body=message).execute()
