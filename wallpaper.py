import praw
import urllib.request
import os
import ctypes


def startReddit():
    reddit = praw.Reddit(client_id='xxxxxxxxxx',
    client_secret = 'xxxxxxxxxxx',
    password = 'xxxxxxxxxxx',
    user_agent = 'xxxxxxxxxxxx',
    username = 'xxxxxxxxxxxxxxxx')
    return reddit

def getTopPost(reddit):
    count = 1
    posts = []
    for topPost in reddit.subreddit('EarthPorn').hot(limit=5):
        posts.append(topPost.url)
    for validPost in posts:
        if ".jpg" in validPost:
            return validPost

def parseUrl(url):
    data = url.split('/')
    return data[3]

def downloadTopPost(url, image):
    urllib.request.urlretrieve(url, image)

def changeFileName(image):
    if os.path.exists('image.jpg'):
        os.remove('image.jpg')
    os.rename(image, 'image.jpg')

def changeWallpaper(path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    return;

def main():
    reddit = startReddit()
    topPostUrl = getTopPost(reddit)
    image = parseUrl(topPostUrl)
    downloadTopPost(topPostUrl, image)
    changeFileName(image)
    path = 'xxxxxxxxxxxxxxxx'
    changeWallpaper(path)

if __name__ == '__main__':
    main()
