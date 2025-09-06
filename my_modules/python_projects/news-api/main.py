import requests
NEWS_API_KEY = "USE_YOUR_OWN_API"

# API used: newsapi.org


def get_news():

    query = input("Enter keyword to search the news for... \n")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}&from=2025-09-01&sortBy=publishedAt"
    print(f"Request URL: {url}")
    res = requests.get(url)

    if (res.status_code == 200):
        data = res.json()
        if (data["totalResults"] > 0):
            print(f"{data["totalResults"]} results retrieved...")
            articles = data["articles"]

            for index, article in enumerate(articles):
                print(index+1, article["title"], article["url"])

                print(
                    "\n **************************************************************** \n")
        else:
            print("No news retrieved for the input Keyword")
    else:
        print("Error while retrieving response:", res.status_code, res.text)


if __name__ == "__main__":
    get_news()
