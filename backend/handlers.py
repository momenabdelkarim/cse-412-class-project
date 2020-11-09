from typing import List

import psycopg2
from ui.widgets.model.entities import *



def main():
    try:
        connection = psycopg2.connect(user="andersonjwan",
                                      password="",
                                      host="127.0.0.1",
                                      port="8888",
                                      database="andersonjwan")

        # Code taken from https://pynative.com/python-postgresql-tutorial/
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        get_all_media_objects_for_playlist(cursor, 707)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
# def get_all_songs(cursor):
#     cursor.execute('SELECT song.name, auditory_media.name, auditory_media.image_url '
#                    'FROM auditory_media, album, song '
#                    'WHERE auditory_media.id = album.id AND album.id = song.auditory_media_id')
#
#     song_list = []
#     record = cursor.fetchone()
#     while record:
#         song = {'song_name':  record[0],
#                 'album_name': record[1],
#                 'album_img':  record[2]}
#
#         song_list.append(song)
#         record = cursor.fetchone()
#
#     print(song_list)
#     return song_list
#
#
# def get_all_podcasts(cursor):
#     cursor.execute('SELECT episode.title, auditory_media.name, auditory_media.image_url '
#                    'FROM auditory_media, podcast, episode '
#                    'WHERE auditory_media.id = podcast.id AND podcast.id = episode.id')
#
#     podcast_list = []
#     record = cursor.fetchone()
#     while record:
#         podcast_episode = {'episode_name': record[0],
#                            'podcast_name': record[1],
#                            'podcast_img':  record[2]}
#
#         podcast_list.append(podcast_episode)
#         record = cursor.fetchone()
#
#     print(podcast_list)
#     return podcast_list
#
#
# def get_all_comedy_specials(cursor):
#     cursor.execute('SELECT  auditory_media.name, auditory_media.image_url '
#                    'FROM auditory_media, comedy_special '
#                    'WHERE auditory_media.id = comedy_special.id')
#
#     comedy_special_list = []
#     record = cursor.fetchone()
#     while record:
#         comedy_special = {'comedy_special_name': record[0],
#                           'comedy_special_img':  record[1]}
#
#         comedy_special_list.append(comedy_special)
#         record = cursor.fetchone()
#
#     print(comedy_special_list)
#     return comedy_special_list
#
#
# def get_all_auditory_media(cursor):
#     auditory_media_list = {'songs': get_all_songs(cursor),
#                            'podcasts': get_all_podcasts(cursor),
#                            'comedy_specials': get_all_comedy_specials(cursor)}
#
#     print(auditory_media_list)
#     return auditory_media_list

#

## ALL MEDIA

