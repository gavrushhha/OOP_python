"""
Задание 3. Чтение и запись каталога космических миссий в SQLite.

Цепочка: old.xml → cosmos → new.sqlite → cosmos → roundtrip.xml + вывод в консоль.
"""

import os

from cosmos import cosmos
from dataxml import dataxml
from datasql import datasql


def sep(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    cat1 = cosmos()
    cat2 = cosmos()

    dxml1 = dataxml(cat1, "old.xml", "new.xml")
    dxml2 = dataxml(cat2, "old.xml", "roundtrip.xml")
    dsql1 = datasql(cat1, "new.sqlite", "new.sqlite")
    dsql2 = datasql(cat2, "new.sqlite", "new.sqlite")

    sep("1. Чтение old.xml")
    dxml1.read()
    print("Миссии:", cat1.getMissionCodes())
    for m in cat1.getMissionList():
        print(" •", m.getInfoStr())

    sep("2. Запись в new.sqlite")
    if os.path.isfile(dsql1.getOut()):
        os.remove(dsql1.getOut())
    dsql1.write()
    print("База сохранена:", dsql1.getOut())

    sep("3. Чтение new.sqlite во второй каталог")
    dsql2.read()
    print("Космонавты:", cat2.getAstronautCodes())
    print("Агентства: ", cat2.getAgencyCodes())
    print("Миссии:    ", cat2.getMissionCodes())

    sep("4. Сводки по миссиям из SQLite")
    for m in cat2.getMissionList():
        print(" •", m.getInfoStr())

    sep("5. Миссии Роскосмоса (agency code=1)")
    for m in cat2.getMissionList():
        if m.getAgencyCode() == 1:
            print(" •", m.getName(), m.getYear(), "—", m.getCrewInfoStr())

    sep("6. Запись roundtrip.xml и сверка")
    dxml2.write()
    print("Записано в", dxml2.getOut())
    print("Число миссий после круга XML→SQLite→XML:", len(cat2.getMissionList()))


if __name__ == "__main__":
    main()
