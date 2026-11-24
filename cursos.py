CURSOS_UFRPE = {  # dicionário: a chave é o número do curso; o valor é outro dicionário com o nome e a tag do departamento
    1: {"curso": "BACHARELADO EM ADMINISTRAÇÃO", "tag": "#DEPAD"},
    2: {"curso": "BACHARELADO EM AGRONOMIA", "tag": "#DEPAGRO"},
    3: {"curso": "BACHARELADO EM CIÊNCIA DA COMPUTAÇÃO", "tag": "#CEAGRI_2"},
    4: {"curso": "BACHARELADO EM CIÊNCIAS BIOLÓGICAS", "tag": "#DEPBIO"},
    5: {"curso": "BACHARELADO EM CIÊNCIAS CONTÁBEIS", "tag": "#DECON"},
    6: {"curso": "BACHARELADO EM CIÊNCIAS ECONÔMICAS", "tag": "#DECON"},
    7: {"curso": "BACHARELADO EM CIÊNCIAS SOCIAIS", "tag": "#DECISO"},
    8: {"curso": "BACHARELADO EM ENGENHARIA AGRÍCOLA E AMBIENTAL", "tag": "#DEAGRI"},
    9: {"curso": "BACHARELADO EM ENGENHARIA AMBIENTAL", "tag": "#DTR"},
    10: {"curso": "BACHARELADO EM ENGENHARIA DE PESCA", "tag": "#DEPAQ"},
    11: {"curso": "BACHARELADO EM ENGENHARIA FLORESTAL", "tag": "#DCFL"},
    12: {"curso": "BACHARELADO EM GASTRONOMIA", "tag": "#DTR"},
    13: {"curso": "BACHARELADO EM MEDICINA VETERINÁRIA", "tag": "#DMV"},
    14: {"curso": "BACHARELADO EM SISTEMAS DE INFORMAÇÃO", "tag": "#DEINFO"},
    15: {"curso": "BACHARELADO EM ZOOTECNIA", "tag": "#DZ"},
    16: {"curso": "BACHARELADO EM ECOLOGIA", "tag": "#DEPBIO"},
    17: {"curso": "BACHARELADO EM EDUCAÇÃO FÍSICA", "tag": "#DEPED"},
    18: {"curso": "LICENCIATURA EM CIÊNCIAS AGRÍCOLAS", "tag": "#DEAGRI"},
    19: {"curso": "LICENCIATURA EM CIÊNCIAS BIOLÓGICAS", "tag": "#DEPBIO"},
    20: {"curso": "LICENCIATURA EM COMPUTAÇÃO", "tag": "#CEAGRI_2"},
    21: {"curso": "LICENCIATURA EM ECONOMIA DOMÉSTICA", "tag": "#DECON"},
    22: {"curso": "LICENCIATURA EM EDUCAÇÃO FÍSICA", "tag": "#DEPFIS"},
    23: {"curso": "LICENCIATURA EM FÍSICA", "tag": "#DEPFIS"},
    24: {"curso": "LICENCIATURA EM HISTÓRIA", "tag": "#DECISO"},
    25: {"curso": "LICENCIATURA EM LETRAS", "tag": "#DECISO"},
    26: {"curso": "LICENCIATURA EM MATEMÁTICA", "tag": "#CEAGRI_2"},
    27: {"curso": "LICENCIATURA EM PEDAGOGIA", "tag": "#DECISO"},
    28: {"curso": "LICENCIATURA EM CIÊNCIAS SOCIAIS", "tag": "#DECISO"},
    29: {"curso": "LICENCIATURA EM ARTES VISUAIS", "tag": "#DECISO"},
    30: {"curso": "LICENCIATURA EM GEOGRAFIA", "tag": "#DECISO"},
}  # fim do dicionário de cursos

def selecionar_curso_usuario():  # mostra os cursos e devolve o que o usuário escolheu
    print("Qual o seu curso? (Digite o número correspondente)\n")  # título da lista

    for numero, info in CURSOS_UFRPE.items():  # percorre o dicionário: numero = chave, info = {curso, tag}
        print(f"{numero}: {info['curso']}")  # mostra cada curso, ex: 3: BACHARELADO EM CIÊNCIA DA COMPUTAÇÃO

    print("-" * 50)  # linha separadora

    while True:  # repete até o usuário digitar um número válido
        resposta = input("Digite o número do seu curso: ").strip()  # lê a resposta como texto

        if resposta.isdigit() and int(resposta) in CURSOS_UFRPE:  # é só número E existe na lista?
            num_escolhido = int(resposta)  # converte o texto para número inteiro
            curso_selecionado = CURSOS_UFRPE[num_escolhido]  # pega os dados do curso escolhido

            return {  # devolve um dicionário com o nome do curso e a tag
                "curso": curso_selecionado["curso"],
                "tag": curso_selecionado["tag"]
            }
        else:  # número inválido ou texto
            print("Número inválido! Você deve digitar um número entre os disponíveis que seja do seu curso.")
