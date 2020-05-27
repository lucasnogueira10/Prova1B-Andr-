import pymongo
from dados import Cliente, Lanche, Funcionario, Pedido, Lanchonete
import jsons

myclient = pymongo.MongoClient("mongodb://localhost:27017/") #conexao com BD
mydb = myclient["Prova01"]
mycliente = mydb["Cliente"]
mylanche = mydb["Lanche"]
myfuncionario = mydb["Funcionario"]
mypedido = mydb["Pedido"]
mylanchonete = mydb["Lanchonete"]


def select (task):
    print("Digite chave/valor de qual classe quer selecionar")
    filtro = {input("CHAVE: "): input("VALOR: ")}
    select = task.find(filtro)

    return select[0]

def altera (task):
        print("Digite chave/valor de qual Classe você quer alterar")
        mydocp = {input("CHAVE: "): input("VALOR: ")}
        print("Certo. Agora digite chave/valor Que vao substituir.")
        new_docp = {"$set": {input("CHAVE: "): input("VALOR: ")}}
        task.update_one(mydocp, new_docp)

def exclui (task):
        print("Digite a chave/valor de Qual instancia deseja DELETAR !")
        myquery = {input("CHAVE: "): input("VALOR: ")}
        try:
            task.delete_one(myquery)
        except:
            print("Erro! NÃO foi encontrado esta Classe!!!")
            print("Possivel erro na digitação da chave ou esta classe nao existe.")

while True:
    opcao = int(input("1-Insere Lanche | 2-Insere Funcionario | 3-Insere Cliente | 4-Insere Pedido | 5-Alterar | 6-Excluir | 7-Dados Lanchonete | 0-Sair"))

    if opcao == 1:
        lanche = Lanche(input("_id"), input("nome: "), input("desc: "), input("preco: "))
        x = mylanche.insert_one(jsons.dump(lanche))
        print(x)

    if opcao == 2:
        funcionario = Funcionario(input("_id"), input("nome: "), input("endereco: "), input("telefone: "), input("cidade: "), input("idade: "))
        x = myfuncionario.insert_one(jsons.dump(funcionario))
        print(x)

    if opcao == 3:
        cliente = Cliente(input("_id"), input("nome: "), input("endereco: "), input("telefone: "))
        x = mycliente.insert_one(jsons.dump(cliente))
        print(x)

    if opcao == 4:
        pedido = Pedido(input("_id"), select(mycliente), select(mylanche))
        x = mypedido.insert_one(jsons.dump(pedido))
        print(x)
    if opcao == 5:
        opcao5 = int(input("ALTERAR: 1-Lanche| 2-Funcionario | 3-Cliente | 4-Pedido | 7-Lanchonete | 0-Sair"))
        if opcao5 == 1:
            altera(mylanche)
        if opcao5 == 2:
            altera(myfuncionario)
        if opcao5 == 3:
            altera(mycliente)
        if opcao5 == 4:
            altera(mypedido)
        if opcao5 == 7:
            altera(mylanchonete)
        print("Sua ação foi alterada com sucesso!!")

    if opcao == 6:
        opcao6 = int(input("EXCLUIR: 1-Lanche| 2-Funcionario | 3-Cliente | 4-Pedido | 7- Lanchonete | 0-Sair"))
        if opcao6 == 1:
            exclui(mylanche)
        if opcao6 == 2:
            exclui(myfuncionario)
        if opcao6 == 3:
            exclui(mycliente)
        if opcao6 == 4:
            exclui(mypedido)
        if opcao6 == 7:
            exclui(mylanchonete)
        print("Sua ação foi deletada com sucesso!!")

    if opcao == 7:
        lanchonete = Lanchonete(input("_id"), input("nome: "), input("endereco: "), input("telefone: "), input("nf: "), input("cnpj: "))
        x = mylanchonete.insert_one(jsons.dump(lanchonete))
        print(x)
