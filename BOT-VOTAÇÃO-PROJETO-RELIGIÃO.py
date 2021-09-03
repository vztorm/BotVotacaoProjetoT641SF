import pyautogui
import time

# bot para votar no video da turma 641(projeto de religião)

# bugs: se o captcha pede pra clicar nas imagens ele não consegue passar

# bot feito por vitor annes simas

pyautogui.PAUSE = 1 # regula a velocidade


pyautogui.press("win") # abre menu iniciar

pyautogui.write("brave") # pesquisa pelo app brave

pyautogui.press("enter") # entra no app

pyautogui.click(x=903, y=54) # clica na barra de endereço

pyautogui.write("https://www.curtanaeducacao.org.br/video/439/dialogar-nesta-pratica-voce-faz-a-diferenca") # escreve o endereço do site

pyautogui.press("enter") # entra no site

pyautogui.PAUSE = 0 # pausa zero para deixar mais rápido

time.sleep(3) # tempo pro site carregar

pyautogui.press("down") # vai até o ponto necessario dentro do site

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down")

pyautogui.press("down") # final

pyautogui.PAUSE = 1 # ajusta a velocidade para o codigo funcionar

pyautogui.click(x=231, y=636) # passa o captcha

pyautogui.click(x=231, y=636) # mesma coisa

pyautogui.PAUSE = 2 # ajusta a velocidade para contabilizar o captcha

pyautogui.click(x=565, y=616) # clica em votar

pyautogui.click(x=565, y=616) # clica em votar denovo para confirmar

pyautogui.click(x=866, y=169) # clica em ok para reiniciar o processo
 
# bot feito por vitor annes simas

