# Auto-login-IoT-devices
This python script is for auto login in raspberry pi to IIT Mandi WiFi also to skip setting up proxy every time you boot.

###Install Dependencies 
pip install selenium

### Web Driver for differnt browser

Downlaod Web Driver:https://www.seleniumhq.org/download/

## For setting up proxy

$ os.system("export_http_proxy="http:// 10.8.0.1: 8080/" ")

$ os.system("export_https_proxy="https://10.8.0.1:8080/" ")

$ os.system("chromium-browser --proxy-server='http://10.8.0.1:8080'")

## Add bash scripts you want to run at boot time. 
$ os.system("bash script goes here")   

