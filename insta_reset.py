import requests, re, json, time, os, random, sys


# URL to prepare for POST request
url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"

g = requests.get("https://www.instagram.com/accounts/password/reset/").text # get request to get the csrftoken data variable
token = re.search(r'csrf_token":"(.*?)"',g).group(1) # csrftoken fetcher

# headers 
headers = {
    "x-requested-with": "XMLHttpRequest",
    "Connection": "Keep-Alive",
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15",
    'x-csrftoken': token,
}

data = {'email_or_username': 'phonunumber', 'recaptcha_challenge_field':''}

def main():
	while True:
		r = requests.post(url, data=data, headers=headers)
		#print(r.headers)
		a = json.loads(r.text)
		if a['status'] == "fail":
			print(f"[-] Status: {a['status']}")
			print(f"[-] Response: {a['message']}")
		else:
			print(f"[+] Status: {a['status']}")
			print(f"[+] Response: {a['message']}")
		time.sleep(300)

if __name__ == "__main__":
	main()
time.sleep(3)