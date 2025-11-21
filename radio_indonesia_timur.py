import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# --- RADIO LIST MALUKU DAN PAPUA ---
RADIO_LIST = {
    # Maluku
    "ambon1": "https://stream-node2.rri.co.id/streaming/23/9323/rriambonpro1.mp3",
    "ternate1": "https://stream-node1.rri.co.id/streaming/24/9024/rriternatepro1.mp3",
    
    # Papua
    "jayapura1": "https://stream-node1.rri.co.id/streaming/25/9025/rrijayapurapro1.mp3",
    "jayapura2": "https://stream-node0.rri.co.id/streaming/23/9023/rrijayapurapro2.mp3",
    "jayapura3": "https://stream-node0.rri.co.id/streaming/14/9014/kbrn.mp3",
    "manokwari1": "https://stream-node1.rri.co.id/streaming/26/9026/rrimanokwaripro1.mp3",
    "manokwari2": "https://stream-node1.rri.co.id/streaming/24/9024/rrimanokwaripro2.mp3",
    "manokwari3": "https://stream-node0.rri.co.id/streaming/14/9014/kbrn.mp3",
    "manokwari4": "https://stream-node1.rri.co.id/streaming/26/9026/rrimanokwaripro4.mp3",
    "sorong1": "https://stream-node1.rri.co.id/streaming/27/9027/rrisorongpro1.mp3",
    "sorong2": "https://stream-node1.rri.co.id/streaming/17/9217/rrisorongpro2.mp3",
    "sorong3": "https://stream-node0.rri.co.id/streaming/14/9014/kbrn.mp3",
    "merauke1": "https://stream-node1.rri.co.id/streaming/28/9028/rrimeraukepro1.mp3",
    "nabire1": "https://stream-node1.rri.co.id/streaming/29/9029/rrinabirepro1.mp3",
    "wamena1": "https://stream-node1.rri.co.id/streaming/30/9030/rriwamenapro1.mp3",
}

@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")
    print("Radio tersedia:", ", ".join(RADIO_LIST.keys()))

@bot.command()
async def radio(ctx, station=None):
    """Play radio di voice channel. 
    !radio <stasiun> - Memutar radio dari stasiun tertentu
    !radiolist - Menampilkan semua stasiun yang tersedia dengan tampilan embed yang cantik
    !nowplaying - Cek status radio saat ini
    
    Gunakan: !radio <nama_stasiun>
    Contoh: !radio ambon1, !radio jayapura1"""
    
    if not ctx.author.voice:
        return await ctx.send("❌ Kamu harus join voice channel terlebih dahulu.")

    if station is None:
        return await ctx.send("❌ Pilih stasiun radio!\nContoh: `!radio ambon1`\nKetik `!radiolist` untuk melihat semua stasiun.")

    station = station.lower()
    if station not in RADIO_LIST:
        return await ctx.send(f"❌ Stasiun '{station}' tidak ditemukan!\nKetik `!radiolist` untuk melihat semua stasiun yang tersedia.")

    channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        await channel.connect()

    voice = ctx.voice_client

    if voice.is_playing():
        voice.stop()

    try:
        voice.play(discord.FFmpegPCMAudio(
            RADIO_LIST[station],
            before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        ))
        
        # Mendapatkan nama stasiun yang lebih readable
        station_name = station.replace("1", " Pro 1").replace("2", " Pro 2").replace("3", " Pro 3").replace("4", " Pro 4")
        station_name = station_name.replace("ambon", "RRI Ambon").replace("ternate", "RRI Ternate")
        station_name = station_name.replace("jayapura", "RRI Jayapura").replace("manokwari", "RRI Manokwari")
        station_name = station_name.replace("sorong", "RRI Sorong").replace("merauke", "RRI Merauke")
        station_name = station_name.replace("nabire", "RRI Nabire").replace("wamena", "RRI Wamena")
        
        await ctx.send(f"🎶 **{station_name}** mulai diputar!")
        
    except Exception as e:
        await ctx.send(f"❌ Error saat memutar radio: {str(e)}")

@bot.command()
async def radiolist(ctx):
    """Menampilkan daftar semua stasiun radio yang tersedia."""
    
    maluku_stations = []
    papua_stations = []
    
    for station in RADIO_LIST.keys():
        if "ambon" in station or "ternate" in station:
            maluku_stations.append(station)
        else:
            papua_stations.append(station)
    
    embed = discord.Embed(
        title="📻 Daftar Stasiun Radio RRI",
        description="Gunakan `!radio <nama_stasiun>` untuk memutar",
        color=0x00ff00
    )
    
    embed.add_field(
        name="RRI Maluku",
        value="\n".join([f"• `{station}`" for station in maluku_stations]),
        inline=True
    )
    
    embed.add_field(
        name="RRI Papua",
        value="\n".join([f"• `{station}`" for station in papua_stations]),
        inline=True
    )
    
    embed.set_footer(text="Contoh: !radio ambon1")
    
    await ctx.send(embed=embed)

@bot.command()
async def stop(ctx):
    """Stop radio & bot keluar dari voice channel."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⛔ Radio dihentikan, bot keluar dari voice channel.")
    else:
        await ctx.send("❌ Bot tidak ada di voice channel.")

@bot.command()
async def nowplaying(ctx):
    """Menampilkan status bot saat ini."""
    if ctx.voice_client and ctx.voice_client.is_playing():
        await ctx.send("🎵 Radio sedang diputar!")
    else:
        await ctx.send("🔇 Tidak ada radio yang sedang diputar.")

# Error handling
@radio.error
async def radio_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Silakan pilih stasiun radio!\nContoh: `!radio ambon1`\nKetik `!radiolist` untuk melihat semua stasiun.")

bot.run("TOKEN DISINI")