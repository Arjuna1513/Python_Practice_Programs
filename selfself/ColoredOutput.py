from colorama import Fore, Style
class ColoredOutput:
    def color(self):
        print(Fore.GREEN+ "I am Green")
        print(Fore.CYAN+ "I am Cyan")

x = ColoredOutput()
x.color()