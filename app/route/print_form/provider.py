from app.api.base import base_name as names
from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_print_form(args):
        query = """
        select *
        from users u
        join "Организация" org on u.id_user = org.id_user  
        where u.id_user = '{id_user}'
            """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_print_form(args):
        fields = ''
        for f in names.print_form_fields:
            if f == names.print_form_fields[0]:
                fields += ' ' + f
            else:
                fields += ', ' + f
            args[f] = args.get(f) or "''"
        args['fields'] = fields
        fields_values = ''
        for f in names.print_form_fields:
            if f == names.print_form_fields[0]:
                fields_values += ' {' + f + '}'
            else:
                fields_values += ', {' + f + '}'
        args['fields_values'] = fields_values
        query = """
            insert into "Организация" (
            {fields}
            )
            VALUES (
              %s
            )
            """ % fields_values
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_print_form(args):
        fields = ''
        for f in names.print_form_fields:
            a = args.get(f) or ''
            args[f] = "'" + a + "'"
            if f == names.print_form_fields[0]:
                fields += ' ' + f + ' = ' + '{' + f + '}'
            else:
                fields += ', ' + f + ' = ' + '{' + f + '}'

        query = """
    update "Организация" 
    set 
    %s
    where
     id_user = {id_user}
    """ % fields
        return Sql.exec(query=query, args=args)
