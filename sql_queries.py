# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop     = "DROP TABLE IF EXISTS users"
song_table_drop     = "DROP TABLE IF EXISTS songs"
artist_table_drop   = "DROP TABLE IF EXISTS artists"
time_table_drop     = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays 
(
    songplay_id SERIAL8 PRIMARY KEY, 
    start_time  CHAR(18) NOT NULL, 
    user_id     INT NOT NULL, 
    level       CHAR(4) NOT NULL, 
    song_id     CHAR(18), 
    artist_id   CHAR(18), 
    session_id  INT NOT NULL, 
    location    VARCHAR, 
    user_agent  VARCHAR NOT NULL
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users 
(
    user_id    INT PRIMARY KEY,
    first_name VARCHAR NOT NULL, 
    last_name  VARCHAR NOT NULL, 
    gender     CHAR, 
    level      CHAR(4) NOT NULL
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs 
(
    song_id   CHAR(18) PRIMARY KEY, 
    title     VARCHAR NOT NULL, 
    artist_id CHAR(18) NOT NULL, 
    year      INT NOT NULL, 
    duration  REAL NOT NULL
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists 
(
    artist_id CHAR(18) PRIMARY KEY, 
    name      VARCHAR NOT NULL, 
    location  VARCHAR, 
    latitude  REAL, 
    longitude REAL
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time 
(
    start_time CHAR(15) PRIMARY KEY, 
    hour       INT NOT NULL, 
    day        INT NOT NULL, 
    week       INT NOT NULL, 
    month      INT NOT NULL, 
    year       INT NOT NULL, 
    weekday    INT NOT NULL
)
""") 

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays 
    (start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
INSERT INTO users 
    (user_id,first_name,last_name,gender,level) 
    VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO UPDATE SET 
    level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs 
    (song_id,title,artist_id,year,duration) 
    VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING
""") 
 
artist_table_insert = ("""
INSERT INTO artists 
    (artist_id,name,location,latitude,longitude) 
    VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""
INSERT INTO time 
    (start_time,hour,day,week,month,year,weekday) 
    VALUES (%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id 
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
WHERE s.title = %s
""")

# QUERY LISTS

create_table_queries = [
    songplay_table_create, 
    user_table_create, 
    song_table_create, 
    artist_table_create, 
    time_table_create
]

drop_table_queries = [
    songplay_table_drop, 
    user_table_drop, 
    song_table_drop, 
    artist_table_drop, 
    time_table_drop
]