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
        title="Modal Title",
        custom_id="modal",
        components=[
            TextInput(
                style=TextStyleType.SHORT,
                label="Short text input",
                custom_id="text-input-1",
            ),
            TextInput(
                style=TextStyleType.PARAGRAPH,
                label="Paragraph text input",
                custom_id="text-input-2",
            ),
        ],
    )
    await ctx.popup(modal)


@bot.command(name="send-button", description="Send a button", scope=925511055034187788)
async def send_button(ctx: CommandContext):
    button = Button(style=1, label="Click for Modal", custom_id="button")
    await ctx.send("Click the button below to send a modal!", components=button)


@bot.component("button")
async def button(ctx: ComponentContext):
    modal = Modal(
        title="Modal Title",
        custom_id="modal",
        components=[
            TextInput(
                style=TextStyleType.SHORT,
                label="Short text input",
                custom_id="text-input-1",
            ),
            TextInput(
                style=TextStyleType.PARAGRAPH,
                label="Paragraph text input",
                custom_id="text-input-2",
            ),
        ],
    )
    await ctx.popup(modal)


@bot.modal("modal")
async def modal_response(ctx: CommandContext, short: str, paragraph: str):
    await ctx.send(f"Short text: {short}\nLong text: {paragraph}")


bot.start()
