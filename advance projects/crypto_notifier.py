import requests
import time
import smtplib
from email.message import EmailMessage

COINS = {
    "1": "bitcoin",
    "2": "ethereum",
    "3": "dogecoin"
}

def get_price(coin):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[coin]['usd']

def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

def main():
    print("Select a coin:")
    for key, coin in COINS.items():
        print(f"{key}. {coin.title()}")

    choice = input("Enter choice: ").strip()
    if choice not in COINS:
        print("Invalid choice.")
        return

    coin = COINS[choice]
    initial_price = get_price(coin)
    print(f"Current {coin.title()} price: ${initial_price:.2f}")

    percent_increase = float(input("Notify when price increases by %: "))
    target_price = initial_price * (1 + percent_increase / 100)

    to_email = input("Enter your email: ").strip()

    print(f"Tracking {coin.title()}... Will notify at ${target_price:.2f}")

    while True:
        try:
            current_price = get_price(coin)
            print(f"{coin.title()} Price: ${current_price:.2f}")

            if current_price >= target_price:
                subject = f"{coin.title()} Price Alert 🚨"
                body = f"{coin.title()} is now ${current_price:.2f}, which is a {percent_increase}% increase from ${initial_price:.2f}"
                send_email(to_email, subject, body)
                print("📧 Email sent. Alert triggered. Exiting.")
                break

            time.sleep(60)  # check every 60 seconds
        except Exception as e:
            print("Error:", e)
            time.sleep(60)

# ------------------------
# Email Credentials Config
# ------------------------
SENDER_EMAIL = "bilalsaeed620@gmail.com"       # 🔁 Replace with your sender Gmail
APP_PASSWORD = "your_email_password_here"    # 🔁 Replace with your Gmail App Password

if __name__ == "__main__":
    main()
