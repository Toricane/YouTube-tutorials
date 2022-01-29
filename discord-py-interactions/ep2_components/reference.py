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
    scope=925511055034187788,
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
    select = interactions.SelectMenu(
        custom_id="select",
        options=[
            interactions.SelectOption(label="Option 1", value="1"),
            interactions.SelectOption(label="Option 2", value="2"),
        ],
        placeholder="Select an option",
        min_values=1,
        max_values=2,
    )
    buttons_row = interactions.ActionRow(
        components=[
            primary_button,
            secondary_button,
            success_button,
            danger_button,
            link_button,
        ]
    )
    select_row = interactions.ActionRow(components=[select])
    await ctx.send("All the components:", components=[buttons_row, select_row])


@bot.component("primary")
@bot.component("secondary")
@bot.component("success")
@bot.component("danger")
@bot.component("select")
async def primary_component(ctx: interactions.ComponentContext):
    await ctx.send(
        f"You clicked the {ctx.data.custom_id} component!\n{('Selected options: ' + ', '.join(ctx.data.values)) if ctx.data.values else ''}",
        ephemeral=True,
    )


bot.start()
