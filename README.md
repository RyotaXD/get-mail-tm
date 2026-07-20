# get-mail

Temp mail generator using mail.tm API.

## Installation
`pip install get-mail`

## Usage
```python
from get_mail import MailTM

mail = MailTM()
account = mail.create_account()
print(f"Address : {account['address']}")
print(f"Password: {account['password']}")

inbox = mail.get_messages()
for msg in inbox:
	print(msg['subject'])
