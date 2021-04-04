import cassandra
from cassandra.cluster import Cluster

def init():
    session, cluster = createKeyspace()
    createTables(session)
    session.shutdown()
    cluster.shutdown()
    
def createTables(session):
    """
    we are going to create all tables needed

    Returns:
        void
    """
    create_artists_by_sessionId(session)
    create_artists_by_userid(session)
    create_artists_by_song(session)

def createKeyspace():
    """
    we are going to create the KeySpace and set it to the session 

    Returns:
        session, cluster
    """
    try: 
        cluster = Cluster(['127.0.0.1']) #If you have a locally installed Apache Cassandra instance
        session = cluster.connect()
    except Exception as e:
        print(e)


    try:
        session.execute("""
        CREATE KEYSPACE IF NOT EXISTS sparkify
        WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };"""
    )

    except Exception as e:
        print(e)

    try:
        session.set_keyspace('sparkify')
    except Exception as e:
        print(e)
    
    return session, cluster
    
def create_artists_by_sessionId(session):
    """
    it's in charge of create new table to filter by session, iten in session and the artist

    Returns:
        void
    """
    query = """
        CREATE TABLE IF NOT EXISTS artists_by_sessionId (
            artist TEXT,
            song TEXT,
            length FLOAT,
            sessionId INT,
            itemInSession INT,
            PRIMARY KEY (sessionId, itemInSession, artist)
        );
    """
    try:
        session.execute(query)
    except Exception as e:
        print(e)

def create_artists_by_userid(session):
    """
    it's in charge of create new table to filter by userid and session

    Returns:
        void
    """
    query = """
        CREATE TABLE IF NOT EXISTS artists_by_userid (
            artist TEXT,
            song TEXT,
            firstName TEXT,
            lastName TEXT
            userId INT,
            sessionId INT,
            itemInSession INT,
            PRIMARY KEY ((userid, sessionid), itemInSession, firstName, lastName)
        );
    """
    try:
        session.execute(query)
    except Exception as e:
        print(e)

def create_artists_by_song(session):
    """
    it's in charge of create new table to filter by song and userId

    Returns:
        void
    """
    query = """
        CREATE TABLE IF NOT EXISTS artists_by_song (
            song TEXT,
            firstName TEXT,
            lastName TEXT,
            userId INT,
            PRIMARY KEY (song, userId)
        );
    """
    try:
        session.execute(query)
    except Exception as e:
        print(e)

def drop_tables(session):
    """
    it's in charge of drop all tables

    Returns:
        void
    """
    query = "DROP TABLE artists_by_sessionId"
    try:
        rows = session.execute(query)
    except Exception as e:
        print(e)

    query = "DROP TABLE artists_by_userid"
    try:
        rows = session.execute(query)
    except Exception as e:
        print(e)

    query = "DROP TABLE artists_by_song"
    try:
        rows = session.execute(query)
    except Exception as e:
        print(e)
if __name__ == "__main__":
    init()