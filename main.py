#Begining of project


import requests

api_key = "9558ec233d504b21baccdf101b12ceed"
url = "https://newsapi.org/v2/top-headlines/"

def get_headlines(country="us",category="technology"):
    params = {
        "apikey" : api_key,
        "country" : country,
        "category" : category,
        "pageSize" : 5
    }

    response = requests.get(url,params)
    data = response.json()

    if response.status_code != 200 or data.get("status") != "ok":
        print(f"That didn't work\n{data.get('message')}")
        return

    print(f"\nTop 5 {category.title()} headlines in {country.upper()}:\n")
    for i, article in enumerate(data["articles"], 1):
        print(f"{i}. {article['title']}")
        print(f" -- {article['url']}\n")


if __name__ == "__main__":
    country = input("Please enter a country code: ").lower().strip()
    category = input("Please enter a news category: ").lower().strip()
    get_headlines(country,category)


