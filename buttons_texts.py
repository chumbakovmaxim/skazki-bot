import tg_types as t

fairy_tail_text = 'Сказки'
about_bot_text = 'О боте'
back_text = 'Вернуться назад ↩️'
#
# topics: list[t.TopicItem] = [
#     {'text': 'Вопросы общей психологии', 'callback_data': '0'},
#     {'text': 'Психология общения', 'callback_data': '1'},
#     {'text': 'Понять себя', 'callback_data': '2'},
#     {'text': 'Семья', 'callback_data': '3'},
#     {'text': 'Дети', 'callback_data': '4'},
#     {'text': 'Школа', 'callback_data': '5'},
#     {'text': 'Иное', 'callback_data': '6'},
# ]
#
# sub_topics: dict[str, list[t.TopicItem]] = {
#     '0': [
#         {'text': 'Мотивы', 'callback_data': '00'},
#         {'text': 'Память', 'callback_data': '01'},
#         {'text': 'Внимание', 'callback_data': '02'},
#         {'text': 'Потребности', 'callback_data': '03'},
#         {'text': 'Характер', 'callback_data': '04'},
#         {'text': 'Мышление', 'callback_data': '05'},
#         {'text': 'Темперамент', 'callback_data': '06'},
#         {'text': 'Способности', 'callback_data': '07'},
#         {'text': 'Воображение', 'callback_data': '08'},
#     ],
#     '1': [
#         {'text': 'Конфликты', 'callback_data': '10'},
#         {'text': 'Комплименты', 'callback_data': '11'},
#         {'text': 'Другая точка зрения', 'callback_data': '12'},
#         {'text': 'Речь', 'callback_data': '13'},
#         {'text': 'Дружба', 'callback_data': '14'},
#         {'text': 'Чувство одиночества', 'callback_data': '15'},
#         {'text': 'Взаимопонимание', 'callback_data': '16'},
#         {'text': 'Другое', 'callback_data': '17'},
#     ],
#     '2': [
#         {'text': 'Развод родителей', 'callback_data': '20'},
#         {'text': 'Появление брата / сестры', 'callback_data': '21'},
#         {'text': 'Не такой, как все', 'callback_data': '22'},
#         {'text': 'Любовь к старшим', 'callback_data': '23'},
#         {'text': 'Роли в семье', 'callback_data': '24'},
#         {'text': 'Выбор своего пути', 'callback_data': '25'},
#     ],
#     '3': [
#         {'text': 'Непослушание детей', 'callback_data': '30'},
#         {'text': 'Разногласия в воспитании', 'callback_data': '31'},
#         {'text': 'Детская агрессия', 'callback_data': '32'},
#         {'text': 'Жадность, детский эгоцентризм', 'callback_data': '33'},
#         {'text': 'Детская ложь', 'callback_data': '34'},
#         {'text': 'Страхи', 'callback_data': '35'},
#         {'text': 'Тревога за детей', 'callback_data': '36'},
#         {'text': 'Воровство, детская кража', 'callback_data': '37'},
#         {'text': 'Застенчивость', 'callback_data': '38'},
#     ],
#     '4': [
#         {'text': 'Личностный рост', 'callback_data': '40'},
#         {'text': 'Жизненное предназначение', 'callback_data': '41'},
#         {'text': 'Понимание своего состояния', 'callback_data': '42'},
#         {'text': 'Приятие себя', 'callback_data': '43'},
#         {'text': 'Депрессия', 'callback_data': '44'},
#         {'text': 'Враждебность', 'callback_data': '45'},
#         {'text': 'Слава', 'callback_data': '46'},
#         {'text': 'Тяга к обмену', 'callback_data': '47'},
#         {'text': 'Умение делать выбор', 'callback_data': '48'},
#         {'text': 'Жить настоящим', 'callback_data': '49'},
#         {'text': 'Достижение цели', 'callback_data': '410'},
#     ],
#     '5': [
#         {'text': 'Школьная адаптация', 'callback_data': '50'},
#         {'text': 'Отношение к вещам', 'callback_data': '51'},
#         {'text': 'Отношение к урокам, к знаниям', 'callback_data': '52'},
#         {'text': 'Здоровье', 'callback_data': '53'},
#         {'text': 'Конфликты', 'callback_data': '54'},
#     ],
#     '6': [
#         {'text': 'Понимание другого человека', 'callback_data': '60'},
#         {'text': 'Творчество', 'callback_data': '61'},
#         {'text': 'Счастье рядом', 'callback_data': '62'},
#         {'text': 'Взаимопомощь', 'callback_data': '63'},
#         {'text': 'Бережливое отношение к планете', 'callback_data': '64'},
#         {'text': 'Новый год', 'callback_data': '65'},
#         {'text': 'Спокойной ночи', 'callback_data': '66'},
#     ],
#
# }
#
# fairy_tails: dict[str, list[t.TopicItem]] = {
#     '00': [
#         {'text': 'Сказка о борьбе мотивов', 'callback_data': '000'} #
#     ],
#     '01': [
#         {'text': 'Сказка о видах памяти и карасе, который был невиновен', 'callback_data': '010'} #
#     ],
#     '02': [
#         {'text': 'Сказка о внимательном Иванушке', 'callback_data': '020'},#
#         {'text': 'Лесное искусство', 'callback_data': '021'}, #
#     ],
#     '03': [
#         {'text': 'Сказка о волшебницах-потребностях и наколдованных эмоциях', 'callback_data': '030'},#
#     ],
#     '04': [
#         {'text': 'Сказка о деревьях-характерах', 'callback_data': '040'},#
#     ],
#     '05': [
#         {'text': 'Сказка о профессоре Мышлении и злом драконе', 'callback_data': '050'},#
#     ],
#     '06': [
#         {'text': 'Сказка о типах темперамента', 'callback_data': '060'},#
#     ],
#     '07': [
#         {'text': 'Сказка о цветах способностей', 'callback_data': '070'},#
#         {'text': 'Сказка о любви', 'callback_data': '071'},
#         {'text': 'Лёва в цирке', 'callback_data': '072'},#
#     ],
#     '08': [
#         {'text': 'Сказкодышащий дракон', 'callback_data': '080'},
#         {'text': 'Игра в разгадки', 'callback_data': '081'}, #
#         {'text': 'Выставка за стеклом', 'callback_data': '082'},#
#         {'text': 'Герой', 'callback_data': '083'},#
#     ],
#     '10': [
#         {'text': 'Сказка о конфликте и контакте', 'callback_data': '100'}
#     ],
#     '11': [
#         {'text': 'Сказка о комплименте', 'callback_data': '110'}
#     ],
#     '12': [
#         {'text': 'Сказка о другой точке зрения', 'callback_data': '120'}
#     ],
#     '13': [
#         {'text': 'Сказка о речке Речь', 'callback_data': '130'}
#     ],
#     '14': [
#         {'text': 'Сказка о дружбе и ее потере', 'callback_data': '140'},
#         {'text': 'Друзья', 'callback_data': '141'},
#         {'text': 'Сказка про Семечку и сиреневых ежиков', 'callback_data': '142'},#
#         {'text': 'Жемчужная сказка', 'callback_data': '143'},#
#         {'text': 'Цепь', 'callback_data': '144'},#
#     ],
#     '15': [
#         {'text': 'Колючка', 'callback_data': '150'},#
#         {'text': 'Мотылек', 'callback_data': '151'},
#         {'text': 'Котенок', 'callback_data': '152'},#
#     ],
#     '16': [
#         {'text': 'Разговоры с кукушкой', 'callback_data': '160'},
#     ],
#     '17': [
#         {'text': 'Сказка о волшебных зеркалах', 'callback_data': '170'},
#     ],
#     '20': [
#         {'text': 'Полосатая история', 'callback_data': '200'},
#     ],
#     '21': [
#         {'text': 'День рождения старшего брата', 'callback_data': '210'},
#         {'text': 'Сестра на удачу', 'callback_data': '211'},
#     ],
#     '22': [
#         {'text': 'Дело не в точках', 'callback_data': '220'},
#     ],
#     '23': [
#         {'text': 'Сказка про Семечку и сиреневых ежиков', 'callback_data': '142'}, #!!!
#     ],
#     '24': [
#         {'text': 'Семейство носовых платочков', 'callback_data': '240'},#
#     ],
#     '25': [
#         {'text': 'Неговорящая фамилия', 'callback_data': '250'},#
#     ],
#     '30': [
#         {'text': 'Непоседа или сказка о том, как облака превращаются в грозовые тучи', 'callback_data': '300'},
#         {'text': 'Золотая рыбка', 'callback_data': '301'},#
#     ],
#     '31': [
#         {'text': 'Няня для медвежонка', 'callback_data': '310'},#
#     ],
#     '32': [
#         {'text': 'Праздник дружбы', 'callback_data': '320'},#
#     ],
#     '33': [
#         {'text': 'Песчаный вулкан', 'callback_data': '330'},
#     ],
#     '34': [
#         {'text': 'Светофорчик', 'callback_data': '340'},
#     ],
#     '35': [
#         {'text': 'Монстрик из шкафа', 'callback_data': '350'},
#         {'text': 'Светлячки', 'callback_data': '351'},
#         {'text': 'Как зайчик воды перестал бояться', 'callback_data': '352'},#
#         {'text': 'Страус', 'callback_data': '353'},
#     ],
#     '36': [
#         {'text': 'Морская история', 'callback_data': '360'},
#         {'text': 'Птенец', 'callback_data': '361'},#
#     ],
#     '37': [
#         {'text': 'Калейдоскоп', 'callback_data': '370'},
#     ],
#     '38': [
#         {'text': 'Талисман', 'callback_data': '380'},#
#     ],
#     '40': [
#         {'text': 'Гусеница', 'callback_data': '400'},
#         {'text': 'Кедр', 'callback_data': '401'},#
#         {'text': 'Дорога', 'callback_data': '402'},
#         {'text': 'Ласточка', 'callback_data': '403'},#
#         {'text': 'Простая и невероятная история о дельталетике', 'callback_data': '404'},
#         {'text': 'Путь', 'callback_data': '405'},
#         {'text': 'Ручейки', 'callback_data': '406'},
#         {'text': 'Сказка о любви', 'callback_data': '407'},
#         {'text': 'Фонарики', 'callback_data': '408'},
#         {'text': 'Обиженный одуванчик', 'callback_data': '409'},
#     ],
#     '41': [
#         {'text': 'Ресурсы черствого пряника', 'callback_data': '410'},
#         {'text': 'Простая и невероятная история о дельталетике', 'callback_data': '411'},
#         {'text': 'Кедр', 'callback_data': '412'},
#         {'text': 'Желуди', 'callback_data': '413'},
#         {'text': 'Колобок', 'callback_data': '414'},
#         {'text': 'Правдивый рассказ о лыжах', 'callback_data': '415'},
#         {'text': 'Поезд наизнанку', 'callback_data': '416'},
#         {'text': 'Сугроб и ручеек', 'callback_data': '417'},
#         {'text': 'Глиняный ляп', 'callback_data': '418'},
#         {'text': 'Кленовый листок', 'callback_data': '419'},
#         {'text': 'История гусиного перышка', 'callback_data': '4110'},
#         {'text': 'Гриб, который рос', 'callback_data': '4111'},
#     ],
#     '42': [
#         {'text': 'Болезнь', 'callback_data': '420'},
#         {'text': 'Горошинка', 'callback_data': '421'},
#         {'text': 'Ресурсы черствого пряника', 'callback_data': '422'},
#         {'text': 'Ушки на макушке. Сказка про Леву', 'callback_data': '423'},
#         {'text': 'Таблетки от несладкой жизни', 'callback_data': '424'},
#         {'text': 'Счастье', 'callback_data': '425'},
#         {'text': 'Малыш и ангел', 'callback_data': '426'},
#     ],
#     '43': [
#         {'text': 'Волшебный ключ', 'callback_data': '430'},
#         {'text': 'Коряга', 'callback_data': '431'},
#         {'text': 'Принять свое счастье', 'callback_data': '432'},
#         {'text': 'Многоголосие молчания', 'callback_data': '433'},
#         {'text': 'Когда вырастают крылья', 'callback_data': '434'},
#         {'text': 'Манная тётя', 'callback_data': '435'},
#     ],
#     '44': [
#         {'text': 'Ласточка', 'callback_data': '440'},
#     ],
#     '45': [
#         {'text': 'Сокровище', 'callback_data': '450'},
#     ],
#     '46': [
#         {'text': 'Всемирная слава', 'callback_data': '460'},
#     ],
#     '47': [
#         {'text': 'Джодди-Менялка', 'callback_data': '470'},
#     ],
#     '48': [
#         {'text': 'Бабочка, стремящаяся к солнцу', 'callback_data': '480'},
#         {'text': 'Ручейки', 'callback_data': '481'},
#     ],
#     '49': [
#         {'text': 'Золотой дождь', 'callback_data': '490'},
#     ],
#     '410': [
#         {'text': 'Бабочка', 'callback_data': '4100'},
#         {'text': 'О чем мечтали камни', 'callback_data': '4102'},
#         {'text': 'Подъемник на небо', 'callback_data': '4103'},
#     ],
#     '50': [
#         {'text': 'Создание Лесной школы', 'callback_data': '500'},
#         {'text': 'Букет для учителя', 'callback_data': '501'},
#         {'text': 'Смешные страхи', 'callback_data': '502'},
#         {'text': 'Игры в школе', 'callback_data': '503'},
#         {'text': 'Школьные правила', 'callback_data': '504'},
#         {'text': 'Счастливая ручка', 'callback_data': '505'},
#     ],
#     '51': [
#         {'text': 'Собирание портфеля', 'callback_data': '510'},
#         {'text': 'Белочкин сон', 'callback_data': '511'},
#         {'text': 'Госпожа Аккуратность', 'callback_data': '512'},
#         {'text': 'Жадность', 'callback_data': '513'},
#         {'text': 'Волшебное яблоко', 'callback_data': '514'},
#         {'text': 'Подарки в День рождения', 'callback_data': '515'},
#     ],
#     '52': [
#         {'text': 'Домашнее задание', 'callback_data': '520'},
#         {'text': 'Школьные оценки', 'callback_data': '521'},
#         {'text': 'Ленивец', 'callback_data': '522'},
#         {'text': 'Списывание', 'callback_data': '523'},
#         {'text': 'Подсказка', 'callback_data': '524'},
#         {'text': 'Гордость школы', 'callback_data': '525'},
#     ],
#     '53': [
#         {'text': 'Режим. Телевизор', 'callback_data': '530'},
#         {'text': 'Бабушкин помощник', 'callback_data': '531'},
#         {'text': 'Прививка', 'callback_data': '532'},
#         {'text': 'Больной друг', 'callback_data': '533'},
#     ],
#     '54': [
#         {'text': 'Ябеда', 'callback_data': '540'},
#         {'text': 'Шапка-невидимка (демонстративное поведение)', 'callback_data': '541'},
#         {'text': 'Задача для Лисенка (ложь)', 'callback_data': '542'},
#         {'text': 'Спорщик', 'callback_data': '543'},
#         {'text': 'Обида', 'callback_data': '544'},
#         {'text': 'Хвосты (межгрупповые конфликты)', 'callback_data': '545'},
#         {'text': 'Драки', 'callback_data': '546'},
#         {'text': 'Грубые слова', 'callback_data': '547'},
#         {'text': 'Дружная страна (межполовые конфликты)', 'callback_data': '548'},
#     ],
#     '60': [
#         {'text': 'Бабочка и жук', 'callback_data': '600'},
#         {'text': 'Бесконечные чипсы', 'callback_data': '601'},
#         {'text': 'Обитая среди животных', 'callback_data': '602'},
#     ],
#     '61': [
#         {'text': 'Волшебство мастера', 'callback_data': '610'},
#         {'text': 'Бумага для мыслей', 'callback_data': '611'},
#         {'text': 'Сказка о маленьком сказочнике', 'callback_data': '612'},
#     ],
#     '62': [
#         {'text': 'Бродячий подсолнух', 'callback_data': '620'},
#         {'text': 'Человек', 'callback_data': '621'},
#     ],
#     '63': [
#         {'text': 'Обыкновенный блокнот', 'callback_data': '630'},
#         {'text': 'Секунденок', 'callback_data': '631'},
#         {'text': 'Муравей и термиты', 'callback_data': '632'},
#         {'text': 'Новогодняя история, как медвежонок научился дарить подарки', 'callback_data': '633'},
#         {'text': 'Как Пых решил стать Суперпыхом', 'callback_data': '634'},
#     ],
#     '64': [
#         {'text': 'Вся правда о драконах', 'callback_data': '640'},
#         {'text': 'Невероятные приключения крышечки', 'callback_data': '641'},
#     ],
#     '65': [
#         {'text': 'Новогоднее чудо для Лёвы', 'callback_data': '650'},
#         {'text': 'Дед Мороз, который верил в себя', 'callback_data': '651'},
#         {'text': 'Лошадиная ёлочка', 'callback_data': '652'},
#     ],
#     '66': [
#         {'text': 'Мудрая песочная горка', 'callback_data': '660'},
#     ],
# }
