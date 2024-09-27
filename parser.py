import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_rasp():
    ua = UserAgent()
    headers = {'accept': '*/*', 'user-agent': ua.firefox}
    # Получаем HTML-код страницы
    response = requests.get("https://kbp.by/rasp/timetable/view_beta_kbp/?page=stable&cat=group&id=44", headers=headers)
    if response.status_code != 200:
        print(f"Ошибка при загрузке страницы: {response.status_code}")
        return []

    # Парсим HTML-код с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # полный блок с таблицой
    main_block = soup.find('div', id='left_week')
    table = main_block.find('table')
    lines = table.find_all('tr')
    

    

    # Извлекаем информацию о матчах
    # upcoming_matches = []
    # for match in matches_section[:5]:  # Берем только первые 5 матчей
    #     time = match.find('span', class_='broadcast__time').get_text(strip=True)
    #     detail = match.find('a', class_='broadcast__link').get_text(strip=True).replace('Футбол.', '').strip()
    #     upcoming_matches.append({'detail': detail, 'id': simple_hash(detail)})

    return lines

def get_line_pars(line):
    pairs = []
    tds = line.find_all('td')
    try:
        for i in range(1,7):
            try:
                is_replaced = False
                td = tds[i]
                if '<div class="empty-pair"></div>' in str(td) and "pair lw_1 added" not in str(td):
                    pairs.append({
                        'subject_name': '',
                        'teacher_1': '',
                        'teacher_2': '',
                        'group': '',
                        'place': '',
                    })
                    continue
                pair_1 = td.find('div', class_=f'pair lw_{i}')
                if not pair_1:
                    pair_1 = td.find('div', class_=f'pair lw_{i} added')
                    is_replaced = True
                left_column = pair_1.find('div', class_='left-column')

                subject = left_column.find('div', class_='subject')
                subject_name = subject.find('a').text
                teachers = left_column.find_all('div', class_='teacher')
                teacher_1 = teachers[0].find('a').text
                teacher_2 = teachers[1].find('a').text

                left_column = pair_1.find('div', class_='right-column')
                group = left_column.find('div', class_='group').find('a').text
                place = left_column.find('div', class_='place').find('a').text

                pairs.append({
                    'subject_name': subject_name,
                    'teacher_1': teacher_1,
                    'teacher_2': teacher_2,
                    'group': group,
                    'place': place,
                    'is_replaced': is_replaced,
                })
            except:
                pass
    except Exception as e:
        pass
    return pairs

# Пример использования
def start():
    lines = get_rasp()
    main_pairs = [
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    j = 0
    for line in lines:
        pairs = get_line_pars(line)
        for pare in pairs:
            main_pairs[j].append(pare)
            j += 1
        j = 0
    return main_pairs


main_pairs = start()
for pare in main_pairs[4]:
    if pare['subject_name'] != '':
        print(f"PARE : {pare}")

