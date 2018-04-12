#!/usr/bin/env python3

import os

def main():
	teste = True
	while(teste):
		file_name = input("Nome do arquivo: \n")
		display_name = input("Nome visível ao usuário: \n")
		type_app = input("Tipo do lançador: \n")
		exec_path = input("Caminho do executável: \n")
		icon = input("Caminho do ícone: \n")
		teste_shell = True
		
		while(teste_shell):
			shell = input("O aplicativo é executado via terminal(S/N)? \n")
			if(shell.upper()== 'S'):
				terminal = "true"
				teste_shell = False
			elif(shell.upper() == 'N'):
				terminal = "false"
				teste_shell = False
			else:
				teste_shell = True
		categories = input("""A quais categorias este aplicativo pertence? (Informe os nomes separando-os e finalizando com ';' Ex.: Graphics;Network;)? \n""")
		comment = input("Comentário (Ex.: Reprodutor de audio, Navegador Web e etc.): \n")
		text = formatar_dados(display_name, type_app, exec_path, icon, terminal, categories, comment)
		var = True
		while(var):
			print("----------- VERIFICAÇÃO DE DADOS ----------- \n")
			exibir_dados(text)
			print("------------------------------------------------ \n")
			verifica = input("Os dados estão corretos (S/N) ?")
			if(verifica.upper() == 'S'):
				gravar_arquivo(file_name, text)
				var = False
				teste = False
			elif(verifica.upper() == 'N'):
				var = False
				teste = True
			else:
				print("Entrada inválida!")
				var = True


def formatar_dados(display_name, type_app, exec_path, icon, terminal, categories, comment):
	texto = []
	texto.append("[Desktop Entry] \n")
	texto.append("Version=1.0")
	texto.append("Encoding=UTF-8")
	texto.append("Type=%s" % type_app)
	texto.append("Name=%s" % display_name)
	texto.append("Exec=%s" % exec_path)
	texto.append("Icon=%s" % icon)
	texto.append("Terminal=%s" % terminal)
	texto.append("Categories=%s" % categories)
	texto.append("Comment=%s" % comment)
	return texto

def gravar_arquivo(file_name, dados):
	file = "/usr/share/applications/%s.desktop" % file_name
	lancador = open(file, 'w')
	for line in dados:
		lancador.write(line + '\n')
	lancador.close()
	os.system("chmod +x %s" % file)


def exibir_dados(dados):
	for line in dados:
		print(line)


if __name__ == '__main__':
	main()