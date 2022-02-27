from interactions import (
    Client,
    CommandContext,
    ComponentContext,
    Modal,
    TextInput,
    TextStyleType,
    Button,
)

bot = Client("token")


@bot.event
async def on_ready():
    print("Ready!")


@bot.command(name="send-modal", description="Send a modal", scope=925511055034187788)
async def send_modal(ctx: CommandContext):
    modal = Modal(
        custom_id="modal",
        title="Modal Title",
        components=[
            TextInput(
                style=TextStyleType.SHORT,
                custom_id="text-input-1",
                label="Short text input",
            ),
            TextInput(
                style=TextStyleType.PARAGRAPH,
                custom_id="text-input-2",
                label="Paragraph text input",
            ),
        ],
    )
    await ctx.popup(modal)


@bot.command(name="send-button", description="Send a button", scope=925511055034187788)
async def send_button(ctx: CommandContext):
    button = Button(style=1, custom_id="button", label="Click for Modal")
    await ctx.send("Click the button below to send a modal!", components=button)


@bot.component("button")
async def button(ctx: ComponentContext):
    modal = Modal(
        custom_id="modal2",
        title="Put stuff here",
        components=[
            TextInput(
                style=TextStyleType.SHORT,
                label="normal text input",
                custom_id="text-input-0",
            ),
            TextInput(
                style=TextStyleType.SHORT,
                label="value text input",
                value="Pizza",
                custom_id="text-input-1",
            ),
            TextInput(
                style=TextStyleType.SHORT,
                label="placeholder text input",
                placeholder="placeholder",
                custom_id="text-input-2",
            ),
            TextInput(
                style=TextStyleType.PARAGRAPH,
                label="not required text input",
                required=False,
                custom_id="text-input-3",
            ),
            TextInput(
                style=TextStyleType.PARAGRAPH,
                label="min and max text input",
                min_length=3,
                max_length=100,
                custom_id="text-input-4",
            ),
        ],
    )
    await ctx.popup(modal)


@bot.modal("modal")
async def modal(ctx: CommandContext, short: str, paragraph: str):
    await ctx.send(f'You said, "{short}" and "{paragraph}"')


@bot.modal("modal2")
async def modal2(ctx: CommandContext, one, two, three, four, five):
    await ctx.send(
        f"""
{one},
{two},
{three},
{four},
{five}
"""
    )


bot.start()
