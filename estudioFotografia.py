import sqlite3

class SessaoFotografia:
    def conexao(self):
        conexao = sqlite3.connect('sessaoFotografia.db')
        consulta = conexao.cursor()
        tabela = '''
        CREATE TABLE IF NOT EXISTS sessao(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente VARCHAR(100),
        data DATE ,
        tipo VARCHAR(100),
        preco FLOAT
        );
        ''' 
        consulta.execute(tabela)
        return conexao

    def cadastrarSessao(self, cliente, data, tipo, preco):
        conexao = self.conexao() 

        sql = 'INSERT INTO sessao VALUES (?,?,?,?,?)'


        campos = (None, cliente, data, tipo, preco)

        consulta = conexao.cursor()
        consulta.execute(sql, campos)

        conexao.commit()
        print("-"  * 50)
        print('Cadastro realizado com sucesso!')
        

    def consultarSessoes(self):
        conexao = self.conexao()
        consulta = conexao.cursor()

        sql = 'SELECT * FROM sessao'
        consulta.execute(sql)

        resultado = consulta.fetchall()

        for itens in resultado:
            if resultado == 0:
                print('Nenhuma sessão cadastrada')
            else:
                print(f'ID: {itens[0]}',end=' | ')
                print(f'Cliente: {itens[1]}',end=' | ')
                print(f'Data: {itens[2]}',end=' | ')
                print(f'Tipo: {itens[3]}',end=' | ')
                print(f'Preço: {itens[4]}')
    
    def deletarSessao(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor()


        sql = 'DELETE FROM sessao WHERE id = ?'
        campos = (id,)
        consulta.execute(sql, campos)

        conexao.commit()

        print(f'A sessão foi deletada com sucesso')
        


    
    def atualizarSessao(self,tipo, id):
        conexao = self.conexao()
        consulta = conexao.cursor()

        sql = 'UPDATE sessao SET tipo = ? WHERE id = ?'

        campos = (tipo, id)

        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, ' linha(s) atualizada(s) com sucesso')

        conexao.close()

    
    def consultarSessaoIndividual(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor()
        
        sql = 'SELECT * FROM sessao WHERE id = ?'
        campos = (id,)
        consulta.execute(sql, campos)

        individual = consulta.fetchall()

        if individual:
            for row in individual:
                print(f'ID: {row[0]}')
                print(f'Cliente: {row[1]}')
                print(f'Data: {row[2]}')
                print(f'Tipo: {row[3]}')
                print(f'Preço: {row[4]}')
                print('-' * 40)

        else:
            print('Consulta inválida, o ID não existe')