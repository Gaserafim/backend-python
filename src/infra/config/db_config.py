from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbConnectionHandler:
    """
    SqlAlchemy database connection
    """

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """
        Return connection engine
        :param - None
        :return - engine connection to Database
        """

        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        """
        Enter method
        """
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit method
        """
        self.session.close()
