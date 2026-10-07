"""Чтение и запись каталога космоса в формате XML."""

import xml.dom.minidom

from data import data


class dataxml(data):
    def read(self):
        dom = xml.dom.minidom.parse(self.getInp())
        dom.normalize()
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == "astronaut"):
                code, surname, name, secname = 0, "", "", ""
                for t in node.attributes.items():
                    if t[0] == "code":
                        code = int(t[1])
                    if t[0] == "name":
                        name = t[1]
                    if t[0] == "surname":
                        surname = t[1]
                    if t[0] == "secname":
                        secname = t[1]
                self.getLib().createAstronaut(code, surname, name, secname)

            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == "agency"):
                code, name, shortname = 0, "", ""
                for t in node.attributes.items():
                    if t[0] == "code":
                        code = int(t[1])
                    if t[0] == "name":
                        name = t[1]
                    if t[0] == "shortname":
                        shortname = t[1]
                self.getLib().createAgency(code, name, shortname)

            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == "mission"):
                code, name, img, agency, year, days = 0, "", "", None, 0, 0
                for t in node.attributes.items():
                    if t[0] == "code":
                        code = int(t[1])
                    if t[0] == "name":
                        name = t[1]
                    if t[0] == "img":
                        img = t[1]
                    if t[0] == "year":
                        year = int(t[1])
                    if t[0] == "days":
                        days = int(t[1])
                    if t[0] == "agency":
                        agency = self.getLib().getAgency(int(t[1]))
                m = self.getLib().createMission(code, name, agency, year, days, img)
                for n in node.childNodes:
                    if (n.nodeType == n.ELEMENT_NODE) and (n.nodeName == "astronaut"):
                        for t in n.attributes.items():
                            if t[0] == "code":
                                person = self.getLib().getAstronaut(int(t[1]))
                                if person and m:
                                    m.appendAstronaut(person)

    def write(self):
        dom = xml.dom.minidom.Document()
        root = dom.createElement("cosmos")
        dom.appendChild(root)

        for a in self.getLib().getAstronautList():
            aut = dom.createElement("astronaut")
            aut.setAttribute("code", str(a.getCode()))
            aut.setAttribute("surname", a.getSurname())
            aut.setAttribute("name", a.getName())
            aut.setAttribute("secname", a.getSecname())
            root.appendChild(aut)

        for p in self.getLib().getAgencyList():
            ag = dom.createElement("agency")
            ag.setAttribute("code", str(p.getCode()))
            ag.setAttribute("name", p.getName())
            ag.setAttribute("shortname", p.getShortname())
            root.appendChild(ag)

        for m in self.getLib().getMissionList():
            ms = dom.createElement("mission")
            ms.setAttribute("code", str(m.getCode()))
            ms.setAttribute("name", m.getName())
            ms.setAttribute("img", m.getImg())
            ms.setAttribute("year", str(m.getYear()))
            ms.setAttribute("days", str(m.getDays()))
            agency_code = m.getAgencyCode()
            ms.setAttribute("agency", str(agency_code) if agency_code is not None else "")
            for ac in m.getAstronautCodes():
                aut = dom.createElement("astronaut")
                aut.setAttribute("code", str(ac))
                ms.appendChild(aut)
            root.appendChild(ms)

        with open(self.getOut(), "w", encoding="utf-8") as f:
            f.write(dom.toprettyxml())
