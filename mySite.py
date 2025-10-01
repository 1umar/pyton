import time
import random
import requests

#   Comanda ca sa pornesti acest script in background, non-modal, cu scriere log:
#   $ nohup python -u mySite.py > my_log.log 2>&1 &
#   Ca sa vezi PID-ul scriptului (ca eventual sa-l kill):
#   $ ps aux | grep mySite.py
# ----------------------------------------------------------------------
# URL of the website you want to access
#url = 'https://lukesis.free.nf/'
#print(f"Script outside main {time.ctime()}", flush=True)

# Define the range of intervals between accesses in seconds
# For example, between 1 hour (3600s) and 3 hours (10800s)
min_interval = 3600  # 1 hour
max_interval = 10000  # 2h47'

def access_website():
    url = "https://lukesis.free.nf/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/92.0.4515.131 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        print(f"Accessed at {time.ctime()}")
        # You can also process response.content or response.text here
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url} at {time.ctime()}: {e}")
        

def main():
    print(f"Script started at {time.ctime()}", flush=True)
    while True:
        ceasul = time.localtime()
        if ceasul.tm_hour >= 21:  # intervalul de accesat pagina: intre orele 6:00 - 21:00
            sleep_time = (30 - ceasul.tm_hour) * 3600 - 60 * ceasul.tm_min + random.randint(0, 2700) # primul acces intre 6 si 6:45 dimineata
            time.sleep(sleep_time)
        access_website()
        # Wait for a random interval
        sleep_time = random.randint(min_interval, max_interval)
        print(f"Next access in {sleep_time} seconds.", flush=True)
        time.sleep(sleep_time)
        

if __name__ == "__main__":
    main()

