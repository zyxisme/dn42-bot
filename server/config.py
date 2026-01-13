import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

BOT_TOKEN = "8342462731:AAGjBwuRJkDQzTwYRvM4rraYmvJjHQprABE"
CONTACT = "@zyxisme"
DN42_ASN = 4242420116

WELCOME_TEXT = (
    f"Hello, I'm the bot for Potat0's DN42 Network (`AS{DN42_ASN}`).\n"
    f"你好，我是 ZYXISME (`AS{DN42_ASN}`) 的 DN42 机器人。\n"
    "\n"
    "For more information, please check: 更多信息请查看：\n"
    "https://dn42.potat0.cc/\n"
)

WHOIS_ADDRESS = "whois.lantian.dn42"
DN42_ONLY = False
ALLOW_NO_CLEARNET = True

# API settings
ENDPOINT = "node.zyx-blog.top"  # Also used for tunnel
API_PORT = 54321
API_TOKEN = "Zyx_apitoken_1234"
SERVERS = {
    "us1": "US1 | RackNerd DC02",
}
HOSTS = {
    "us1": "us1.node.zyx-blog.top",
}

# Webhook settings
WEBHOOK_URL = ""
WEBHOOK_LISTEN_HOST = "127.0.0.1"
WEBHOOK_LISTEN_PORT = 3443

# Optional settings
LG_DOMAIN = "https://lg.dn42.zyx-blog.top"
PRIVILEGE_CODE = ""
SINGLE_PRIVILEGE = False
CN_WHITELIST_IP = ["8.8.8.8", "2001:4860:4860::8888"]
SENTRY_DSN = None


# Email-sending function
def send_email(asn, mnt, code, email):
    text = (
        f"Hi {mnt} (AS{asn}),\n"
        "\n"
        "Welcome to my DN42 Network.\n"
        "\n"
        f"Here is your code: {code}\n"
        "\n"
        "Have fun!\n"
    )
    try:
        mimemsg = MIMEMultipart()
        mimemsg["From"] = "My DN42<mail@zyx-blog.top>"
        mimemsg["To"] = f"{mnt}<{email}>"
        mimemsg["Subject"] = "Verification Code"
        mimemsg.attach(MIMEText(text, "plain"))
        connection = smtplib.SMTP(host="smtpdm.aliyun.com", port=465)
        connection.starttls()
        connection.login("mail@zyx-blog.top", "AsdfQwer1234")
        connection.send_message(mimemsg)
        connection.quit()
    except BaseException:
        raise RuntimeError
