
class Cliente:
    def __init__(self, _id, nome, telefone, endereco):
        self._id = _id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Lanche:
    def __init__(self, _id, nome, desc, preco):
        self._id = _id
        self.nome = nome
        self.desc = desc
        self.preco = preco


class Funcionario:
    def __init__(self, _id, nome, endereco, telefone, cidade, idade):
        self._id = _id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.idade = idade


class Pedido:
    def __init__(self, _id, cliente, lanche):
        self._id = _id
        self.cliente = cliente
        self.lanche = lanche

class Lanchonete:
    def __init__(self, _id, nome, endereco, telefone, nf, cnpj):
        self._id = _id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.nf = nf
        self.cnpj = cnpj
