from torrentp import TorrentDownloader
import requests
import os


def select_movie(movie_list):
    choice_num = int(input("Enter the number to download the movie : "))
    return movie_list[choice_num]


def get_movie_list(movie_name):
    response = requests.get(
        f'https://yts.mx/api/v2/list_movies.json?query_term={movie_name}')
    return response.json()["data"]["movies"]


def print_movie_list(movie_list):
    for i in range(len(movie_list)):
        print(
            f"{i}.-{movie_list[i]['title_long']}----->{movie_list[i]['year']}")


def select_quality(movie):
    for i, torrent in enumerate(movie["torrents"]):
        if torrent["quality"] == "720p":
            return i
    return 0


def generate_magnet_link(movie, quality_index):
    movie_hash = movie["torrents"][quality_index]["hash"]
    movie_quality = movie["torrents"][quality_index]["quality"]
    movie_type = movie["torrents"][quality_index]["type"]
    magnet_link = f'magnet:?xt=urn:btih:{movie_hash}&dn={movie["title_long"]}+{movie_quality}+{movie_type}+YTS.MX&tr=udp://tracl.two:80&tr=&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:1337&tr=udp://tracker.leechers-paradise.org:6969'
    return magnet_link


movie_name = input("Enter the name of the movie: ")
movie_name = movie_name.replace(" ", "+")
movie_list = get_movie_list(movie_name)
print_movie_list(movie_list)
selected_movie = select_movie(movie_list)
quality_index = select_quality(selected_movie)
magnet_link = generate_magnet_link(selected_movie, quality_index)

torrent_file = TorrentDownloader(magnet_link, '.')
torrent_file.start_download()

print("Download has been started successfully")
