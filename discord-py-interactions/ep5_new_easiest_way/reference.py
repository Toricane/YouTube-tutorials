import interactions as ipy  # 1) go over why it should be imported as ipy


# 2) define bot
bot = ipy.Client("token", default_scope=123)  # 7) add default scope after first 2 commands


# 3) first event, also say why on_ready is bad
@bot.event
async def on_start():
    print("Bot started")


# 5) first command, explain defaults
@bot.command(scope=123)  # show scope after coding this and explain what it is
async def ping(ctx: ipy.CommandContext):
    await ctx.send(f"Pong! {bot.latency}ms")


# 6) second command, show configuration
@bot.command(name="random-command")  # show scope here too
async def random_command(ctx: ipy.CommandContext):
    """This is the command's description"""
    await ctx.send("Random command")


# 7) show how to make global command with default scope enabled
@bot.command(default_scope=False)
async def global_command(ctx: ipy.CommandContext):
    await ctx.send("Global command")


# 8) show how to make command with options
@bot.command()
@ipy.option("description")
@ipy.option()
@ipy.option()
@ipy.option()
@ipy.option(name="opt5")
async def options(
    ctx: ipy.CommandContext,
    opt1: str,
    opt2: int,
    opt3: ipy.Channel = None,
    opt4: ipy.OptionType.ROLE = None,
    converter: str = "idk",
):
    await ctx.send(f"You chose: {opt1=}, {opt2=}, {opt3=}, {opt4=}, {converter=}")


# 9) show subcommand system
@bot.command()
async def base(ctx: ipy.CommandContext):  # say *args and **kwargs can be included
    await ctx.send("Base command")  # say you could do whatever

    # depending on the user or whatever,
    # you could return different data
    # or stop the command chain altogether.
    # show how to do that, one by one

    # return "something"
    # return ipy.StopCommand


@base.subcommand()
async def subcommand(ctx: ipy.CommandContext, base_res: ipy.BaseResult):
    await ctx.send("Subcommand")
    print(base_res)  # say this param is optional


# make it clear that you need to
# define sole subcommands
# **before** grouped ones


@base.group()
async def group(ctx: ipy.CommandContext):
    await ctx.send("Group")

    # depending on the user or whatever,
    # you could return different data
    # or stop the command chain altogether.
    # show how to do that, one by one

    # return "something"
    # return ipy.StopCommand


@group.subcommand()
async def subcommand2(ctx: ipy.CommandContext, group_res: ipy.GroupResult):
    await ctx.send("Subcommand2")
    print(group_res)  # say this param is optional


# 10) show ActionRow.new and spread_to_rows
@bot.command()
async def buttons(ctx: ipy.CommandContext):
    await ctx.send(
        "Here is 1 row of buttons:",
        components=ipy.ActionRow.new(
            ipy.Button(style=ipy.ButtonStyle.PRIMARY, custom_id="primary", label="Primary"),
            ipy.Button(style=ipy.ButtonStyle.SECONDARY, custom_id="secondary", label="Secondary"),
            ipy.Button(style=ipy.ButtonStyle.SUCCESS, custom_id="success", label="success"),
            ipy.Button(
                style=ipy.ButtonStyle.DANGER, custom_id="danger", label="danger", disabled=True
            ),
            ipy.Button(style=ipy.ButtonStyle.LINK, url="https://example.com/", label="Link"),
        ),
    )
    await ctx.send(
        "Here are 2 rows of buttons:",
        components=[
            ipy.ActionRow.new(
                ipy.Button(style=ipy.ButtonStyle.SUCCESS, custom_id="1", label="1"),
            ),
            ipy.ActionRow.new(
                ipy.Button(style=ipy.ButtonStyle.DANGER, custom_id="2", label="2"),
            ),
        ],
    )
    await ctx.send(
        "Here are 3 rows of buttons with 3 in each:",
        components=ipy.spread_to_rows(
            *(ipy.Button(style=2, custom_id=i, label=i) for i in range(1, 10)), max_in_row=3
        ),
    )


# 4) start the bot
bot.start()
