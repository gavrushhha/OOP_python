"""
Задание 2a. Чтение и запись каталога космических миссий в JSON.

Демонстрация: old.json → объекты cosmos → new.json + вывод в консоль.
"""

from cosmos import cosmos
from datajson import datajson


def sep(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    catalog = cosmos()
    dat = datajson(catalog, "old.json", "new.json")

    sep("1. Чтение old.json")
    dat.read()
    print("Космонавты:", catalog.getAstronautCodes())
    print("Агентства: ", catalog.getAgencyCodes())
    print("Миссии:    ", catalog.getMissionCodes())

    sep("2. Сводки по миссиям")
    for m in catalog.getMissionList():
        print(" •", m.getInfoStr())

    sep("3. Миссии Роскосмоса (agency code=1)")
    for m in catalog.getMissionList():
        if m.getAgencyCode() == 1:
            print(" •", m.getName(), m.getYear(), "—", m.getCrewInfoStr())

    sep("4. Поиск космонавта по коду")
    person = catalog.getAstronaut(1)
    print(person.getInfoStr(), "| код:", person.getCode())

    sep("5. Запись в new.json")
    dat.write()
    print("Записано в", dat.getOut())

    sep("6. Контрольное перечитывание new.json")
    catalog2 = cosmos()
    dat2 = datajson(catalog2, "new.json", "new2.json")
    dat2.read()
    for m in catalog2.getMissionList():
        print(" •", m.getInfoStr())


if __name__ == "__main__":
    main()
