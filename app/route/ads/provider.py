from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_ads():
        query = """
    select 
        *
    from ads
    order by title
    """
        return Sql.exec(query=query)
