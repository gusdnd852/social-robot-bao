import api.api_weather as weather
from hanspell.spell_checker import fix


def response(named_entity):
    keyword_group = named_entity[0]
    entity_group = named_entity[1]
    date = []
    location = []

    for k in zip(keyword_group, entity_group):
        if 'DATE' in k[1]:
            date.append(k[0])
        elif 'LOCATION' in k[1]:
            location.append(k[0])

    if len(date) == 0:
        date.append('오늘')

    if len(location) == 0:
        while len(location) == 0:
            print('> ' + fix('지역을 말해주세요 : '), end='')
            loc = input()
            if loc is not None and loc.replace(' ', '') != '':
                location.append(loc)

    if '오늘' in date:
        return weather.today_weather(' '.join(location))
    elif date[0] == '내일':
        return weather.tomorrow_weather(' '.join(location))
    elif '모레' in date or '내일모레' in date:
        return weather.after_tomorrow_weather(' '.join(location))
    return "그 기능은 아직 배우고 있어요"


a = (['내일', '관악구', '날씨', '알려줘'], ['B-DATE', 'B-LOCATION', 'O', 'O'])
response(a)