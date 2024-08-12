import google.generativeai as genai
import os
from random import randint

tentativas = 0

#Coloque sua api no luga de "sua api"
genai.configure(api_key="AIzaSyAuptMLsAZq9BGWfMBy3dUB2ogG74NnumI")

#aqui escolhemos qual ia queremos usar
model = genai.GenerativeModel('gemini-pro')
#uma lista que é usada para que o chat com usuario, possa lembrar das antigas informações faladas
chat = model.start_chat(history=[])

print("Seja bem-vindo ao jogo de adivinhação\n")
print("Nesse jogo, temos duas opções\n")
print("1-O gemini acerta seu numero")
print("2-Voce acerta o numero do gemini\n")

escolha = int(input("OPÇÂO: "))
os.system("cls")

#nessa primeira opção o usuario ira escolher um numero
#e o usuario ira dar dicas para o gemini acertar seu numero
if escolha == 1:
    
    numero_usuario = str(input("Digite o seu numero: "))
    print("De dicas ao gemini até ele acertar seu numero")
    os.system("cls")
    while True:     
        texto = input("Usuario: ")
        print("-"*40)

        #prompt dado ao gemini para acertar seu numero 
        response = chat.send_message(f"Pensei em um numero: a dica que te dou é {texto}, voce so pode responder um numero, sem textos, não repita os numeros que voce ja disse, e leve em consideração sempre as ultimas informas que te passei")

        print("Gemini:", response.text)
        tentativas += 1
        print("-"*40)

        #se a response do gemini for igual ao numero_usuario damos um break no while
        if response.text == numero_usuario:
            print(f"Voce perdeu, ele acertou em {tentativas} tentativa(s)")
            break

#nessa segunda opção o gemini ira escolher um numero
#e o gemini ira dar dicas para o usuario acertar seu numero
elif escolha == 2:
    numero_gemini = randint(1,101)
    print(numero_gemini)
    while True:  
            #prompt dado ao gemini para dar dicas ao usuario 
            response = chat.send_message(f"Você dara apenas um dica por vez ao usuario para acertar esse numero {numero_gemini}, não diga qual numero é, não pode repetir dicas") 

            print("Gemini:", response.text)
            print("-"*40)
            numero = int(input("Usuario: "))
            tentativas += 1
            print("-"*40)

            #se o numero que o usuario chutou for igual ao numero_gemini.text, damos um break no while
            if numero == numero_gemini:
                print(f"Voce ganhou, voce acertou em {tentativas} tentativa(s)")
                break