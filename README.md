# WallGet

### Video Demo: [Youtube](https://youtu.be/E-7SbDP4CXQ?si=QmVIDx8x-xev7Ut1)
<iframe width="560" height="315" src="https://www.youtube.com/embed/E-7SbDP4CXQ?si=xdfcJVIrBHnc6jMH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Description:
This Python script allows you to download wallpapers in bulk from [wallhaven.cc](https://wallhaven.cc) using the API provided by Wallhaven. The program does not require an API key from wallhaven to download wallpapers, but it only allows you to download non-NSFW images. Users can choose from different categories and specify a specific page to download wallpapers from. Additionally, this program provides the user with the ability to change the specified output destination too.

Here are some of the categories you can choose from when using this script:

- General
- Anime
- People
- Fantasy
- Science Fiction
- Vehicles
- Video Games
- Animals
- Nature
- Architecture

Please note that this script only allows you to download non-NSFW images. If you want to download NSFW images, you will need to use the official Wallhaven API and obtain an API key.


## Libraries used in the projects:
- os
- random
- requests
- string

## Wallhaven API
[API Link](https://wallhaven.cc/help/api)

## Options
- You can also modify the program to filter wallpapers based on their resolution. To do this, you can edit **Line 6** in ```project.py``` and specify the minimum resolution for the wallpapers you want to download.Furthermore, you can change the output directory for the downloaded wallpapers by editing **Line 7** in ```project.py```. This will allow you to save the wallpapers to a specific folder of your choice.
