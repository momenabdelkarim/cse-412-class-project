# Spudify User Manual
*Spudify* is a project for Database Management with the intention of enabling users to take control of their audio preferences. Whether that includes songs, podcast episodes, or comedy specials, users are able to access our database of carefully selected auditory media and create unlimited playlists to their heart’s content.

There are two components within this documentation:

1. [Setup & Installation](https://github.com/momenabdelkarim/cse-412-class-project/blob/main/README.md#setup--installation)
2. [Walkthrough & Navigation](https://github.com/momenabdelkarim/cse-412-class-project/blob/main/README.md#walkthrough--navigation)

# Setup & Installation
  The setup and installation involves setting up the database, editing the correct files, and starting up the application with the correct data loaded. This procedure should be simple as long as all the pre-requisites are covered.

### Clone Repository
  The repository must first be cloned to ease the package dependencies and installation. Additionally, it should be noted that the development of the application was under **Pycharm Professional**; therefore, to properly run the application without any issues, use the recommended IDE. Pycharm Community edition is also permissible.

To clone the repository, run the following command:

```
$ git clone https://www.github.com/momenabdelkarim/cse-412-class-project/
```

### Dependencies
  For the database and application to work, the following dependencies must first be installed beforehand with the associated versions:

1. PostgreSQL (v12.4+)
2. Python (v3.8)
3. PyQT5 (v5.15.1)
4. Psychopg2 (Binary v2.8.6)

To install the two Python packages, simply enter the root directory of the project and run the following command:

```
$ pip3 install --user -r requirements.txt
```

### Database Setup
  To setup the database used within the project and ensure that the correct data is populated the steps below should be followed sequentially:

1. Set Environment Variables
2. Initialize Database Structure Folder
3. Start the Database
4. Create a User for the Database
5. Populate Database
6. Verify Data

#### Set Environment Variables
  The following environment variables must be set before initializing the database:

- `PGPORT`
- `PGHOST`

If you are unsure of whether they are already defined, you can echo them appropriately. In our use case, we set the following values to each variable:

```
$ export PGPORT=8888
$ export PGHOST=/tmp
```

The `PGPORT` variable can be changed depending on whether that port is available to you; however, please note that certain port numbers are restricted for various purposes, so we will assume you understand not to set a used port.

#### Initialize Database Structure Folder
  The next step includes setting a path to where the data should be held locally. This is up to your own discretion. In our use case, we initialized our database to a folder in the repository called `database`.

```
$ initdb /path/to/cse-412-class-project/database/
```

#### Start the Database
  The next step is to start the database on the port associated with `PGPORT` and the database root folder. The following command can be used to start the database:

```
pg_ctl -D /path/to/database/root/folder -o '-k /tmp' start
```

The `/path/to/database/root/folder/` is the path set when running the command in ![Initialize Database Structure Folder](#Initalize-Database-Structure-Folder) above.

#### Create a User for the Database
  The next step is to create a user for the database in order to access it. This can be done by running the following command:

```
$ createdb $USER
```

This will create a database with the associated username, `$USER`.

#### Populate Database
  The last step is to populate the database with the appropriate tables and data that we constructed. This is easily completed with a Makefile. The Makefile can be found under `/path/to/cse-412-class-project/phase2/makefile`.

There needs to be one edit made to this Makefile in order for it to work effectively. On `Line 3`, edit the variable `MAKEFILE_PATH` to be set to the path to the Makefile. This would result in the following value as shown below:

```
MAKEFILE_PATH = /path/to/cse-412-class-project/phase2/
```

With the path set, only two make targets need to be ran below:

```
make setup_postgre
make insert_postgre
```

#### Verify Data
  With the above steps complete, you can verify that you are able to connnect to the database via the following command:

```
$ psql -d $USER
```

Once you are connected, you can pose the following query below with the expected results as shown:

```
SELECT * FROM song WHERE song.auditory_media = 101;
```

```
 auditory_media_id |   name    | duration | view_count 
-------------------+-----------+----------+------------
               101 | Natural   |      189 |  621539875
               101 | Boomerang |      188 |   53977701
               101 | Machine   |      182 |   78769871
(3 rows)
```
If you obtain the following three songs and their associated attributes, then you are ready to start the application setup following.

## Application Database Sync
  In order for the application to appropriately recognize the database, we need to make one change in regards to the files inside the `handlers.py` folder located under `/path/to/cse-412-class-project/backend/handlers.py`.

With the file open, **line 8** and **line 12** should be changed to appropriately match the name of your database and username. In this case, the common subsitute for both values will be the output of `echo $USER`.

This results in the `user` and `database` variables to be set to `$USER`. With this step complete, simple run the application via the `driver.py` file located under `/path/to/cse-412-class-project/bin/driver.py` using the **Pycharm** IDE.

# Walkthrough & Navigation
  Once setup is complete, the user can run the application and view the landing screen.
  
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/Landing%20Screen.png width="500">
  
### Viewing All Media
  To view all media that is available on the application, select the "All Media" tab. This will bring up all auditory media objects - albums, podcasts, and comedy specials - that are available to the user. 
  
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/All%20Media%20Tab.png width="500">

### Filtering
  To view a narrower list of auditory media based on genre or rating specifications, select the "Search" button in the lower right-hand corner. This will bring up a new window where a user can specify genre and/or rating parameters to apply to the auditory media in the "All Media" tab. 
  
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/Filtering.png width="500">
  
  To clear a search, a user should select the "Search" button on the "All Media" tab to bring up the filter window and apply the default parameters of genre "---" and rating "0+" to view all auditory media objects available in the database. 
  
### Viewing a Playlist
  To view a playlist, navigate to the "Playlist" tab and double click on a playlist cover to reveal underneath what items belong to that playlist. 
  
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/Playlist%20view.png width="500"> 

### Creating a New Playlist
  To create a new playlist, visit the "Playlist" tab on the main window and scroll horizontally to the right. Click "Create Playlist" and give it a descriptive name. 
  
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/Adding%20a%20new%20playlist.png width="500"> 
  
  To **rename** an existing playlist, right click and select "Rename Playlist" from the dropdown. A playlist name accepts only alphabetical characters and must contain no special symbols or punctuation. 
  To **delete** an existing playlist, right click and select "Delete Playlist" from the dropdown. Note, this action is permanent and deleted playlists cannot be recovered.
  
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/Renaming%20or%20deleting%20playlist.png width="500">

### Auditory Media Details
  To view auditory media details such as songs that are members of an album, episodes that belong to a podcast, or general comedy special information, double click on an auditory media to bring up the details view. 
  
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/Detail%20view.png width="500">
  
  In the details view, users have the option to add an item to a playlist. See [Adding to a Playlist](https://github.com/momenabdelkarim/cse-412-class-project/blob/main/README.md#adding-to-a-playlist) for more information

### Adding to a Playlist
  To add a song, episode, or comedy special to a playlist, navigate to the detail window of the auditory media that contains the item you wish to add to the a playlist - see [Auditory Media Details](https://github.com/momenabdelkarim/cse-412-class-project#auditory-media-details) for more information - and right click on an item and select the a playlist of choice.
  
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/Adding%20item%20to%20playlist.png width="300"> 
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/Adding%20item%20to%20playlist2.png width="300">

### Removing from a Playlist
  To remove a song, episode, or comedy special from a playlist, [navigate to the playlist](https://github.com/momenabdelkarim/cse-412-class-project/blob/main/README.md#viewing-a-playlist) and right click on the item you wish to remove. Select "Remove from this playlist" from the dropdown.
  
  <img src=https://github.com/momenabdelkarim/cse-412-class-project/blob/main/screenshots/Removing%20item%20from%20playlist.png width="500">

### Stopping the Application
  To end the application, select the red exit mark in the upper left-hand corner. 
  
  
