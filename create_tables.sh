CREATE TABLE "charity" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(128) NOT NULL,
    "youtube_url" varchar(256),
    "up_votes" integer NOT NULL
);
INSERT INTO "charity" VALUES(1,'Boys and Girls Club','http://youtu.be/-pr-xzajQo0',0);
INSERT INTO "charity" VALUES(2,'Seat Belts Save','http://youtu.be/WlP9aJnzyZw',0);
CREATE TABLE "company" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(128) NOT NULL
);
INSERT INTO "company" VALUES(1,'Digital Ocean');
INSERT INTO "company" VALUES(2,'Merck');
CREATE TABLE "campaign" (
    "id" integer NOT NULL PRIMARY KEY,
    "charity_id" integer NOT NULL,
    "company_id" integer NOT NULL,
    "dollars_per_upvote" integer NOT NULL,
    "ad_url" varchar(256)
);
INSERT INTO "campaign" VALUES(1,1,1,1,"http://pandodaily.files.wordpress.com/2013/08/digital-ocean-logo-4x3.png");
INSERT INTO "campaign" VALUES(2,2,2,1,"http://www.merck.com/img/merck_be_well_green_gray.png");
