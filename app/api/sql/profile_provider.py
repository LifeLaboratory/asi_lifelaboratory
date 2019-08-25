from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_profile(args):
        query = """
    select name
      , photo
      , rate
      , description
      , budget::float
      , card
    from users
    where "id_user" = {id_user}
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_profile(args):
        query = """
    update users 
      set name = '{name}'
        , login = '{login}'
        , description = '{description}'
        , photo = '{photo}'
      where "id_user" = {id_user}
    """
        return Sql.exec(query=query, args=args)
