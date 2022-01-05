import interactions


bot = interactions.Client("token")


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
