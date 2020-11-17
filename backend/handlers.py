from typing import List

import psycopg2

from ui.widgets.model.entities import *

#_connection = psycopg2.connect(user="bailey",
#                               password="",
#                               host="127.0.0.1",
#                               port="8888",
#                               database="bailey")
#cursor = _connection.cursor()


def main():
    try:
        connection = psycopg2.connect(user="andersonjwan",
                                      password="",
                                      host="127.0.0.1",
                                      port="8888",
                                      database="andersonjwan")

        # user="$USER"
        # password=""
        # host="127.0.0.1"
        # port="8888"
        # database="$USER"

        # Code taken from https://pynative.com/python-postgresql-tutorial/
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        get_all_media_objects_for_playlist(cursor, 708)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


## ALL MEDIA
def get_all_media(cursor, genre=None, rating=None) -> List[Media]:
    albums = get_all_album_media_helper(cursor, genre, rating)
    comedies = get_all_comedy_special_media_helper(cursor, genre, rating)
    podcasts = get_all_podcast_media_helper(cursor, genre, rating)

    media_list = albums + comedies + podcasts
    return media_list


def get_all_album_media_helper(cursor, genre=None, rating=None) -> List[Album]:
    if genre is None and rating is None:
        cursor.execute(
            'SELECT album.release_format, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, album '
            'WHERE auditory_media.id = album.id')
    elif genre is not None and rating is not None:
        cursor.execute(
            'SELECT album.release_format, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, album '
            'WHERE auditory_media.id = album.id AND auditory_media.genre = \'%s\' AND auditory_media.rating >= %f' % (
                genre, rating))
    elif genre is None and rating is not None:
        cursor.execute(
            'SELECT album.release_format, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, album '
            'WHERE auditory_media.id = album.id AND auditory_media.rating >= %f' % (rating))
    elif genre is not None and rating is None:
        cursor.execute(
            'SELECT album.release_format, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, album '
            'WHERE auditory_media.id = album.id AND auditory_media.genre = \'%s\'' % (genre))

    album_list = []
    record = cursor.fetchone()
    while record:
        album = Album(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        album_list.append(album)

        record = cursor.fetchone()

    return album_list


def get_all_comedy_special_media_helper(cursor, genre=None, rating=None) -> List[ComedySpecial]:
    if genre is None and rating is None:
        cursor.execute(
            'SELECT comedy_special.runtime, comedy_special.venue, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, comedy_special '
            'WHERE auditory_media.id = comedy_special.id')
    elif genre is not None and rating is not None:
        cursor.execute(
            'SELECT comedy_special.runtime, comedy_special.venue, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, comedy_special '
            'WHERE auditory_media.id = comedy_special.id AND auditory_media.genre = \'%s\' AND auditory_media.rating >= %f' % (
                genre, rating))
    elif genre is None and rating is not None:
        cursor.execute(
            'SELECT comedy_special.runtime, comedy_special.venue, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, comedy_special '
            'WHERE auditory_media.id = comedy_special.id AND auditory_media.rating >= %f' % (rating))
    elif genre is not None and rating is None:
        cursor.execute(
            'SELECT comedy_special.runtime, comedy_special.venue, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, comedy_special '
            'WHERE auditory_media.id = comedy_special.id AND auditory_media.genre = \'%s\'' % (genre))

    comedy_special_list = []
    record = cursor.fetchone()
    while record:
        comedy_special = ComedySpecial(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                       record[7])
        comedy_special_list.append(comedy_special)

        record = cursor.fetchone()

    return comedy_special_list


def get_all_podcast_media_helper(cursor, genre=None, rating=None) -> List[Podcast]:
    if genre is None and rating is None:
        cursor.execute(
            'SELECT podcast.end_year, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, podcast '
            'WHERE auditory_media.id = podcast.id')
    elif genre is not None and rating is not None:
        cursor.execute(
            'SELECT podcast.end_year, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, podcast '
            'WHERE auditory_media.id = podcast.id AND auditory_media.genre = \'%s\' AND auditory_media.rating >= %f' % (
                genre, rating))
    elif genre is None and rating is not None:
        cursor.execute(
            'SELECT podcast.end_year, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, podcast '
            'WHERE auditory_media.id = podcast.id AND auditory_media.rating >= %f' % (rating))
    elif genre is not None and rating is None:
        cursor.execute(
            'SELECT podcast.end_year, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
            'FROM auditory_media, podcast '
            'WHERE auditory_media.id = podcast.id AND auditory_media.genre = \'%s\'' % (genre))

    podcast_list = []
    record = cursor.fetchone()
    while record:
        podcast = Podcast(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        podcast_list.append(podcast)

        record = cursor.fetchone()

    return podcast_list


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
    cursor.execute(
        'SELECT DISTINCT comedy_special.runtime, comedy_special.venue, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
        'FROM auditory_media, member_of_comedy, comedy_special '
        'WHERE auditory_media.id = comedy_special.id AND member_of_comedy.auditory_media_id = auditory_media.id AND member_of_comedy.playlist_id = %d' % (
            playlist_id))

    comedy_special_list = []
    record = cursor.fetchone()
    while record:
        comedy_special = ComedySpecial(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                       record[7])
        comedy_special_list.append(comedy_special)

        record = cursor.fetchone()

    cursor.execute(
        'SELECT DISTINCT episode.episode_number, episode.view_count, episode.title, episode.duration '
        'FROM auditory_media, member_of_episode, episode '
        'WHERE auditory_media.id = episode.id AND member_of_episode.auditory_media_id = auditory_media.id AND member_of_episode.playlist_id = %d' % (playlist_id))

    episode_list = []
    record = cursor.fetchone()
    while record:
        episode = Episode(record[0], record[1], record[2], record[3])
        episode_list.append(episode)

        record = cursor.fetchone()

    cursor.execute(
        'SELECT DISTINCT song.view_count, song.name, song.duration '
        'FROM auditory_media, member_of_song, song '
        'WHERE auditory_media.id = song.auditory_media_id AND member_of_song.auditory_media_id = auditory_media.id AND member_of_song.playlist_id = %d' % ( playlist_id))

    song_list = []
    record = cursor.fetchone()
    while record:
        song = Song(record[0], record[1], record[2])
        song_list.append(song)

        record = cursor.fetchone()
    media_list = song_list + comedy_special_list + episode_list
    return media_list


def rename_playlist(cursor, connection, playlist_id: int, new_name: str):
    cursor.execute('UPDATE playlist '
                   'SET name = \'%s\' '
                   'WHERE playlist.id = %d' % (new_name, playlist_id))

    connection.commit()


def delete_playlist(cursor, connection, playlist_id: int):
    cursor.execute('DELETE '
                   'FROM playlist '
                   'WHERE playlist.id = %d' % (playlist_id))

    connection.commit()


def create_new_playlist(cursor, connection, playlist_name: str, playlist_owner: str):
    cursor.execute('SELECT MAX(playlist.id) '
                   'FROM playlist')

    record = cursor.fetchone()
    curr_max_playlist_id = record[0]
    new_playlist_id = curr_max_playlist_id + 1

    cursor.execute('INSERT INTO playlist(id, name, owner) '
                   'VALUES(%d, \'%s\', \'%s\')' % (new_playlist_id, playlist_name, playlist_owner))

    connection.commit()


def add_song_to_playlist(cursor, connection, media_id: int, song_name: str, playlist_id: int):
    cursor.execute('INSERT INTO member_of_song(name, auditory_media_id, playlist_id) '
                   'VALUES(\'%s\', %d, %d) ' % (song_name, media_id, playlist_id))

    connection.commit()


def add_episode_to_playlist(cursor, connection, media_id: int, episode_num: int, episode_title: str, playlist_id: int):
    cursor.execute('INSERT INTO member_of_episode(episode_number, name, auditory_media_id, playlist_id) '
                   'VALUES(%d, \'%s\', %d, %d) ' % (episode_num, episode_title, media_id, playlist_id))

    connection.commit()


def add_comedy_special_to_playlist(cursor, connection, media_id: int, playlist_id: int):
    cursor.execute('INSERT INTO member_of_comedy(auditory_media_id, playlist_id) '
                   'VALUES(%d, %d) ' % (media_id, playlist_id))

    connection.commit()


## PLAYLIST DETAILS
def delete_comedy_special_from_playlist(cursor, connection, playlist_id: int, media_id: int):
    cursor.execute('DELETE '
                   'FROM member_of_comedy '
                   'WHERE member_of_comedy.auditory_media_id = %d AND member_of_comedy.playlist_id = %d' % (
                       media_id, playlist_id))

    connection.commit()


def delete_song_from_playlist(cursor, connection, playlist_id: int, media_id: int, song_name: str):
    cursor.execute('DELETE '
                   'FROM member_of_song '
                   'WHERE member_of_song.auditory_media_id = %d AND member_of_song.playlist_id = %d AND member_of_song.name = \'%s\'' % (
                       media_id, playlist_id, song_name))

    connection.commit()


def delete_episode_from_playlist(cursor, connection, playlist_id: int, media_id: int, episode_num: int):
    cursor.execute('DELETE '
                   'FROM member_of_episode '
                   'WHERE member_of_episode.auditory_media_id = %d AND member_of_episode.playlist_id = %d AND member_of_episode.episode_number = %d' % (
                       media_id, playlist_id, episode_num))

    connection.commit()


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
def get_all_songs_in_album(cursor, media_id: int) -> List[Song]:
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
    cursor.execute(
        'SELECT album.release_format, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
        'FROM auditory_media, album '
        'WHERE auditory_media.id = album.id AND auditory_media.id = %d' % (media_id))

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
    cursor.execute(
        'SELECT podcast.end_year, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
        'FROM auditory_media, podcast '
        'WHERE auditory_media.id = podcast.id AND auditory_media.id = %d' % (media_id))

    record = cursor.fetchone()
    podcast = Podcast(record[0], record[1], record[2], record[3], record[4], record[5], record[6])

    return podcast


## COMEDY SPECIAL DETAILS
def get_comedy_special(cursor, media_id: int) -> ComedySpecial:
    cursor.execute(
        'SELECT comedy_special.runtime, comedy_special.venue, auditory_media.id, auditory_media.name, auditory_media.release_date, auditory_media.image_url, auditory_media.genre, auditory_media.rating '
        'FROM auditory_media, comedy_special '
        'WHERE auditory_media.id = comedy_special.id AND auditory_media.id = %d' % (media_id))

    record = cursor.fetchone()
    comedy = ComedySpecial(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7])

    return comedy


## COMEDY SPECIAL DETAILS AND PODCAST OR ALBUM DETAILS

def get_publisher(cursor, media_id: int) -> Publisher:
    cursor.execute('SELECT publisher.id, publisher.name '
                   'FROM auditory_media, publishes, publisher '
                   'WHERE auditory_media.id = publishes.auditory_media_id AND publishes.publisher_id = publisher.id AND auditory_media.id = %d' % (
                       media_id))

    record = cursor.fetchone()
    publisher = Publisher(record[0], record[1])

    return publisher


def get_award(cursor, media_id: int) -> List[Award]:
    cursor.execute('SELECT award.name, award.year, award.organization_id '
                   'FROM auditory_media, award, won '
                   'WHERE auditory_media.id = won.auditory_media_id AND award.organization_id = won.organization_id AND auditory_media.id = %d' % (
                       media_id))

    award_list = []
    record = cursor.fetchone()
    while record:
        award = Award(record[0], record[1], record[2])
        award_list.append(award)

        record = cursor.fetchone()

    return award_list


def get_organization(cursor, org_id):
    cursor.execute('SELECT organization.id, organization.name '
                   'FROM organization '
                   'WHERE organization.id = %d' % (org_id))

    record = cursor.fetchone()
    org = Organization(record[0], record[1])

    return org


def get_person(cursor, media_id: int) -> List[Person]:
    cursor.execute('SELECT person.date_of_death, person.id, person.name, person.date_of_birth, person.country '
                   'FROM auditory_media, produces, person '
                   'WHERE auditory_media.id = produces.auditory_media_id AND produces.person_id = person.id AND auditory_media.id = %d' % (
                       media_id))

    person_list = []
    record = cursor.fetchone()
    while record:
        person = Person(record[4], record[3], record[2], record[1], record[0])
        person_list.append(person)

        record = cursor.fetchone()

    return person_list


if __name__ == "__main__":
    main()
