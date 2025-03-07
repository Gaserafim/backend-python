from collections import namedtuple
from src.infra.config import DbConnectionHandler
from src.infra.entities import Users


class UserRepository:
    """Class to manage User repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """
        Insert data in user entity
        :param - name: person name
        :param - password: user password
        :return - tuple with new user inserted
        """

        InsertData = namedtuple("Users", "id, name, password")

        with DbConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return InsertData(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
