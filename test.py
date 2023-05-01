day = int(input('write your date of birthday: '))
month = input('write your month of birth (e.g. march, july etc): ')
if month == 'march':
    astro = 'Pisces' if (day < 20) else 'Aries'
elif month == 'april':
    astro = 'Aries' if (day < 20) else 'Taurus'
elif month == 'may':
    astro = 'Taurus' if (day < 21) else 'Gemini'
elif month == 'june':
    astro = 'Gemini' if (day < 21) else 'Cancer'
elif month == 'july':
    astro = 'Cancer' if (day < 22) else 'Leo'
elif month == 'august':
    astro = 'Leo' if (day < 21) else 'Virgo'
elif month == 'september':
    astro = 'Virgo' if (day < 23) else 'Libra'
elif month == 'october':
    astro = 'Libra' if (day < 23) else 'Scorpio'
elif month == 'november':
    astro = 'Scorpio' if (day < 22) else 'Sagittarius'
elif month == 'december':
    astro = 'Sagittarius' if (day < 22) else 'Capricorn'
elif month == 'january':
    astro = 'Capricorn' if (day < 20) else 'Aquarius'
elif month == 'february':
    astro = 'Aquarius' if (day < 19) else 'Pisces'
print('Your Astrological astro is :', astro)

if astro == 'Aries':
    print('Не варто витрачати всю енергію на те, щоб заробити більше грошей, оскільки ви навряд чи будете задоволені результатом.')
elif astro == 'Taurus':
    print('Ключ до успіху протягом тижня – це вміння вибрати з десятка справ одну, але найважливішу, та довести її до успішного завершення.')
elif astro == 'Gemini':
    print('Зосередьтеся на найголовнішому і, отже, попрацюйте - тоді цей тиждень допоможе вам значно зміцнити свої позиції.')
elif astro == 'Canser':
    print('Не шкодуйте часу для того, щоб побути на самоті, подумати, спробувати розгадати те, що здається вам незрозумілим.')
elif astro == 'Leo':
    print('Сміливо беріть на себе роль керівника, не бійтеся взяти участь у конкурсі чи змаганні.')
elif astro == 'Virgo':
    print('Не дозволяйте своїм емоціям виходити з-під контролю та брати над вами вгору.')
elif astro == 'Libra':
    print('Має сенс зустрітися зі старими друзями. Найімовірніше, у них накопичилося багато цікавого для вас.')
elif astro == 'Scorpio':
    print('Будьте практичними, раціональними та намагайтеся діяти відповідно до певної системи.')
elif astro == 'Sagittarius':
    print('Гарний час для відряджень, цікавих зустрічей та спілкування.')
elif astro == 'Capricorn':
    print('Відпустіть ситуацію та насолоджуйтесь тим, що маєте.')
elif astro == 'Aquarius':
    print('Напружений тиждень, значно підвищується ймовірність розлучитися з партнером через дурість.')
elif astro == 'Pisces':
    print('Дайте шанс колишньому партнеру, поспілкувавшись, ви знайдете багато нових якостей, які раніше не помічали.')
