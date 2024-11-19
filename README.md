<img src="https://github.com/user-attachments/assets/3296ec13-8cea-47cc-a4d7-d81e931de2e8" align="center" alt="Authentications">

![GitHub last commit](https://img.shields.io/github/last-commit/zugadum/module-20)
![GitHub repo size](https://img.shields.io/github/repo-size/zugadum/module-20)
![GitHub Repo stars](https://img.shields.io/github/stars/zugadum/module-20)
![GitHub watchers](https://img.shields.io/github/watchers/zugadum/module-20)
![GitHub followers](https://img.shields.io/github/followers/zugadum)
![Static Badge](https://img.shields.io/badge/e--mail%3A-zugadum%40gmail.com-blue?link=mailto:zugadum@gmail.com)

# Анализатор прайс-листов

## Оглавление
- [Введение](#intro)
- [Описание](#struct)
- [Особенностии](#unic)
- [Приложение 1. Файловая структура проекта](#add_1)
- [Приложение 2. Список необходимых библиотек](#add_2)

## <img src="https://github.com/user-attachments/assets/0a965a32-a89b-4cbd-9e52-eb61f242a3f1" width="48"> <a id='intro'>Введение</a>
Программный модуль по анализу данных в прайс-листах поставщиков.

## <img src="https://github.com/user-attachments/assets/9b01a7ad-5146-46b8-91ff-72db872fe160" width="48"> <a id='struct'>Описание</a>
В папке [resources](https://github.com/ZugaduM/price_analyzer/tree/main/resources) содержатся файлы прайс-листов от разных поставщиков.
Ввиду разрозненности поступающих данных точное количество и названия файлов заранее неизвестно, но по шаблону все они содержат ключ "price".
Файлы, в имени которых отсутствует ключ "price", игнорируются.
Формат поступающих файлов: данные, разделенные точкой с запятой.
Так же ввиду уникальности источников данных порядок колонок в присылаемых файлах может разниться. Тем не менее поступающие файлы содержат в себе колонки с одним из следующих названий:
 - для названия продуктов это "название", "продукт", "товар", "наименование";
 - для цен это "цена" или "розница";
 - для указания веса это "фасовка", "масса" или "вес" (строго в килограммах).

Остальные столбцы в данном проекте не интересны и игнорируются.

## <img src="https://github.com/user-attachments/assets/b8c35cb4-585e-4223-bc9c-f3c1da27d842" width="48"> <a id='unic'>Особенности</a>
Программный модуль выполнен в формате консольного приложения, для оформления меню применяется пакет [Rich](https://pypi.org/project/rich/).
В функционал программного модуля входит:
 - сканирование папки [resources](https://github.com/ZugaduM/price_analyzer/tree/main/resources) на наличие файлов и составление списка доступных для анализа файлов с помощью модуля [glob](https://docs.python.org/3/library/glob.html);
 - изменение расположение папки с прайс-листами для последующего анализа;
 - поиск товара по фрагменту названия с сорторовкой по цене за килогорамм;
 - экспорт полученных после поиска данных в табличной форме в HTML файл;
 - отображение документации.

Пример выводимых данных при успешном поиске:
![image](https://github.com/user-attachments/assets/f23c650d-946d-44bd-a04b-679b03cce3bf)

## <a id='add_1'>Приложение 1. Файловая структура проектаа</a>
![image](https://github.com/user-attachments/assets/a2703517-9a20-489a-9215-aaf42b8f9ac6)

## <a id='add_2'>Приложение 2. Список необходимых библиотек</a>
 - markdown-it-py==3.0.0
 - mdurl==0.1.2
 - Pygments==2.18.0
 - python-dateutil==2.9.0.post0
 - pytz==2024.2
 - rich==13.9.4
 - six==1.16.0
 - tzdata==2024.2

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=zugadum&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
<h3 align="left">Я использую:</h3>
<p align="left"> <a href="https://www.arduino.cc/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/arduino-1.svg" alt="arduino" width="40" height="40"/> </a> <a href="https://www.blender.org/" target="_blank" rel="noreferrer"> <img src="https://download.blender.org/branding/community/blender_community_badge_white.svg" alt="blender" width="40" height="40"/> </a> <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.qt.io/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Qt_logo_2016.svg" alt="qt" width="40" height="40"/> </a> <a href="https://www.sketch.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sketchapp/sketchapp-icon.svg" alt="sketch" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> </p>
