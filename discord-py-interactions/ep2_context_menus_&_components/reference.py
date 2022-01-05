import interactions

bot = interactions.Client("ODc0NzgwOTE4MDgxMDE1ODg5.YRL9Nw.-X7UXQg3v43oeDHG0xPEEuNQO8c")


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


# @bot.command(
#     type=interactions.ApplicationCommandType.USER,
#     name="Hello user",
#     description="A simple example user context menu",
#     scope=874781880489222154,
# )
# async def hello_user(ctx: interactions.CommandContext):
#     await ctx.send("Hello user!")


# @bot.command(
#     type=interactions.ApplicationCommandType.MESSAGE,
#     name="Hello message",
#     description="A simple example message context menu",
#     scope=874781880489222154,
# )
# async def hello_message(ctx: interactions.CommandContext):
#     await ctx.send("Hello message!")


@bot.command(
    name="component-command",
    description="A simple example command that sends components",
    scope=874781880489222154,
)
async def component_command(ctx: interactions.CommandContext):
    primary_button = interactions.Button(
        style=interactions.ButtonStyle.PRIMARY,
        label="PRIMARY",
        custom_id="primary",
    )
    secondary_button = interactions.Button(
        style=interactions.ButtonStyle.SECONDARY,
        label="SECONDARY",
        custom_id="secondary",
    )
    success_button = interactions.Button(
        style=interactions.ButtonStyle.SUCCESS,
        label="SUCCESS",
        custom_id="success",
    )
    danger_button = interactions.Button(
        style=interactions.ButtonStyle.DANGER,
        label="DANGER",
        custom_id="danger",
    )
    link_button = interactions.Button(
        style=interactions.ButtonStyle.LINK,
        label="LINK",
        url="https://example.com",
    )
    action_row = interactions.ActionRow(
        components=[
            primary_button,
            secondary_button,
            success_button,
            danger_button,
            link_button,
        ]
    )
    await ctx.send("All the components:", components=action_row)


@bot.component("primary")
async def primary_component(ctx: interactions.ComponentContext):
    await ctx.send("You clicked the primary component!", ephemeral=True)


bot.start()
