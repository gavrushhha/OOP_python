"""
Задание 2.2. Чтение и запись каталога космических миссий в XML.

Демонстрация: old.xml → объекты cosmos → new.xml + вывод в консоль.
"""

from cosmos import cosmos
from dataxml import dataxml


def sep(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    catalog = cosmos()
    dat = dataxml(catalog, "old.xml", "new.xml")

    sep("1. Чтение old.xml")
    dat.read()
    print("Космонавты:", catalog.getAstronautCodes())
    print("Агентства: ", catalog.getAgencyCodes())
    print("Миссии:    ", catalog.getMissionCodes())

    sep("2. Сводки по миссиям (запрос преподавателя)")
    for m in catalog.getMissionList():
        print(" •", m.getInfoStr())

    sep("3. Миссии Роскосмоса (agency code=1)")
    for m in catalog.getMissionList():
        if m.getAgencyCode() == 1:
            print(" •", m.getName(), m.getYear(), "—", m.getCrewInfoStr())

    sep("4. Поиск космонавта по коду")
    person = catalog.getAstronaut(1)
    print(person.getInfoStr(), "| полный код:", person.getCode())

    sep("5. Запись в new.xml")
    dat.write()
    print("Записано в", dat.getOut())

    sep("6. Контрольное перечитывание new.xml")
    catalog2 = cosmos()
    dat2 = dataxml(catalog2, "new.xml", "new2.xml")
    dat2.read()
    for m in catalog2.getMissionList():
        print(" •", m.getInfoStr())


if __name__ == "__main__":
    main()
