# Spudify User Manual
*Spudify* is a project for Database Management with the intention of enabling users to take control of their audio preferences. Whether that includes songs, podcast episodes, or comedy specials, users are able to access our database of carefully selected auditory media and create unlimited playlists to their heart’s content.

There are two components within this documentation:

1. Setup & Installation
2. Walkthrough & Navigation

## Setup & Installation
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

## Walkthrough & Navigation
  Once setup is complete, the user can run the application and be presented with the following landing screen.
  <pic>
  
### Viewing All Media

### Filtering

### Creating a New Playlist

### Viewing Album and Podcast Details

### Adding to a Playlist

### Removing from a Playlist

### Deleting a Playlist

### Stopping the Application
  
  
