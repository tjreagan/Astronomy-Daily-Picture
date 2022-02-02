import requests
import pwd
import os
from datetime import datetime
from pathlib import Path

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def get_filename(filename):
    # Get the username in order to assemble the proper directory
    username = pwd.getpwuid(os.getuid()).pw_name
    directory = "/Users/" + username + "/Downloads/Astronomy Pic of the Day/"

    return os.path.join(directory, filename)

def download_pic():
    r = requests.get(url)

    if r.status_code != 200:
        print("error")
        return

    picture_url = r.json()["url"]
    print(picture_url)

    if "jpg" not in picture_url:
        print("No image today. Must be a video.")
        return
    else:
        pic = requests.get(picture_url, allow_redirects=True)
    
    todays_date = datetime.now()
    date_string = todays_date.strftime("%m-%d-%Y")
    jpg_name = date_string + ".jpg"
    filename = get_filename(jpg_name)
    pathName = Path(filename)

    if pathName.exists():
        print("File already exists!!!!!!!!!!")
        return
    else:
        open(filename, "wb").write(pic.content)
        print(f"Picture of the day saved to {filename}")

def main():
    download_pic()

if __name__ == "__main__":
    main()