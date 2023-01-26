import requests
import os

movie_name = input("Enter the name of the movie: ")
movie_name = movie_name.replace(" ", "+")


def get_response(movie_name):
    response = requests.get(
        "https:// yts.mx/api/v2/list_movies.json?query_term={movie_name}")
    datas = response.json()["data"]["movies"]
    return datas


movie_list = get_response(movie_name)
movie_title = []
movie_year = []
movie_torrent = []

for i in range(0, len(movie_list)):
    movie_title.append(movie_list[i]["title_long"])
    movie_year.append(movie_list[i]["year"])
    movie_torrent.append(movie_list[i]["torrents"])

# Print the list of titles
for i in range(0, len(movie_list)):
    print(f"{i}.-{movie_title[i]}----->{movie_year[i]}")
    # print(movie_torrent[i])

choice_num = int(input("Enter the number to download the movie : "))
hd_quality = 0
for i in range(0, len(movie_torrent)):
    quality = movie_torrent[choice_num][i]["quality"]
    if (quality == "720p"):
        hd_quality = i
        break

movie_hash = movie_torrent[choice_num][hd_quality]["hash"]
movie_quality = movie_torrent[choice_num][hd_quality]["quality"]
movie_type = movie_torrent[choice_num][hd_quality]["type"]

magnet_link = f'magnet:?xt=urn:btih:{movie_hash}&dn={movie_title[choice_num]}+{movie_quality}+{movie_type}+YTS.MX&tr=udp://tracl.two:80&tr=&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:1337&tr=udp://tracker.leechers-paradise.org:6969'

command = f'qbt torrent add url"{magnet_link}" --username admin --password adminadmin --url http://localhost:8080'
os.system(command)
print("Download has been started successfully")
