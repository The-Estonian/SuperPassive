import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError
from writeToFile import save_to_file

def check_site(site, username, headers):
    site_name = site["name"]
    uri_check = site["uri_check"].format(account=username)
    try:
        res = requests.get(uri_check, headers=headers, timeout=10)
        estring_pos = site["e_string"] in res.text
        estring_neg = site["m_string"] in res.text
        if res.status_code == site["e_code"] and estring_pos and not estring_neg:
            return site_name, uri_check
    except:
        pass
    return None

def find_username(username):
    headers = {
    "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-language": "en-US;q=0.9,en,q=0,8",
    "accept-encoding": "gzip, deflate",
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }
    # Fetch wmn-data from WhatsMyName repository
    response = requests.get("https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json")
    data = response.json()
    found_sites = []
    # Scan all websites for the username 
    if username:
        sites = data["sites"]
        total_sites = len(sites)
        found_sites = []
        try:
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = {executor.submit(check_site, site, username, headers): site for site in sites}
                with tqdm(total=total_sites, desc="Checking sites") as pbar:
                    completed = 0
                    for future in as_completed(futures):
                        try:
                            result = future.result()
                            if result:
                                site_name, uri_check = result
                                found_sites.append((site_name, uri_check))
                                print("\033[32m" + "-" * 133)
                                print(f"\033[32m[+] \033[1mTarget found\033[0m\033[32m ✓ on: \033[1m{site_name}\033[0m")
                                print(f"\033[32m[+] Profile URL: {uri_check}\033[0m")
                                print("\033[32m" + "-" * 133)
                        except:
                            pass
                        finally:
                            completed += 1
                            pbar.n = completed
                            pbar.refresh()
        except TimeoutError:
            print("Some sites took too long to respond and were skipped.")
        pbar.n = total_sites
        pbar.refresh()
        print("\nChecked all sites.")
        if found_sites:
            print(f"\nThe user \033[1m{username}\033[0m was found on {len(found_sites)} sites:")
            save_to_file(found_sites, "result.txt")
        else:
            print(f"\nNo sites found for the user \033[1m{username}\033[0m.")
