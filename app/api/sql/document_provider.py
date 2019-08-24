from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_document(args):
        query = """
    select 
        *
    from document
    where "id_document" = {id_document}
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_documents(args):
        query = """
    select 
          upd.id_project
        , upd.id_document
        , upd.id_user
        , u.name
        , u.photo
        , d.url
        , d.title
        , d.type
    from user_project_doc upd
      left join users u using (id_user)
      left join project p using (id_project)
      left join document d using (id_document)
    where
      case when '{id_document}' = 'None' then upd."id_document"::Text = '{id_document}' else True end
      and case when '{id_project}' = 'None' then upd."id_project"::Text = '{id_project}' else True end
      and case when '{id_user}' = 'None' then upd."id_user"::Text = '{id_user}' else True end
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_project_document(args):
        query = """
    select 
          upd.id_project
        , upd.id_document
        , upd.id_user
        , u.name
        , u.photo
        , d.url
        , d.title
        , d.type
    from user_project_doc upd
      left join users u using (id_user)
      left join project p using (id_project)
      left join document d using (id_document)
    where "id_project" = {id_project}
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_user_project_document(args):
        query = """
    select 
          upd.id_user
        , upd.id_project
        , upd.id_document
        , d.url
        , d.title
        , d.type
    from user_project_doc upd
      left join document d using (id_document)
    where "id_document" = {id_document}
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_document(args):
        query = """
    insert into document(url, title, type)
    VALUES (
      '{url}'
      , '{title}'
      , {type}
    )
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_document(args):
        query = """
    update document 
    set url = '{url}'
      , title = '{title}'
      , type = {type}
    where id_document = {id_document}
    )
    """
        return Sql.exec(query=query, args=args)
