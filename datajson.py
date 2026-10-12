"""Чтение и запись каталога космоса в формате JSON."""

import json

from data import data


class datajson(data):
    def read(self):
        with open(self.getInp(), "r", encoding="utf-8") as f:
            data = json.load(f)
        for k in data.keys():
            if k == "astronauts":
                for a in data[k]:
                    code, surname, name, secname = 0, "", "", ""
                    for ak in a.keys():
                        if ak == "code":
                            code = a[ak]
                        if ak == "name":
                            name = a[ak]
                        if ak == "surname":
                            surname = a[ak]
                        if ak == "secname":
                            secname = a[ak]
                    self.getLib().createAstronaut(code, surname, name, secname)
            if k == "agencies":
                for a in data[k]:
                    code, name, shortname = 0, "", ""
                    for ak in a.keys():
                        if ak == "code":
                            code = a[ak]
                        if ak == "name":
                            name = a[ak]
                        if ak == "shortname":
                            shortname = a[ak]
                    self.getLib().createAgency(code, name, shortname)
            if k == "missions":
                for a in data[k]:
                    code, name, img, agency, year, days, crew = 0, "", "", None, 0, 0, []
                    for ak in a.keys():
                        if ak == "code":
                            code = a[ak]
                        if ak == "name":
                            name = a[ak]
                        if ak == "img":
                            img = a[ak]
                        if ak == "year":
                            year = a[ak]
                        if ak == "days":
                            days = a[ak]
                        if ak == "agency":
                            agency = self.getLib().getAgency(int(a[ak]))
                        if ak == "astronauts":
                            crew = a[ak]
                    m = self.getLib().createMission(code, name, agency, year, days, img)
                    for ac in crew:
                        person = self.getLib().getAstronaut(ac)
                        if person and m:
                            m.appendAstronaut(person)

    def write(self):
        data = {"astronauts": [], "agencies": [], "missions": []}
        for a in self.getLib().getAstronautList():
            ad = {}
            ad["code"] = a.getCode()
            ad["surname"] = a.getSurname()
            ad["name"] = a.getName()
            ad["secname"] = a.getSecname()
            data["astronauts"].append(ad)
        for p in self.getLib().getAgencyList():
            pd = {}
            pd["code"] = p.getCode()
            pd["name"] = p.getName()
            pd["shortname"] = p.getShortname()
            data["agencies"].append(pd)
        for m in self.getLib().getMissionList():
            md = {}
            md["code"] = m.getCode()
            md["name"] = m.getName()
            md["img"] = m.getImg()
            md["year"] = m.getYear()
            md["days"] = m.getDays()
            md["agency"] = m.getAgencyCode()
            md["astronauts"] = m.getAstronautCodes()
            data["missions"].append(md)
        with open(self.getOut(), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
