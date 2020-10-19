import psycopg2
import json


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

        get_all_auditory_media(cursor)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_all_songs(cursor):
    cursor.execute('SELECT song.name, auditory_media.name, auditory_media.image_url '
                   'FROM auditory_media, album, song '
                   'WHERE auditory_media.id = album.id AND album.id = song.auditory_media_id')

    song_list = []
    record = cursor.fetchone()
    while record:
        song = {'song_name':  record[0],
                'album_name': record[1],
                'album_img':  record[2]}

        song_list.append(song)
        record = cursor.fetchone()

    print(song_list)
    return song_list


def get_all_podcasts(cursor):
    cursor.execute('SELECT episode.title, auditory_media.name, auditory_media.image_url '
                   'FROM auditory_media, podcast, episode '
                   'WHERE auditory_media.id = podcast.id AND podcast.id = episode.id')

    podcast_list = []
    record = cursor.fetchone()
    while record:
        podcast_episode = {'episode_name': record[0],
                           'podcast_name': record[1],
                           'podcast_img':  record[2]}

        podcast_list.append(podcast_episode)
        record = cursor.fetchone()

    print(podcast_list)
    return podcast_list


def get_all_comedy_specials(cursor):
    cursor.execute('SELECT  auditory_media.name, auditory_media.image_url '
                   'FROM auditory_media, comedy_special '
                   'WHERE auditory_media.id = comedy_special.id')

    comedy_special_list = []
    record = cursor.fetchone()
    while record:
        comedy_special = {'comedy_special_name': record[0],
                          'comedy_special_img':  record[1]}

        comedy_special_list.append(comedy_special)
        record = cursor.fetchone()

    print(comedy_special_list)
    return comedy_special_list


def get_all_auditory_media(cursor):
    auditory_media_list = {'songs': get_all_songs(cursor),
                           'podcasts': get_all_podcasts(cursor),
                           'comedy_specials': get_all_comedy_specials(cursor)}

    print(auditory_media_list)
    return auditory_media_list


if __name__ == "__main__":
    main()