INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(101, 'https://upload.wikimedia.org/wikipedia/en/9/95/Origins_cover.png', '2018-11-09', 'Origins', 'pop rock', 7);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(102, 'https://upload.wikimedia.org/wikipedia/en/6/68/Jerry_Seinfeld%2C_I%27m_Telling_You_for_the_Last_Time_video_box.jpg', '8/8/1998', 'Im Telling You for the Last Time', 'comedy', 10);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(103, 'media3.com', '5/1/2018', 'John Mulaney: Kid Gorgeous at Radio City', 'comedy', 8);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(104, 'media4.com', '8/21/2020' , 'Dynamite', 'pop', 8);

INSERT INTO auditory_media(id, image_url, release_date, name,genre, rating)
VALUES(105, 'media5.com', '8/11/2017', 'Dont Smile at Me', 'eloctropop', 9.5);

INSERT INTO auditory_media(id, image_url, release_date, name,genre, rating)
VALUES(106, 'media6.com', '8/11/2017', '24K Magic', 'eloctropop', 9.5);

INSERT INTO auditory_media(id, image_url, release_date, name,genre, rating)
VALUES(107, 'media7.com', '8/11/2017', 'Office Ladies', 'comedy podcast', 7.5);

INSERT INTO auditory_media(id, image_url, release_date, name,genre, rating)
VALUES(108, 'media8.com', '11/30/1982', 'Thriller', 'pop', 10);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(109,'https://upload.wikimedia.org/wikipedia/en/8/88/Jeff_Dunham_Arguing_With_Myself.jpg', '4/11/2006', 'Jeff Dunham: Arguing with Myself', 'comedy', 6);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(110, 'media10.com', '11/21/1975', 'A Night at the Opera', 'rock', 10);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(111, 'media11.com', '11/28/2018', 'Conan O Brien Needs a Friend', 'comedy podcast', 6);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(112, 'media12.com', '5/8/1970', 'Let It Be', 'rock', 9);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(113, 'media13.com', '4/7/2013', 'Aloha Fluffy', 'comedy', 9.5);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(114, 'media14.com', '8/28/1988', 'Descanso Dominical', 'pop', 8.5);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(115, 'media15.com', '5/4/2019', 'The TryPod', 'podcast', 7.5);

INSERT INTO auditory_media (id, image_url, release_date, name,genre, rating)
VALUES(116, 'media15.com', '9/8/2020', 'CTF Radiooo', 'podcast', 7.3);

/* Comedy Special Table: */

INSERT INTO comedy_special (id, runtime, venue)
VALUES(102, 75, 'Broadhurst Theatre');

INSERT INTO comedy_special (id, runtime, venue)
VALUES(103, 64, 'Radio City Music Hall');

INSERT INTO comedy_special (id, runtime, venue)
VALUES(109, 76, 'Santa Anna Theatre');

INSERT INTO comedy_special (id, runtime, venue)
VALUES(113, 60,'Hawaii Theatre Center');

/* Album Table: */
INSERT INTO album(id, release_format)
VALUES (101, 'CD');

INSERT INTO album(id, release_format)
VALUES (104, 'digital');

INSERT INTO album(id, release_format)
VALUES (105, 'digital');

INSERT INTO album(id, release_format)
VALUES (106, 'digital');

INSERT INTO album(id, release_format)
VALUES(108, 'CD');

INSERT INTO album(id, release_format)
VALUES(110, 'Vinyl');

INSERT INTO album(id, release_format)
VALUES(112, 'Vinyl');

INSERT INTO album(id, release_format)
VALUES(114, 'Vinyl');


