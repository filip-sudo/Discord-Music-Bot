import discord
from discord.utils import get
from discord import TextChannel
from discord import FFmpegPCMAudio
from discord.ext import commands
from youtube_dl import YoutubeDL
import ffmpeg

client = commands.Bot(command_prefix="!")

#Online check

@client.event  # check if bot is ready
async def on_ready():
    print('Bot online')

#playing the music

@client.command()
async def p(ctx, url):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await ctx.send("Sviram drugde gazda")
    else:
        await channel.connect()

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Ide pesma gazda')
    else:
        await ctx.send("Sviram vec gazda, ne mogu dvije odjednom")
        return

#disconnecting from cahnnel

@client.command()
async def mrš(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Sta me teraš gazda, a ni nisam tu")


#pausing  the music

@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Nista ne sviram gazda")


#resuming the music

@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Sviram gazda, sviram već")


#stop playing

@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()

    

client.run("ODg4NzU4Mzc1NzcxNDE0NTY5.YUXWvQ.75Gp7z-xA2l-ig7weMsa9MemQok")