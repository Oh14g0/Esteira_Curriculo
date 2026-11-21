from sqlalchemy import text
from app.config.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database()")
        )

    database = result.scalar()

    print("Conexão Realizada com sucesso!")
    print(f"Banco conectado: {database}")

except Exception as error:
    print("Erro ao conectar no banco")
    print(error)