from tkinter import *
from Functions import *

bg = "#777CB5"
fgE = "purple"


def linha(classe):
    linha = Label(classe, bg=bg).pack()


def logo(classe):
    logo = Label(classe, text='Py ManaGer', width='15', font='impact 30 ', fg='black', bg=bg).pack()


def button(nome, classe, texto, comando):
    nome = Button(classe, text=texto, width='15', font='Arial 16 bold', bg='#7F7F7F', fg='black',
                  command=comando).pack()


def label(nome, classe, texto):
    nome = Label(classe, text=texto, width='15', font='Arial 20 bold', fg='black', bg=bg)
    nome.pack()


def PyManaGer():
    saveV()
    pmg = Tk()
    pmg.title('Py ManaGer')

    def b1f():
        command = pmg.destroy()
        sellProduct()

    def b2f():
        command = pmg.destroy()
        home()

    def b3f():
        command = pmg.destroy()
        about()

    def b4f():
        command = pmg.destroy()

    logo(pmg)
    linha(pmg)
    button('b1', pmg, 'Vender', b1f)
    linha(pmg)
    button('b2', pmg, 'Gerenciar Produtos', b2f)
    linha(pmg)
    button('b3', pmg, 'Sobre', b3f)
    linha(pmg)
    button('b4', pmg, 'Sair', b4f)
    linha(pmg)

    pmg['bg'] = bg
    pmg.geometry("500x400+100+100")
    pmg.mainloop()


def sellProduct():
    sell = Tk()
    sell.title('Py ManaGer: Venda de Produtos')
    sell['bg'] = bg

    global sellTotal
    sellTotal = 0

    def b2f():
        ok = True
        en1['bg'] = 'white'
        en2['bg'] = 'white'
        nome = str(en1.get())
        nome = nome.upper().strip().replace(' ', '_')
        qnt = en2.get()
        try:
            qnt = int(qnt)
        except:
            ok = False
        if ok and qnt != 0:
            if check(nome):
                text = "{0} {2}*{1} {3}".format(nome, price(nome), qnt, float(price(nome)) * int(qnt))
                list1.insert(0, text)
                total = float(lt.get(0)) + float(price(nome)) * int(qnt)
                total = str(total)
                lt.delete(0)
                lt.insert(0, total)
            else:
                en1['bg'] = 'red'
        else:
            en2['bg'] = 'red'

    def b3f():
        command = sell.destroy()
        PyManaGer()

    def b4f():
        lt['bg'] = 'white'
        lt['selectbackground'] = 'white'
        if float(lt.get(0)) > 0:
            lista = list1.get(0, END)
            listax = ''
            for x in range(len(lista)):
                listax = listax + lista[x] + '\n'
            total = float(lt.get(0))
            total = str(total)
            impression(listax, total)
            command = sell.destroy()
            PyManaGer()

        else:
            lt['bg'] = 'red'
            lt['selectbackground'] = 'red'

    logo(sell)
    l1 = Label(sell, text='Nome Produto              Quantidade', font='Arial 14 bold', bg=bg).pack()
    row = Frame(sell, bg=bg)
    en1 = Entry(row, font='Arial 18', width='15')
    en1.pack(side=LEFT, padx='2')
    en2 = Entry(row, font='Arial 18', width='8')
    en2.pack(padx='2', side=LEFT)
    row.pack()
    l1 = Label(sell, font='Arial 2', bg=bg).pack()
    row2 = Frame(sell, bg=bg)

    b2 = Button(row2, text='Adicionar Produto', width='20', font='Arial 13 bold', bg='#7F7F7F', fg='black',
                command=b2f).pack()
    row2.pack(padx='4')
    l2 = Label(sell, font='Arial 2', fg=fgE, bg=bg)
    l2.pack()
    list1 = Listbox(sell, font='Arial 12', width='40', height='9')
    list1.pack()
    l3 = Label(sell, font='Arial 2', fg=fgE, bg=bg)
    l3.pack()
    row3 = Frame(sell, bg=bg)
    lt = Listbox(row3, width='15', height='1', font='Arial 16', bg='white', selectbackground='white',
                 selectforeground='black')
    lt.insert(0, "0.00")
    lt.pack(side=LEFT)
    b3 = Button(row3, text='Cancelar', width='10', font='Arial 13 bold', bg='#7F7F7F', fg='black', command=b3f)
    b3.pack(side=LEFT, padx='4')
    b4 = Button(row3, text='Inprimir', width='10', font='Arial 13 bold', bg='#7F7F7F', fg='black', command=b4f)
    b4.pack(side=LEFT, padx='4')
    row3.pack()

    sell.geometry("500x400+100+100")
    sell.mainloop()


