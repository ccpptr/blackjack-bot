import time
import os
import sys
from multiprocessing.connection import wait
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
def printSameLine(string):
    import sys
    sys.stdout.write(string)
    sys.stdout.flush()
os.system("")
red='\033[31m'
outracor='\033[33m'
normal = '\033[0m'
print(outracor+'********************************************************************************************')
print("* "+red+"                                     Roulette Bot 1.0                                    "+outracor+"*\n* "+red+"Faça apostas automáticas no Roleta do TibiaBlackJack seguindo a estratégia de Martingale "+outracor+"*")
print('********************************************************************************************'+normal)
time.sleep(0.2)
printSameLine("Loading")
time.sleep(0.2)
printSameLine(".")
time.sleep(0.2)
printSameLine(".")
time.sleep(0.2)
printSameLine(".")
time.sleep(0.2)

user=input("\n Digite o nome de usuário para confirmar que o bot fez o login:\n")
valorApostado=int(input("Qual a aposta mínima desejada?\n"))
n=int(input("Até quantas vezes você quer dobrar a aposta mínima?\n"))-1
apostaMinima=valorApostado
saldoLimite=16*valorApostado
# options = Options()
# options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://tibiablackjack.com/roulette")
# title = WebDriverWait(driver, timeout=10).until(lambda d: d.title)
# print(title)
loginButton = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH,'//*[@id="root"]/nav/section[2]/div[2]/div/button'))
loginButton.click()
# time.sleep(40)
print("Aguarde: ")
for tempo in range(40):
    print(40-tempo)
    time.sleep(1)
    
isLogged = WebDriverWait(driver, timeout=41).until(lambda d: d.find_element(By.XPATH,'//*[@id="root"]/nav/section[2]/div[2]/div/a[2]/span')).text                                           

#####FUNÇÃO QUE VERIFICA SE DEU VERMELHO OU PRETO E DOBRA APOSTA
def verifica_se_ganhou(totalCoins, antigoTotalCoins,valorApostado):
        if float(totalCoins)>=float(antigoTotalCoins):
            valorApostado=apostaMinima
            print('Ganhou!!! - Aposta ',valorApostado)
            print('\n===================================\n')
        elif valorApostado>apostaMinima*(2**n):
            valorApostado=apostaMinima
            print(f'Perdeu {n+2} rodadas seguidas!!! - Aposta {valorApostado}')
            print('\n===================================\n')
        else:
            valorApostado*=2
            print('Perdeu!!! - Aposta ',valorApostado)
            print('\n===================================\n')
        return valorApostado
###################################################################    

if isLogged==user: 
    print("Login realizado com SUCESSO!!!")

    #### Se estiver logado, começa a lógica###
    aposta=WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/div/section[3]/div[1]/div[1]/input'))
    rodando=WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="counter"]/p'))
    totalCoins=WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/nav/section[2]/div[2]/div/div/div[1]/div[1]/span')).text
    antigoTotalCoins=totalCoins
    enviaAposta=WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/div/section[3]/div[2]/button[1]'))
    # valorApostado=1
    
    
    
    while int(float(totalCoins))>valorApostado:
        rodando=WebDriverWait(driver, timeout=20).until(lambda d: d.find_element(By.XPATH, '//*[@id="counter"]/p'))
        # antigoTotalCoins=WebDriverWait(driver, timeout=10 ).until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/nav/section[2]/div[2]/div/div/div[1]/div[1]/span')).text
        if rodando.is_displayed():
            #termina aposta com antigo total/dinheiro antes de fazer a aposta
            totalCoins=WebDriverWait(driver, timeout=10 ).until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/nav/section[2]/div[2]/div/div/div[1]/div[1]/span')).text
            totalCoins=float(totalCoins)
            print('novo total:', totalCoins)
            print('antigo total:', antigoTotalCoins)
            valorApostado=verifica_se_ganhou(totalCoins, antigoTotalCoins,valorApostado)
            antigoTotalCoins=float(totalCoins)
            aposta.click()
            aposta.click()
            actions = ActionChains(driver)
            actions.double_click(aposta).perform()
            aposta.clear()
            aposta.clear()
            aposta.clear()
            aposta.send_keys(str(valorApostado))
            enviaAposta.click()
            time.sleep(11)
            
            # totalCoins=WebDriverWait(driver, timeout=10 ).until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/nav/section[2]/div[2]/div/div/div[1]/div[1]/span')).text   
        else:
            print('chegou no else pelo menos')
            totalCoins=WebDriverWait(driver, timeout=10 ).until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/nav/section[2]/div[2]/div/div/div[1]/div[1]/span')).text
            # print('novo total:',totalCoins)
            
            rodando=WebDriverWait(driver, timeout=20).until(lambda d: d.find_element(By.XPATH, '//*[@id="counter"]/p'))
            # novoTotalCoins=totalCoins
            
        # if totalCoins>antigoTotalCoins:
        #     valorApostado=1
        # else:
        #     valorApostado*=2
        
else:
    print("Erro ao realizar LOGIN")
    driver.close()



