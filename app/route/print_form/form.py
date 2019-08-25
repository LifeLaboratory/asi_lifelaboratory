#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
# from fpdf import FPDF
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from app.api.base import base_name as names
from app.api.base.base_sql import Sql
from datetime import datetime as dt


class RegistrationIPPrintForm():
    def __init__(self):
        # self.pdf = FPDF()
        self.model = ModelPrintForm()
        self.MyCanvas = None

    def get_print_form(self, args):
        self.MyCanvas = canvas.Canvas(self.model.name_form + args.get(names.ID_USER)+'.pdf')
        result_dict = self.select_mlr(args)
        self.model.apply_filter(result_dict)
        self.create_form()

    @staticmethod
    def select_mlr(args):
        query = """
            select *
            from users u
            left join "Организация" org on u.id_user = org.id_user  
            where u.id_user = '{id_user}'
                """
        # print(query)
        result = Sql.exec(query=query, args=args)
        if isinstance(result, list):
            result = result[0]
        return result

    @staticmethod
    def get_field(field):
        str = ''
        for f in field:
            str += f + '  '
        return str

    def get_field_date(self, date):
        day = date.split('-')[2]
        month = date.split('-')[1]
        year = date.split('-')[0]
        return self.get_field(day) + '.  ' + self.get_field(month) + ' .  ' + self.get_field(year)

    def quadro(self, width, height, count):
        # , width=450, height=20
        for c in range(count):
            self.MyCanvas.drawImage('D:/asi_lifelaboratory_backend/app/route/print_form/quadro1.png', width, height, width=15, height=20)
            width += 13

    def create_form(self):
        try:
            os.remove(self.model.name_form)
        except OSError:
            pass

        MyFontObject = ttfonts.TTFont('Arial', 'arial.ttf')
        pdfmetrics.registerFont(MyFontObject)
        self.MyCanvas.setFont('Arial', 12)
        self.MyCanvas.drawImage('D:/asi_lifelaboratory_backend/app/route/print_form/ip_shtrih_code.png', 1, 795, 100, 30)
        self.MyCanvas.drawString(280, 810, 'Стр 001')
        self.MyCanvas.drawString(480, 795, 'Форма № Р21001')
        self.MyCanvas.drawString(480, 780, 'Код по КНД 1112501')
        self.MyCanvas.drawString(270, 780, 'Заявление')
        self.MyCanvas.drawString(160, 765, 'о государственой регистрации физического лица')
        self.MyCanvas.drawString(166, 748, 'в качестве индивидаульного прдпринимателя')
        form_strings = [
            '1.  Фамилия, имя. отчество физического лица',
            '1.1  На русском языке',
            '1.1.1  Фамилия       %s' % self.get_field(self.model.surname),
            '1.1.2  Имя               %s' % self.get_field(self.model.name),
            '1.1.3  Отчество       %s' % self.get_field(self.model.patronymic),
            '1.2  С использованием букв латинского алфавита',
            '1.1.1  Фамилия       %s' % self.get_field(self.model.surname),
            '1.1.2  Имя               %s' % self.get_field(self.model.name),
            '1.1.3  Отчество       %s' % self.get_field(self.model.patronymic),
            '2  ИНН (при наличии)             %s' % self.get_field(self.model.inn),
            '3  Пол                %s' % self.get_field(str(self.model.sex)),
            '4  Сведения о рождении',
            '4.1  Дата рождения      %s' % self.get_field_date(self.model.birthday),
            '4.2  Место рождения',
      ]
        lines = [623, 590, 554, 483, 448, 415]
        height = 700
        for h in lines:
            # self.MyCanvas.drawImage('quadro2.png', 120, h, width=450, height=20)
            self.quadro(121.5, h, 34)
        self.quadro(175, 378, 12)  # ИНН
        self.quadro(100, 343, 1)  # Пол
        self.quadro(140, 274, 2)  # ДатаРождения День
        self.quadro(180, 274, 2)  # ДатаРождения Месяц
        self.quadro(220, 274, 4)  # ДатаРождения Год
        self.quadro(20, 219, 41)  # Место Рождения
        self.quadro(20, 197, 41)  # Место Рождения
        self.MyCanvas.drawString(15, 224, '  %s' % self.get_field(str(self.model.place_birth)), )
        self.quadro(120, 155, 1)  # Гражданство
        self.MyCanvas.drawString(117, 160, '  %s' % self.get_field(str(self.model.сitizenship)), )
        self.quadro(350, 135, 3)  # Код Страны
        self.MyCanvas.drawString(347, 140, '  %s' % self.get_field(str(self.model.country_code)), )

        for _string in form_strings:
            self.MyCanvas.drawString(15, height, _string)
            height -= 35

        form_strings = [
            '5  Гражданство',
            '5.1  Государство гражданства иностранного гражданина',
        ]
        for _string in form_strings:
            height -= 35
            self.MyCanvas.drawString(15, height, _string)

        form_strings = [
            '------------------------------------------------------------------------------------------------------------------------------------------------',
            '                                                  Для служебных отметок регистрирующего органа'
        ]
        for _string in form_strings:
            height -= 20
            self.MyCanvas.drawString(15, height, _string)

        self.MyCanvas.showPage()
        self.MyCanvas.drawImage('D:/asi_lifelaboratory_backend/app/route/print_form/ip_shtrih_code.png', 1, 795, 100, 30)
        self.MyCanvas.setFont('Arial', 12)
        self.MyCanvas.drawString(280, 810, 'Стр 002')
        self.MyCanvas.drawString(480, 795, 'Форма № Р21001')

        form_strings = [
            '    Адрес места жительства (пребывания) в Российской Федерации',
            '6.1  Почтовый индекс   %s                  6.2 Субъект Российской Федерации   %s ' % (self.get_field(str(self.model.post_code)), self.get_field(str(self.model.subject_code_rf))),
            '6.3  Район (улус и т.п)                      Наименование района (улуса и т.п.)',
        ]
        height = 750

        self.quadro(142, 707, 6)  # Почтовый индекс
        self.quadro(491, 707, 2)  # Субъект РФ
        self.quadro(20, 650, 10)  # Район
        self.quadro(220, 650, 29)  # Наименование района
        self.quadro(20, 626, 45)  # Наименование района
        self.MyCanvas.drawString(18, 658, '  %s' % self.get_field(str(self.model.area)), )
        self.MyCanvas.drawString(214.5, 658, '  %s' % self.get_field(str(self.model.name_area)), )

        for _string in form_strings:
            self.MyCanvas.drawString(15, height, _string)
            height -= 35

        form_strings = [

        '7.4 Кем выдан',
        '7.5 Код подразделения',

    ]
        self.quadro(20, 580, 10)  # Город
        self.quadro(220, 580, 29)  # Наименование города
        self.MyCanvas.drawString(18, 589, '  %s' % self.get_field(str(self.model.city)), )
        self.MyCanvas.drawString(214.5, 589, '  %s' % self.get_field(str(self.model.name_city)), )
        self.MyCanvas.drawString(15, height-35, '6.4  Город (волость и т.п.)          Наименование города (волости и т.п.)')

        self.quadro(20, 535, 10)  # Населенный пункт
        self.quadro(220, 535, 29)  # Наименование населенного пункта
        self.quadro(20, 510, 45)  # Наименование населенного пункта
        # self.MyCanvas.drawString(18, 589, '  %s' % self.get_field(str(self.model.locality)), )
        # self.MyCanvas.drawString(214.5, 589, '  %s' % self.get_field(str(self.model.locality_name)), )
        self.MyCanvas.drawString(15, height-85, '6.5 Населенный пункт (село и т.п.)   Наименование населенного пункта (села и т.п.)',)
        self.MyCanvas.drawString(15, height-150, '6.6 Улица (проспект и т.п.)          Наименование населенного пункта (села и т.п.)',)
        self.quadro(20, 465, 10)  # Населенный пункт
        self.quadro(220, 465, 29)  # Наименование населенного пункта
        self.quadro(20, 440, 45)  # Наименование населенного пункта
        self.MyCanvas.drawString(17, 471, '  %s' % self.get_field(str(self.model.street)), )
        self.MyCanvas.drawString(214.5, 471, '  %s' % self.get_field(str(self.model.street_name)), )

        self.MyCanvas.drawString(15, height - 220, '6.7 Дом (владение и т.п.)     Номер дома (владения и т.п.)    6.8 Корпус (строение и т.п.)',)
        self.quadro(20, 400, 10)  # Дом
        self.quadro(210, 400, 10)  # Номер дома
        self.quadro(210, 375, 10)  # Номер дома
        self.quadro(350, 400, 10)  # Корпус
        self.quadro(540, 374, 3)  # Квартира
        self.MyCanvas.drawString(17, 408, '  %s' % self.get_field(str(self.model.house)), )
        self.MyCanvas.drawString(201, 408, '   %s' % self.get_field(str(self.model.house_number)), )
        self.MyCanvas.drawString(344, 408, '  %s' % self.get_field(str(self.model.corps)), )
        self.MyCanvas.drawString(15, height - 265, '6.9 Квартира (комната и т.п.)   %s                                                  Номер квартиры (комнаты и т.п.) %s' % (self.get_field(str('')), self.get_field(str(self.model.room_number))),)

        self.quadro(140, 300, 2)  # Квартира
        self.MyCanvas.drawString(15, height - 300, '7 Данные документа, удостоверяющего личность',)
        self.MyCanvas.drawString(15, height - 340, '7.1 Вид документа ',)
        self.MyCanvas.drawString(136, 308, '  %s' % self.get_field(str(self.model.type_doc)), )
        self.quadro(190, 256, 16)  # Паспорт
        self.MyCanvas.drawString(15, height - 380, '7.2 Серия и номер документа    %s' % self.get_field(str(self.model.passport)))
        self.quadro(140, 219, 2)  # ДатаВыдачи День
        self.quadro(180, 219, 2)  # ДатаВыдачи Месяц
        self.quadro(220, 219, 4)  # ДатаВыдачм Год
        self.quadro(101.5, 190, 40)  # Кем выдан
        self.quadro(20, 166, 50)  # Кем выдан
        self.quadro(20, 140, 50)  # Кем выдан
        self.MyCanvas.drawString(15, height - 415, '4.1  Дата выдачи           %s' % self.get_field_date(self.model.date_passport))
        self.MyCanvas.drawString(15, height - 445, '7.4 Кем выдан   %s' % self.get_field(self.model.issued_passport))
        self.MyCanvas.drawString(15, height - 560, '                                                                 Подпись заявителя_______________________')
        #
        # self.MyCanvas.showPage()
        # self.MyCanvas.setFont('Arial', 12)
        # self.MyCanvas.drawString(280, 810, 'Стр 003')
        # self.MyCanvas.drawString(480, 795, 'Форма № Р21001')
        #
        # form_strings = [
        #     '8    Данные документа, подтверждающиего право иностранного гражданина или лица без гражданства временно или',
        #     'постоянно проживать на территории Российской Федерации',
        #     '8.1        1 - вид на жительство 2 - разрешение на временное проживание',
        #     '8.2  Номер документа',
        #     '8.3  Дата выдачи',
        #     '8.4  Кем выдан',
        #     '6.7 Дом (владение и т.п.)     Номер дома (владения и т.п.)    6.8 Корпус (строение и т.п.)   Номер корпуса (строения и т.п.)',
        #     '8.5 Срок действия ',
        # ]
        # height = 750
        # for _string in form_strings:
        #     self.MyCanvas.drawString(15, height, _string)
        #     height -= 35
        #
        # self.MyCanvas.showPage()
        # self.MyCanvas.setFont('Arial', 12)
        # self.MyCanvas.drawString(280, 810, 'Стр 004')
        # self.MyCanvas.drawString(480, 795, 'Форма № Р21001')
        # self.MyCanvas.drawString(480, 780, 'Лист А заявления')
        #
        # form_strings = [
        #     '      Сведения о кодах по Общероссийскому классификатору видом экономической деятельности',
        #     '1  Код основного вида деятельности',
        #     '2. Коды дополнительных видов деятельности',
        # ]
        # height = 750
        # for _string in form_strings:
        #     self.MyCanvas.drawString(15, height, _string)
        #     height -= 35
        #
        # self.MyCanvas.showPage()
        # self.MyCanvas.setFont('Arial', 12)
        # self.MyCanvas.drawString(280, 810, 'Стр 005')
        # self.MyCanvas.drawString(480, 795, 'Форма № Р21001')
        # self.MyCanvas.drawString(480, 780, 'Лист Б заявления')
        #
        # form_strings = [
        #     '1. Я, ',
        #     'подтверждаю, что сведения, содержащиеся в заявлении, достоверны и соответствуют представленным документам.',
        #     'Мне известно, что в случае представления в регистрирующий орган недостоверных сведений, я несу ответственность,',
        #     'установленную законодательством Россифской Федерации',
        #     'Прошу доументы, подтверждающие факт внесения записи в Единый государственный реестр индивидуальных',
        #     'предпринимателей, или решение об отказе в государственной регистрации',
        #     '',
        #     '1 - выдать заявителю',
        #     '2 - выдать заявителю или лицу, действующему на основании доверенности',
        #     '3 - направить по почте',
        #     'Контактные данные    Телефон',
        #     'E-mail',
        #     '                                                                 Подпись заявителя_______________________'
        #     '2 Заявление предоставлено в регистрирующий орган непосредственно заявителем и подписано им в присутствии',
        #     'длжностного лица регистрирующего органа. Документ, удостоверябющий личность, заявителем предоставлен',
        #     '_____________________________________                        _______________________________________',
        #     '           (должность)                                            (подпись, фамилия и инициалы)',
        #     '3  Сведения о лице, засвидетельствовавшем подлинность подписи заявителя в нотариальном порядке',
        #     'Лицом, засвидетельстовавшим подлинность подписи заявителя, является',
        #     '[  ]   1 - нотариус  2 - лицо, замещающее времено отсутствующего нотариуса',
        #     '       3 - должностное лицо, уполномоченное на совершение нотариального действия',
        #     'ИНН лица, засвидетельстовавшего подлинность подписи заявителя  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] ',
        # ]
        # height = 750
        # for _string in form_strings:
        #     self.MyCanvas.drawString(15, height, _string)
        #     height -= 35

        self.MyCanvas.save()


