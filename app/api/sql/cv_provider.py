from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_user_cv(args):
        query = """
    select 
        *
    from cv uc
    where "id_user" = {id_user}
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_cv():
        query = """
    select 
        *
    from cv
    order by title
    """
        return Sql.exec(query=query)

    @staticmethod
    def insert_cv(args):
        query = """
    insert into cv(id_user, title, url, description)
    VALUES (
      {id_user}
      , '{title}'
      , '{url}'
      , '{description}'
    )
    returning id_cv
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_cv(args):
        query = """
    update cv 
    set url = '{url}'
      , title = '{title}'
      , description = '{descriprion}'
    where id_user = {id_user}
    )
    """
        return Sql.exec(query=query, args=args)
