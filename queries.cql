CREATE KEYSPACE IF NOT EXISTS sparkify
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };


--1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4

CREATE TABLE IF NOT EXISTS artists_by_sessionId (
    sessionId INT,
    itemInSession INT,
    artist TEXT,
    song TEXT,
    length FLOAT,
    PRIMARY KEY (sessionId, itemInSession)
);

INSERT INTO artists_by_sessionId (sessionId, itemInSession, artist, song, length) VALUES (%s, %s, %s, %s, %s)

SELECT
    artist,
    song,
    length
FROM
    artists_by_sessionId
WHERE 
    sessionId = 637 AND itemInSession = 4


-- 2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182

CREATE TABLE IF NOT EXISTS artists_by_userid (
    userId INT,
    sessionId INT,
    artist TEXT,
    song TEXT,
    firstName TEXT,
    lastName TEXT,
    itemInSession INT,
    PRIMARY KEY ((userid, sessionid), itemInSession, firstName, lastName)
);

INSERT INTO artists_by_userid (sessionId, itemInSession, artist, song, firstName, lastName, userId) VALUES (%s, %s, %s, %s, %s, %s, %s)

SELECT
    artist,
    song,
    firstName,
    lastName
FROM
    artists_by_userid
WHERE 
    userid = 10 and sessionid = 182


-- 3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

CREATE TABLE IF NOT EXISTS artists_by_song (
    song TEXT,
    userId INT,
    firstName TEXT,
    lastName TEXT,
    PRIMARY KEY (song, userId)
);

INSERT INTO artists_by_song (userId, song, firstName, lastName) VALUES (%s, %s, %s, %s)


SELECT
  firstName,
  lastName
FROM
  artists_by_sessionId
WHERE 
  song = 'All Hands Against His Own'


--- Drop tables


DROP TABLE artists_by_sessionId;
DROP TABLE artists_by_userid;
DROP TABLE artists_by_song;
