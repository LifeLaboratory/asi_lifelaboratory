from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_document(args):
        query = """
    select 
        *
    from document
    where "id_document" = {id_document}
      and lesson is False
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_lesson(args):
        query = """
    select 
        *
    from document
    where "id_document" = {id_document}
      and lesson is True
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_lessons():
        query = """
    select 
        *
    from document
    where lesson is True
    order by title
    """
        return Sql.exec(query=query)

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
    where True
      {id_document}
      {id_project}
      {id_user}
      and lesson is False
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
      and lesson is False
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
      and lesson is False
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_document(args):
        query = """
    insert into document(url, title, type, photo, lesson)
    VALUES (
      '{url}'
      , '{title}'
      , {type}
      , photo = '{photo}'
      , lesson = {lesson}
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
