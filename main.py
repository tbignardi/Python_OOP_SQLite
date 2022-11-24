#importar nosso arquivo Pessoa.py no diretório modelf
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#exemplo de uso
thiago = Pessoa(1, "Thiago Bignardi")
print(thiago)

#quero mostrar só o nome
print(thiago.nome)
print("DAQUI PRA FRENTE É ACESSO AO BANCO!")

#chama o objeto de banco de dados
db = Database()

#instancia o objeto
PessoaDAO = PessoaDAO(db.conexao, db.cursor)

#quero carregar uma lista com o que veio do banco de dados
pessoas = PessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)

#Criar um objeto com qualquer ator/atriz/diretor/diretora
novo = Pessoa(0, "Denzel Washington")

#Olha que simples...
novo = pessoaDAO.save(novo)

#consulta o banco de novo..
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)
                          