"""Quick script to test SMTP connection and sending"""
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv(override=True)

smtp_server = os.environ.get("SMTP_SERVER", "").strip()
smtp_port_raw = os.environ.get("SMTP_PORT")
try:
    smtp_port = int(smtp_port_raw) if smtp_port_raw else 587
except (ValueError, TypeError):
    print(f"WARNING: Invalid SMTP_PORT value '{smtp_port_raw}', falling back to 587")
    smtp_port = 587
smtp_username = os.environ.get("SMTP_USERNAME", "").strip()
smtp_password = os.environ.get("SMTP_PASSWORD", "").strip()

print(f"SMTP_SERVER: [{smtp_server}]")
print(f"SMTP_PORT: [{smtp_port}]")
print(f"SMTP_USERNAME: [{smtp_username}]")
if not smtp_password:
    print("SMTP_PASSWORD: [EMPTY]")
elif len(smtp_password) <= 3:
    print("SMTP_PASSWORD: [***]")
else:
    print(f"SMTP_PASSWORD: [{smtp_password[:3]}***]")

to_email = smtp_username

msg = EmailMessage()
msg['Subject'] = 'Test OTP Email from ERP'
msg['From'] = smtp_username
msg['To'] = to_email
msg.set_content("Hello, this is a test email from your ERP system. OTP: 123456")

try:
    print(f"\nConnecting to {smtp_server}:{smtp_port}...")
    with smtplib.SMTP(smtp_server, smtp_port, timeout=15) as server:
        server.set_debuglevel(1)
        server.ehlo()
        print("EHLO done")
        server.starttls()
        print("STARTTLS done")
        server.ehlo()
        print("Second EHLO done")
        server.login(smtp_username, smtp_password)
        print("LOGIN done")
        server.send_message(msg)
        print("\nEMAIL SENT SUCCESSFULLY!")
except Exception as e:
    print(f"\nFAILED: {type(e).__name__}: {e}")
