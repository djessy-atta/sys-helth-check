import os
import smtplib
import mimetypes
import email.message

def generate_email(sender, recipient, subject="", body="", attachment_path=""):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Add attachment if she exist
  if attachment_path:
    # Process the attachment and add it to the email
    attachment_file = Path(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_file.name)

  return message

def send_email(message):
  """Sends the message to the configured SMTP server."""
  #mail_server = smtplib.SMTP('localhost')
  mail_server = smtplib.SMTP('smtp.live.com', 587)
  mail_server.starttls()
  mail_server.login('djessyatta@live.fr', 'AlphaMito2009')
  mail_server.send_message(message)
  mail_server.quit()
