import pandas
import pyautogui
import time
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
# abrir o opera
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
# entrar no site da empresa
time.sleep(2)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(2)
# cadastrar no site da empresa
pyautogui.click(x=874, y=384)
pyautogui.write('lucas@gmail.com')
pyautogui.press('tab')
pyautogui.write('12344556324234324233424')
pyautogui.press('tab')
pyautogui.press('enter')
# importa base de dados
tabela = pandas.read_csv("arquivo.csv")
# cadastrar o primeiro produto

for linha in tabela.index:
    time.sleep(2)
    pyautogui.click(x=930, y=274)
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]
    time.sleep(2)
    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    if not pandas.isna(obs): # se nao vazio (isna(verifica se esta vazio)) 
        pyautogui.write(str(obs))
    # passar para o botao de enviar
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.scroll(1000)
    time.sleep(0.2)
    # repetir para todos os produtos