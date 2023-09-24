from bottle import (
    route, run, template, request, redirect
)

from scraputils import get_news
from db import News, Session
from bayes import NaiveBayesClassifier


@route("/news")
def news_list():
    with Session.begin() as session:
        rows = session.query(News).filter(News.label == None).all()
        return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    with Session.begin() as session:
        row = session.query(News).filter(News.id == request.query.id).first()
        row.label = request.query.label
        session.commit()
    redirect("/news")


@route("/update")
def update_news():
    news = get_news("https://news.ycombinator.com/newest")
    with Session.begin() as session:
        for new in news:
            if len(new.keys()) == 5 and not len(
                    session.query(News)
                            .filter(News.author == new["author"], News.title == new["title"])
                            .all()
            ):
                session.add(
                    News(
                        author=new["author"],
                        title=new["title"],
                        points=new["points"],
                        comments=new["comments"],
                        url=new["url"],
                    )
                )
        session.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    PUT YOUR CODE HERE


if __name__ == "__main__":
    run(host="localhost", port=8080)

