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
