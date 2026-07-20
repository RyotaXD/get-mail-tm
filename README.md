# 📧 get-mail-tm

[![PyPI version](https://img.shields.io/pypi/v/get-mail.svg)](https://pypi.org/project/get-mail/)
[![Python versions](https://img.shields.io/pypi/pyversions/get-mail.svg)](https://pypi.org/project/get-mail/)
[![GitHub stars](https://img.shields.io/github/stars/RyotaXD/get-mail-tm.svg?style=social)](https://github.com/RyotaXD/get-mail-tm/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/RyotaXD/get-mail-tm.svg?style=social)](https://github.com/RyotaXD/get-mail-tm/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, lightning-fast, and modular temporary email generator powered by the mail.tm public API. 

This package is designed to be easily integrated into your automation scripts, bot creators, and Termux environments without any unnecessary bloat.

## ✨ Features

- 🚀 **Dynamic Domain Fetching:** Automatically grabs the latest active domains to bypass IP blocks.
- ⚡ **Instant Generation:** Create random email addresses and passwords on the fly.
- 🔑 **Token Management:** Seamlessly handles Bearer Tokens for authorization.
- 📬 **Inbox Polling:** Read incoming messages, subjects, and extract full email content (useful for OTPs or verification links).
- 🛠️ **No Bloatware:** Pure Python `requests`, raw and simple to read.

## 💡 Perfect For
- Social Media Auto-Register Bots
- VPN / SSH Account Snipers
- ReCaptcha / OTP Verification Automation
- Privacy Protection & Testing

## 📦 Installation
`pip install get-mail`


## Usage
```python
from get_mail import MailTM

mail = MailTM()
account = mail.create_account()
print(f"Alamat   : {account['address']}")
print(f"Password : {account['password']}")
print(f"Token    : {account['token']}")```


## Detail nya
```python
from get_mail import MailTM
import time

def main():
	mail = MailTM()
	account = mail.create_account()
	
	print(f"[*] Email dibuat: {account['address']}")
	print(f"[*] Password: {account['password']}")
	print("[*] Menunggu email masuk...\n")
	
	try:
		while True:
			inbox = mail.get_messages()
			if inbox:
				for msg in inbox:
					print(f"[+] Email Baru Dari: {msg['from']['address']}")
					print(f"[+] Subjek: {msg['subject']}")
					
					# Ambil isi lengkap pesan
					content = mail.get_message_content(msg['id'])
					if content:
						print(f"[+] Isi:\n{content['text']}\n")
				break # Hentikan perulangan setelah menerima email
			
			time.sleep(5)
			
	except KeyboardInterrupt:
		print("\n[-] Dihentikan oleh user.")

if __name__ == "__main__":
	main()
```
