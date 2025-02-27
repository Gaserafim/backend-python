from src.infra.config.db_config import DbConnectionHandler
from src.infra.entities.users import Users


class FakerRepo:
    """
    A Simple Repository
    """

    @classmethod
    def insert_user(cls):
        """
        Insert data into fake table
        """
        with DbConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Programador", password="Teste")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
