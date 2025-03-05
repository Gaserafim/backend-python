from faker import Faker
from sqlalchemy import text
from src.infra.config import DbConnectionHandler
from src.infra.repo.user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection = DbConnectionHandler()


def test_insert_user():
    """
    Should Insert User
    """

    name = faker.name()
    password = faker.word()

    # Inserção do usuário
    new_user = user_repository.insert_user(name, password)

    # Consulta usando uma sessão
    with db_connection.get_engine().connect() as session:
        query_user = session.execute(
            text("SELECT * FROM users WHERE id=:id"), {"id": new_user.id}
        ).fetchone()

    with db_connection.get_engine().connect() as session:
        session.execute(text("DELETE FROM users WHERE id=:id"), {"id": new_user.id})
        session.commit()

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
