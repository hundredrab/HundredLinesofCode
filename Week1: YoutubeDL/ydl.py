import youtube_dl
import os

options = {
    'format': 'bestaudio/best',
    'extractaudio': True,  # only keep the audio
    'audioformat': "mp3",  # convert to mp3
    'outtmpl': os.path.join(os.getcwd(), "music_new/%(title)s-%(id)s.mp3"),
    'noplaylist': True,    # only download single song, not playlist
    'quiet': True,  # Don't print anything
    'no_warnings': True,
}


def download_list():
    """ 
    Takes list of strings as input and donwloads videos into the base folder.
    """

    with open('songlist.txt', 'r') as songs_file:
        song_list = [line.strip() for line in songs_file.readlines()]
    
    if not os.path.exists('music_new'):
    	os.mkdir('music_new')
    print("Downloading to " + os.path.join(os.getcwd(), 'music_new'),)

    for song in song_list:
        youtube_dl.YoutubeDL(options).download(
        	['ytsearch:' + str(song)]
        	)
        print(song.strip() + ' downloaded')
    
    print("\nFinished.")

if __name__ == '__main__':
	download_list()
