from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_budget(args):
        query = """
  select *
  from(
    select 
      b.id_user
      , b.id_project
      , p.title
      , sum(b.budget) as budget
    from budget b
      left join project p using (id_project)
    where b."id_user" = {id_user}
    group by b.id_user
      , b.id_project
      , p.title
  ) nd
  order by budget
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_budgets(args):
        query = """
    select 
        *
    from budget
    order by budget
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
    def insert_budget(args):
        query = """
    insert into budget(id_user, id_project, budget)
    VALUES (
      {id_user}
      , {id_project}
      , {budget}
    )
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_budget(args):
        query = """
    update document 
    set budget = {budget}
    where id_user = {id_user}
      and id_project = {id_project}
    )
    """
        return Sql.exec(query=query, args=args)
