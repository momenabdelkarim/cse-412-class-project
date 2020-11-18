"""
The classes defined here are used to transmit data between backend and frontend
"""
from abc import ABC


class Media(ABC):
    def __init__(self, media_id: int, name: str, release_date: str, cover_url: str, genre: str, rating: int):
        self.media_id = media_id
        self.name = name
        self.release_date = release_date
        self.cover_url = cover_url
        self.genre = genre
        self.rating = rating


class Podcast(Media):
    def __init__(self, end_year: int, media_id: int, name: str, release_date: str, cover_url: str, genre: str,
                 rating: int):
        super().__init__(media_id, name, release_date, cover_url, genre, rating)

        self.end_year = end_year


class Album(Media):
    """
    Do the media stuff
    """

    def __init__(self, release_format: str, media_id: int, name: str, release_date: str, cover_url: str, genre: str,
                 rating: int):
        super().__init__(media_id, name, release_date, cover_url, genre, rating)
        self.release_format = release_format


class ComedySpecial(Media):
    def __init__(self, runtime: int, venue: str, media_id: int, name: str, release_date: str, cover_url: str,
                 genre: str, rating: int):
        super().__init__(media_id, name, release_date, cover_url, genre, rating)
        self.runtime = runtime
        self.venue = venue


class Episode:
    """
    episodeNumber, Title, ID
    """

    def __init__(self, media_id: int, episode_number: int, view_count: int, title: str, duration: int):
        self.media_id = media_id
        self.duration = duration
        self.name = title
        self.view_count = view_count
        self.episode_number = episode_number


class Song:
    """
    View Count, Name, Duration, mediaID
    """

    def __init__(self, media_id: int, view_count: int, song_name: str, duration: int):
        self.media_id = media_id
        self.duration = duration
        self.name = song_name
        self.view_count = view_count


class Organization:
    def __init__(self, organization_id: int, name: str):
        self.name = name
        self.organization_id = organization_id


class Award:
    def __init__(self, award_name: str, award_year: int, organization_id: int):
        self.organization_id = organization_id
        self.award_year = award_year
        self.award_name = award_name


class Person:
    def __init__(self, country: str, dob: str, name: str, person_id: int, dod: str):
        self.dod = dod
        self.person_id = person_id
        self.name = name
        self.dob = dob
        self.country = country


class Publisher:
    def __init__(self, publisher_id: int, name: str):
        self.publisher_id = publisher_id
        self.name = name


class Playlist:
    def __init__(self, playlist_id: int, name: str):
        self.playlist_id = playlist_id
        self.name = name
