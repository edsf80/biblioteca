from flask import Flask, render_template, request, redirect, url_for
from dao import AlunoDao

app = Flask(__name__)

aluno_dao = AlunoDao()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    login = request.form["login"]
    senha = request.form["senha"]
    if login == "aluno" and senha == "1234":
        return redirect(url_for("principal"))
    else:
        return redirect(url_for("index"))

@app.route("/principal")
def principal():
    return render_template("main.html")

@app.route("/imprime-nome/<nome>")
def imprime_nome(nome):
    return f'O nome passado foi {nome}'

@app.route("/alunos")
def alunos():
    lista = aluno_dao.listar()

    return render_template("alunos.html", alunos = lista)

@app.route("/alunos/adicionar")
def adicionar():
    return render_template("cadaluno.html")

@app.route("/filho")
def filho():
    return render_template("filho.html")

@app.route("/filho2")
def filho2():
    return render_template("filho2.html")

@app.route("/imprime-numero/<float:numero>")
def imprime_numero(numero):
    return f'Olá, o número foi {numero}'

@app.route("/teste-dados")
def teste_dados():
    nome = request.args.get("nome")
    x = request.args.get("servico")
    sobrenome = request.args.get("sobrenome")
    print(nome)
    print(x)
    print(sobrenome)
    return ""

@app.route("/teste")
def teste():
    lista = [
        {
            "nascimento": "12/06/2000",
            "nome": "Victor Gabriel",
            "matricula": "1234567"        
        },
        {
            "nascimento": "12/06/2005",
            "nome": "João Vitor",
            "matricula": "7654321"        
        },
        {
            "nascimento": "12/06/2001",
            "nome": "Erenilson",
            "matricula": "4444444"        
        },
        {
            "nascimento": "12/06/2001",
            "nome": "Luiz Ricardo",
            "matricula": "5555555"        
        }
    ]

    return render_template("teste.html", alunos = lista)


if __name__ == "__main__":
    app.run()