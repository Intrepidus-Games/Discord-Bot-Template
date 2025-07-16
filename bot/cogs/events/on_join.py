import discord
from discord.ext import commands
from lib.debug import Debug

class OnJoinEvents(commands.Cog):
    def __init__(self, bot: commands.Bot, debug: Debug):
        self.bot = bot
        self.debug = debug

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
            Event triggered when a member joins the server.
            Assigns a default role to the member if it exists.
        """
        # Debugs
        self.debug.print(f'User joined: {member.name}')

        role = discord.utils.get(member.guild.roles, name="Member")

        if role:
            try:
                await member.add_roles(role)
                self.debug.print(f"Assigned role '{role.name}' to {member.name}")
            except discord.Forbidden:
                self.debug.print("Missing permissions to assign roles.")
            except Exception as e:
                self.debug.print(f"Error assigning role: {e}")
        else:
            self.debug.print(f"Role '{role.name}' not found in guild.")

async def setup(bot: commands.Bot, debug: Debug):
    await bot.add_cog(OnJoinEvents(bot, debug))