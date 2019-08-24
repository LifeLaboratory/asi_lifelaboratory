
from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_project(args):
        query = """
    select 
        *
    from project
    where "id_project" = {id_project}
    order by title
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_filter_project(args):
        query = """
    select 
          upd.id_project
        , upd.id_document
        , upd.id_user
        , u.name
        , u.photo
    from user_project_doc upd
      left join project p using (id_project)
      left join users u on p.id_user = u.id_user
      left join project_category pc on pc.id_project = p.id_project
    where
      case when '{id_user}' = 'None' then upd."id_user"::Text = '{id_user}' else True end
      and case when '{id_category}' = 'None' then pc."id_category"::Text = any('{id_category}'::text[]) else True end
    order by p.title
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_project(args):
        query = """
    insert into project(title, description, photo, budget)
    VALUES (
      '{title}'
      , '{description}'
      , '{photo}'
      , {budget}
    )
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_project(args):
        query = """
    update project 
    set title = '{title}'
      , description = '{description}'
      , photo = '{photo}'
      , budget = {budget}
    where id_project = {id_project}
      and id_user = {id_user}
    )
    """
        return Sql.exec(query=query, args=args)
