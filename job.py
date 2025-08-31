import requests
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Tumhari SerpAPI Key
API_KEY = "b0ddd49c86e2fc0bc165ff1c00065fd5bd499fd8fb79153077a6edfdd47d5f05"

# Tumhara email
SENDER_EMAIL = "malik.umerkhan97@gmail.com"
SENDER_PASS = "zkkg ukhb qcdb mpek"  # Gmail App Password (not normal password)
RECEIVER_EMAIL = "malik.umerkhan97@gmail.com"

def fetch_jobs():
    url = f"https://serpapi.com/search.json?q=Entry+Level+MERN+Stack+Web+Developer+jobs+site:angel.co+OR+site:linkedin.com/jobs&engine=google&api_key={API_KEY}"
    res = requests.get(url).json()

    jobs = []
    for result in res.get("organic_results", []):
        title = result.get("title")
        link = result.get("link")
        jobs.append(f"{title}\n{link}")

    return "\n\n".join(jobs[:10])  # top 10 results

def send_email(body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "Daily MERN Stack Jobs"

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASS)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    server.quit()
    print("✅ Email sent!")

def job_task():
    jobs = fetch_jobs()
    send_email(jobs)

# Roz 1 PM par schedule karo
schedule.every().day.at("13:00").do(job_task)

print("🚀 Job bot started, waiting for 1 PM...")
while True:
    schedule.run_pending()
    time.sleep(60)