def get_all_media(cursor, genre=None, rating=None) -> List[Media]:
    if genre is None and rating is None:
        cursor.execute('SELECT auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                       'FROM auditory_media')
    elif genre is not None and rating is not None:
        cursor.execute('SELECT auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                       'FROM auditory_media '
                       'WHERE auditory_media.genre = \'%s\' AND auditory_media.rating >= %f' % (genre, rating))
    elif genre is None and rating is not None:
        cursor.execute('SELECT auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                       'FROM auditory_media '
                       'WHERE auditory_media.rating >= %f' % (rating))
    elif genre is not None and rating is None:
        cursor.execute('SELECT auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                       'FROM auditory_media '
                       'WHERE auditory_media.genre = \'%s\'' % (genre))

    media_list = []
    record = cursor.fetchone()
    while record:
        media = Media(record[0], record[1], record[2], record[3], record[4], record[5])
        media_list.append(media)

        record = cursor.fetchone()

    return media_list

def get_all_user_playlists(cursor) -> List[Playlist]:
    cursor.execute('SELECT playlist.id, playlist.name '
                   'FROM playlist')

    playlist_list = []
    record = cursor.fetchone()
    while record:
        playlist = Playlist(record[0], record[1])
        playlist_list.append(playlist)

        record = cursor.fetchone()

    print(playlist_list)
    return playlist_list


def get_all_media_objects_for_playlist(cursor, playlist_id: int) -> List[Media]:
    cursor.execute('SELECT DISTINCT auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                   'FROM auditory_media, member_of_comedy '
                   'WHERE member_of_comedy.auditory_media_id = auditory_media.id AND member_of_comedy.playlist_id = %d' % (playlist_id))

    media_list = []
    record = cursor.fetchone()
    while record:
        media = Media(record[0], record[1], record[2], record[3], record[4], record[5])
        media_list.append(media)

        record = cursor.fetchone()

    cursor.execute('SELECT DISTINCT auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                   'FROM auditory_media, member_of_episode '
                   'WHERE member_of_episode.auditory_media_id = auditory_media.id AND member_of_episode.playlist_id = %d' % (playlist_id))

    record = cursor.fetchone()
    while record:
        media = Media(record[0], record[1], record[2], record[3], record[4], record[5])
        media_list.append(media)

        record = cursor.fetchone()

    cursor.execute('SELECT DISTINCT auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                   'FROM auditory_media, member_of_song '
                   'WHERE member_of_song.auditory_media_id = auditory_media.id AND member_of_song.playlist_id = %d' % (playlist_id))

    record = cursor.fetchone()
    while record:
        media = Media(record[0], record[1], record[2], record[3], record[4], record[5])
        media_list.append(media)

        record = cursor.fetchone()

    return media_list

def rename_playlist(cursor, playlist_id, new_name):
    pass

def delete_playlist(cursor, playlist_id):
    pass

def create_new_playlist(cursor, playlist_name, playlist_owner, playlist_id):
    pass

def add_song_to_playlist(cursor, media_id, song_name, playlist_id):
    pass

def add_episode_to_playlist(cursor, media_id, episode_num, episode_title, playlist_id):
    pass

def add_comedy_special_to_playlist(cursor, media_id, playlist_id):
    pass

## PLAYLIST DETAILS
def delete_comedy_special_from_playlist(cursor, playlist_id, media_id):
    pass

def delete_song_from_playlist(cursor, playlist_id, media_id, song_name):
    pass

def delete_episode_from_playlist(cursor, playlist_id, media_id, episode_num, episode_title):
    pass

## FILTERS
def get_all_available_genres(cursor) -> List[str]:
    cursor.execute('SELECT DISTINCT auditory_media.genre '
                   'FROM auditory_media')

    genre_list = []
    record = cursor.fetchone()
    while record:
        genre_list.append(record[0])
        record = cursor.fetchone()

    return genre_list

## PODCAST OR ALBUM DETAILS
def get_all_songs_in_album(cursor, media_id : int) -> List[Song]:
    cursor.execute('SELECT song.name, song.duration, song.view_count '
                   'FROM song '
                   'WHERE song.auditory_media_id = %d' % (media_id))

    song_list = []
    record = cursor.fetchone()
    while record:
        song = Song(record[2], record[0], record[1])
        song_list.append(song)

        record = cursor.fetchone()

    return song_list

def get_album_for_selected_song(cursor, media_id: int) -> Album:
    cursor.execute('SELECT album.release_format, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                   'FROM auditory_media, album '
                   'WHERE auditory_media.id = album.id AND auditory_media.id = %d' %(media_id))

    record = cursor.fetchone()
    album = Album(record[0], record[1], record[2], record[3], record[4], record[5], record[6])

    return album

def get_episodes_in_podcast(cursor, media_id: int) -> List[Episode]:
    cursor.execute('SELECT episode.episode_number, episode.view_count, episode.title, episode.duration '
                   'FROM episode '
                   'WHERE episode.id = %d' % (media_id))

    episode_list = []
    record = cursor.fetchone()
    while record:
        episode = Episode(record[0], record[1], record[2], record[3])
        episode_list.append(episode)

        record = cursor.fetchone()

    return episode_list

def get_podcast_for_selected_episode(cursor, media_id: int) -> Podcast:
    cursor.execute('SELECT podcast.end_year, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                   'FROM auditory_media, podcast '
                   'WHERE auditory_media.id = podcast.id AND auditory_media.id = %d' %(media_id))

    record = cursor.fetchone()
    podcast = Podcast(record[0], record[1], record[2], record[3], record[4], record[5], record[6])

    return podcast

## COMEDY SPECIAL DETAILS
def get_comedy_special(cursor, media_id: int) -> ComedySpecial:
    cursor.execute('SELECT comedy_special.runtime, comedy_special.venue, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
                   'FROM auditory_media, comedy_special '
                   'WHERE auditory_media.id = comedy_special.id AND auditory_media.id = %d' %(media_id))

    record = cursor.fetchone()
    comedy = ComedySpecial(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7])

    return comedy

## COMEDY SPECIAL DETAILS AND PODCAST OR ALBUM DETAILS

def get_publisher(cursor, media_id: int) -> Publisher:
    cursor.execute('SELECT publisher.id, publisher.name '
                   'FROM auditory_media, publishes, publisher '
                   'WHERE auditory_media.id = publishes.auditory_media_id AND publishes.publisher_id = publisher.id AND auditory_media.id = %d' % (media_id))

    record = cursor.fetchone()
    publisher = Publisher(record[0], record[1])

    return publisher

def get_award(cursor, media_id: int) -> List[Award]:
    cursor.execute('SELECT award.name, award.year, award.organization_id '
                   'FROM auditory_media, award, won '
                   'WHERE auditory_media.id = won.auditory_media_id AND award.organization_id = won.organization_id AND auditory_media.id = %d' % (media_id))

    award_list = []
    record = cursor.fetchone()
    while record:
        award = Award(record[0], record[1], record[2])
        award_list.append(award)

        record = cursor.fetchone()

    return award

def get_organization(cursor, org_id):
    cursor.execute('SELECT organization.id, organization.name '
                   'FROM organization '
                   'WHERE organization.id = %d' % (org_id))

    record = cursor.fetchone()
    org = Organization(record[0], record[1])

    return record

def get_person(cursor, media_id: int) -> List[Person]:
    cursor.execute('SELECT person.date_of_death, person.id, person.name, person.date_of_birth, person.country '
                   'FROM auditory_media, produces, person '
                   'WHERE auditory_media.id = produces.auditory_media_id AND produces.person_id = person.id AND auditory_media.id = %d' % (media_id))

    person_list = []
    record = cursor.fetchone()
    while record:
        person = Person(record[4], record[3], record[2], record[1], record[0])
        person_list.append(person)

        record = cursor.fetchone()

    return person_list

if __name__ == "__main__":
    main()