import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []

    # PUT YOUR CODE HERE
    # news_list: NewsList = []
    links = parser.select("a[rel='nofollow noreferrer']")
    subtext = parser.select(".subtext")
    for pos, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        points = int(subtext[pos].select(".score")[0].getText().split()[0])
        comments = subtext[pos].select("a:last-of-type")[1].getText().split()[0]
        comments = 0 if comments.isalpha() else int(comments)
        user = subtext[pos].select(".hnuser")[0].getText()
        if user is None:
            user = "None"
        news_list.append({"title": title, "url": href, "points": points, "comments": comments,  "author": user})
    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    # PUT YOUR CODE HERE

    return parser.select(".morelink")[0].get("href")


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news

