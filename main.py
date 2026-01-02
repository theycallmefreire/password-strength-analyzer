import os
from Teste_de_vazamento import verificar_senha_vazada

logo = '''
                                                                     
 mm              mm         ]                    ."          .       .m 
]` `. .  m,     ]` ` m, .., ].,  m,      m,     .dm  m,  ,m .dm  m,  ` [
'bm ] ] ' ]     'bm ]`] ]`] ]`] ' ]     ]`]      ]  ]`T  P ` ]  ]`]  .P 
  '[] ] ."T       '[]"" ] ] ] ] ."T     ]""      ]  ] ]  [   ]  ]""  '  
'md`'mT 'mT     'md`'b/ ] ] ] ] 'mT     'b/      ]  'bP  [   'm 'b/  ]  
                                                                        
'''

while True:
    pontos = 0
    feedback = []

    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title Sua Senha é Fraca? - by Theycallmefreire')
    print(logo)
    x = input('Aperte Enter pra começar!')
   
    if x == '':
        senha = input('Digite uma senha para verificar se é forte: ')

        # Verificando comprimento
        if len(senha) >= 12:
            pontos += 3
        elif len(senha) >= 8:
            pontos += 2
        else:
            pontos -= 5
            feedback.append('- A senha deve ter pelo menos 8 caracteres.')
        
        # Verifica letras minúsculas
        if any(c.islower() for c in senha):
            pontos += 2
        else:
            pontos -= 1
            feedback.append('- Falta letras minúsculas (a-z)')

        # Verifica letras maiúsculas
        if any(c.isupper() for c in senha):
            pontos += 2
        else:
            pontos -= 1
            feedback.append('- Falta letras maiúsculas (A-Z)')

        # Verifica números
        if any(c.isdigit() for c in senha):
            pontos += 2
        else:
            pontos -= 1
            feedback.append('- Falta números (0-9)')

        # Verifica caracteres especiais
        if any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in senha):
            pontos += 3
        else:
            pontos -= 1
            feedback.append('- Falta caracteres especiais (!@#$% etc)')
        
        print(f'\nSua pontuação final é: {pontos} pontos.')
        
        if feedback:
            print('\nMelhorias necessárias:')
            for item in feedback:
                print(item)
        else:
            print('\nSenha forte! Passou em todos os critérios.')

        # Verificando se a senha foi vazada
        foi_vazada, vezes = verificar_senha_vazada(senha)

        if foi_vazada:
            pontos -= 10  
            print(f' ALERTA! Esta senha foi vazada {vezes} vezes em vazamentos de dados!\n RECOMENDO TROCAR SENHA')
        elif foi_vazada == False:
            pontos += 5
            print(' Senha não encontrada em vazamentos conhecidos')
    else:
        print('Entrada inválida. Por favor, aperte Enter para começar.')

    f = input('\nAperte Enter pra recomeçar ou digite "sair" para encerrar: ')
    if f == 'sair':
        break