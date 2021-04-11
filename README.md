# sparkify-modeling-with-cassandra


## Getting Started


## Summary

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to.


## Schema

#### **Base on Columns family**
* It's compounded by three tables response what the project needs artists _by_ sessionId, artists_by_userid, and artists_by_song


#### **Tables**
* artists_by_sessionId --1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
    ( artist, song, length, sessionId, itemInSession )
    
* artists_by_userid -- 2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
    ( artist , song, firstName, lastName, userId, sessionId, itemInSession )
    
* artists_by_song -- 3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
    ( song, firstName, lastName, userId )


## Prerequisites/Installing

In order to run the project have to be intalled following programs

### Git

Go to the [oficial page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and choose your OS


### Python

* macOS and OS X

```
$ xcode-select --install
```

or through brew

```
$ brew install openssl xz gdbm
```


* Linux

```
$ sudo apt-get update
$ sudo apt-get build-dep python3.6
```

### psycopg2

```
$ pip install psycopg2
```

### Pandas

```
$ pip install pandas
```


## Project Structure

    .
    ├── event_data                           # cvs files in which contains the data
    ├── main.py                              # create the kwyspace ans tables 
    ├── queries.cql                          # queries to reesponds to the challengue
    ├── Project_1B_ Project_Template.ipynb   # book that contain the process
    └── README.md



## Author

* **Enrique Yepez** - *Prject Data Modeling with Apache Cassandra* - [sparkify-modeling-with-cassandra](https://github.com/enriqueyt/sparkify-modeling-with-cassandra)