/* Song Table: */

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 101, 'Natural', 189,  621539875);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 101, 'Boomerang', 188,  53977701);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 101, 'Machine', 182,  78769871);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 106, 'Thats What I like', 226,  1115782736);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 106, 'Chunky', 187,  198284225);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 104, 'Dynamite', 199,  259027195);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 108, 'Beat it', 378,  459385390);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 108, 'Billie Jean', 294,  742519652);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 108, 'Thriller', 357, 456276389);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 108, 'P.Y.T. (Pretty Young Thing)', 238, 1284596);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 105, 'Ocean Eyes', 200, 639047103);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 105, 'Bellyache', 179, 489127257);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 105, 'Watch', 176, 265400429);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 105, 'Copycat', 193, 294773489);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 105, 'Idontwannabeyouanymore', 204, 575068180);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 105, 'My Boy', 170, 315143707);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 105, 'Party Favor', 204, 156051931);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 110, 'Bohemian Rhapsody', 355, 1235434565);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 110, 'Youre My Best Friend', 172, 12457849);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 112, 'Get It Back', 194, 43112687);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES(112, 'Let It Be', 230, 6743829);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES ( 112, 'The Long and Winding Road', 220, 76328379);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 114, 'La Fuerza del Destino', 317, 703900);

INSERT INTO song(auditory_media_id, name, duration, view_count)
VALUES( 114, 'El Cine', 255, 342876);

/* Podcast Table: */

INSERT INTO podcast(id, end_year)
VALUES(107, 2020);

INSERT INTO podcast(id, end_year)
VALUES(111, 2020);

INSERT INTO podcast(id, end_year)
VALUES(115, 2020);

INSERT INTO podcast(id, end_year)
VALUES(116, NULL);

/* Episode Table: */
INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(107,'The Pilo', 1, 3064, 93832);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(107,'Diversity Day', 2, 2838, 67343);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(107, 'Health Care with Rainn Wilson', 3, 3245, 84342);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(111, 'Guest: Will Ferrell', 1, 267, 146524);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(111, 'Guest: Kristen Bell', 2, 358, 256244);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(111, 'Guest: Adam Sandler', 9, 3033, 98547);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(115, 'Sex Tapes & First Dates', 1, 3400, 87665);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(116, 'What is Capture the Flag (CTF)?', 1, 2320, 1337);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(116, 'How to get into Capture the Flag (CTF)?', 2, 3230, 13337);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(116, 'nooode DEF CON 28 CTF Challenge w/ Guest kaptain', 3, 2752, 133337);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(116, 'Founding of OOO and gameboooy DEF CON 28 CTF Challenge w/ Guest Jeff', 4, 3467, 1333337);

INSERT INTO episode(id, title, episode_number, duration, view_count)
VALUES(116, 'ropshipai with anton00b and Jay, Corwin, and Matt from PPP', 5, 5153, 13333337); 

/* Publisher Table: */
INSERT INTO publisher(id, name)
VALUES(301, 'Interscope Records');

INSERT INTO publisher(id, name)
VALUES(302, 'Epic Records');

INSERT INTO publisher(id, name)
VALUES(303, 'EMI Records');

INSERT INTO publisher(id, name)
VALUES (304, 'Apple Records');

INSERT INTO publisher(id, name)
VALUES (305, 'Big Hit Entertainment');

/* Playlist Table: */
INSERT INTO playlist(id, name, owner)
VALUES(701,'Pop PLAYLIST', 'Danial');

INSERT INTO playlist(id, name, owner)
VALUES(702,'KPOP PLAYLIST', 'Luis');

INSERT INTO playlist(id, name, owner)
VALUES(703, 'COMEDY PLAYLIST', 'Bailey');

INSERT INTO playlist(id, name, owner)
VALUES(704, 'ROCK PLAYLIST', 'Momen');

INSERT INTO playlist (id, name, owner)
VALUES(705, 'OLDIES PLAYLIST', 'Sophia');

INSERT INTO playlist (id, name, owner)
VALUES(706, 'MODERN PLAYLIST', 'Jacob');

INSERT INTO playlist (id, name, owner)
VALUES( 707, 'FAMOUS PEOPLE TALKING', 'Timestamps');

INSERT INTO playlist (id, name, owner)
VALUES (708, 'CYBER NERD TALK', 'DJ Huang');

