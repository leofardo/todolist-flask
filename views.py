from flask import render_template, request, url_for, redirect
from app import app, db
from helpers import FormularioTarefa
from models import Tarefas

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int) #padrao da variavel ao acessar a index é igual a 1
    per_page = 5

    status_view = request.args.get('status', 'todos', type=str)

    tarefas_page = None

    #Filtros
    if status_view == 'Em andamento':
        tarefas_page = Tarefas.query.filter(Tarefas.status == 'Em andamento').order_by(Tarefas.id.desc()).paginate(page=page, per_page=per_page, error_out=False)
    elif status_view == 'Finalizado':
        tarefas_page = Tarefas.query.filter(Tarefas.status == 'Finalizado').order_by(Tarefas.id.desc()).paginate(page=page, per_page=per_page, error_out=False)
    elif status_view == 'Pendente':
        tarefas_page = Tarefas.query.filter(Tarefas.status == 'Pendente').order_by(Tarefas.id.desc()).paginate(page=page, per_page=per_page, error_out=False)
    else:
        tarefas_page = Tarefas.query.order_by(Tarefas.id.desc()).paginate(page=page, per_page=per_page, error_out=False)

    tarefas = tarefas_page.items

    form = FormularioTarefa()

    return render_template("index.html", tarefas=tarefas, form=form, pagination=tarefas_page, status_view=status_view)

@app.route('/processa_cadastro', methods=['POST',])
def processa_cadastro():
    form = FormularioTarefa(request.form)

    if not form.validate_on_submit():
        redirect(url_for('index'))

    descricao = form.descricao.data

    nova_descriao = Tarefas(descricao=descricao)
    db.session.add(nova_descriao)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/deletar/<int:id>/<string:status>')
def deletar(id, status):
    query = Tarefas.query.filter_by(id=id)
    if not query:
        return redirect(url_for('index'))
    query.delete()
    db.session.commit()
    return redirect(url_for('index', status=status))

@app.route('/finalizar/<int:id>/<int:page>/<string:status>')
def finalizar(id, page, status):
    query = Tarefas.query.filter_by(id=id).first()

    if not query:
        return redirect(url_for('index'))

    query.status = 'Finalizado'
    db.session.add(query)
    db.session.commit()

    return redirect(url_for('index', status=status, page=page))

@app.route('/tornar_em_andamento/<int:id>/<int:page>/<string:status>')
def tornar_em_andamento(id, page, status):
    query = Tarefas.query.filter_by(id=id).first()

    if not query:
        return redirect(url_for('index'))

    query.status = 'Em andamento'
    db.session.add(query)
    db.session.commit()

    return redirect(url_for('index', status=status, page=page))

@app.route('/editar/<int:page>/<int:id>/<string:status>', methods=['POST',])
def editar(page, id, status):
    descricao = request.form['descricao']

    query = Tarefas.query.filter_by(id=id).first()
    query.descricao = descricao

    db.session.add(query)
    db.session.commit()

    return redirect(url_for('index', status=status, page=page))