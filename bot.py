intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot online como {bot.user}")


class VerificacaoView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Verificar-se",
        style=discord.ButtonStyle.success,
        custom_id="verificacao_unica"
    )
    async def verificar(self, interaction: discord.Interaction, button: discord.ui.Button):

        cargo = interaction.guild.get_role(1473001188206182480)

        if cargo is None:
            await interaction.response.send_message(
                "❌ Cargo não encontrado.",
                ephemeral=True,
                delete_after=5
            )
            return

        if cargo in interaction.user.roles:
            await interaction.response.send_message(
                "⚠️ Você já possui o cargo.",
                ephemeral=True,
                delete_after=5
            )
            return

        try:
            await interaction.user.add_roles(cargo)
            await interaction.response.send_message(
                "✅ Cargo adicionado com sucesso!",
                ephemeral=True,
                delete_after=5
            )
        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ Não tenho permissão para dar esse cargo.",
                ephemeral=True,
                delete_after=5
            )


@bot.command()
async def painel(ctx):

    embed = discord.Embed(
        title="🔐 Verificação",
        description="Clique no botão abaixo para receber o cargo.",
        color=discord.Color.green()
    )

    await ctx.send(embed=embed, view=VerificacaoView())
