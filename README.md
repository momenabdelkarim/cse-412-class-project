# Spudify User Manual
*Spudify* is a project for Database Management with the intention of enabling users to take control of their audio preferences. Whether that includes songs, podcast episodes, or comedy specials, users are able to access our database of carefully selected auditory media and create unlimited playlists to their heart’s content.

There are two components within this documentation:

1. Setup & Installation
2. Walkthrough & Navigation

## Setup & Installation
  The setup and installation involves setting up the database, editing the correct files, and starting up the application with the correct data loaded. This procedure should simple as long as all the pre-requisites are covered.

### Clone Repository
  The repository must first be cloned to ease the package dependencies and installation. Additionally, it should be noted that the development of the application was under **Pycharm Professional**; therefore, to properly run the application without any issues, use the recommended IDE - Pycharm Community edition is also permissible.

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

## Walkthrough & Navigation

## Set Up
I don't know how this part works and setting up the database with the frontend in a way that will work for the TA? how to install the dependencies and whatnot

they set up their own database and we just give instructions on how to get it all up

## Walkthrough
I'll do the walkthrough with the UI and screenshots explaining the steps
