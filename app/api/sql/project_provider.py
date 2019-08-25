from app.api.base import base_name as names
from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_project(args):
        if args.get(names.ID_PROJECT):
            query = """
        select 
            *
        from project
        where "id_project" = {id_project}
        order by title
        """
            return Sql.exec(query=query, args=args)
        else:
            query = """
            select 
                *
            from project
            order by title
                    """
            return Sql.exec(query=query)

    @staticmethod
    def get_project_category(args):
        query = """
    select 
        *
    from project_category
      left 
    where "id_project" = {id_project}
    order by title
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_filter_project(args):
        query = """
    select 
        distinct
          upd.id_project
        , p.title
        , p.description
        , p.photo
        , p.id_user
        , p.budget::Text
        , p.rate
        , u.name
        , u.photo
        , category
    from (
      select distinct
        upd.id_project
        , array_agg(json_object(array['id_category', 'title', 'description', 'photo'], array[c.id_category::text, c.title::text, c.description::text, c.photo::text])::Text) as category
      from user_project_doc upd
      left join project_category pc on pc.id_project = upd.id_project
      left join category c using(id_category)
      where upd.id_project is not null
        {id_user}
      group by upd.id_project
    ) upd
      left join project p using (id_project)
      left join users u on p.id_user = u.id_user
    where true
      {id_category}
    order by p.title
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_project(args):
        query = """
    insert into project(title, description, photo, budget, rate, id_user)
    VALUES (
      '{title}'
      , '{description}'
      , '{photo}'
      , {budget}
      , '{rate}'
      , '{id_user}'
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

    @staticmethod
    def get_budget(args):
        query = """
    select 
        *
    from budget
    where "id_project" = {id_project}
    order by budget
    """
        return Sql.exec(query=query, args=args)
