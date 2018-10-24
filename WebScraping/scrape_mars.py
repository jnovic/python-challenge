


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import pymongo

def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    title = soup.find('div', class_="content_title").text
    p_text= soup.find('div', class_="article_teaser_body").text
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    html2 = browser.html
    soup2 = bs(html2, "html.parser")
    featured_image= soup2.find("a", class_="button fancybox")["data-fancybox-href"]
    featured_image_url = url2 + featured_image
    url3 ="https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    html3 = browser.html
    soup3 = bs(html3, "html.parser")
    mars_weather = soup3.find("div", class_="js-tweet-text-container").text
    url4 = "https://space-facts.com/mars/"
    tables = pd.read_html(url4)
    df = tables[0]
    df.columns=["Fact Type", "Fact"]
    dfhtml = df.to_html()
    dfhtml = dfhtml.replace('\n', '')
    results = soup5.find_all("h3")
    trythis = ["https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced", "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced", "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced", "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"]
    screwthis = []
    for x in results:
        url5= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url5)
        html5 = browser.html
        soup5 = bs(html5, "lxml")
        time.sleep(5)
        browser.click_link_by_partial_text(x.text)
        html5 = browser.html
        soup5 = bs(html5, "lxml")
        maybe = soup5.find("img", class_="wide-image")["src"]
        alex = urljoin(url5, maybe)
        screwthis.append({"title": x.text,
                       "url": alex })
    post = {"title":title, 
            "description":p_text, 
            "feature_image": featured_image_url,
            "weather": mars_weather,
            "facts": dfhtml,
            "images": screwthis
            }
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.db
    collection = db.factoids
    collection.insert_one(post)
