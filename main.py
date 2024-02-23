import nextcord
import aiohttp
import os
import random
from nextcord.ext import commands, tasks

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Your bot is ready!")
    game = nextcord.Game("Helps nature")
    await bot.change_presence(status=nextcord.Status.do_not_disturb, activity=game)

 # FAKE DONATE COMMAND
       
@bot.command(name="donate", description="Creates a fake donate and demands you to become a philanthropist")
async def donate(ctx, сумма: float):
    user = ctx.user.name

    if сумма >= 1000:
        await ctx.send(f'Внимание! {user} официально стал филантропом! Спасибо за щедрое пожертвование в размере {сумма}$!')
    elif сумма >= 100:
        await ctx.send(f'Спасибо, {user}, за донат в размере {сумма}$! Ты крутой!')
    elif сумма >= 0:
        await ctx.send(f'Спасибо за ваше пожертвование, {user}! Ваш вклад в размере {сумма}$ ценится.')
    else:
        await ctx.send("Пожалуйста, введите положительную сумму для пожертвования.")

#SET AVATAR COMMAND
@bot.slash_command(name='set_avatar', description='Set an animated avatar for the bot')
async def set_avatar():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(avatar_url) as resp:
                if resp.status == 200:
                    avatar_image = await resp.read()
                    await bot.user.edit(avatar=avatar_image)
                    await ctx.send("Avatar changed successfully.")
                else:
                    await ctx.send(f"Failed to fetch avatar. Status code: {resp.status}")
    except Exception as e:
        await ctx.send(f"Error changing avatar: {e}")

#ECOLOGY MEME GENERATOR
@bot.(name='ecology_memes', description="Sends you a random ecology meme.")
async def ecology_mem():
    meme_folder = "images"
    meme = [f for f in os.listdir(meme_folder) if os.path.isfile(os.path.join(meme_folder, f))]

    if meme:
        random_meme = os.path.join(meme_folder, random.choice(meme))
        with open(random_meme, 'rb') as f:
            picture = nextcord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send("No meme found.")
