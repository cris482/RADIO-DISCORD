import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ==============================
# DAFTAR RADIO (ISI URL DI SINI)
# ==============================
RADIO_LIST = {
    # Jakarta
    "jakarta_pro1": "https://stream-node1.rri.co.id/streaming/01/9001/rrijakartapro1.mp3",
    "jakarta_pro2": "https://stream-node1.rri.co.id/streaming/01/9001/rrijakartapro2.mp3",
    "jakarta_pro3": "https://stream-node1.rri.co.id/streaming/01/9001/rrijakartapro3.mp3",
    "jakarta_pro4": "https://stream-node1.rri.co.id/streaming/01/9001/rrijakartapro4.mp3",
    
    # Sumatera
    "medan_pro1": "https://stream-node1.rri.co.id/streaming/02/9002/rrimedanpro1.mp3",
    "medan_pro2": "https://stream-node1.rri.co.id/streaming/02/9002/rrimedanpro2.mp3",
    "palembang_pro1": "https://stream-node1.rri.co.id/streaming/03/9003/rripalembangpro1.mp3",
    "padang_pro1": "https://stream-node1.rri.co.id/streaming/04/9004/rripadangpro1.mp3",
    "pekanbaru_pro1": "https://stream-node1.rri.co.id/streaming/05/9005/rripekanbarupro1.mp3",
    "jambi_pro1": "https://stream-node1.rri.co.id/streaming/06/9006/rrijambipro1.mp3",
    "bengkulu_pro1": "https://stream-node1.rri.co.id/streaming/07/9007/rribengkulupro1.mp3",
    "bandar_lampung_pro1": "https://stream-node1.rri.co.id/streaming/08/9008/rribandarlampungpro1.mp3",
    "banda_aceh_pro1": "https://stream-node1.rri.co.id/streaming/09/9009/rribandaacehpro1.mp3",
    
    # Jawa
    "bandung_pro1": "https://stream-node1.rri.co.id/streaming/10/9010/rribandungpro1.mp3",
    "bandung_pro2": "https://stream-node1.rri.co.id/streaming/10/9010/rribandungpro2.mp3",
    "bandung_pro3": "https://stream-node1.rri.co.id/streaming/10/9010/rribandungpro3.mp3",
    "bandung_pro4": "https://stream-node1.rri.co.id/streaming/10/9010/rribandungpro4.mp3",
    "semarang_pro1": "https://stream-node1.rri.co.id/streaming/11/9011/rrisemarangpro1.mp3",
    "semarang_pro2": "https://stream-node1.rri.co.id/streaming/11/9011/rrisemarangpro2.mp3",
    "yogyakarta_pro1": "https://stream-node1.rri.co.id/streaming/12/9012/rriyogyakartapro1.mp3",
    "yogyakarta_pro2": "https://stream-node1.rri.co.id/streaming/12/9012/rriyogyakartapro2.mp3",
    "surabaya_pro1": "https://stream-node1.rri.co.id/streaming/13/9013/rrisurabayapro1.mp3",
    "surabaya_pro2": "https://stream-node1.rri.co.id/streaming/13/9013/rrisurabayapro2.mp3",
    
    # Kalimantan
    "pontianak_pro1": "https://stream-node1.rri.co.id/streaming/14/9014/rripontianakpro1.mp3",
    "banjarmasin_pro1": "https://stream-node1.rri.co.id/streaming/15/9015/rribanjarmasinpro1.mp3",
    "palangkaraya_pro1": "https://stream-node1.rri.co.id/streaming/16/9016/rripalangkarayapro1.mp3",
    "samarinda_pro1": "https://stream-node1.rri.co.id/streaming/17/9017/rrisamarindapro1.mp3",
    
    # Sulawesi
    "makassar_pro1": "https://stream-node1.rri.co.id/streaming/18/9018/rrimakassarpro1.mp3",
    "makassar_pro2": "https://stream-node1.rri.co.id/streaming/18/9018/rrimakassarpro2.mp3",
    "palu_pro1": "https://stream-node2.rri.co.id/streaming/19/9319/rripalupro1.mp3",
    "kendari_pro1": "https://stream-node1.rri.co.id/streaming/20/9020/rrikenddripro1.mp3",
    "gorontalo_pro1": "https://stream-node1.rri.co.id/streaming/21/9021/rrigorontalopro1.mp3",
    "manado_pro1": "https://stream-node1.rri.co.id/streaming/22/9022/rrimanadopro1.mp3",
    "manado_pro2": "https://stream-node1.rri.co.id/streaming/22/9022/rrimanadopro2.mp3",
    
    # Maluku dan Papua
    "ambon_pro1": "https://stream-node2.rri.co.id/streaming/23/9323/rriambonpro1.mp3",
    "ternate_pro1": "https://stream-node1.rri.co.id/streaming/24/9024/rriternatepro1.mp3",
    "jayapura_pro1": "https://stream-node1.rri.co.id/streaming/25/9025/rrijayapurapro1.mp3",
    "manokwari_pro1": "https://stream-node1.rri.co.id/streaming/26/9026/rrimanokwaripro1.mp3",
    "manokwari_pro4": "https://stream-node1.rri.co.id/streaming/26/9026/rrimanokwaripro4.mp3",
    "sorong_pro1": "https://stream-node1.rri.co.id/streaming/27/9027/rrisorongpro1.mp3",
    "sorong_pro2": "https://stream-node1.rri.co.id/streaming/27/9027/rrisorongpro2.mp3",
    "merauke_pro1": "https://stream-node1.rri.co.id/streaming/28/9028/rrimeraukepro1.mp3",
    "nabire_pro1": "https://stream-node1.rri.co.id/streaming/29/9029/rrinabirepro1.mp3",
    "wamena_pro1": "https://stream-node1.rri.co.id/streaming/30/9030/rriwamenapro1.mp3",
    
    # Bali dan Nusa Tenggara
    "denpasar_pro1": "https://stream-node1.rri.co.id/streaming/31",
}

# ==============================


@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")


async def play_radio(ctx, station_name):
    """Fungsi umum untuk play radio."""
    if station_name not in RADIO_LIST:
        return await ctx.send("❌ Nama radio tidak ditemukan.")

    url = RADIO_LIST[station_name]

    if url == "URL_STREAM_DI_SINI":
        return await ctx.send("⚠️ URL untuk radio ini belum diisi.")

    if not ctx.author.voice:
        return await ctx.send("❌ Kamu harus join voice channel dulu!")

    channel = ctx.author.voice.channel

    # connect atau pindah
    if ctx.voice_client is None:
        await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)

    voice = ctx.voice_client

    if voice.is_playing():
        voice.stop()

    voice.play(discord.FFmpegPCMAudio(
        url,
        before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
        options="-vn"
    ))

    await ctx.send(f"🎶 Sedang memutar **{station_name}**")


@bot.command()
async def radio(ctx, nama):
    """Memulai radio pertama kali."""
    await play_radio(ctx, nama)


@bot.command()
async def ganti(ctx, nama):
    """Ganti ke radio lain tanpa disconnect."""
    await play_radio(ctx, nama)


@bot.command()
async def stop(ctx):
    """Stop dan keluarkan bot."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⛔ Radio dihentikan. Bot keluar.")
    else:
        await ctx.send("Bot tidak ada di voice channel.")


bot.run("ISI TOKEN DISINI") 

""" COMMAND DISCORD
!radio <stasiun> - Memutar radio dari stasiun tertentu
!radiolist - Menampilkan semua stasiun yang tersedia dengan tampilan embed yang cantik
!nowplaying - Cek status radio saat ini """