def home():
    saveV()
    # s de Screean
    sHome = Tk()
    sHome.title('Py ManaGer: Gerenciar Produtos')
    sHome['bg'] = bg

    def b1f():
        command = sHome.destroy()
        newProduct()

    def b2f():
        command = sHome.destroy()
        alterProduct()

    def b3f():
        command = sHome.destroy()
        removeProduct()

    def b4f():
        command = sHome.destroy()
        listProduct()

    def b5f():
        command = sHome.destroy()
        PyManaGer()

    logo(sHome)
    linha(sHome)
    button('b1', sHome, 'Novo Produto', b1f)
    linha(sHome)
    button('b2', sHome, 'Alterar Produto', b2f)
    linha(sHome)
    button('b3', sHome, 'Remover Produto', b3f)
    linha(sHome)
    button('b4', sHome, 'Listar', b4f)
    linha(sHome)
    button('b5', sHome, 'Voltar', b5f)

    sHome.geometry("500x400+100+100")
    sHome.mainloop()


def newProduct():
    sNewP = Tk()
    sNewP.title('Py ManaGer: Novo Produto')
    sNewP['bg'] = bg

    def b1f():
        l2["text"] = ''
        en2['bg'] = 'white'
        nome = str(en1.get())
        nome = nome.upper().strip().replace(' ', '_')
        preco = str(en2.get())
        preco = preco.strip().replace(',', '.')
        if len(nome) > 1:
            if preco.replace('.', '').isdigit():
                if check(nome) == False:
                    register(nome, preco)
                    command = sNewP.destroy()
                    home()
                elif check(nome) == True:
                    l2["text"] = 'Produto já cadastrado!'
            else:
                en2['bg'] = 'red'
        else:
            l2["text"] = 'Verifique o Nome'

    def b2f():
        command = sNewP.destroy()
        home()

    logo(sNewP)
    linha(sNewP)
    label('l1', sNewP, 'Nome do produto')
    en1 = Entry(sNewP, font='Arial 20')
    en1.pack()
    l2 = Label(sNewP, font='Arial 12 bold', fg=fgE, bg=bg)
    l2.pack()
    label('l3', sNewP, 'Preço do produto')
    en2 = Entry(sNewP, font='Arial 20')
    en2.pack()
    linha(sNewP)
    button('b1', sNewP, 'Confirmar', b1f)
    linha(sNewP)
    button('b2', sNewP, 'Cancelar', b2f)
    sNewP.geometry("500x400+100+100")
    sNewP.mainloop()


def alterProduct():
    sAlterP = Tk()
    sAlterP.title('Py ManaGer: Alterar Produto')
    sAlterP['bg'] = bg

    def b1f():
        l2['text'] = ''
        nome = str(en1.get())
        nome = nome.upper().strip().replace(' ', '_')
        if check(nome) == True:
            command = sAlterP.destroy()
            alterName(nome)
        else:
            l2['text'] = 'Não encontrado!'

    def b2f():
        l2['text'] = ''
        nome = str(en1.get())
        nome = nome.upper().strip().replace(' ', '_')

        if check(nome) == True:
            command = sAlterP.destroy()
            alterPrice(nome)
        else:
            l2['text'] = 'Não encontrado!'

    def b3f():
        command = sAlterP.destroy()
        home()

    logo(sAlterP)
    linha(sAlterP)
    linha(sAlterP)
    label('l1', sAlterP, 'Nome do produto')
    en1 = Entry(sAlterP, font='Arial 20')
    en1.pack()
    l2 = Label(sAlterP, font='Arial 15 bold', fg=fgE, bg=bg)
    l2.pack(pady='2')
    button('b1', sAlterP, 'Alterar o Nome', b1f)
    linha(sAlterP)
    button('b2', sAlterP, 'Alterar o Preço', b2f)
    linha(sAlterP)
    button('b3', sAlterP, 'Voltar', b3f)
    sAlterP.geometry("500x400+100+100")
    sAlterP.mainloop()


def alterName(nome):
    sAlterN = Tk()
    sAlterN.title('Py ManaGer: Alterar Nome do Pruduto')
    sAlterN['bg'] = bg

    def b1f():
        l3['text'] = ""
        name = en1.get()
        newName = str(en1.get())
        newName = newName.upper().strip().replace(' ', '_')
        if check(newName):
            l3['text'] = "O nome já está sendo utilizado!"
        else:
            alterNames(nome, newName)
            command = sAlterN.destroy()
            home()

    def b2f():
        command = sAlterN.destroy()
        home()

    logo(sAlterN)
    linha(sAlterN)
    if len(nome) < 20:
        l1 = Label(sAlterN, text='Nome atual: ' + nome.title(), font='arial 15', fg=fgE, bg=bg).pack()
    else:
        l1 = Label(sAlterN, text='Nome atual: ' + nome[:20].title() + '...', font='arial 15', fg=fgE, bg=bg).pack()
    linha(sAlterN)
    label('l2', sAlterN, 'Novo Nome')
    en1 = Entry(sAlterN, font='Arial 20')
    en1.pack()
    l3 = Label(sAlterN, font='Arial 15 bold', fg=fgE, bg=bg)
    l3.pack(pady='2')
    button('b1', sAlterN, 'Confirmar', b1f)
    linha(sAlterN)
    button('b2', sAlterN, 'Cancelar', b2f)
    sAlterN.geometry("500x400+100+100")
    sAlterN.mainloop()


