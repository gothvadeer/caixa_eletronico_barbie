from tkinter import *
from PIL import Image, ImageTk
from time import sleep

janela = Tk()
janela.title('Caixa Eletrônico')
janela.geometry('800x600')
janela.configure(bg='pink')
saldo_atual = 5000
saque_total = 0
caixa = 0
pagamento = False
deposito_celular = True
nome = 'Alanne'


def menu_principal():
    conclusao['text'] = 'Deseja realizar mais uma operação?'
    botao1['text'] = 'SALDO'
    botao1['command'] = saldo
    botao2['text'] = 'SAQUE'
    botao2['command'] = saque
    botao3['text'] = 'PAGAR\nCONTA'
    botao3['command'] = pagar_conta
    botao4['text'] = 'DEPÓSITO'
    botao4['command'] = deposito
    botao5['text'] = 'DESBQ.\nCELULAR'
    botao5['command'] = desbloquear_celular
    botao6['text'] = 'SAIR'
    botao6['command'] = sair
    janela.update()


def saldo():
    conclusao['text'] = f'Seu saldo atual é R$ {saldo_atual:.2f}'
    janela.update()
    sleep(4)
    menu_principal()


def saque():
    conclusao['text'] = 'Quanto deseja sacar?'
    btn_valores()

def btn_valores():
    botao1['text'] = '50'
    botao1['command'] = saque50
    botao2['text'] = '100'
    botao2['command'] = saque100
    botao3['text'] = '500'
    botao3['command'] = saque500
    botao4['text'] = '1000'
    botao4['command'] = saque1000
    botao5['text'] = '1500'
    botao5['command'] = saque1500
    botao6['text'] = 'CONFIRMAR'
    botao6['command'] = confirmar_saque
    janela.update()

def saque50():
    global saque_total
    saque_total += 50
    conclusao['text'] = f'Valor  R$ {saque_total:.2f}'


def saque100():
    global saque_total
    saque_total += 100
    conclusao['text'] = f'Valor R$ {saque_total:.2f}'


def saque500():
    global saque_total
    saque_total += 500
    conclusao['text'] = f'Valor R$ {saque_total:.2f}'


def saque1000():
    global saque_total
    saque_total += 1000
    conclusao['text'] = f'Valor R$ {saque_total:.2f}'


def saque1500():
    global saque_total
    saque_total += 1500
    conclusao['text'] = f'Valor R$ {saque_total:.2f}'


def confirmar_saque():
    global saque_total, saldo_atual, pagamento
    if saque_total > saldo_atual:
        conclusao['text'] = f'Saldo insuficiente!\n' \
                            f'Saldo atual de R$ {saldo_atual:.2f}'
    else:
        saldo_atual -= saque_total
        if pagamento:
            conclusao['text'] = f'Pagamento realizado com sucesso'
            pagamento = False
        else:
            conclusao['text'] = f'Saque de R$ {saque_total:.2f} realizado com sucesso!\n' \
                f'Saldo atual de R$ {saldo_atual:.2f}'

        saque_total = 0
    janela.update()
    sleep(4)
    menu_principal()


def pagar_conta():
    global pagamento
    conclusao['text'] = 'Qual o valor do pagamento?'
    btn_valores()
    pagamento = True


def deposito():
    global deposito_celular, caixa
    if deposito_celular:
        conclusao['text'] = 'Qual o valor do deposito?'
    else:
        conclusao['text'] = 'Digite seu celular'
    botao1['state'] = DISABLED
    botao2['state'] = DISABLED
    botao3['state'] = DISABLED
    botao4['state'] = DISABLED
    botao5['state'] = DISABLED
    botao6['text'] = 'CONFIRMAR'
    botao6['command'] = confirmar_deposito
    caixa_texto = Entry(janela, font='georgia 15')
    caixa_texto.grid(column=2, row=3)
    caixa = caixa_texto

def confirmar_deposito():
    global caixa, saldo_atual, deposito_celular
    if caixa.get().isnumeric():
        valor_deposito = int(caixa.get())
        if deposito_celular:
            saldo_atual += valor_deposito
            conclusao['text'] = f'Valor R$ {valor_deposito:.2f} depositado com sucesso\n' \
                                f'Seu novo saldo é de R$ {saldo_atual:.2f}'
        else:
            conclusao['text'] = f'O número {valor_deposito} foi cadastrado com sucesso!'

    else:
        if deposito_celular:
            conclusao['text'] = 'Valor inválido'
        else:
            conclusao['text'] = 'Número inválido'
    deposito_celular = True
    caixa.destroy()
    janela.update()
    botao1['state'] = NORMAL
    botao2['state'] = NORMAL
    botao3['state'] = NORMAL
    botao4['state'] = NORMAL
    botao5['state'] = NORMAL
    sleep(4)
    menu_principal()


def desbloquear_celular():
    global deposito_celular
    deposito_celular = False
    deposito()

def sair():
    quit()


introducao = Label(janela, text=f'Bem vindo(a) ao seu caixa eletrônico, Senhor(a)'
                                f' {nome.title()}!', font='georgia', bg='pink', fg='deep pink')
introducao.grid(column=1, row=0, padx=10, pady=(50, 15), columnspan=3)

imagem_original = Image.open('visa.png')
imagem_usada = imagem_original.resize((300, 180))
img = ImageTk.PhotoImage(imagem_usada)
imagem = Label(janela, image=img, bg='pink')
imagem.grid(column=1, row=1, pady=10, columnspan=3)

conclusao = Label(janela, text='Deseja realizar alguma operação?', font='georgia', bg='pink')
conclusao.grid(column=1, row=2, padx=10, pady=30, columnspan=3)

botao1 = Button(janela, text='SALDO', command=saldo, height=3, width=8, bg='deep pink', fg='pink')
# Sticky 'w':  A letra 'w' representa o lado oeste (west) da célula (a margem esquerda.)
botao1.grid(column=0, row=3, padx=10, pady=5, sticky='w')
botao2 = Button(janela, text='SAQUE', command=saque, height=3, width=8, bg='deep pink', fg='pink')
botao2.grid(column=0, row=4, padx=10, pady=5, sticky='w')
botao3 = Button(janela, text='PAGAR\nCONTA', command=pagar_conta, height=3, width=8, bg='deep pink', fg='pink')
botao3.grid(column=0, row=5, padx=10, pady=5, sticky='w')
botao4 = Button(janela, text='DEPOSITO', command=deposito, height=3, width=8, bg='deep pink', fg='pink')
botao4.grid(column=4, row=3, padx=10, pady=5, sticky='e')
botao5 = Button(janela, text='DESBQ.\nCELULAR', command=desbloquear_celular, height=3, width=8, bg='deep pink', fg='pink')
# Sobre o sticky: faz com que o botão seja alinhado à direita dentro da célula em que está posicionado.
# A letra 'e' representa o lado leste (east) da célula (a margem direita).
botao5.grid(column=4, row=4, padx=10, pady=5, sticky='e')
botao6 = Button(janela, text='SAIR', command=sair, height=3, width=9, bg='orange', fg='white')
botao6.grid(column=4, row=5, padx=10, pady=5, sticky='e')
# Configura a primeira coluna (índice 0) para ter peso igual a 1
janela.grid_columnconfigure(0, weight=1)
# Configura a quinta coluna (índice 4) para ter peso igual a 1
janela.grid_columnconfigure(4, weight=1)
#  configura a sétima linha da janela principal (janela) para ter um peso igual a 1.
janela.grid_rowconfigure(6, weight=1)

janela.mainloop()
