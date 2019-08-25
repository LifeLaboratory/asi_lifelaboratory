from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def auth_user(args):
        query = """
    select id_user
    from users
    where ("login" = '{login}'
      and "password" = '{password}'
      )
                """
        # print(query)
        return Sql.exec(query=query, args=args)

    @staticmethod
    def check_user(args):
        query = """
  select 1
  from users
  where ("login" = '{login}'
    and "password" = '{password}'
    )
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def register_user(args):
        query = """
    insert into "users"("login", "password", "name") 
    VALUES ('{login}', 
    '{password}', 
    '{name}')
    returning id_user
    """
        print(query)
        return Sql.exec(query=query, args=args)
