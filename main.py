from aiohttp import ClientSession
from random import shuffle
from os import listdir,mkdir
from colorama import init
from termcolor import colored
from asyncio import run
from multiprocessing import Process
async def parser():
    abc,headers=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9"],{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    while True:
        async with ClientSession(headers=headers) as session:
            async with session.get("https://thispersondoesnotexist.com/image") as image:
                shuffle(abc)
                abcd="".join(abc[:10])
                with open("date\\"+abcd+".jpg","wb") as saveImage:
                    saveImage.write(await image.content.read())
                    print(colored("Сохранено:","green"),colored(abcd+".jpg","yellow"))
def date():
    if not "date" in listdir("."):
        mkdir("date")
def run1():run(parser())
def threads():
    try:
        print(colored("Введите количество потоков(больше 10 - не рекомендую): ","magenta"),end="")
        for i in range(int(input())):
            Process(target=run1,args=()).start()
        print(colored("Работа начата...","blue"))
    except:
        print(colored("Неверное значение!","red"))
        threads()
if __name__ == '__main__':
    init()
    date()
    threads()
