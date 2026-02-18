import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = "harshsingh1676@gmail.com"
APP_PASSWORD = "mftr zypk sqhr vkuz"

# Email setup
msg = MIMEMultipart()
msg["From"] = EMAIL
msg["To"] = "harshsingh1676@outlook.com"
msg["Subject"] = "Testing mail by Python 😎"

body = "Hum kar sakte hai sab kuch 😎🔥 Hindi bhi chalegi!"

# UTF-8 encoding (IMPORTANT)
msg.attach(MIMEText(body, "plain", "utf-8"))

# SMTP login
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, APP_PASSWORD)

receivers = [
    "harshsingh1676@outlook.com",
    "er.harsh2212@gmail.com",
    "235ucm052@gbu.ac.in",
    "harshsingh1676@gmail.com"
]

server.sendmail(EMAIL, receivers, msg.as_string())
server.quit()

print("✅ Mail sent successfully with emoji & Hindi")
