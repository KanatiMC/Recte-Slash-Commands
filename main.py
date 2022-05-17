import os
import hikari
import lightbulb
import uvloop
import random
from keep_alive import keep_alive
bot=lightbulb.BotApp(
	os.environ["Token"],
	default_enabled_guilds=int(os.environ["GuildID"]),
	help_slash_command=False,
	intents=hikari.Intents.ALL,
)

Hex = [
    0x986303, 0x986303, 0xc5428f, 0x118291, 0x89bd1e, 0xc1faca, 0xc18d36,
    0xcca0d0, 0xe16af2, 0x4ca0e5, 0x86eefd, 0xe81d97, 0xf1874c, 0xee895b,
    0xc920b1, 0x573744, 0x26b66d, 0x50e971, 0x3dbb6f, 0xe4f483, 0x136845,
    0x4eac23, 0xdf6658, 0x3a2c9e, 0xfa6d4b, 0x8b4585, 0xa344f9, 0x31a9b0,
    0x4a68d5, 0x9eb5da, 0xe66ffc, 0x746cb2, 0x6b9066, 0x19b2e4, 0xe4d88a,
    0x8fcaf4, 0x0132aa, 0xcd4c93, 0x718248, 0x6925f0, 0x69e761, 0xf313b2,
    0x0e5555, 0x33e0fb, 0x9653db, 0xea8f55, 0x312b6d, 0x2332ed, 0x1d8c4b,
    0xd1e9d6, 0x6f88c5, 0xd2bc42, 0xe186d9, 0x4686ad, 0x075b69, 0xa5ba89,
    0xcd1f6e, 0x70430a, 0xb5f438, 0x15aef6, 0x0ebd87, 0xa567e0, 0xa6e3b8,
    0x6ad74c, 0x468a2c, 0xb597bd, 0xbce8b7, 0x233aef, 0xb92946, 0xf9a51b,
    0x5de431, 0xfe4ff8, 0x323f44
]

@bot.command()
@lightbulb.option("suggestion", "What You'd Like To Suggest")
@lightbulb.command("suggest", "Give A Suggestion To The Client")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_suggest(ctx: lightbulb.SlashContext) -> None:
	await ctx.respond("Suggestion Added")
	embedded = (
		hikari.Embed(
			description=ctx.options.suggestion,
			colour=random.choice(Hex),
		)
		.set_footer(
			text="Recte By Kanati"
		)
		.set_author(
			name=f"{ctx.member.username}#{ctx.member.discriminator} | {ctx.member.id}",
			icon=ctx.author.avatar_url
		)
	)
	rp = await bot.rest.create_message(os.environ["SuggestionChannelID"], embedded)
	msg = await rp.message()
	await msg.add_reaction("👍")
	await msg.add_reaction("👎")

@bot.command()
@lightbulb.command("ping", "Check The Ping Of The Bot In Ms")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_ping(ctx: lightbulb.SlashContext) -> None:
	await ctx.respond(f"My Ping Is Approximately {round(ctx.bot.heartbeat_latency * 1000)} ms.")

@bot.command()
@lightbulb.option("query", "What You Want To Google")
@lightbulb.command("google", "Let Me Googe That For You")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_google(ctx: lightbulb.SlashContext) -> None:
    q = ctx.options.query

    if len(q) > 500:
        await ctx.respond("What You Want To Search Shouldn't Be More Than 500 Characters")
        return

    await ctx.respond(f"<https://google.gprivate.com/search.php?search?q={q.replace(' ', '+')}>")

@bot.command()
@lightbulb.option("question", "What Question You'd Like To Poll")
@lightbulb.command("poll", "Creates A Poll")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_poll(ctx: lightbulb.SlashContext) -> None:
	await ctx.respond("Poll Created")
	embed = (
		hikari.Embed(
			description=ctx.options.question,
			colour=random.choice(Hex)
		)
		.set_footer(
			text="Recte Bot By Kanati"
		)
		.set_author(
			name=f"{ctx.member.username}#{ctx.member.discriminator} | {ctx.member.id}",
			icon=ctx.author.avatar_url
		)
	)
	rp = await bot.rest.create_message(os.environ["AnnouncementID"], embed)
	await rp.add_reaction("👍")
	await rp.add_reaction("👎")




@bot.command()
@lightbulb.option("reporting", "What You'd Like To Report To Kanati")
@lightbulb.command("report", "List A Bug In The Client")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_report(ctx: lightbulb.SlashContext) -> None:
	await ctx.respond("Bug Reported")
	embedded = (
		hikari.Embed(
			description=ctx.options.suggestion,
			colour=random.choice(Hex),
		)
		.set_footer(
			text="Recte By Kanati"
		)
		.set_author(
			name=f"{ctx.member.username}#{ctx.member.discriminator} | {ctx.member.id}",
			icon=ctx.author.avatar_url
		)
	)
	await bot.rest.create_message(int(os.environ["BugChannelID"]), embedded)



@bot.listen(hikari.StartedEvent)
async def on_started(event):
	print(f"Bot Has Been Booted Up")

keep_alive()
uvloop.install()
bot.run()