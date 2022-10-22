import interactions as ipy

bot = ipy.Client("token")


@bot.event
async def on_start():
    print("Bot started!")


@bot.command()
async def ping(ctx: ipy.CommandContext):
    """Sends the bot's latency"""
    await ctx.send(f"Pong! {bot.latency}ms")


bot.start()
