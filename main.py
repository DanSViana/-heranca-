# superclasse (classe-pai)
class Pessoa:
    # atributos
    cidade = "Brasília"
    telefone = "(61) 98765-4321"
    email = "nome@gmail.com"

# subclasse (classe-filha)
class PessoaFisica(Pessoa):
    # atributos
    nome = "Fulano da Silva"
    cpf = "123.456.4789-12"
    peso = 90
    altura = 1.75

class PessoaJuridica(Pessoa):
    # atributos
    nome_fantasia = "Cobra Kai LTDA"
    razao_social = "Fulano da Silva S.A."
    cnpj = "62.245.916/0001-69"

# programa principal
if __name__ == '__main__':
    # instância dos objetos 
    usuario = PessoaFisica()
    empresa = PessoaJuridica()

    print(f'{'-'*30} DADOS DO USUÁRIO {'-'*30}\n')
    print(f'Nome do usuário: {usuario.nome}.')
    print(f'CPF do usuário: {usuario.cpf}.')
    print(f'Peso do usuário: {usuario.peso}.')
    print(f'Altura do usuário: {usuario.altura}.')
    print(f'Cidade onde o usuário mora: {usuario.cidade}.')
    print(f'Telefone do usuário: {usuario.telefone}.')
    print(f'E-mail do usuário: {usuario.email}.')

    print(f'{'-'*30} DADOS DA EMPRESA {'-'*30}\n')
    print(f'Nome da empresa: {empresa.nome_fantasia}.')
    print(f'Razão social da empresa: {empresa.razao_social}.')
    print(f'CNPJ da empresa: {empresa.cnpj}.')
    print(f'Cidade sede da empresa: {empresa.cidade}.')
    print(f'Telefone da empresa: {empresa.telefone}.')
    print(f'E-mail da empresa: {empresa.email}.')
   
   