class ModelPrintForm():
    def __init__(self):
        self.name_form = 'D:/asi_lifelaboratory_backend/app/print_form/read/'
        self.filter = None
        self.surname = None  # Фамилия
        self.name = None
        self.patronymic = None
        self.surname_lat = None
        self.name_lat = None
        self.patronymic_lat = None
        self.inn = None
        self.sex = None
        self.birthday = None
        self.place_birth = None
        self.сitizenship = None  # Гражданство
        self.country_code = None
        self.post_code = None  # Почтовый индекс
        self.subject_code_rf = None  # Субъект РФ
        self.area = None  # Район
        self.name_area = None  # Наименование района
        self.city = None
        self.name_city = None
        self.locality = None  # Населенный пункт
        self.locality_name = None
        self.street = None
        self.street_name = None
        self.house = None
        self.house_number = None
        self.corps = None  # Корпус
        self.corps_number = None
        self.room_number = None
        self.type_doc = None
        self.passport = None
        self.date_passport = None
        self.issued_passport = None  # Кем выдан паспорт
        self.code_division = None  # Код подразделения
        self.residence = None  # 1 - вид на жительство 2 - временное
        self.number_doc_residence = None
        self.date_residence = None
        self.issued_residence = None
        self.exiration_date_residence = None
        self.code_activity = None  # код осн вида деятельности
        self.code_another_activity = []
        self.get_answer = None  # 1, 2, 3
        self.tel_number = None
        self.email = None
        self.position = None  # должность
        self.attestor = None  # свидетель
        self.inn_attestor = None

    def apply_filter(self, filter):
        self.filter = filter
        fio = self.filter.get(names.NAME).split(' ')
        fio_lat = self.filter.get(names.NAME).split(' ')
        self.surname = fio[0]
        self.name = fio[1]
        self.patronymic = fio[2]
        self.surname_lat = fio_lat[0]
        self.name_lat = fio_lat[1]
        self.patronymic_lat = fio_lat[2]
        self.inn = self.filter.get(names.INN)
        self.sex = self.filter.get(names.SEX)
        self.birthday = self.filter.get(names.BIRTHDAY)
        self.place_birth = self.filter.get(names.PLACE_BIRTHDAY)
        self.сitizenship = self.filter.get(names.сitizenship)
        self.country_code = self.filter.get(names.country_code)
        self.post_code = self.filter.get(names.post_code)
        self.subject_code_rf = self.filter.get(names.subject_code_rf)
        self.area = self.filter.get(names.area)
        self.name_area = self.filter.get(names.name_area)
        self.city = self.filter.get(names.city)
        self.name_city = self.filter.get(names.name_city)
        self.locality = self.filter.get(names.locality)
        self.locality_name = self.filter.get(names.locality_name)
        self.street = self.filter.get(names.street)
        self.street_name = self.filter.get(names.street_name)
        self.house = self.filter.get(names.house)
        self.house_number = self.filter.get(names.house_number)
        self.corps = self.filter.get(names.corps)
        self.corps_number = self.filter.get(names.corps_number)
        self.room_number = self.filter.get(names.room_number)
        self.type_doc = self.filter.get(names.type_doc)
        self.passport = self.filter.get(names.passport)
        self.date_passport = self.filter.get(names.date_passport)
        self.issued_passport = self.filter.get(names.issued_passport)
        self.code_division = self.filter.get(names.code_division)
        self.residence = self.filter.get(names.residence)
        self.number_doc_residence = self.filter.get(names.number_doc_residence)
        self.date_residence = self.filter.get(names.date_residence)
        self.issued_residence = self.filter.get(names.issued_residence)
        self.exiration_date_residence = self.filter.get(names.exiration_date_residence)
        self.code_activity = self.filter.get(names.code_activity)
        self.code_another_activity = self.filter.get(names.code_another_activity)
        self.get_answer = self.filter.get(names.get_answer)
        self.tel_number = self.filter.get(names.tel_number)
        self.email = self.filter.get(names.email)
        self.position = self.filter.get(names.position)
        self.attestor = self.filter.get(names.attestor)
        self.inn_attestor = self.filter.get(names.inn_attestor)
