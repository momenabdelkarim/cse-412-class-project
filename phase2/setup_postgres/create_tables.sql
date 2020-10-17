CREATE TABLE auditory_media(
id integer not null,
image_url text,
release_date date,
name text,
genre text,
rating float,
PRIMARY KEY (id)
);


CREATE TABLE comedy_special(
id integer,
runtime integer,
venue text,
PRIMARY KEY (id),
FOREIGN KEY (id) REFERENCES  auditory_media(id)
);

CREATE TABLE album(
id integer,	
release_format text,
PRIMARY KEY (id),
FOREIGN KEY (id) REFERENCES  auditory_media(id)
);

CREATE TABLE song(
auditory_media_id integer,
name text,
duration integer,
view_count integer,
PRIMARY KEY (auditory_media_id, name),
FOREIGN KEY (auditory_media_id) REFERENCES  album(id)
);

CREATE TABLE podcast(
id integer,
end_year integer,
PRIMARY KEY (id),
FOREIGN KEY (id) REFERENCES  auditory_media(id)
);

CREATE TABLE episode(
id integer,	
title text,
episode_number integer,
duration integer,
view_count integer,
PRIMARY KEY (title,episode_number,id),
FOREIGN KEY (id) REFERENCES podcast(id)
);


CREATE TABLE publisher(
id integer not null,
name text,
PRIMARY KEY (id)
);

CREATE TABLE playlist(
id integer not null,
name text,
owner text,
PRIMARY KEY (id)
);

CREATE TABLE organization(
id integer not null,
name text,
PRIMARY KEY (id)
);

CREATE TABLE award(
organization_id integer not null,
name text not null,
year integer not null,
PRIMARY KEY (organization_id,name,year),
FOREIGN KEY (organization_id) REFERENCES  organization(id) ON DELETE CASCADE
);

CREATE TABLE person(
id integer not null,
country text,
name text,
date_of_birth date,
date_of_death text,
PRIMARY KEY (id)
);


CREATE TABLE won(
award_name text,
award_year integer,
organization_id integer,
auditory_media_id integer not null,
PRIMARY KEY(award_name, award_year, organization_id, auditory_media_id),
FOREIGN KEY(organization_id,award_name,award_year) REFERENCES award(organization_id,name,year) ON DELETE CASCADE,
FOREIGN KEY(auditory_media_id) REFERENCES auditory_media(id) ON DELETE CASCADE
);

CREATE TABLE produces(
auditory_media_id integer not null,
person_id integer not null,
PRIMARY KEY(person_id, auditory_media_id),
FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE,
FOREIGN KEY(auditory_media_id) REFERENCES auditory_media(id) ON DELETE CASCADE
);

CREATE TABLE publishes(
auditory_media_id integer not null,
publisher_id integer not null,
PRIMARY KEY(auditory_media_id),
FOREIGN KEY(publisher_id) REFERENCES publisher(id) ON DELETE CASCADE,
FOREIGN KEY(auditory_media_id) REFERENCES auditory_media(id) ON DELETE CASCADE
);


CREATE TABLE member_of_song(
name text not null,
auditory_media_id integer not null,
playlist_id integer not null,
PRIMARY KEY(name, auditory_media_id, playlist_id),
FOREIGN KEY(playlist_id) REFERENCES playlist(id) ON DELETE CASCADE,
FOREIGN KEY(auditory_media_id, name) REFERENCES song(auditory_media_id,name) ON DELETE CASCADE
);

CREATE TABLE member_of_episode(
episode_number integer not null,
name text not null,
auditory_media_id integer not null,
playlist_id integer not null,
PRIMARY KEY(episode_number, name, auditory_media_id, playlist_id),
FOREIGN KEY(playlist_id) REFERENCES playlist(id) ON DELETE CASCADE,
FOREIGN KEY(name,episode_number, auditory_media_id) REFERENCES episode(title,episode_number,id) ON DELETE CASCADE
);

CREATE TABLE member_of_comedy(
auditory_media_id integer not null,
playlist_id integer not null,
PRIMARY KEY(auditory_media_id, playlist_id),
FOREIGN KEY(playlist_id) REFERENCES playlist(id) ON DELETE CASCADE,
FOREIGN KEY(auditory_media_id) REFERENCES comedy_special(id) ON DELETE CASCADE
);

CREATE TABLE guest_appearance(
person_id integer,
episode_number integer,
title text,
podcast_id integer,
PRIMARY KEY(person_id, episode_number, title, podcast_id),
FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE,
FOREIGN KEY(episode_number,title,podcast_id) REFERENCES episode(episode_number,title,id) ON DELETE CASCADE
);