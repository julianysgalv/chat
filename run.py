from flask import Flask, render_template, redirect, request,session
from controllers.clientes import Cliente
from controllers.mensagens import Mensagem
from datetime import datetime
from controllers.sql import Banco
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)
app.secret_key = 'senai123'

# Rotas
# ------------------------------------------------------
@app.route('/')
def index():
    return render_template('login.html')



@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        cliente = Cliente(request.form.get('usuario'), request.form.get('senha'))
        try:
            cliente.inserir_usuario()
            return redirect('/chat')
        except Exception:
            return render_template('erro.html', erro="impossivel cadastrar")

    return render_template('cadastro.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
     if request.method == 'POST':
        cliente = Cliente()
      
        resultado = cliente.logar(request.form.get('usuario'), request.form.get('senha'))
      
        if resultado:            
            
            session['usuario'] = resultado 
                         
            return redirect('/chat')
        else:
             return redirect('/')
     return render_template('login.html')

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    mensagem = Mensagem(None,None,None)

    if not session.get('usuario'):
        return redirect('/')
    
    lista_mensagens = mensagem.carregar_mensagens()

    usuario = session['usuario'][1]

    # lista_minhas_mensagens = mensagem.carregar_minhas_mensagens(usuario)

    socketio.emit('atualizar_lista')
    
    print(lista_mensagens)
    return render_template('chat.html', lista_mensagens=lista_mensagens) 

@app.route('/enviar_mensagens', methods=['POST', 'GET'])
def enviar_mensagem():
    if request.method == 'POST':
        texto = request.form.get('mensagem')
        nome_usuario = session['usuario'][1]
        mensagem = Mensagem(texto, datetime.now(), nome_usuario)
       
        mensagem.inserir_mensagem()

        data = {
        'sender': nome_usuario,
        'message': texto,
        'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

        print(texto)
        
        print(session['usuario'])
        socketio.emit('atualizar_lista', data)
    
        return redirect('/chat')


socketio.run(app, host="127.0.0.1", port=80, debug=True)