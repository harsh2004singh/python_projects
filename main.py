import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = "XYZ@gmail.com"
APP_PASSWORD = "mftr zypk sqhr vkuz"

# Email setup
msg = MIMEMultipart()
msg["From"] = EMAIL
msg["To"] = "XYZoutlook.com"
msg["Subject"] = "Testing mail by Python 😎"

body = "Hum kar sakte hai sab kuch 😎🔥 Hindi bhi chalegi!"

# UTF-8 encoding (IMPORTANT)
msg.attach(MIMEText(body, "plain", "utf-8"))

# SMTP login
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, APP_PASSWORD)

receivers = [
    "XYZ@outlook.com",
    "2212@gmail.com",
    "2052@gbu.ac.in",
    "ha@gmail.com"
]

server.sendmail(EMAIL, receivers, msg.as_string())
server.quit()

print("✅ Mail sent successfully with emoji & Hindi")

