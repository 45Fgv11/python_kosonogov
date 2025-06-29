#В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным).

import re


def extract_domains_from_file(filename):
    pattern = r'https?://([^/:]+)'

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    domains = re.findall(pattern, content)

    return domains


input_filename = 'radio_stations.txt'
output_filename = 'domains.txt'

try:
    domains = extract_domains_from_file(input_filename)

    print("Найденные домены:")
    for domain in domains:
        print(domain)

    with open(output_filename, 'w', encoding='utf-8') as out_file:
        out_file.write('\n'.join(domains))

    print(f"\nРезультат сохранен в файл: {output_filename}")

except FileNotFoundError:
    print(f"Ошибка: Файл {input_filename} не найден!")
except Exception as e:
    print(f"Произошла ошибка: {e}")