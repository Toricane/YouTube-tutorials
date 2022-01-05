import interactions

bot = interactions.Client("token")


@bot.event
async def on_ready():
    print("Ready!")


@bot.command(
    name="hello-world",
    description="A simple example command",
    scope=874781880489222154,
)
async def hello_world(ctx: interactions.CommandContext):
    await ctx.send("Hello World!")


@bot.command(
    name="hello-options",
    description="A simple example command",
    scope=874781880489222154,
    options=[
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="string",
            description="string",
        ),
        interactions.Option(
            type=interactions.OptionType.INTEGER,
            name="integer",
            description="integer",
        ),
        interactions.Option(
            type=interactions.OptionType.BOOLEAN,
            name="boolean",
            description="boolean",
        ),
        interactions.Option(
            type=interactions.OptionType.USER,
            name="user",
            description="user",
        ),
        interactions.Option(
            type=interactions.OptionType.CHANNEL,
            name="channel",
            description="channel",
        ),
        interactions.Option(
            type=interactions.OptionType.ROLE,
            name="role",
            description="role",
        ),
        interactions.Option(
            type=interactions.OptionType.MENTIONABLE,
            name="mentionable",
            description="mentionable",
        ),
        interactions.Option(
            type=interactions.OptionType.NUMBER,
            name="number",
            description="number",
        ),
    ],
)
async def hello_options(
    ctx: interactions.CommandContext,
    string,
    integer,
    boolean,
    user,
    channel,
    role,
    mentionable,
    number,
):
    await ctx.send(
        f"Hello {string=}, {integer=}, {boolean=}, {user=}, {channel=}, {role=}, {mentionable=}, {number=}!"
    )


# choices dont work in v4.0.1
@bot.command(
    name="hello-choices",
    description="A simple example command",
    scope=874781880489222154,
    options=[
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="choose_wisely",
            description="choose wisely",
            choices=[
                interactions.Choice(
                    name="dog",
                    value="🐶",
                ),
                interactions.Choice(
                    name="cat",
                    value="🐱",
                ),
            ],
        ),
    ],
)
async def hello_choices(ctx: interactions.CommandContext, choose_wisely):
    await ctx.send(f"You chose {choose_wisely}!")


bot.start()
