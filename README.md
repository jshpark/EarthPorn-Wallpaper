# EarthPorn-Wallpaper

A basic Python script that grabs the hottest post on Reddit's /r EarthPorn and changes the user's wallpaper. This script only works in Windows 32/64 bit.  

## Getting Started
First, you must acquire a Secret from Reddit's API. You can do this by using **Reddit's old website**. 
1. Preferences (next to profile)
2. Apps
3. Create an APP 
    - You can use https://localhost8080 for your redirect uri
4. Fill in appropriate information in the code snippet from wallpaper.py
    - client_id: The 14 character string underneath your project name
    - client_secret = String generated when creating your application
    - password: Your personal account password
    - user_agent: Should contain your applicaition name and your username
        - ex) EarthPorn script by /u/xxxxx
    - username = Your personal account username
```
def startReddit():
    reddit = praw.Reddit(client_id='xxxxx',
    client_secret = 'xxxxxxx',
    password = 'xxxxxx',
    user_agent = 'xxxxxxxx',
    username = 'xxxxx')
```
    
