import requests
import os



API_KEY = 'trnsl.1.1.20181209T125123Z.1cdad3a79c5ec297.b422869a67f6eb20b403e32e2cc2011802e15ced'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


# Указываем пути к файлам и папкам
new_txt_files = 'translated'
txt_files = 'for_translate'
current_dir = os.path.dirname(os.path.abspath(__file__))
txt_files_dir = os.path.join(current_dir, txt_files)
txt_files_list = os.listdir(txt_files_dir)

def create_dict():
    new_dict = {}
    for file_names in txt_files_list:
        new_dict[file_names[:2].lower()] = file_names
    return new_dict

check_keys = create_dict()

def read_txt_files(from_lang):
    if from_lang in check_keys.keys():
        need_txt = check_keys[from_lang]
        with open(os.path.join(current_dir, txt_files, need_txt), 'r') as f:
            text_news = f.read()
    return text_news

# Переводим текст

def translate_it(text_for_translate, from_lang, to_lang):
    params = {
        'key': API_KEY,
        'text': text_for_translate,
        'lang': '{}-{}'.format(from_lang, to_lang)
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

# Записываем новый файл с переводом

def record_new_file(from_lang, to_lang, after_translate):
    new_file_name = from_lang.upper() + '_' + 'to' + '_' + to_lang.upper() + '.txt'
    new_txt_files_dir = os.path.join(current_dir, new_txt_files, new_file_name)
    with open (new_txt_files_dir, 'w', encoding='UTF-8') as f:
        f.write(after_translate)


def translate_and_record_files():
    from_lang = input('Выберите язык новостей')
    to_lang = input('Выберите язык для перевода')
    text_for_translate = read_txt_files(from_lang)
    after_translate = translate_it(text_for_translate, from_lang, to_lang)
    create_dict()
    read_txt_files(from_lang)
    translate_it(text_for_translate, from_lang, to_lang)
    record_new_file(from_lang, to_lang, after_translate)
    print('Ваш файл успешно записан! Расположение: {}'.format(os.path.join(current_dir, new_txt_files)))
translate_and_record_files()
