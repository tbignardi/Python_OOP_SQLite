#importar nosso arquivo Pessoa.py no diretório modelf
from model.Pessoa import Pessoa

#exemplo de uso
thiago = Pessoa(1, "Thiago Bignardi")
print(thiago)

#quero mostrar só o nome
print(thiago.nome)