import pytesseract as tess
from PIL import Image
import PIL
import pyautogui
import time

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "?")
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

owner = 523473772548980736

coords_target_x = ["580", "580", "580", "580", "580", "975", "975", "975", "975", "975"]
coords_target_y = ["560", "600", "640", "680", "720", "560", "600", "640", "680", "720"]

coords_ip_left = ["600", "600", "600", "600", "600", "800", "800", "800", "800", "800"]
coords_ip_top = ["540", "580", "620", "660", "700", "540", "580", "620", "660", "700"]
coords_ip_right = ["750", "750", "750", "750", "750", "960", "960", "960", "960", "960"]
coords_ip_bottom = ["558", "598", "638", "678", "716", "558", "598", "638", "678", "716"]

coords_level_left = ["640", "640", "640", "640", "640", "935", "935", "935", "935", "935"]
coords_level_top = ["560", "600", "640", "680", "720", "560", "600", "640", "680", "720"]
coords_level_right = ["725", "725", "725", "725", "725", "960", "960", "960", "960", "960"]
coords_level_bottom = ["578", "618", "658", "698", "738", "578", "618", "658", "698", "738"]


def global_screen(): # capture global    GOOD
    snapshot = PIL.ImageGrab.grab()
    save_path = "C:/mes_projets/test/img" + ".png"
    snapshot.save(save_path)


def data(): # capture data in img   GOOD
    im = Image.open("img.png")
    left = 550  # GOOD
    top = 160  # GOOD
    right = 1010  # GOOD
    bottom = 495  # GOOD
    crop_done = im.crop((left, top, right, bottom))
    save_path = "C:/mes_projets/test/data" + ".png"
    crop_done.save(save_path)


def ip(): # global GOOD
    im = Image.open("img.png")
    left = int(coords_ip_left[loop])
    top = int(coords_ip_top[loop])
    right = int(coords_ip_right[loop])
    bottom = int(coords_ip_bottom[loop])
    crop_done = im.crop((left, top, right, bottom))
    save_path = "C:/mes_projets/test/ip" + ".png"
    crop_done.save(save_path)


def level(): # global
    im = Image.open("img.png")
    left = int(coords_level_left[loop])
    top = int(coords_level_top[loop])
    right = int(coords_level_right[loop])
    bottom = int(coords_level_bottom[loop])
    crop_done = im.crop((left, top, right, bottom))
    save_path = "C:/mes_projets/test/level" + ".png"
    crop_done.save(save_path)


def username(): # data  GOOD
    im = Image.open("data.png")
    left = 45  # GOOD
    top = 60  # GOOD
    right = 108  # GOOD
    bottom = 80  # GOOD
    crop_done = im.crop((left, top, right, bottom))
    save_path = "C:/mes_projets/test/username" + ".png"
    crop_done.save(save_path)
    

def username_verif(): # data    GOOD
    im = Image.open("data.png")
    left = 115  # GOOD
    top = 60  # GOOD
    right = 250  # GOOD
    bottom = 80  # GOOD
    crop_done = im.crop((left, top, right, bottom))
    save_path = "C:/mes_projets/test/username_verif" + ".png"
    crop_done.save(save_path)


def global_img(): # GOOD
    global_screen()
    data()


def send():
    ip_send = Image.open("ip.png")
    ip_split = tess.image_to_string(ip_send)
    ip_splited = ip_split.split("\n")   # ip done
        
    level_send = Image.open("level.png")
    level_split = tess.image_to_string(level_send)
    level_splited = level_split.split("\n")
        
    username_check_send = Image.open("username.png")
    username_check_split = tess.image_to_string(username_check_send)
    username_check_splited = username_check_split.split("\n")

    username_verif_send = Image.open("username_verif.png")
    username_verif_split =tess.image_to_string(username_verif_send)
    username_verif_splited = username_verif_split.split("\n")
    
    random_ip_channel = client.get_channel(802286081290403842)
    random_ip_channel.send(f"{ip_splited} {level_splited} {username_verif_splited}")
    # print(f"voici l'ip : {ip_splited[0]}\n\n")
    # print(f"voici le niveau : {level_splited[0]}\n\n")
    # print(f"voici la base de la comparaison : {username_check_splited[0]}\n\n")
    # print(f"voici le pseudo : {username_verif_splited[0]}\n\n")


loop = 0
done = 0
made = 0

def get():
    global loop
    global done
    while done < int(made):
        pyautogui.click(button="left", x=int(coords_target_x[loop]), y=int(coords_target_y[loop]))
        if loop == 0:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        elif loop == 1:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        elif loop == 2:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        elif loop == 3:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        elif loop == 4:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        elif loop == 5:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        elif loop == 6:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        elif loop == 7:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        elif loop == 8:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        elif loop == 9:
            global_img()
            ip()
            username()
            username_verif()
            level()
            
            send()
        
        loop = loop + 1
        done = done + 1
        
        if loop == 10:
            loop = 0


@client.event
async def on_ready():
    print("Bot connected")


    # commands
 
@client.command() # everyone
async def get(ctx, made : int):
    log_random_ip = client.get_channel()
    get()
    # await log_random_ip.send(f"{made} ip will be sent to <#802286081290403842>")


        # admin command
        
@client.command() # admin
async def clear(ctx, nombre : int):
    if ctx.author.id == owner:
        messages = await ctx.channel.history(limit = nombre + 1).flatten()
        for message in messages:
            await message.delete()
    else:
        await ctx.send(f"**{ctx.author.mention}** You do not have the rights to execute this command")

@client.command() # admin
async def shutdown(ctx):
    if ctx.author.id == owner:
        await ctx.send("done")
        messages = await ctx.channel.history(limit = 2).flatten()
        time.sleep(0.50)
        for message in messages:
            await message.delete()
        time.sleep(0.50)
        exit()
    else:
        await ctx.send(f"**{ctx.author.mention}** You do not have the rights to execute this command")

client.run("")
