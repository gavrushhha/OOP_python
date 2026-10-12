"""Чтение и запись каталога космоса в базе SQLite."""

import sqlite3 as db

from data import data

emptydb = """
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS mission_astronaut;
DROP TABLE IF EXISTS mission;
DROP TABLE IF EXISTS agency;
DROP TABLE IF EXISTS astronaut;

CREATE TABLE astronaut
(code integer primary key,
 surname text,
 name text,
 secname text);

CREATE TABLE agency
(code integer primary key,
 name text,
 shortname text);

CREATE TABLE mission
(code integer primary key,
 name text,
 img text,
 year integer,
 days integer,
 agency integer references agency(code) on update cascade on delete set null);

CREATE TABLE mission_astronaut
(code integer primary key autoincrement,
 mission integer references mission(code) on update cascade on delete cascade,
 astronaut integer references astronaut(code) on update cascade on delete cascade,
 unique(mission, astronaut));
"""


class datasql(data):
    def read(self):
        conn = db.connect(self.getInp())
        curs = conn.cursor()
        curs.execute("select code,surname,name,secname from astronaut")
        rows = curs.fetchall()
        for r in rows:
            self.getLib().createAstronaut(r[0], r[1], r[2], r[3])

        curs.execute("select code,name,shortname from agency")
        rows = curs.fetchall()
        for r in rows:
            self.getLib().createAgency(r[0], r[1], r[2])

        curs.execute("select code,name,img,year,days,agency from mission")
        rows = curs.fetchall()
        for r in rows:
            agency = self.getLib().getAgency(int(r[5])) if r[5] is not None else None
            self.getLib().createMission(r[0], r[1], agency, r[3], r[4], r[2])

        curs.execute("select mission,astronaut from mission_astronaut")
        rows = curs.fetchall()
        for r in rows:
            m = self.getLib().getMission(r[0])
            person = self.getLib().getAstronaut(r[1])
            if m and person:
                m.appendAstronaut(person)
        conn.close()

    def write(self):
        conn = db.connect(self.getOut())
        curs = conn.cursor()
        curs.executescript(emptydb)

        for a in self.getLib().getAstronautList():
            curs.execute(
                "insert into astronaut(code,surname,name,secname) values(?,?,?,?)",
                (a.getCode(), a.getSurname(), a.getName(), a.getSecname()),
            )

        for p in self.getLib().getAgencyList():
            curs.execute(
                "insert into agency(code,name,shortname) values(?,?,?)",
                (p.getCode(), p.getName(), p.getShortname()),
            )

        for m in self.getLib().getMissionList():
            curs.execute(
                "insert into mission(code,name,img,year,days,agency) values(?,?,?,?,?,?)",
                (
                    m.getCode(),
                    m.getName(),
                    m.getImg(),
                    m.getYear(),
                    m.getDays(),
                    m.getAgencyCode(),
                ),
            )
            for ac in m.getAstronautCodes():
                curs.execute(
                    "insert into mission_astronaut(mission,astronaut) values(?,?)",
                    (m.getCode(), ac),
                )

        conn.commit()
        conn.close()
