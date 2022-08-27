PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE artist (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                biog TEXT NOT NULL,
                releases_uri TEXT NOT NULL,
                external_id INTEGER NOT NULL
            );
INSERT INTO artist VALUES(1,'Circuit Breaker (7)','Circuit Breaker are an Industrial band, consisting of London based brothers Peter and Edward Simpson. ','https://api.discogs.com/artists/3552343/releases',3552343);
CREATE TABLE artist_images (
                id INTEGER PRIMARY KEY,
                width TEXT NOT NULL,
                height TEXT NOT NULL,
                uri TEXT NOT NULL,
                artist_id INTEGER NOT NULL,
                artist_external_id INTEGER NOT NULL,

                FOREIGN KEY (artist_external_id) REFERENCES artist (external_id),
                FOREIGN KEY (artist_id) REFERENCES artist (id)
            );
INSERT INTO artist_images VALUES(1,'500','296','https://i.discogs.com/fylHsufHKr6xQEMXJQnAvRnsJEMOI6fPUVBwdnLbd14/rs:fit/g:sm/q:90/h:296/w:500/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM1NTIz/NDMtMTQxMTIyNTA3/Mi02NDQyLmpwZWc.jpeg',1,3552343);
INSERT INTO artist_images VALUES(2,'600','521','https://i.discogs.com/_wMMxjb4YJCURqAEUzAbFetptf2GpN5ntbtAGZ4Dgho/rs:fit/g:sm/q:90/h:521/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9BLTM1NTIz/NDMtMTQxMTIyNTE0/NS0yODA0LmpwZWc.jpeg',1,3552343);
CREATE TABLE releases (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                year INTEGER NOT NULL,
                link TEXT NOT NULL , 
                external_id INTEGER NOT NULL,
                artist_external_id INTEGER NOT NULL,
                artist_id INTEGER NOT NULL,

                FOREIGN KEY (artist_external_id) REFERENCES artist (external_id),
                FOREIGN KEY (artist_id) REFERENCES artist (id)
            );
INSERT INTO releases VALUES(1,'Grid',2013,'https://api.discogs.com/releases/5099743',5099743,3552343,1);
INSERT INTO releases VALUES(2,'Spore City Survey',2022,'https://api.discogs.com/releases/23646134',23646134,3552343,1);
INSERT INTO releases VALUES(3,'Hands Return To Shake',2018,'https://api.discogs.com/releases/11243074',11243074,3552343,1);
INSERT INTO releases VALUES(4,'The Harbinger Sound Sampler',2017,'https://api.discogs.com/masters/1155379',1155379,3552343,1);
INSERT INTO releases VALUES(5,'Live Life',2017,'https://api.discogs.com/masters/1177776',1177776,3552343,1);
INSERT INTO releases VALUES(6,'My Descent Into Capital',2015,'https://api.discogs.com/masters/884186',884186,3552343,1);
INSERT INTO releases VALUES(7,'TV12 ',2014,'https://api.discogs.com/releases/6109393',6109393,3552343,1);
INSERT INTO releases VALUES(8,'Cairn',2013,'https://api.discogs.com/releases/19910101',19910101,3552343,1);
CREATE TABLE release_images (
                id INTEGER PRIMARY KEY,
                width TEXT NOT NULL,
                height TEXT NOT NULL,
                uri TEXT NOT NULL,
                release_id INTEGER NOT NULL,
                artist_id INTEGER NOT NULL,
                artist_external_id INTEGER NOT NULL,

                FOREIGN KEY (release_id) REFERENCES release (id),
                FOREIGN KEY (artist_external_id) REFERENCES artist (external_id),
                FOREIGN KEY (artist_id) REFERENCES artist (id)
            );
COMMIT;
