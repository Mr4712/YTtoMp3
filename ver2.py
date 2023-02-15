import os
import youtube_dl
import time
import webbrowser

print("Loading…")
time.sleep(3)


print("""
 __     _________ _____                      _                 _ 
 \ \   / /__   __|  __ \                    | |               | |
  \ \_/ /   | |  | |  | | _____      ___ __ | | ___   __ _  __| |
   \   /    | |  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |
    | |     | |  | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |
    |_|     |_|  |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|
                                                                                                                
                           Made by Torte
""")


link = input("Please insert YouTube link ➔ ")


folder_path = input("Destination Path (Leave blank to download in Downloads folder) ➔ ")
if not folder_path:
    folder_path = os.path.join(os.path.expanduser("~"), "Downloads")


os.chdir(folder_path)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': True
}

while True:
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download complete!")
        webbrowser.open(folder_path)
        answer = input("Would you like to download another video? (Y/N)")
        if answer.lower() == 'n':
            break
        elif answer.lower() == 'y':
            link = input("Please insert YouTube link: ")
        else:
            print("Please enter Y or N")
    except Exception as e:
        print("DONE:", str(e))
        answer = input("Would you like to download another video? (Y/N)")
        if answer.lower() == 'n':
            break
        elif answer.lower() == 'y':
            link = input("Please insert YouTube link: ")
        else:
            print("Please enter Y or N")