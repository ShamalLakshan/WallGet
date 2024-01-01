import requests
import random
import os
import string

resolution = "1920x1080"
path = "./images/"

def wall_search_api(keyword, pagination, category):
    url = f"https://wallhaven.cc/api/v1/search?q={keyword}&page={pagination}&categories={category}&atleast={resolution}"
    res = requests.get(url)
    json_data = res.json()
    dl_links = []
    for wallpaper in json_data["data"]:
        dl_links.append(wallpaper["path"])
    return dl_links

def generate_id():
    return ''.join(random.choices(string.ascii_lowercase+string.digits, k=6))

def download_wallpaper(url):
    print(f"Downloading --> {url}")
    res = requests.get(url)
    wall_name = generate_id()
    ext = os.path.splitext(url)[1]
    dl_path = f"{path}{wall_name}{ext}"
    open(dl_path, 'wb').write(res.content)

def header():
    print("                                                                        ")
    print("I8,        8        ,8I          88 88   ,ad8888ba,                     ")
    print("`8b       d8b       d8:          88 88  d8;:    `;8b              ,d    ")
    print(" ;8,     ,8;8,     ,8;           88 88 d8:                        88    ")
    print("  Y8     8P Y8     8P ,adPPYYba, 88 88 88             ,adPPYba, MM88MMM ")
    print("  `8b   d8: `8b   d8: ;;     `Y8 88 88 88      88888 a8P_____88   88    ")
    print("   `8a a8:   `8a a8:  ,adPPPPP88 88 88 Y8,        88 8PP;;;;;;;   88    ")
    print("    `8a8:     `8a8:   88,    ,88 88 88  Y8a.    .a88 ;8b,   ,aa   88,   ")
    print("     `8:       `8:    `;8bbdP;Y8 88 88   `;Y88888P;   `;Ybbd8;:   ;Y888 ")
    print("                                                                        ")


def main():
    header()
    keyword = input("Enter a keyword to search wallpapers: ")
    pagination = input("Enter page number to search (Press 'Enter if none'): ")
    category = input("Enter a specific category to search(anime/general/people...) (Press 'Enter if none'): ")

    if pagination == "":
        pagination = 1
    if category == "":
        category == 0

    waldlurl = wall_search_api(keyword, pagination, category)
    for url in waldlurl:
        download_wallpaper(url)

if __name__ == "__main__":
    main()