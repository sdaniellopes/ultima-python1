#Sistema Magazine Luiza

estoque = {} #Armazenar os dados do meu sistema
for i in range(5):
    codigo = int(input("Digite o codigo do produto: "))
    categoria = input("Digite a categoria  do produto: ")
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))

    produto = {"codigo": codigo, "produto": nome, "info": descricao, "preco": preco}
    if categoria not in estoque:
        estoque[categoria] = []
        estoque[categoria].append(produto)
    else:
        estoque[categoria].append(produto)
print(estoque)

estoque = {'Eletrônicos': [{'codigo': 2568, 'produto': "Televisão Smart 70'", 'info': 'Televisão smart de 70 polegadas, para você assistir a filmes e séries com o maior que a tecnologia pode oferecer. Aproveite!', 'preco': 4799.99}, {'codigo': 2749, 'produto': 'Iphone 14 Pro Max 256GB', 'info': 'Iphone 14 Pro Max 256GB de armazenamento interno, acompanha carregador, capinha e película de vidro 3D. Entrega Grátis.', 'preco': 9499.99}, {'codigo': 1478, 'produto': 'Smartphone Samsung Galaxy S23 Ultra', 'info': 'Smartphone Galaxy S23 Ultra 512GB de armazenamento interno, 16GB de memória RAM. Câmera de 200MP e Zoom de 10X.', 'preco': 6799.99}, {'codigo': 3658, 'produto': 'Notebook Dell Inspiron', 'info': 'Notebook Dell Inspiron: 32GB de RAM, 1TB SSD, 4GB Placa de Vídeo Dedicada, Processador Intel Core i9.', 'preco': 12499.99}], 'Livros': [{'codigo': 6987, 'produto': 'Livro O Senhor dos Anéis (Volume único)', 'info': 'Livro da obra literária O senhor dos anéis, de J.R.R.Tolkien. Aproveite esta oferta exclusiva!', 'preco': 129.0}]}
print("------------------------------------------")
print("--------- Informações do produto ---------")
print("------------------------------------------")
for categoria in estoque:
    for produto in estoque[categoria]:
        print("PRODUTO:")
        print(f"Código: {produto['codigo']}")
        print(f"Categoria: {categoria}")
        print(f"Nome: {produto['produto']}")
        print(f"Descrição: {produto['info']}")
        print(f"Preço: {produto['preco']}\n")

