import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd7ddf28978bc465596fa4cad095cb3ac.mailgun.org/messages",
        auth=("api", "key-f8862e37e74200e025f2217cc07904f9"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxd7ddf28978bc465596fa4cad095cb3ac.mailgun.org>",
              "to": "Nitin Pai <pai.nitin+mailgun@gmail.com>",
              "subject": "Hello Nitin Pai",
              "text": "Congratulations Nitin Pai, you just sent an email with Mailgun!  You are truly awesome!"})

# You can see a record of this email in your logs: https://mailgun.com/app/logs .

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10,000 emails/month for free.

send_simple_message()
