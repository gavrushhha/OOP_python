"""
Задание 2.1. Предметная область: космические миссии.

Сущности:
  astronaut — космонавт
  agency    — космическое агентство
  mission   — космическая миссия (экипаж + агентство)
"""

from agency import agency
from astronaut import astronaut
from astronautList import astronautList
from generalList import generalList
from mission import mission


def sep(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    # --- Агентства ---
    roscosmos = agency(1, "Госкорпорация «Роскосмос»", "Роскосмос")
    nasa = agency(2, "National Aeronautics and Space Administration", "NASA")
    esa = agency(3, "European Space Agency", "ESA")

    agencies = generalList()
    agencies.appendItem(roscosmos)
    agencies.appendItem(nasa)
    agencies.appendItem(esa)

    # --- Космонавты ---
    gagarin = astronaut(1, "Гагарин", "Юрий", "Алексеевич")
    titov = astronaut(2, "Титов", "Герман", "Степанович")
    armstrong = astronaut(3, "Армстронг", "Нил", "Олден")
    aldrin = astronaut(4, "Олдрин", "Базз", "")
    terechkova = astronaut(5, "Терешкова", "Валентина", "Владимировна")

    pool = astronautList()
    for a in (gagarin, titov, armstrong, aldrin, terechkova):
        pool.appendItem(a)

    # --- Миссии ---
    vostok1 = mission(1, "Восток-1", roscosmos, year=1961, days=1, img="vostok1.png")
    vostok1.appendAstronaut(gagarin)

    apollo11 = mission(2, "Apollo 11", nasa, year=1969, days=8, img="apollo11.png")
    apollo11.appendAstronaut(armstrong)
    apollo11.appendAstronaut(aldrin)

    vostok6 = mission(3, "Восток-6", roscosmos, year=1963, days=3, img="vostok6.png")
    vostok6.appendAstronaut(terechkova)

    missions = generalList()
    missions.appendItem(vostok1)
    missions.appendItem(apollo11)
    missions.appendItem(vostok6)

    # ========== Запросы ==========

    sep("1. Агентства")
    for a in agencies.getItems():
        print("[%s] %s (%s)" % (a.getCode(), a.getName(), a.getShortname()))

    sep("2. Пул космонавтов")
    print(pool.getInfoStr())
    print("Коды:", pool.getCodes())

    sep("3. Сводки по миссиям")
    for m in missions.getItems():
        print(" •", m.getInfoStr())

    sep("4. Поиск миссии по коду (code=2)")
    found = missions.findByCode(2)
    print(found.getInfoStr())

    sep("5. Детали миссии «Восток-1»")
    print("Название:     ", vostok1.getName())
    print("Год:          ", vostok1.getYear())
    print("Длительность: ", vostok1.getDays(), "дн.")
    print("Эмблема:      ", vostok1.getImg())
    print("Агентство:    ", vostok1.getAgencyName())
    print("Кратко:       ", vostok1.getAgencyShortName())
    print("Код агентства:", vostok1.getAgencyCode())
    print("Коды экипажа: ", vostok1.getAstronautCodes())
    print("Экипаж:       ", vostok1.getCrewInfoStr())

    sep("6. Поиск космонавта в экипаже Apollo 11")
    person = apollo11.getAstronaut(3)
    print(person.getInfoStr())
    print("  Фамилия:", person.getSurname())
    print("  Имя:    ", person.getName())
    print("  Отчество:", person.getSecname())

    sep("7. Миссии агентства Роскосмос (code=1)")
    for m in missions.getItems():
        if m.getAgencyCode() == 1:
            print(" •", m.getName(), m.getYear())

    sep("8. Миссии с участием Гагарина (code=1)")
    for m in missions.getItems():
        if 1 in m.getAstronautCodes():
            print(" •", m.getInfoStr())

    sep("9. Добавление космонавта в экипаж Восток-1")
    vostok1.appendAstronaut(titov)
    print(vostok1.getInfoStr())

    sep("10. Удаление космонавта и очистка экипажа")
    vostok1.removeAstronaut(2)
    print("После remove:", vostok1.getCrewInfoStr())
    vostok1.clearCrew()
    print("После clear: «%s»" % vostok1.getCrewInfoStr())
    vostok1.appendAstronaut(gagarin)
    print("Восстановлено:", vostok1.getInfoStr())

    sep("11. Новый код и createItem / newItem")
    print("Свободный код:", pool.getNewCode())
    leonov = pool.newItem("Леонов", "Алексей", "Архипович")
    print("Добавлен:", leonov.getInfoStr(), "code=", leonov.getCode())

    sep("12. Удаление агентства из списка")
    print("До: ", agencies.getCodes())
    agencies.removeItem(3)
    print("После removeItem(3):", agencies.getCodes())


if __name__ == "__main__":
    main()
