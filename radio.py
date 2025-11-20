import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
# --- URL RADIO ----
RADIO_URL = "https://radio10.pro-fhi.net/flux-qlvuthph/192stream"



@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")


@bot.command()
async def radio(ctx):
    """Play radio di voice channel."""
    if not ctx.author.voice:
        return await ctx.send("❌ Kamu harus join voice channel terlebih dahulu.")

    channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        await channel.connect()

    voice = ctx.voice_client

    if voice.is_playing():
        voice.stop()

    voice.play(discord.FFmpegPCMAudio(
        RADIO_URL,
        before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
    ))

    await ctx.send("🎶 KZFX Z-93.7 FM Ridgecrest CA, Amerika Serikat!")


@bot.command()
async def stop(ctx):
    """Stop radio & bot keluar."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⛔ Radio dihentikan, bot keluar.")
    else:
        await ctx.send("Bot tidak ada di voice channel.")


bot.run("ISI TOKEN DISINI")
