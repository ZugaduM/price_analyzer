import os
import csv
import glob
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.prompt import Prompt

# Note: системная переменная для включения/отключения вывода отладочной информации
debug = True


class PriceAnalyzer:
    """Программный модуль по анализу прайс-листов.

    Методы:
        - __init__() переопределенный метод инициализации
        - clear() статический метод для очистки консоли при перемещении между меню
        - find_text() поиск товара по прайс-листам
        - load_prices() принимает self.data_path: str, обрабатывает файлы прайс-листов и формирует список
        self.files_to_analyze
        - analyz_proc() принимает request: str, находит совпадения в self.files_to_analyze и формирует словарь
        self.result с результатами
        - get_resource_path() изменение пути к директории, в которой лежат прайс-листы
        - about() отображение документации
        - export_menu() меню экспорта
        - change_export_path() изменение пути до папки хранения HTML файла с результатами
        - export_to_html экспорт результатов в HTML файла
        - show_menu() отображение главного меню

    Атрибуты:
        - self.data_path папка с прайс-листами, по-умолчанию resources
        - self.export_path папка для экспорта HTML файлов, по-умолчанию exports
        - self.export_file_name название экспортируемого HTML файла, по-умолчанию output
        - self.files_to_analyze список прайс-листов, содержащих ключевое слово price в названии, иные файлы игнорируются
        - self.result словарь с результатами поиска

    Программный модель предоставляет возможность поиска необходимых товаров по прайс-листам
    и формирование результата с совпадениями в табличной форме, а также сохранение полученных
    результатов в отдельные HTML файлы.
    """

    def __init__(self) -> None:
        self.data_path = '\\resources'
        self.export_path = '\\exports'
        self.export_file_name = 'output'
        self.files_to_analyze = None
        self.result = None

    @staticmethod
    def clear() -> None:
        """Кросс-платформенный метод очищения окна консоли
        при переходе между меню

        """
        if 'nt' in os.name:
            os.system('cls')
        else:
            os.system('clear')

    def find_text(self) -> None:
        """find_text(self)

        Получает пользовательский запрос из Prompt.ask(): str библиотеки rich.
        Передает строку в self.analyz_proc() для анализа по прайс-листам.
        Принимает от self.analyz_proc() словарь и формирует таблицу с результатами совпадений.

        """
        self.load_prices(self.data_path)
        if debug:
            print(f'Files to search in is: {self.files_to_analyze}')
        self.clear()
        search_choice = Prompt.ask("Введите наименование товара, который хотите найти")
        if not search_choice:
            if debug:
                print(f'Your choice is: {search_choice}')
            self.show_menu()
        else:
            temp_result = self.analyz_proc(search_choice)
            if not temp_result:
                print(Panel('Ничего не нашлось. Попробуйте изменить запрос.',
                            title="Анализатор", style="grey66 on black"))
                Prompt.ask('Нажмите Enter для возврата в главное меню')
                self.show_menu()
            table = Table(title="Результаты поиска")
            table.add_column("№", justify="right")
            table.add_column("Наименование", justify="left")
            table.add_column("Цена", justify="right")
            table.add_column("Вес", justify="right")
            table.add_column("Файл", justify="left")
            table.add_column("Цена за кг", justify="right")
            self.result = dict(sorted(temp_result.items(),
                                      key=lambda x: x[1]['Цена за кг']))
            for index, item in enumerate(self.result.values(), 1):
                table.add_row(
                    str(index),
                    str(item['Наименование']),
                    str(item['Цена']),
                    str(item['Вес']),
                    str(item['Файл']),
                    str(item['Цена за кг'])
                )
            print(Panel(table, style="grey66 on black"))
            find_text_choice = Prompt.ask("Нажмите Enter для возврата в главное меню")
            match find_text_choice:
                case _:
                    self.show_menu()

    def load_prices(self, data_path: str) -> None:
        """load_prices(self, data_path: str)

        Формирует список из файлов прайс-листов.

        """
        try:
            if ':\\' in data_path:
                path_to_search = f"{data_path}"
            else:
                path_to_search = f".{data_path}"
            self.files_to_analyze = glob.glob(os.path.join(path_to_search, "*price*"))
        except FileNotFoundError as e:
            print(f'Файл не найден. Проверьте правильность указанного пути. {e}')
        except TypeError as err:
            print(f'Ошибка в адресе расположения папки с данными. {err}')

    def analyz_proc(self, request) -> dict:
        """analyz_proc(self, request)

        Анализатор файлов прайс-листов. Принимает запрос от пользователя (request),
        перебирает каждый файл прайс-листа на совпадение, формирует и возвращает словарь
        для дальнейшей обработки.

        """
        filtered_data = {}
        global_counter = 1

        for path in self.files_to_analyze:
            file_name = path.split('\\')[-1]
            with open(path, 'r', encoding='utf-8') as file:
                read_csv = csv.DictReader(file)
                for rows in read_csv:
                    for key, value in rows.items():
                        if request.lower() in str(value).lower():
                            filtered_data[global_counter] = {
                                '№': global_counter,
                                'Наименование': rows.get("название") or rows.get("продукт")
                                                or rows.get("товар") or rows.get("наименование"),
                                'Цена': float(rows.get("цена") or rows.get("розница")),
                                'Вес': float(rows.get("фасовка") or rows.get("масса") or rows.get("вес")),
                                'Файл': file_name
                            }
                            filtered_data[global_counter]['Цена за кг'] = (
                                                                        round(filtered_data[global_counter]['Цена'] /
                                                                              filtered_data[global_counter]['Вес'], 1))
                            global_counter += 1

        return filtered_data

    def get_resource_path(self) -> None:
        """get_resource_path(self)

        Позволяет изменить адрес пути до директории с прайс-листами.

        """
        self.clear()
        get_path_menu = Text()
        get_path_menu.append("Введите адрес расположения файлов с прайс-листами\n")
        get_path_menu.append("Формат: [буква диска]:\...\[имя папки]\n")
        get_path_menu.append(r"(например, C:\Users\Downloads)""\n")
        get_path_menu.append(r"По умолчанию [папка с программой]\resources")
        print(Panel(get_path_menu, title="Анализатор", style="grey66 on black"))
        get_path_choice = Prompt.ask("Введите адрес или оставьте поле пустым")
        if not get_path_choice:
            if debug:
                print(f'Data path is: {self.data_path}')
            self.show_menu()
        else:
            self.data_path = get_path_choice
            if debug:
                print(f'Data path is: {self.data_path}')
            self.load_prices(data_path=self.data_path)
            self.show_menu()

    def about(self) -> None:
        """about(self)

        Отображает документацию по классу PriceAnalyzer.

        """
        print(self.__doc__)
        about_choice = Prompt.ask("Нажмите Enter для возврата в главное меню")
        match about_choice:
            case _:
                self.show_menu()

    def export_menu(self) -> None:
        """export_menu(self)

        Подменю меню экспорта.
        Позволяет:
         - изменить адрес пути до директории, в которую сохранится HTML файл с результатами поиска
         - произвести экспорт результатов поиска в HTML файл
         - вернуться в главное меню

        """
        export_menu = Text()
        export_menu.append("1. Изменить папку для сохранения\n")
        export_menu.append("2. Экспорт в папку по умолчанию (exports)\n")
        export_menu.append("3. Вернуться в главное меню")
        print(Panel(export_menu, title="Анализатор", style="grey66 on black"))
        export_choice = Prompt.ask("Выберите действие")
        match export_choice:
            case "1":
                self.change_export_path()
            case "2":
                self.export_to_html(self.export_path)
            case "3":
                self.show_menu()
            case _:
                self.clear()
                self.show_menu()

    def change_export_path(self) -> None:
        """change_export_path(self)

        Позволяет изменить путь до папки хранения HTML файла с результатами.

        """
        self.clear()
        change_path_menu = Text()
        change_path_menu.append("Введите адрес папки, в которую хотите сохранить HTML файл\n")
        change_path_menu.append("Формат: [буква диска]:\...\[имя папки]\n")
        change_path_menu.append(r"(например, C:\Users\Downloads)""\n")
        change_path_menu.append(r"По умолчанию [папка с программой]\exports")
        print(Panel(change_path_menu, title="Анализатор", style="grey66 on black"))
        change_path_choice = Prompt.ask("Введите адрес или оставьте поле пустым")
        if not change_path_choice:
            if debug:
                print(f'Export path is: {self.export_path}')
            self.show_menu()
        else:
            self.export_path = change_path_choice
            if debug:
                print(f'Export path is: {self.export_path}')
            self.export_to_html(self.export_path)


    def export_to_html(self, export_path: str) -> None:
        """export_to_html(self, export_path)

        Позволяет экспортировать результаты поиска в HTML файл
        для удобного просмотра.
        Принимает адрес пути папки хранения HTML фйлов (export_path)

        """
        html_content = """
                <html>
                <head>
                    <style>
                        table { border-collapse: collapse; width: 100%; }
                        th, td { border: 1px solid black; padding: 8px; text-align: left; }
                        th { background-color: #f2f2f2; }
                    </style>
                </head>
                <body>
                    <h2>Результаты поиска</h2>
                    <table>
                        <tr>
                            <th>№</th>
                            <th>Наименование</th>
                            <th>Цена</th>
                            <th>Вес</th>
                            <th>Файл</th>
                            <th>Цена за кг</th>
                        </tr>
                """
        try:
            for i, item in enumerate(self.result.values(), 1):
                html_content += f"""
                            <tr>
                                <td>{i}</td>
                                <td>{item['Наименование']}</td>
                                <td>{item['Цена']:.2f}</td>
                                <td>{item['Вес']:.2f}</td>
                                <td>{item['Файл']}</td>
                                <td>{item['Цена за кг']:.2f}</td>
                            </tr>
                        """
        except AttributeError as err:
            print(f'Ошибка доступа к данным. Возможно не найдено совпадений в обработанных данных. {err}')

        html_content += """
                    </table>
                </body>
                </html>
                """

        if ':\\' in export_path:
            path_to_export = f"{export_path}"
        else:
            path_to_export = f".{export_path}"

        filename_to_export = os.path.join(path_to_export, f"{self.export_file_name}.html")

        if not os.path.exists(path_to_export):
            os.makedirs(path_to_export)

        all_files = glob.glob(os.path.join(path_to_export, "*output*"))
        if all_files:
            last_file = all_files[-1]
            if os.path.isfile(last_file) and '_' in last_file:
                last_count = last_file.split("output")[1].split(".")[0]
                counter = int(last_count.strip('_')) + 1
                filename_to_export = os.path.join(path_to_export, f"{self.export_file_name}_{counter}.html")
            else:
                filename_to_export = os.path.join(path_to_export, f"{self.export_file_name}_1.html")
        try:
            with open(filename_to_export, 'w', encoding='utf-8') as export_file:
                export_file.write(html_content)
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(f"Произошла ошибка: {e}")
        else:
            print(Panel("Файл успешно создан!", title="Анализатор", style="grey66 on black"))
            export_choice = Prompt.ask("Нажмите Enter для возврата в главное меню")
            match export_choice:
                case _:
                    self.show_menu()

    def show_menu(self) -> None:
        """show_menu(self)

        Отображение основного меню.
        Позволяет:
        - перейти к поиску совпадений в прайс-листах по текстовому запросу пользователя
        - перейти к изменению адреса пути до директории, в которой располагаются прайс-листы
        - отобразить документацию по программному модулю
        - перейти к экспорту результатов поиска в HTML файл
        - завершить работу программного модуля

        """
        self.clear()

        main_menu = Text()
        main_menu.append("Добро пожаловать!\n\n")
        main_menu.append("1. Поиск\n")
        main_menu.append("2. Указать директорию поиска\n")
        main_menu.append("3. Справка\n")
        main_menu.append("4. Экспорт\n")
        main_menu.append("5. Выход\n")

        print(Panel(main_menu, title="Анализатор", style="grey66 on black"))

        main_choice = Prompt.ask("Выберите действие")
        match main_choice:
            case "1":
                self.find_text()
            case "2":
                self.get_resource_path()
            case "3":
                self.about()
            case "4":
                self.export_menu()
            case "5":
                exit()
            case _:
                self.clear()
                self.show_menu()


if __name__ == "__main__":
    analyzer = PriceAnalyzer()
    analyzer.show_menu()
