from pony.orm import *

db = Database('sqlite', './database.db', create_db=True)


class Filme(db.Entity):
    nome = Required(str)
    ano_lancamento = Required(int)
    genero = Required(str)


db.generate_mapping(create_tables=True)


@db_session
def populate_database():
    filme01 = Filme(nome='Cruela', ano_lancamento=2021, genero='Crime/Comedia')
    filme02 = Filme(nome='Army of the Dead: Invasão em Las Vegas',
                    ano_lancamento=2021, genero='Terror/Acao')
    filme03 = Filme(nome='Raya e o Ultimo Dragao',
                    ano_lancamento=2021, genero='Infantil/Fantasia')
    filme04 = Filme(nome='Assalto ao Banco da Espanha',
                    ano_lancamento=2021, genero=' Acao/Assalto')
    filme05 = Filme(nome='Sem Remorso', ano_lancamento=2021,
                    genero='Acao/Thriller')

    commit()
