import discord
from discord.ext import commands

# Configurações do Discord
TOKEN_DISCORD = 1317632789495156766
GUILD_ID = 1301856786416013395
CARGO_ASSINANTE = 1307080567845556316
CARGO_MEMBRO = 1307080455194935360

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def atualizar_cargo(user_id_discord, action, cargo_id):
    guild = bot.get_guild(GUILD_ID)
    member = guild.get_member(int(user_id_discord))
    if not member:
        print(f"Usuário {user_id_discord} não encontrado no servidor.")
        return False

    role = guild.get_role(cargo_id)
    if not role:
        print(f"Cargo {cargo_id} não encontrado.")
        return False

    if action == "adicionar":
        await member.add_roles(role)
        print(f"Cargo {role.name} adicionado a {member.name}.")
    elif action == "remover":
        await member.remove_roles(role)
        print(f"Cargo {role.name} removido de {member.name}.")
    return True

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

if __name__ == "__main__":
    bot.run(TOKEN_DISCORD)
