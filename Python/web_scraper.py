# Author: Rohtash Lakra
import requests
import random
import inspect
from bs4 import BeautifulSoup
import datetime as dt

class WebScraper:

    # base_url = "https://www.linkedin.com"
    # base_url = "https://linkedin.com"

    #b'403 - Forbidden | Access to this page is forbidden.\n'
    # To avoid above error, use customer header user-agent value.
    base_url = "https://pixelford.com/blog"

    # __init__
    def __init__(self):
        self.headers = {
            # "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            "User-Agent" : f"{random.randint(1, 100)}"
        }
        self.params = {}
        self.contents = {}

    # loads the website
    def load_website(self, url):
        print(f"{inspect.stack()[0][3]}{url, self.headers}")
        response = requests.get(url, headers=self.headers)
        self.contents = response.content;
        # print(self.contents)

    def prettify(self):
        soup = BeautifulSoup(self.contents, 'html.parser')
        html = soup.prettify();
        print(f"\n{html}\n")

    def read_href_links(self):
        soup = BeautifulSoup(self.contents, 'html.parser')
        # html = soup.prettify();
        a_tags = soup.find_all("a", class_="entry-title-link")
        for a_tag in a_tags:
            # find only title text
            print(a_tag.get_text())

        print("\n")
        # map all the blog titles
        blog_titles = list(map(lambda a_tag: a_tag.get_text(), a_tags))
        print(blog_titles)
        # find all urls
        print(f"\n{list(map(lambda a_tag: a_tag.get('href'), a_tags))}\n")
        # all attributes
        print(f"\n{list(map(lambda a_tag: a_tag.attrs, a_tags))}\n")        

    # Returns the value of the element
    def get_element(self, html_element, tag_name, class_name="", attr_name=""):
        if len(class_name) > 0 and len(attr_name) > 0:
            return html_element.find(tag_name, class_=f"{class_name}").get(attr_name)
        elif len(class_name) > 0:
            return html_element.find(tag_name, class_=f"{class_name}").get_text()
        elif len(attr_name) > 0:
            return html_element.find(tag_name).get(attr_name)
        else:
            return html_element.find(tag_name).get_text()
    
    # prints the article details as needed
    def print_article_details(self, article_element):
        # find only title text
        for a_tag in article_element.children:
            # find all href links
            href_links = a_tag.find_all("a", class_="entry-title-link")
            for link in href_links:
                print(link.get_text())

            # find all time-stamps
            entry_times = a_tag.find_all("time", class_="entry-time")
            for link_time in entry_times:
                print(link_time.get_text())
            
            authors = a_tag.find_all("span", class_="entry-author-name")
            for author in authors:
                print(author.get_text())

    # format's the date
    def format_date(self, date_text, date_pattern=""):
        date = dt.datetime.fromisoformat(date_text)
        if len(date_pattern) > 0:
            return date.strftime(date_pattern)            
        else:
            return date

    def scrap(self):
        soup = BeautifulSoup(self.contents, 'html.parser')
        # html = soup.prettify();
        blogs = soup.find_all("article", class_="type-post")
        # print("\n")
        for blog in blogs:
            # self.print_article_details(blog)
            # title = blog.find("a", class_="entry-title-link").get_text()
            # published_on = blog.find("time", class_="entry-time").get_text()
            # author = blog.find("span", class_="entry-author-name").get_text()
            title = self.get_element(blog, "a", "entry-title-link")
            published_on = self.get_element(blog, "time", "entry-time")
            # read published datatime attribute
            # https://strftime.org/
            published_datetime = self.get_element(blog, "time", "entry-time", "datetime")
            published_pretty = self.format_date(published_datetime, "%m/%d/%Y %I:%M:%S %p (%a)")
            author = self.get_element(blog, "span", "entry-author-name")
            print(title)
            print(f"{published_on} By {author}")
            print(f"{published_datetime} - {published_pretty}")
            print("\n")
            # print(article.get_text())


        print("\n")
        # map all the blog titles
        # all_articles = list(map(lambda article: article.get_text(), articles))
        # print(all_articles)

# create instance and execute requests.
webScraper = WebScraper()
webScraper.load_website(WebScraper.base_url)
# webScraper.prettify()
webScraper.scrap()
