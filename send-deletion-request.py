import base64

def send_deletion_request(user_full_name: str, user_email: str, company_email: str, service, company_name: str):
    """
    Sends a data deletion request email on behalf of the user to the target company.
    
    Parameters:
        user_full_name (str): Full name of the user requesting deletion
        user_email (str): User's email address (used as sender)
        company_email (str): Recipient company’s data protection contact
        service: An authenticated Gmail API service object
        company_name (str): Name of the target company/service
    """
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

    # Compose the full email message
    message_content = (
        "From: {}\n"
        "To: {}\n"
        "Subject: Data deletion request\n\n"
        "{}".format(user_full_name, company_email, email_body)
    )
    # Encode the message in base64 (required by Gmail API)
    encoded_message = base64.urlsafe_b64encode(message_content.encode()).decode()

    # Send via Gmail API
    message = {
        "raw": encoded_message
    }
    service.users().messages().send(userId=user_email, body=message).execute()
