#!/usr/bin/env python

import requests
import time
import os

# gateway.iitmandi.ac.in/facstaff/login.php
login_req = requests.get("gateway.iitmandi.ac.in/facstaff/login.php")
login_req_url = login_req.url
magic_token = login_req_url[32:]
os.system("export_http_proxy="http:// 10.8.0.1: 8080/" ")
os.system("export_https_proxy="https://10.8.0.1:8080/" ")
os.system("chromium-browser --proxy-server='http://10.8.0.1:8080'")


if(login_req_url!=" "):
	with requests.session() as s: 
		login_url = "https://gateway.iitmandi.ac.in/facstaff/login.php"     #gateway.iitmandi.ac.in/facstaff/login.php
		referer = login_req_url

		login_form = {
                    # https://gateway.iitmandi.ac.in/3e7e3480-e7e1-4e8b-9894-5838fb30c2a5
        "4Tredir": "https://gateway.iitmandi.ac.in/3e7e3480-e7e1-4e8b-9894-5838fb30c2a5",
		"magic":magic_token,
		"username":"intern_tapaswin",
		"password":"ITW@1234#"
		}

		login = s.post(url = login_url,data = login_form,headers={'referer':referer})
		
