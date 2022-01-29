import interactions
from interactions import Button, ButtonStyle, SelectMenu, SelectOption, ActionRow

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
    name="component-command",
    description="A simple example command that sends components",
    scope=925511055034187788,
)
async def component_command(ctx: interactions.CommandContext):
    select_menu = SelectMenu(
        custom_id="select-menu",
        options=[
            SelectOption(label="Option 1", value="option-1"),
            SelectOption(label="Option 2", value="option-2"),
        ],
        placeholder="Placeholder of the select menu",
        min_values=1,
        max_values=2,
    )
    await ctx.send("Hello World!", components=select_menu)


@bot.component("select-menu")
async def primary_component(ctx: interactions.ComponentContext):
    select_menu = SelectMenu(
        custom_id="select-menu",
        options=[
            SelectOption(label="Option 1", value="option-1"),
            SelectOption(label="Option 2", value="option-2"),
        ],
        placeholder="Placeholder of the select menu",
        min_values=1,
        max_values=2,
    )
    await ctx.send("Hidden message!", ephemeral=True, components=select_menu)


bot.start()
