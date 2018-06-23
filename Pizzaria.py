
def cadastro (): 
    somatoria = '1.2' + '2.3' + '3.4' + '4.5' + '5.6'
    print("=" * 40)
    print ("{:^40}".format("BEM-VINDO A PIZZARIA SENAI!"))
    print('=' * 40)
    contador = True
    if contador:

        while True:
                try:
                    nome = str(input("NOME (APENAS LETRAS) :\n==>> ")) .upper()
                    aux  = nome.replace(" ", "")
                    if aux.isalpha():
                        break
                except ValueError: 
                    print ("INVALIDO, POR FAVOR DIGITE NOVAMENTE SEU NOME.")
                    return nome 
                    
        
        while True :
                try:
                    telefone = input("INFORME SEU TELEFONE: \n==>>")
                    if telefone.isnumeric() and len (telefone) == 9:
                        break
                except ValueError: 
                    print ("INVALIDO, POR FAVOR DIGITE NOVAMENTE SEU TELEFONE\nSOMENTE NÚMEROS.")
           
           
        while True:
                try:
                    email = input("E-MAIL: \n==> ")
                    confirmarEmail = input("FAVOR CONFIME SEU E-MAIL: \n==>")
                    email_aux = email.find("@")
                    if email == confirmarEmail and email_aux > 0:
                        break
                except ValueError:
                    print("E-MAIL INVALIDO, COLOQUE SEU E-MAIL CORRETO.")
                    
                    
        while True:
                try:
                   senha = input("CADESTRE UMA SENHA COM NO MINIMO 6 DIGITOS: \n==>> ")
                   if senha.isalnum and len (senha) > 5:
                       criptografia = senha + somatoria
                       print("=" * 40)
                       print("""
                              BEM-VINDO, {}!      
                       DADOS CADASTRADOS COM SUCESSO!
                       Telefone: {}
                       E-mail:{}
                       Senha:{}
                       AGORA FAÇA SEU PEDIDO!
                       ========================================""".format(nome, telefone, email, senha))
                       break
                       
                except ValueError:
                    print ("POR FAVOR, SENHA ALFANUMÉRICA E MAIOR QUE 5 DÍGITOS.")                
    contador = False

def tamanho (preco = 0.0): 
    listas_tamanho = []
    codigo = input("""Faca seu pedido, digite:
    G para pizza grande, 
    M para pizza media,"
    P para pizza pequena:\n""").upper()
      
    while True:
        if codigo =="G":
            tamanho = "pizza grande"
            preco = 60.00
            break
        elif codigo == "M":
            tamanho = " pizza media"
            preco = 45.00
            break
        elif codigo == "P":
            tamanho = "pizza pequena"
            preco = 30.00
            break
        
    return lista_tamanho[preco, tamanho]


def sabor (): 
    print ("""Dê uma olhada nos seguintes sabores:
    	1  - Bacon; 
    	2  - Calabresa;
    	3  - Quatro Queijos;
    	4  - Marguerita;
    	5  - Vegetariana;
    	6  - Portuguesa;
    	7  - Lombo;
    	8  - Camarão;
    	9  - Atum;
    	10 - Especial do Chef.""")
        
    while True:
        try:
            numero = int (input ("Digite um número corrrespondente à sua escolha: "))
            if numero == 1: 
                sabor = "Bacon"
                break 
            elif numero == 2:
                sabor = "Calabresa"
                break
            elif numero == 3:
                sabor = "Quatro Queijos"
                break
            elif numero == 4:
                sabor = "Marguerita"
                break
            elif numero == 5:
                sabor = "Vegetariana"
                break
            elif numero == 6:
                sabor = "Portuguesa"
                break
            elif numero == 7:
                sabor = "Lombo"
                break
            elif numero == 8:
                sabor = "Camarão"
                break
            elif numero == 9:
                sabor = "Atum"
                break
            elif numero == 10:
                sabor = "Especial do Chef"
                break

        except ValueError:
            print ("Por favor, digite um número correspondente.")
    
    return sabor
def frete ():
    while True:
        try:
            entrega = input("""Digite: 
                           ( E )para entrega en domicilio
                           ( B ) para retirar no balcão: \n==>>""").upper()
            if entrega == "E":
                entrega = "Domicílio"
                break
            elif entrega == "B":
                entrega = "Balcão"
                break
        except ValueError:
            print ("Escolha um valor correto!")
            
    return entrega



def pagamento ():
    while True: 
        try:
            metodo = input("Qual será o seu método de pagamento? \n").capitalize ()
            if metodo ==  "Dinheiro":
                    print("Ótimo! A sua compra de R$ %0.2f foi efeituada com sucesso!" % A)
                    break
            elif  metodo == "Cartão":
                try:
                    cartao = input ("Débito ou crédito?").capitalize()
                    if cartao == "Debito":
                        print("A sua compra de R$ %0.2f foi efeituada com sucesso! Bonna Petit!" % A)
                        break
                    if cartao == "Credito".upper(): 
                        print("A sua compra de R$ {:.2f} foi efeituada com sucesso! Bonna Petit!".format (tamanho(A)))
                        break
                except ValueError: 
                    print ("Por favor, descreva corretamente o seu cartão.")
        except ValueError:
            print("Por favor, descreva corretamente a sua operação!")
            return metodo

def boleto ():
    print("""+++++++++++++++++++++++++++++++++++++++++++++++++++
      ++++++++++++++++++++++++++++++++++++++++++++++++++++++
      +++++++ Seu pedido foi efetuado com sucesso!!! +++++++
      ++++++++++++++++++++++++++++++++++++++++++++++++++++++
             +++++++++++++++++++++++++++++++++++++++++++++++++++
              TAMANHO: {}
              SABOR: {}
              ENTREGA: {}
              TOTAL: {}
      ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""".format(tamanho(0), sabor(), frete(), A))

cadastro ()
A = tamanho ()
pagamento ()
boleto ()
