from app.api.base import base_name as names
from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_investors():
        query = '''
  select * 
  from users 
  where inv = 1 
  order by name
        '''
        return Sql.exec(query=query)
