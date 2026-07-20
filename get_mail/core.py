import requests
import random
import string

class MailTM:
	def __init__(self):
		self.base_url = "https://api.mail.tm"
		self.address = None
		self.password = None
		self.token = None

	def _generate_string(self, length=10):
		letters = string.ascii_lowercase + string.digits
		return ''.join(random.choice(letters) for i in range(length))

	def get_domain(self):
		res = requests.get(f"{self.base_url}/domains")
		if res.status_code == 200:
			return res.json()['hydra:member'][0]['domain']
		raise Exception("Failed to fetch domain")

	def create_account(self):
		domain = self.get_domain()
		self.address = f"{self._generate_string()}@{domain}"
		self.password = self._generate_string(12)

		payload = {"address": self.address, "password": self.password}
		res = requests.post(f"{self.base_url}/accounts", json=payload)
		if res.status_code != 201:
			raise Exception("Failed to create account")

		token_res = requests.post(f"{self.base_url}/token", json=payload)
		if token_res.status_code == 200:
			self.token = token_res.json()['token']
			return {
				"address": self.address, 
				"password": self.password, 
				"token": self.token
			}
		raise Exception("Failed to get token")

	def get_messages(self):
		if not self.token:
			return []
		headers = {"Authorization": f"Bearer {self.token}"}
		res = requests.get(f"{self.base_url}/messages", headers=headers)
		if res.status_code == 200:
			return res.json()['hydra:member']
		return []

	def get_message_content(self, msg_id):
		headers = {"Authorization": f"Bearer {self.token}"}
		res = requests.get(f"{self.base_url}/messages/{msg_id}", headers=headers)
		if res.status_code == 200:
			return res.json()
		return None
