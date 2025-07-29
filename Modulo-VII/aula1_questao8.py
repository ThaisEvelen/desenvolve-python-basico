def calcular_digito(cpf_parcial, multiplicadores):
    soma = sum(int(cpf_parcial[i]) * multiplicadores[i] for i in range(len(cpf_parcial)))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()

    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido: formato incorreto."

    cpf_parcial = cpf[:9]

    
    multiplicador1 = list(range(10, 1, -1))
    digito1 = calcular_digito(cpf_parcial, multiplicador1)

 
    cpf_parcial += digito1
    multiplicador2 = list(range(11, 1, -1))
    digito2 = calcular_digito(cpf_parcial, multiplicador2)

   
    if cpf.endswith(digito1 + digito2):
        return "CPF válido"
    else:
        return "CPF inválido"

cpf_usuario = input("Digite seu CPF (somente números ou com pontos e traço): ")
resultado = validar_cpf(cpf_usuario)
print(resultado)
