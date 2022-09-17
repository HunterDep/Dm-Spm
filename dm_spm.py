import os
clear = lambda: os.system("clear")
try:
	import discord, pyfiglet
	from discord.ext import commands
	from colorama import Fore
except:
	os.system("pip install python-discord")
	os.system("pip install colorama")
	os.system("pip install pyfiglet")
	import discord, pyfiglet
	from discord.ext import commands
	from colorama import Fore

def banner(x=15):
	banner = pyfiglet.figlet_format("DmSpm".center(x))
	print(Fore.GREEN + banner + Fore.RESET)
	
def DmSpm():
	banner()
	print(f"{Fore.GREEN}Criado Por: {Fore.RED}HunterDep{Fore.GREEN}\nGithub: {Fore.RED}https://github.com/HunterDep{Fore.RESET}")
	token = input(f"\n[{Fore.RED}>{Fore.RESET}] Token: " + Fore.RED)
	msg = input(Fore.RESET + f"[{Fore.RED}>{Fore.RESET}] Mensagem: " + Fore.RED)
	
	intents = discord.Intents.all()
	bot = commands.Bot(command_prefix=None, self_bot=True, intents=intents)
	
	@bot.event
	async def on_ready():
		clear()
		for servidores, servidor in enumerate(bot.guilds):
			servidores += 1
		for amigos, amigo in enumerate(bot.user.friends):
			amigos += 1
			
		print(Fore.GREEN + f"Conectado Em: {Fore.RED}{bot.user}{Fore.GREEN}\nServidores: {Fore.RED}{servidores}{Fore.GREEN}\nAmigos: {Fore.RED}{amigos}{Fore.RESET}")
		
		for amigo in bot.user.friends:
			try:
				print(Fore.RESET + f"Mandando Mensagem Para: {Fore.GREEN}{amigo}{Fore.RESET}")
				await amigo.send(msg)
			except:
				pass
	
	bot.run(token, bot=False)
	
DmSpm()
