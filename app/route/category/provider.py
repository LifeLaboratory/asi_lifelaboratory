from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_user_category(args):
        query = """
    select 
        uc.id_category
      , title
      , description
      , photo
    from user_category uc
      left join category using(id_category)
    where "id_user" = {id_user}
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_category(args):
        query = """
    select 
        *
    from category
    where "id_category" = {id_category}
    """
        return Sql.exec(query=query, args=args)
