import requests
from bs4 import BeautifulSoup
import json

# This is the help to put the cookies in the right place.
# https://stackoverflow.com/questions/23102833/how-to-scrape-a-website-which-requires-login-using-python-and-beautifulsoup

# This code is used to login to the sligro webpage. This variables need to be put in after the url to the API
cookies = {
    'browser_uid': '1444331a-9faa-40f1-a7b1-1cdca3cb1aa3',
    'logged_in_once': 'true',
    '_ga_4W72JJ120N': 'GS1.1.1665490156.2.1.1665490157.0.0.0',
    '_gid': 'GA1.2.385465738.1671977603',
    'at_check': 'true',
    'AMCVS_FCFE24465E2570490A495C1F%40AdobeOrg': '1',
    'mboxEdgeCluster': '37',
    'highprioritymessagetarget': 'De%20feestdagen%20komen%20er%20aan.%20Let%20op%3A%20aangepaste%20bestel-%20en%20levermomenten%20en%20houd%20rekening%20met%20drukte.%20Klik%20hier%C2%A0voor%20meer%20informatie',
    'expHist': '%5B%22812226%3A1%22%2C%22772289%3A1%22%2C%22786155%3A1%22%2C%22817074%3A0%22%2C%22742620%3A1%22%2C%22728092%3A1%22%2C%22717797%3A1%22%5D',
    'access_token': 'a6iqbKH7ODyL0W1OoOM5eEelVXU',
    'id_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRlc3QxIn0.eyJzdWIiOiJpbmZvQGJpZy1iZWxseXMubmwiLCJhdWQiOiJ0ZXN0MSIsInVzZXJndWlkIjoiYmQ5YmQ2YWUtNDI0MC00MGM4LThjZGQtZDg0M2E4ZjQ0Y2IyIiwic2NvcGUiOlsib3BlbmlkIl0sImlzcyI6InNsaWdyby9hdXRob3JpemF0aW9uc2VydmVyIiwibmFtZSI6IkhVTklOSyBCICBIdW5pbmsgQiIsImdyb3VwcyI6WyJWaWV3QnVkZ2V0cyIsIlZpZXdFeGNsdXNpdmVEaXNjb3VudHMiLCJQZXJmb3JtVHJhbnNhY3Rpb25hbEFjdGlvbnMiLCJWaWV3UHJvbW90aW9uYWxFeHByZXNzaW9ucyIsIkVkaXRMaXN0cyIsIk1hbmFnZUJ1ZGdldHMiLCJTZW5kT3JkZXIiLCJWaWV3SW52b2ljZXMiLCJjdXN0b21lcmFkbWluZ3JvdXAiLCJNYW5hZ2VVc2VycyIsIlZpZXdQcmljZXMiXSwibG9jYXRpb24iOiIyNDA5NDciLCJleHAiOjE2NzIwOTYwNzEsImlhdCI6MTY3MjA1Mjg3MSwidXVpZCI6IjE0NDQzMzFhLTlmYWEtNDBmMS1hN2IxLTFjZGNhM2NiMWFhMyIsImVtYWlsIjoiaW5mb0BiaWctYmVsbHlzLm5sIn0.Pjr8lxrMBuzlJrl9jLzDZsrhgbCPI7M1lvjgzsmQdpTDTuVzL4TbbBK_HftaoLRpn4PD7kzq5nsIxEdzj4H2XeofnbpF-cpRPCLDnN0V_4R0Sb6YSJSdmfbP5xumSPsNx0Sryco-lECPVSIuXt5Sx5Ta31GNwtPw8kcS-XIa3joOo_S7urAo6HZB90DY7-T4vQm6NhGOmqiTzpBeupWoFtsIgR82s5UJTaL6V5lc9gUQabarUDZO-TmkUxc0lYmbuOxLgXNOvtieKj9_Q54qBprLdbE5PSmgwU5HHUanDcBJygOPEpJeptfTZxj8_9EyAw1GEhMm5o9RluX9ooHbNA',
    'refresh_token': 'RgqviReMMea_NateRTWckjWYRc4',
    'AMCV_FCFE24465E2570490A495C1F%40AdobeOrg': '-408604571%7CMCIDTS%7C19352%7CMCMID%7C51070872107548686141410382834031342824%7CMCAAMLH-1672657672%7C6%7CMCAAMB-1672657672%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C763785440%7CMCOPTOUT-1672060072s%7CNONE%7CvVersion%7C4.6.0',
    '_ga': 'GA1.2.33674288.1631534396',
    'mbox': 'PC#0de076e6b010451e870d0e7febd62538.37_0#1735298122|session#daaa3d8e16844ef2b88861da8c5cb3ce#1672055182',
    '_ga_6CQ7R82LWS': 'GS1.1.1672045165.13.1.1672053323.0.0.0',
    '_dd_s': 'rum=1&id=efa233a8-c92b-4ce7-b4a6-84fb712ab57e&created=1672045164619&expire=1672054289405',
}

