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


@bot.message_command(name="Hello message", scope=925511055034187788)
async def hello_message(ctx: interactions.CommandContext):
    await ctx.send(f'You said, "{ctx.target.content}"')


@bot.user_command(name="Hello user", scope=925511055034187788)
async def hello_user(ctx: interactions.CommandContext):
    await ctx.send(f"Hello, {ctx.target.username}#{ctx.target.discriminator}!")


@bot.user_command(name="Hello member", scope=925511055034187788)
async def hello_member(ctx: interactions.CommandContext):
    member = interactions.Member(
        **await bot._http.get_member(ctx.guild_id, ctx.target.id), _client=bot._http
    )
    await ctx.send(
        f"Hello, {member.user.username if member.nick is None else member.nick}!"
    )


bot.start()
