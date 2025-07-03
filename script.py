import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all post rows
posts = soup.find_all("tr", class_="athing")

with open("data.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'score', 'user'])

    for post in posts:
        title_tag = post.find("span", class_="titleline")
        title = title_tag.get_text() if title_tag else "N/A"

        subtext = post.find_next_sibling("tr").find("td", class_="subtext")
        if subtext:
            score_tag = subtext.find("span", class_="score")
            score = score_tag.get_text() if score_tag else "N/A"

            user_tag = subtext.find("a", class_="hnuser")
            user = user_tag.get_text() if user_tag else "N/A"
        else:
            score = "N/A"
            user = "N/A"

        writer.writerow([title, score, user])
