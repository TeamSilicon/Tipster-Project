import requests
import time

def requester(page_url, index):
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' }
    while True:
        page_content = ""
        for page in page_url:
            try:
                page_content = requests.get(page, headers=headers, timeout=10)
                try:
                    page_content.raise_for_status()
                except Exception as error:
                    print('There was a problem getting web data: %s' % error)
                if page_content.status_code != 200:
                    print('There was a problem getting web data: %s' % error)
                    break
            except requests.ConnectionError as e:
                print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
                print(str(e))
                time.sleep(5) # wait 4 seconds before we make the next request
                break
            except requests.Timeout as e:
                print("OOPS!! Timeout Error")
                print(str(e))
                time.sleep(5) # wait 4 seconds before we make the next request
                break
            except requests.RequestException as e:
                print("OOPS!! General Error")
                print(str(e))
                time.sleep(5) # wait 4 seconds before we make the next request
                break
            except KeyboardInterrupt:
                print("Someone closed the program")
            print("Page %d done!!!. Proceeding to the next trial" % index)
        if page_content != "":
            break
    return page_content
