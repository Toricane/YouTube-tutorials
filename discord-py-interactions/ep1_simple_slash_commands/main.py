import interactions


bot = interactions.Client("OTI4MDU0Njc5Nzg1NTc4NTc2.YdTMRg.BrsQGPsof-k7MZECxv4JWj3dbtg")


@bot.event
async def on_ready():
    print("Ready!")


@bot.command(
    name="hello-world",
    description="A simple example command",
    scope=925511055034187788,
)
async def hello_world(ctx: interactions.CommandContext):
    await ctx.send("Hello World!")


@bot.command(
    name="say",
    description="Make the bot say something!",
    scope=925511055034187788,
    options=[
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="message",
            description="The message to send",
            required=True,
        ),
        interactions.Option(
            type=interactions.OptionType.INTEGER,
            name="number",
            description="The number to say",
            required=False,
        ),
    ],
)
async def say(ctx: interactions.CommandContext, message: str, number: int = None):
    await ctx.send(message + str(number))


bot.start()
