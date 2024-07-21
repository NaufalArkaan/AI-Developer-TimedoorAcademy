# import discord
# intents = discord.Intents.default()
# intents.message_content = True #Konfigurasi agar pesan dari client bisa dibaca
# client = discord.Client(intents=intents) #Membuat koneksi antara klien dengan discord. Kelas Client digunakan untuk berinteraksi dengan discord.

# @client.event
# async def on_message(message): #on_message()dipanggil ketika bot menerima pesan
#     if message.author == client.user:
#         return

#     if message.content.startswith('!hi'):
#         await message.channel.send(f'Hello 👋😃')        
# #add code above
# client.run('token')


# @client.event 
# async def on_ready(): 
#     print("We have logged in as {0.user}".format(client))

# client.run("MTI0MjY4NzgyODM0NTg4NDcxNA.GEEANS.CZvYqB1Hw18KqDX7q-FfAOT4SU9j2ViJ8hM2Mg")