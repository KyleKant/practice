from time import sleep
from pprint import pprint
from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtexts = soup.select('.subtext')


def create_hacker_news(links: list, subtexts: list):
    hn = []
    for idx, link in enumerate(links):
        votes = subtexts[idx].select('.score')
        if votes:
            score = int(votes[0].getText().replace('points', ''))
            if score >= 100:
                title = link.getText()
                href = link.get('href')
                hn.append({'title': title, 'href': href, 'score': score})
                hn = sorted(hn, key=lambda i: i['score'], reverse=True)
    return hn


def get_multi_page(numpage: int):
    """Get data of multipage on website

    Args:
        numpage (int): Number page need to get data

    Returns:
        dictionary: A dictionary contain data gotten
    """
    links_page = []
    subtexts_page = []
    rank_page = []
    for page in range(1, numpage):
        response = requests.get(
            'https://news.ycombinator.com/news?p=' + str(page))
        soup = BeautifulSoup(response.text, 'html.parser')
        rank = soup.select('.rank')
        links = soup.select('.titleline > a')
        subtexts = soup.select('.subtext')
        if len(soup) == 0:
            print('break here')
            break
        # if len(rank) == 0:
        #     break
        links_page.append(links)
        subtexts_page.append(subtexts)
        rank_page.append(rank)
        sleep(1)
        print('sleep 1s')
    return {'stt': rank_page, 'links_page': links_page, 'subtexts_page': subtexts_page}


def get_hacker_news(links_page: list, subtexts_page: list):
    """Get hot news

    Args:
        links_page (list): A list contain links of news
        subtexts_page (list): A list contain subtexts of news

    Returns:
        hack_news: A news dictionary contain informations of news such as news title, news url, news vote score
    """
    hack_news = []
    for page, links in enumerate(links_page):
        # pprint((page, links))
        for idx, link in enumerate(links):
            scores = subtexts_page[page][idx].select('.score')
            if len(scores):
                score = int(scores[0].getText().replace('points', ''))
                if score >= 100:
                    title = links[idx].getText()
                    href = links[idx].get('href')
                    hack_news.append(
                        {'page': page, 'stt': idx, 'title': title, 'href': href, 'score': score})
    return hack_news


def sort_hacker_news_by_score(hacker_news: dict[str, list]):
    """Sort news by score

    Args:
        hacker_news (dict[str, list]): A news dictionary contain informations such as news title, news url address, and score of news

    Returns:
        sorted: A news dictionary sorted by decrease score its
    """
    return sorted(hacker_news, key=lambda i: i['score'], reverse=True)


response = get_multi_page(30)
links_page = response['links_page']
subtexts_page = response['subtexts_page']
stt = response['stt']
pprint(sort_hacker_news_by_score(get_hacker_news(links_page, subtexts_page)))
# pprint(get_multi_page(30))
# create_hacker_news(links, subtexts)