def alterPrice(nome):
    sAlterPr = Tk()
    sAlterPr.title('Py ManaGer: Alterar Preço do Pruduto')
    sAlterPr['bg'] = bg

    def b1f():
        l3['text'] = ''
        newPrice = str(en1.get())
        newPrice = newPrice.strip().replace(',', '.')
        if newPrice.replace('.', '').isdigit() and newPrice.count('.') <= 1 and float(newPrice) > 0:
            alterPrices(nome, newPrice)
            command = sAlterPr.destroy()
            home()
        else:
            l3['text'] = 'Verifique o valor inserido'

    def b2f():
        command = sAlterPr.destroy()
        home()

    logo(sAlterPr)
    linha(sAlterPr)
    preco = price(nome)
    if len(preco) < 20:
        l1 = Label(sAlterPr, text='Preço atual: R$' + preco.title(), font='arial 15', fg=fgE, bg=bg).pack()
    else:
        l1 = Label(sAlterPr, text='Preço atual: ' + preco[:20].title() + '...', font='arial 15', fg=fgE, bg=bg).pack()
    linha(sAlterPr)
    label('l2', sAlterPr, 'Novo Preço')
    en1 = Entry(sAlterPr, font='Arial 20')
    en1.pack()
    l3 = Label(sAlterPr, font='Arial 15 bold', fg=fgE, bg=bg)
    l3.pack(pady='2')
    button('b1', sAlterPr, 'Confirmar', b1f)
    linha(sAlterPr)
    button('b2', sAlterPr, 'Cancelar', b2f)
    sAlterPr.geometry("500x400+100+100")
    sAlterPr.mainloop()


def removeProduct():
    sRemoveP = Tk()
    sRemoveP.title('Py ManaGer: Remover Produto')
    sRemoveP['bg'] = bg

    def b1f():
        l2['text'] = ''
        name = str(en1.get())
        name = name.upper().strip().replace(' ', '_')
        if check(name):
            delete(name)
            command = sRemoveP.destroy()
            home()
        else:
            l2['text'] = 'Produto não encontrado!'

    def b2f():
        command = sRemoveP.destroy()
        home()

    logo(sRemoveP)
    linha(sRemoveP)
    label('l1', sRemoveP, 'Nome do produto')
    en1 = Entry(sRemoveP, font='Arial 20')
    en1.pack()
    l2 = Label(sRemoveP, font='Arial 15 bold', fg=fgE, bg=bg)
    l2.pack(pady='2')
    linha(sRemoveP)
    button('b1', sRemoveP, 'Confirmar', b1f)
    linha(sRemoveP)
    linha(sRemoveP)
    button('b2', sRemoveP, 'Cancelar', b2f)
    linha(sRemoveP)
    sRemoveP.geometry("500x400+100+100")
    sRemoveP.mainloop()


def listProduct():
    LP = Tk()
    LP.title('Py ManaGer: Lista de Produtos')
    LP['bg'] = bg

    def b1f():
        command = LP.destroy()
        home()

    all = listing()
    logo(LP)
    linha(LP)
    list1 = Listbox(LP, font='Arial 12', width='40', height='12')
    text = []
    w = 1
    for x in range(len(all)):
        if x % 2 != 0:
            text.append(all[x - 1])
            text.append(all[x])
            aaa = str(w) + ') ' + all[x - 1] + '  R$' + all[x]
            w = w + 1
            list1.insert(x, aaa.title())
            text = []
    list1.pack()
    linha(LP)
    button('b1', LP, 'Voltar', b1f)
    LP.geometry("500x400+100+100")
    LP.mainloop()


def about():
    about = Tk()
    about.title('Py ManaGer: Sobre')
    about['bg'] = bg

    def b1f():
        command = about.destroy()
        PyManaGer()

    logo(about)

    string = '-' * 44
    msgt = string + '\n  Projeto Final ADS 1 Módulo\n                        Data: 29/11/18\n' + string + '\n  Developer:\n  Jhonatan Luiz Chagas\n' + string
    msg = Message(about, text=msgt, font='Arial 20 bold', width='400', bg=bg)
    msg.pack()

    linha(about)
    button('b1', about, 'Voltar', b1f)
    about.geometry("500x400+100+100")
    about.mainloop()

PyManaGer()