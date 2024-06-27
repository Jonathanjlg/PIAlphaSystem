from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models.equipamento_model import Equipamento
from app.models.marca_model import Marca
from app.forms.equipamento_form import EquipamentoForm

@app.route('/cadequipamento', methods=['GET', 'POST'])
def cadastrar_equipamento():
    form = EquipamentoForm()

    marcas = Marca.query.all()
    marca_choices = [(marca.id, marca.nome) for marca in marcas]
    form.marca_id.choices = marca_choices

    if form.validate_on_submit():
        marca_id = form.marca_id.data
        quantidade = form.quantidade.data
        acessorios = form.acessorios.data

        equipamento = Equipamento(quantidade=quantidade, acessorios=acessorios, marca_id=marca_id)

        try:
            db.session.add(equipamento)
            db.session.commit()
            flash('Equipamento cadastrado com sucesso!', 'success')
            return redirect(url_for('listar_equipamentos'))
        except Exception as e:
            print(f"Erro ao cadastrar equipamento: {e}")
            flash('Erro ao cadastrar equipamento. Por favor, tente novamente.', 'error')
            db.session.rollback()

    return render_template("equipamento/form_equipamento.html", form=form)

@app.route('/listarequipamentos')
def listar_equipamentos():
    equipamentos = Equipamento.query.all()
    return render_template('equipamento/lista_equipamento.html', equipamentos=equipamentos)


@app.route('/editar_equipamento/<int:equipamento_id>', methods=['GET', 'POST'])
def editar_equipamento(equipamento_id):
    equipamento = Equipamento.query.get_or_404(equipamento_id)
    form = EquipamentoForm(obj=equipamento)

    marcas = Marca.query.all()
    form.marca_id.choices = [(marca.id, marca.nome) for marca in marcas]

    if form.validate_on_submit():
        equipamento.quantidade = form.quantidade.data
        equipamento.acessorios = form.acessorios.data
        equipamento.marca_id = form.marca_id.data

        try:
            db.session.commit()
            flash('Equipamento atualizado com sucesso!', 'success')
            return redirect(url_for('listar_equipamentos'))
        except Exception as e:
            print(f"Erro ao atualizar equipamento: {e}")
            flash('Erro ao atualizar equipamento. Por favor, tente novamente.', 'error')
            db.session.rollback()

    return render_template('equipamento/lista_equipamento.html', form=form, equipamento=equipamento)

@app.route('/remover_equipamento/<int:equipamento_id>', methods=['GET', 'POST'])
def remover_equipamento(equipamento_id):
    equipamento = Equipamento.query.get_or_404(equipamento_id)

    if request.method == 'POST':
        try:
            db.session.delete(equipamento)
            db.session.commit()
            flash('Equipamento excluído com sucesso!', 'success')
            return redirect(url_for('listar_equipamentos'))
        except Exception as e:
            print(f"Erro ao excluir equipamento: {e}")
            flash('Erro ao excluir equipamento. Por favor, tente novamente.', 'error')
            db.session.rollback()

    return render_template('equipamento/remover_equipamento.html', equipamento=equipamento)