/* Organization Table: */

INSERT INTO organization(id, name)
VALUES(501, 'ECHO Awards');

INSERT INTO organization(id, name)
VALUES(502, 'Recording Academy');

INSERT INTO organization(id, name)
VALUES(503, 'Guiness');

/* Award Table: */
INSERT INTO award(organization_id, name, year)
VALUES(501, 'International Band of the Year', 2018);

INSERT INTO award(organization_id, name, year)
VALUES(502, 'Album of the Year', 2018);

INSERT INTO award(organization_id, name, year)
VALUES(503, 'Best Selling Album of All Time', 1984);

/* Person Table: */

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(201, 'United States', 'Taylor Swift', '12/13/1989', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(202, 'United States', 'Jerry Seinfeld', '4/29/1954',  NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES( 203, 'South Korea', 'RM', '9/12/1994', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES( 204, 'South Korea' , 'V', '12/30/1995', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(205, 'South Korea', 'J-Hope', '2/18/1994', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES (206, 'South Korea', 'Jin', '12/4/1992', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(207, 'South Korea', 'Jimin', '10/13/1995', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(208, 'South Korea', 'Jungkook', '9/1/1997', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(209, 'South Korea', 'Suga', '3/9/1993', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(210, 'United States', 'Dan Reynolds', '7/14/1987', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(211, 'United States', 'Wayne Sermon', '6/15/1984', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(212, 'United States', 'Ben McKee', '4/7/1985', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(213, 'United States', 'Daniel Platzman', '9/28/1986', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(214, 'United States', 'John Mulaney', '8/26/1982', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(215, 'United States', 'Bruno Mars', '8/8/1985', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(216, 'United States', 'Angela Kinsey', '6/25/1971', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(217, 'United States', 'Jenna Fischer', '3/7/1974', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(218, 'United States', 'Rainn Wilson', '1/20/1966', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(219, 'United States', 'Michael Jackson', '8/29/1958', '6/25/2009');

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(220, 'England', 'John Lennon', '10/9/1940', '12/8/1980');

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(221, 'England', 'Paul McCartney', '6/18/1942', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(222, 'England', 'George Harrison', '2/15/1943', '11/29/2001');

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(223, 'England', 'Ringo Star', '7/7/1940', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(224, 'England', 'Freddie Mercury', '9/5/1946', '11/24/1991');

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(225, 'United States', 'Jeff Dunham', '4/18/1962', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(226, 'United States', 'Conan O Brien', '4/18/1963', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(227, 'United States', 'Will Ferrell', '7/16/1967', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(228, 'United States', 'Kristen Bell', '7/18/1980', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(229, 'United States', 'Gabriel Iglesias', '7/15/1976', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(230, 'United States', 'Adam Sandler', '9/9/1966', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(231, 'United States', 'Billie Eilish', '12/18/2001', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(232, 'Spain', 'Ana Torroja', '12/28/1959', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(233, 'United States', 'Eugene Lee Yang', '1/18/1986', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(234, 'United States', 'Adam Doupe', '11/11/1111', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(235, 'United States', 'Yan Shoshitaishvili', '01/31/1337', NULL);

INSERT INTO person(id, country, name, date_of_birth, date_of_death)
VALUES(236, 'United States', 'kaptain', '01/13/1373', NULL);

/* Won Table: */
INSERT INTO won(award_name, award_year, organization_id, auditory_media_id)
VALUES('International Band of the Year', 2018, 501, 101);

INSERT INTO won(award_name, award_year, organization_id, auditory_media_id)
VALUES('Album of the Year', 2018, 502, 106);

INSERT INTO won(award_name, award_year, organization_id, auditory_media_id)
VALUES('Best Selling Album of All Time', 1984, 503, 108);


/* Produces Table */
INSERT INTO produces (auditory_media_id, person_id)
VALUES (102, 202);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (104, 203);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (103, 214);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (104, 204);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (104, 205);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (104, 206);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (104, 207);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (104, 208);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (104, 209);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (101, 210);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (101, 211);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (101, 212);

INSERT INTO produces (auditory_media_id, person_id)
VALUES (101, 213);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(107,216);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(107,217);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(108,219);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(109,225);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(111,226);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(105, 231);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(113, 229);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(112, 220);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(112, 221);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(112, 222);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(112, 223);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(110, 224);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(114, 232);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(115, 233);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(116, 234);

INSERT INTO produces (auditory_media_id, person_id)
VALUES(116, 235);

/*Publishes Table:*/

INSERT INTO publishes (auditory_media_id, publisher_id)
VALUES(101,301);

INSERT INTO publishes (auditory_media_id, publisher_id)
VALUES(108,302);

INSERT INTO publishes (auditory_media_id, publisher_id)
VALUES(110, 303);

INSERT INTO publishes (auditory_media_id, publisher_id)
VALUES(112, 304);

INSERT INTO publishes (auditory_media_id, publisher_id)
VALUES(104, 305);

/* Member Of Table: */
INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Natural',101, 701);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Boomerang', 101, 701);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Machine', 101, 701);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Thats What I like', 106, 701);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Dynamite', 104, 702);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Bohemian Rhapsody', 110, 704);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Youre My Best Friend', 110, 704);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Bohemian Rhapsody', 110, 705);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Youre My Best Friend', 110, 705);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Get It Back', 112, 705);
INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Let It Be', 112, 705);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Thats What I like', 106, 706);

INSERT INTO member_of_song_playlist (name, auditory_media_id, playlist_id)
VALUES('Chunky', 106, 706);


/*Member of Episode Playlist */

INSERT INTO member_of_episode_playlist(episode_number, name, auditory_media_id, playlist_id)
VALUES(2, 'Guest: Kristen Bell', 111, 706);

INSERT INTO member_of_episode_playlist(episode_number, name, auditory_media_id, playlist_id)
VALUES(1, 'Guest: Will Ferrell', 111, 706);

INSERT INTO member_of_episode_playlist(episode_number, name, auditory_media_id, playlist_id)
VALUES(4,'Founding of OOO and gameboooy DEF CON 28 CTF Challenge w/ Guest Jeff', 116, 707);

INSERT INTO member_of_episode_playlist(episode_number, name, auditory_media_id, playlist_id)
VALUES(3,'nooode DEF CON 28 CTF Challenge w/ Guest kaptain', 116, 707);

INSERT INTO member_of_episode_playlist(episode_number, name, auditory_media_id, playlist_id)
VALUES(1,'What is Capture the Flag (CTF)?', 116, 707);


/*Member of Comedy Playlist*/
INSERT INTO member_of_comedy_playlist(auditory_media_id, playlist_id)
VALUES(102, 703);

INSERT INTO member_of_comedy_playlist(auditory_media_id, playlist_id)
VALUES(103, 703);

INSERT INTO member_of_comedy_playlist(auditory_media_id, playlist_id)
VALUES(109, 703);

INSERT INTO member_of_comedy_playlist(auditory_media_id, playlist_id)
VALUES(113, 703);


/* Guest Appearance Table: */
INSERT INTO guest_appearance (person_id, episode_number, title, podcast_id)
VALUES(218, 3, 'Health Care with Rainn Wilson',107);

INSERT INTO guest_appearance (person_id, episode_number, title, podcast_id)
VALUES(227, 1, 'Guest: Will Ferrell',111);

INSERT INTO guest_appearance (person_id, episode_number, title, podcast_id)
VALUES(228, 2, 'Guest: Kristen Bell',111) ;

INSERT INTO guest_appearance (person_id, episode_number, title, podcast_id)
VALUES(230, 9, 'Guest: Adam Sandler',111) ;

INSERT INTO guest_appearance (person_id, episode_number, title, podcast_id)
VALUES(236, 3, 'nooode DEF CON 28 CTF Challenge w/ Guest kaptain',116) ;



