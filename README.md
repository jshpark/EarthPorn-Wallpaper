# EarthPorn-Wallpaper

A basic Python script that grabs the hottest post on Reddit's /r EarthPorn and changes the user's wallpaper. This script only works in Windows 64 bit.  

## Getting Started
First, you must acquire a Secret from Reddit's API. You can do this by using **Reddit's old website**. 
1. Preferences (next to profile)
2. Apps
3. Create an APP 
    - You can use https://localhost8080 for your redirect uri
4. Fill in appropriate information in the code snippet from wallpaper.py
    - **client_id**: The 14 character string underneath your project name
    - **client_secret**: String generated when creating your application
    - **password**: Your personal account password
    - **user_agent**: Should contain your applicaition name and your username
        - ex) EarthPorn script by /u/xxxxx
    - **username**: Your personal account username
```
def startReddit():
    reddit = praw.Reddit(client_id='xxxxx',
    client_secret = 'xxxxxxx',
    password = 'xxxxxx',
    user_agent = 'xxxxxxxx',
    username = 'xxxxx')
```

## Updating Path 
Now that you have all credentials ready to go, you must change the path in the following snippet
```
def main():
    reddit = startReddit()
    topPostUrl = getTopPost(reddit)
    image = parseUrl(topPostUrl)
    downloadTopPost(topPostUrl, image)
    changeFileName(image)
    path = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    changeWallpaper(path)
```
The path must be an absolute path, and it must contain escape character '\' before every '\'.
    -ex) C:\\Users\\jshpark\\Desktop\\EarthPorn\\image.jpg
***When updating the path, the file name must be image.jpg***

## Final
Everything is now setup. Run the program, and your wallpaper will change to /r EarthPorn's hottest picture!
You can also add this to your task scheduler to start the script on login or to run every 2 hours.
