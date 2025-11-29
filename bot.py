import os
import discord
import os
import discord
from discord.ext import commands
from advent import open_door
from datetime import datetime

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"🎄 Advent Calendar Bot logged in as {bot.user}")


@bot.command()
async def open(ctx, day: int = None):
    """
    Command: !open <day>
    Example: !open 5
    """

    if day is None:
        await ctx.reply("❄️ Please specify a day (1–24). Example: `!open 7`")
        return

    if not 1 <= day <= 24:
        await ctx.reply("🎁 Advent days go from **1–24** only.")
        return

    result = open_door(user_id=ctx.author.id, day=day)

    if result["status"] == "already_opened":
        await ctx.reply(f"🎅 You've **already opened** day **{day}**!")
    else:
        await ctx.reply(f"✨ **Day {day} Opened!**\n{result['content']}")


@bot.command()
async def today(ctx):
    """
    Command: !today — automatically open today's door
    """

    day = datetime.utcnow().day

    if not 1 <= day <= 24:
        await ctx.reply("❄️ The Advent Calendar runs from **Dec 1 to Dec 24**.")
        return

    result = open_door(user_id=ctx.author.id, day=day)

    if result["status"] == "already_opened":
        await ctx.reply(f"🎄 You've already opened day **{day}** today!")
    else:
        await ctx.reply(f"✨ **Day {day} Opened!**\n{result['content']}")


bot.run(TOKEN)
