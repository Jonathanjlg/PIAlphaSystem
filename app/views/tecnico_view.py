from flask import render_template, redirect, url_for, flash ,request
from app import app, db
from app.models.nivel_model import Nivel
from app.models.tecnico_model import Tecnico  # Importe o modelo Tecnico
from app.forms.nivel_form import NivelForm
from app.forms.tecnico_form import TecnicoForm  # Importe o formulário TecnicoForm

from sqlalchemy.orm import joinedload

@app.route("/cadtecnico", methods=["POST", "GET"])
def cadastrar_tecnico():
    form = TecnicoForm()
    
    # Carregar os níveis do banco de dados
    niveis = Nivel.query.all()
    # Formatar os níveis para o formato necessário para o campo de seleção
    nivel_choices = [(nivel.id, nivel.nome) for nivel in niveis]
    # Adicionar os níveis ao campo de seleção
    form.nivel_id.choices = nivel_choices
    
    if form.validate_on_submit():
        nome = form.nome.data
        nivel_id = form.nivel_id.data
        email = form.email.data
        cpf = form.cpf.data
        telefone = form.telefone.data
        senha = form.senha.data
        
        tecnico = Tecnico(nome=nome, email=email, nivel_id=nivel_id, cpf=cpf, telefone=telefone, senha=senha)
        
        try:
            db.session.add(tecnico)
            db.session.commit()
            return redirect(url_for('listar_tecnicos'))
        except Exception as e:
            print(f"Erro ao cadastrar técnico: {e}")
          
    return render_template("tecnico/form_tecnico.html", form=form)

from sqlalchemy.orm import joinedload

# Exemplo de consulta na rota de listar técnicos
@app.route('/listartecnicos', methods=['GET'])
def listar_tecnicos():
    tecnicos_com_nivel = db.session.query(Tecnico).options(joinedload(Tecnico.nivel)).all()
    return render_template('tecnico/listar_tecnico.html', tecnicos=tecnicos_com_nivel)

@app.route('/editar_tecnico/<int:tecnico_id>', methods=['GET', 'POST'])
def editar_tecnico(tecnico_id):
    tecnico = Tecnico.query.get_or_404(tecnico_id)
    form = TecnicoForm(obj=tecnico)
    
    # Carregar os níveis do banco de dados
    niveis = Nivel.query.all()
    # Formatar os níveis para o formato necessário para o campo de seleção
    nivel_choices = [(nivel.id, nivel.nome) for nivel in niveis]
    # Adicionar os níveis ao campo de seleção
    form.nivel_id.choices = nivel_choices

    if form.validate_on_submit():
        tecnico.nome = form.nome.data
        tecnico.nivel_id = form.nivel_id.data
        tecnico.email = form.email.data
        tecnico.cpf = form.cpf.data
        tecnico.telefone = form.telefone.data
        tecnico.senha = form.senha.data

        try:
            db.session.add(tecnico)
            db.session.commit()
            return redirect(url_for('listar_tecnicos'))
        except Exception as e:
            print(f"Erro ao cadastrar técnico: {e}")
          
    return render_template("tecnico/form_tecnico.html", form=form)



@app.route("/remover_tecnico/<int:id>", methods=["POST", "GET"])
def remover_tecnico(id):
    tecnicos = Tecnico.query.filter_by(id=id).first()
    
    if request.method == "POST":
        try:
            db.session.delete(tecnicos)
            db.session.commit()
            return redirect(url_for("listar_tecnicos"))
        except:
            print("Erro ao deletar técnico")
    
    return render_template("tecnico/remover_tecnico.html", tecnico=tecnicos)

