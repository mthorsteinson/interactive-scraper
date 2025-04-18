#Begining of project


import requests
import json
import colorama

colorama.init(autoreset=True)
api_key = "9558ec233d504b21baccdf101b12ceed"
url = "https://newsapi.org/v2/top-headlines/"

def get_headlines(country="us",category="technology"):
    params = {
        "apikey" : api_key,
        "country" : country,
        "category" : category,
        "pageSize" : 5
    }
    global response
    response = requests.get(url,params)
    global data
    data = response.json()

    if response.status_code != 200 or data.get("status") != "ok":
        print(colorama.Fore.RED + f"That didn't work\n{data.get('message')}")
        return

    print(f"\nTop 5 {category.title()} Headlines in {country.upper()}:\n")
    for i, article in enumerate(data["articles"], 1):
        print(f"{i}. {article['title']}")
        print(f" -- {article['url']}\n")

def pick_country():
    fakecountry = input("Please enter a country code: \nApologies, the only available country right now is the US (any key to continue): ").lower().strip()
    print(f"\n")
    return fakecountry

def pick_category():
    category = input("Please enter a news category:\nOptions -- " + colorama.Fore.GREEN + "Business, Entertainment, General, Health, Science, Sports, Technology\n" + colorama.Style.RESET_ALL).lower().strip()
    options = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    if category not in options:
        print(colorama.Fore.RED + f"\nThat's not a valid category. Try again.\n")
        category = pick_category()
    print(f"\n")
    return category

def more_details(index):
    details = data["articles"][index]["description"]
    print(colorama.Style.BRIGHT + f"\nDetails:\n{details}\n")



if __name__ == "__main__":
    fakecountry = pick_country()
    category = pick_category()
    get_headlines("us",category)
    more = input(f"Would you like to learn more about one of these headlines? (y/n) ").lower()
    while more not in ("y","n"):
        more = input(colorama.Fore.RED + "Uh, try again (y/n): " + colorama.Style.RESET_ALL).lower()
    if more == "y":
        index = int(input("Which headline would you like to learn more about? (1, 2, 3, 4, or 5): "))
        index = index - 1
        more_details(index)
    else:
        print(colorama.Style.BRIGHT + f"\nThanks for coming by!\n")
    #response = response.json()
    #print(json.dumps(response,indent=4))

