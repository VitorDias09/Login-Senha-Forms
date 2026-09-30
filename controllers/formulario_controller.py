from models.formulario_model import FormularioModel  

class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        if not data:
            return {"error": "Todos os campos são obrigatórios"}, 400

        nome = data.get('nome')  
        email = data.get('email') 
        data_nascimento = data.get('data_nascimento') 
        cpf = data.get('cpf')  
        genero = data.get('genero')  

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400  

        formulario = FormularioModel.create_formulario(
            user_id,
            str(nome).strip(),
            str(email).strip(),
            str(data_nascimento).strip(),
            str(cpf).strip(),
            str(genero).strip()
        )
        if formulario:
            return {"message": "Formulário criado com sucesso"}, 201
        return {"error": "Erro ao criar formulário"}, 500 

    @staticmethod
    def get_formulario_by_id(formulario_id):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"error": "Formulário não encontrado"}, 404
        return formulario, 200

    @staticmethod
    def update_formulario(formulario_id, data):
        if not data:
            return {"error": "Dados para atualização não fornecidos"}, 400

        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"error": "Formulário não encontrado"}, 404

        nome = data.get('nome', formulario['nome'])
        email = data.get('email', formulario['email'])
        data_nascimento = data.get('data_nascimento', formulario['data_nascimento'])
        cpf = data.get('cpf', formulario['cpf'])
        genero = data.get('genero', formulario['genero'])

        if not str(nome).strip() or not str(email).strip() or not str(data_nascimento).strip() or not str(cpf).strip() or not str(genero).strip():
            return {"error": "Nenhum campo pode ser vazio"}, 400

        if FormularioModel.update_formulario(
            formulario_id,
            str(nome).strip(),
            str(email).strip(),
            str(data_nascimento).strip(),
            str(cpf).strip(),
            str(genero).strip()
        ):
            return {"message": "Formulário atualizado com sucesso"}, 200
        return {"error": "Erro ao atualizar formulário"}, 500

    @staticmethod
    def delete_formulario(formulario_id):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"error": "Formulário não encontrado"}, 404

        if FormularioModel.delete_formulario(formulario_id):
            return {"message": "Formulário excluído com sucesso"}, 200
        return {"error": "Erro ao excluir formulário"}, 500