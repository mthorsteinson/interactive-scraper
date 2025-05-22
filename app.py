import requests
import json
import colorama
import flask

app = flask.Flask(__name__)

colorama.init(autoreset=True)
api_key = "9558ec233d504b21baccdf101b12ceed"
url = "https://newsapi.org/v2/top-headlines/"
choices = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
choices1 = [item.title() for item in choices]


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
        return [], f"Error: {data.get('message', 'Unknown error')}"
    '''
    print(f"\nTop 5 {category.title()} Headlines in {country.upper()}:\n")
    for i, article in enumerate(data["articles"], 1):
        print(f"{i}. {article['title']}")
        print(f" -- {article['url']}\n")
    '''
    articles = data["articles"][:5]  # Get top 5 articles
    return articles, None


def pick_country():
    fakecountry = input("Please enter a country code: \nApologies, the only available country right now is the US (any key to continue): ").lower().strip()
    print(f"\n")
    return fakecountry

def pick_category():
    category = input("Please enter a news category:\nOptions -- " + colorama.Fore.GREEN + "Business, Entertainment, General, Health, Science, Sports, Technology\n" + colorama.Style.RESET_ALL).lower().strip()
    global choices
    if category not in choices:
        print(colorama.Fore.RED + f"\nThat's not a valid category. Try again.\n")
        category = pick_category()
    print(f"\n")
    return category

def more_details(index):
    details = data["articles"][index]["description"]
    print(colorama.Style.BRIGHT + f"\nDetails:\n{details}\n")




@app.route("/", methods=["GET","POST"])
def index():
    articles = []
    error = None
    listitems = choices1
    category = flask.request.form.get("category", "technology").capitalize()
    if flask.request.method in ["POST","GET"]:
        articles, error = get_headlines("us",category)
    if error == None:
        return flask.render_template("index.html",articles=articles,error=error,listitems=listitems,category=category)
    else:
        return flask.render_template("failure.html",articles=articles,error=error,listitems=listitems,category=category)

@app.route("/index2", methods=["GET","POST"])
def index2():
    articles = []
    error = None
    listitems = choices1
    category = flask.request.form.get("category", "technology").capitalize()
    print(category)
    if flask.request.method in ["POST","GET"]:
        articles, error = get_headlines("us",category)
    if error == None:
        return flask.render_template("index2.html",articles=articles,error=error,listitems=listitems,category=category)
    else:
        return flask.render_template("failure.html",articles=articles,error=error,listitems=listitems,category=category)
    
@app.route("/index3", methods=["GET","POST"])
def index3():
    articles = []
    error = None
    listitems = choices1
    category = flask.request.form.get("category", "technology").capitalize()
    print(category)
    if flask.request.method in ["POST","GET"]:
        articles, error = get_headlines("us",category)
    if error == None:
        return flask.render_template("index3.html",articles=articles,error=error,listitems=listitems,category=category)
    else:
        return flask.render_template("failure.html",articles=articles,error=error,listitems=listitems,category=category)

@app.route("/search", methods=["GET","POST"])
def search():
    articles = []
    error = None
    listitems = choices1
    category = flask.request.form.get("category", "technology").capitalize()
    if flask.request.method in ["POST","GET"]:
        articles, error = get_headlines("us",category)
    if error == None:
        return flask.render_template("search.html",articles=articles,error=error,listitems=listitems,category=category)
    else:
        return flask.render_template("failure.html",articles=articles,error=error,listitems=listitems,category=category)
           
            
@app.route("/failure", methods=["GET","POST"])
def failure():
    articles = []
    error = None
    listitems = choices1
    return flask.render_template("failure.html",articles=articles,error=error,listitems=listitems)


if __name__ == "__main__":
    app.run(debug=True)
'''
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
'''