headers = {
    'authority': 'www.sligro.nl',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': 'browser_uid=1444331a-9faa-40f1-a7b1-1cdca3cb1aa3; logged_in_once=true; _ga_4W72JJ120N=GS1.1.1665490156.2.1.1665490157.0.0.0; _gid=GA1.2.385465738.1671977603; expHist=%5B%22772289%3A1%22%2C%22786155%3A1%22%2C%22817074%3A0%22%2C%22742620%3A1%22%2C%22728092%3A1%22%2C%22717797%3A1%22%5D; at_check=true; AMCVS_FCFE24465E2570490A495C1F%40AdobeOrg=1; AMCV_FCFE24465E2570490A495C1F%40AdobeOrg=-408604571%7CMCIDTS%7C19352%7CMCMID%7C51070872107548686141410382834031342824%7CMCAAMLH-1672649964%7C6%7CMCAAMB-1672649964%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C763785440%7CMCOPTOUT-1672052364s%7CNONE%7CvVersion%7C4.6.0; mboxEdgeCluster=37; highprioritymessagetarget=De%20feestdagen%20komen%20er%20aan.%20Let%20op%3A%20aangepaste%20bestel-%20en%20levermomenten%20en%20houd%20rekening%20met%20drukte.%20Klik%20hier%C2%A0voor%20meer%20informatie; access_token=Gggo_gAO7cR37yhN3LqDy_TShsI; id_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InRlc3QxIn0.eyJzdWIiOiJpbmZvQGJpZy1iZWxseXMubmwiLCJhdWQiOiJ0ZXN0MSIsInVzZXJndWlkIjoiYmQ5YmQ2YWUtNDI0MC00MGM4LThjZGQtZDg0M2E4ZjQ0Y2IyIiwic2NvcGUiOlsib3BlbmlkIl0sImlzcyI6InNsaWdyby9hdXRob3JpemF0aW9uc2VydmVyIiwibmFtZSI6IkhVTklOSyBCICBIdW5pbmsgQiIsImdyb3VwcyI6WyJWaWV3QnVkZ2V0cyIsIlZpZXdFeGNsdXNpdmVEaXNjb3VudHMiLCJQZXJmb3JtVHJhbnNhY3Rpb25hbEFjdGlvbnMiLCJWaWV3UHJvbW90aW9uYWxFeHByZXNzaW9ucyIsIkVkaXRMaXN0cyIsIk1hbmFnZUJ1ZGdldHMiLCJTZW5kT3JkZXIiLCJWaWV3SW52b2ljZXMiLCJjdXN0b21lcmFkbWluZ3JvdXAiLCJNYW5hZ2VVc2VycyIsIlZpZXdQcmljZXMiXSwibG9jYXRpb24iOiIyNDA5NDciLCJleHAiOjE2NzIwOTA1MDcsImlhdCI6MTY3MjA0NzMwNywidXVpZCI6IjE0NDQzMzFhLTlmYWEtNDBmMS1hN2IxLTFjZGNhM2NiMWFhMyIsImVtYWlsIjoiaW5mb0BiaWctYmVsbHlzLm5sIn0.O-p2pxk3j3bEzyotvbndSpth1x7fank9Sh3y7souKFk41MOuNVYCaoLPfy3p6zwxO2XBA65dXTF103Z0lpVwUmX2WsnsbhXapmSPj0Guj581O_TXO-e3W0swGuml0oy6-2Fz786BwZWcOvIER8uxOOQgrrGYbx8ZYady31pcJDYltVcqQ6qAc1FpHRDqfcj4cTBZUfLciCr6RUIpBd3nynNLlRWXziuHH16qRGpJQXzRfIP3Fl2VRWu5eF1s8JXpSZQH8rIY_l3Ii61oVsRB03xGDkQWoK619VpHsyMvScugdcJTMCX1zQvl15kQ3GIM7noEvI4q_bnSPLPM5AL2Uw; refresh_token=pXli3ePb43H6kEqnrfYV2yJB9AM; _gat_UA-156260857-1=1; mbox=PC#0de076e6b010451e870d0e7febd62538.37_0#1735292110|session#daaa3d8e16844ef2b88861da8c5cb3ce#1672049170; _ga=GA1.2.33674288.1631534396; _ga_6CQ7R82LWS=GS1.1.1672045165.13.1.1672047310.0.0.0; _dd_s=rum=1&id=efa233a8-c92b-4ce7-b4a6-84fb712ab57e&created=1672045164619&expire=1672048215029',
    'referer': 'https://www.sligro.nl/inloggen.html?logoutreason=inactivity&target=%2Fhome.html%23firstLogin',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

# dictionary for the product codes
product_codes = {
    'coca_cola': "192603",
    'chaudfontaine' : '838327',
    'guinness fust 30l' : '412862'
}


# This is my own code

def get_price(product_code):
    # This is the GET request to the api with the product code at the end. It also puts in the cookie and head info for authentication.
    r = requests.get("https://www.sligro.nl/api/cart/sligro-nl/customerorganizationdatas?productCodes={}".format(product_code), cookies=cookies, headers=headers)
    # Maybe the BS library is not needed anymore???
    soup = BeautifulSoup(r.text, 'html.parser')
    # Change the data to json
    site_json = json.loads(soup.text)
    # Put the data in a variable
    price = site_json['data']['products'][0]['price']['value']
    # Return it
    return price
    
for item in product_codes:
    print(item, get_price(product_codes[item]))

coca_cola = get_price('192603')
red = get_price('838327')

# print(coca_cola)
# print(red)