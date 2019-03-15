from datetime import datetime

saveP = 'save.txt'
historic = 'historico.txt'
notinha = 'notaFiscal.txt'


def dataHora():
    now = datetime.now()
    data = 'data: {}/{}/{}'.format(now.day, now.month, now.year)
    hora = 'hora: {}:{}:{}'.format(now.hour, now.minute, now.second)
    return (data + ' ' + hora)


def impression(gravar, total):

    mm = '{}'.format('-' * 36)
    gravar = 'Py Manager\n{}\nTotal R${}\n{}{}'.format(dataHora(), total, gravar, mm)

    with open(historic, 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
        if conteudo == '':
            with open(historic, 'w', encoding='utf-8') as arq:
                arq.write(gravar.upper())
        else:
            with open(historic, 'w', encoding='utf-8') as arq:
                gravarx = conteudo + "\n" + gravar
                arq.write(gravarx.upper())

    with open(notinha, 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
        if conteudo == '':
            with open(notinha, 'w', encoding='utf-8') as arq:
                arq.write(gravar.upper())
        else:
            with open(notinha, 'w', encoding='utf-8') as arq:
                arq.write(gravar.upper())


def saveV():
    try:
        with open(historic, 'r', encoding='utf-8') as arq:
            pass
    except:
        with open(historic, 'w', encoding='utf-8') as arq:
            pass
    try:
        with open(notinha, 'r', encoding='utf-8') as arq:
            pass
    except:
        with open(notinha, 'w', encoding='utf-8') as arq:
            pass
    try:
        with open(saveP, 'r', encoding='utf-8') as arq:
            pass
    except:
        with open(saveP, 'w', encoding='utf-8') as arq:
            pass


def priceT(preco):
    return str(float(preco))


def check(x):
    with open(saveP, 'r', encoding='utf-8') as arq:
        conteudo = arq.read().split()
        if x in conteudo and index(x) % 2 == 0:
            return True
        else:
            return False


def index(nome):
    with open(saveP, 'r', encoding='utf-8') as arq:
        conteudo = arq.read().split()
        for x in range(len(conteudo)):
            p = conteudo[x]
            if p == nome:
                indice = x
                return x


def register(produto, preco):
    with open(saveP, 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
        if conteudo == '':
            with open(saveP, 'w', encoding='utf-8') as arq:
                gravar = produto + "\n" + priceT(preco)
                arq.write(gravar.upper())
        else:
            with open(saveP, 'w', encoding='utf-8') as arq:
                gravar = conteudo + "\n" + produto + "\n" + priceT(preco)
                arq.write(gravar.upper())


def alterNames(nome, nomeN):
    with open(saveP, 'r', encoding='utf-8') as arq:
        conteudo = arq.read().split()
        conteudo.pop(index(nome))
        conteudo.insert(index(nome), nomeN)
    with open("save.txt", 'w', encoding='utf-8') as arq:
        gravar = "\n".join(conteudo)
        arq.write(gravar)


def price(nome):
    with open(saveP, 'r', encoding='utf-8') as arq:
        conteudo = arq.read().split()
        return conteudo[index(nome) + 1]


def alterPrices(nome, preco):
    with open(saveP, 'r', encoding='utf-8') as arq:
        conteudo = arq.read().split()

    indice = index(nome) + 1
    preco = str(preco)
    conteudo.pop(indice)
    conteudo.insert(indice, priceT(preco))

    with open("save.txt", 'w', encoding='utf-8') as arq:
        gravar = "\n".join(conteudo)
        arq.write(gravar)


def delete(nome):
    with open(saveP, 'r', encoding='utf-8') as arq:
        conteudo = arq.read().split()
        conteudo.pop(index(nome))
        conteudo.pop(index(nome))
    with open("save.txt", 'w', encoding='utf-8') as arq:
        gravar = "\n".join(conteudo)
        arq.write(gravar)


def listing():
    with open(saveP, 'r', encoding='utf-8') as arq:
        conteudo = arq.read()
        return conteudo.split()
