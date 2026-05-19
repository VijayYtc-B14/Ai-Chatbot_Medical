import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_contact_email(name, email, subject, message):
    """
    Send contact form email.
    
    Args:
        name (str): Sender's name
        email (str): Sender's email
        subject (str): Email subject
        message (str): Email message
        
    Returns:
        tuple: (success: bool, response: str)
    """
    try:
        # You can configure these environment variables
        sender_email = os.getenv("CONTACT_EMAIL", "contact@medicalaiwebsite.com")
        sender_password = os.getenv("EMAIL_PASSWORD", "")
        
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email
        msg['Subject'] = f"New Contact: {subject}"
        
        body = f"""
New Contact Form Submission:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email (requires SMTP configuration)
        # For now, just log the contact
        print(f"Contact received from {name} ({email}): {subject}")
        
        return True, "Thank you! We'll contact you soon."
        
    except Exception as e:
        return False, f"Error sending email: {str(e)}"

def save_contact_to_db(name, email, phone, subject, message):
    """Save contact information to database/file."""
    try:
        contact_data = f"""
Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject}
Message: {message}
---
"""
        # Save to file (can be replaced with database)
        with open("contacts.txt", "a") as f:
            f.write(contact_data)
        return True, "Contact saved successfully!"
    except Exception as e:
        return False, f"Error saving contact: {str(e)}"
