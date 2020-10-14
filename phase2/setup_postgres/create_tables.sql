CREATE TABLE auditory_media(
id integer not null,
image_url text,
release_date date,
time_added timestamp,
name text,
genre text,
rating integer,
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
id integer,
name text,
duration integer,
view_count integer,
PRIMARY KEY (name,id),
FOREIGN KEY (id) REFERENCES  album(id)
);

CREATE TABLE podcast(
id integer,
end_year date,
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
FOREIGN KEY (organization_id) REFERENCES  organization(id)
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
FOREIGN KEY(organization_id,award_name,award_year) REFERENCES award(organization_id,name,year),
FOREIGN KEY(auditory_media_id) REFERENCES auditory_media(id)
);

CREATE TABLE produces(
auditory_media_id integer not null,
person_id integer not null,
PRIMARY KEY(person_id, auditory_media_id),
FOREIGN KEY(person_id) REFERENCES person(id),
FOREIGN KEY(auditory_media_id) REFERENCES auditory_media(id)
);

CREATE TABLE publishes(
auditory_media_id integer not null,
publisher_id integer not null,
PRIMARY KEY(auditory_media_id),
FOREIGN KEY(publisher_id) REFERENCES publisher(id),
FOREIGN KEY(auditory_media_id) REFERENCES auditory_media(id)
);


CREATE TABLE member_of(
person_id integer,
auditory_media_id integer not null,
playlist_id integer not null,
PRIMARY KEY(person_id, auditory_media_id),
FOREIGN KEY(playlist_id) REFERENCES playlist(id),
FOREIGN KEY(auditory_media_id) REFERENCES auditory_media(id)
);

CREATE TABLE guest_appearance(
person_id integer,
episode_number integer,
title text,
podcast_id integer,
PRIMARY KEY(person_id, episode_number, title, podcast_id),
FOREIGN KEY(person_id) REFERENCES person(id),
FOREIGN KEY(episode_number,title,podcast_id) REFERENCES episode(episode_number,title,id)
);