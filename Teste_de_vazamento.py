import hashlib
import requests

def verificar_senha_vazada(senha):
    """
    Verifica se a senha já foi vazada usando a API Have I Been Pwned
    """
    # Gera o hash SHA-1 da senha
    sha1_senha = hashlib.sha1(senha.encode('utf-8')).hexdigest().upper()
    
    # Pega os primeiros 5 caracteres
    prefixo = sha1_senha[:5]
    sufixo = sha1_senha[5:]
    
    # Faz a requisição para a API
    url = f'https://api.pwnedpasswords.com/range/{prefixo}'
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            # Procura o sufixo na resposta
            hashes = response.text.splitlines()
            
            for linha in hashes:
                hash_sufixo, count = linha.split(':')
                if hash_sufixo == sufixo:
                    return True, int(count)  # Senha foi vazada
            
            return False, 0  # Senha não encontrada
        else:
            print("Erro ao consultar a API")
            return None, 0
            
    except Exception as e:
        print(f"Erro na conexão: {e}")
        return None, 0