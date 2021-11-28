#Cog with commands to manage the custom list of pokemon of user

import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle


class shinyhunt(commands.Cog):

	server_ids = [760880935557398608]

	def __init__(self, client):
		self.client = client

	#Updates Winston's status
	@cog_ext.cog_slash( name="my_shiny",
						guild_ids=server_ids,
						description="The Pokemon you are shiny hunting"
					  )
	async def my_shiny(self, ctx):

		shiny_hunt_list = ((self.client.ki_users[ctx.author.id]).name).split("-")[1:]
		shiny_hunt = ""
		for sh in shiny_hunt_list:
			shiny_hunt += (sh.capitalize() + " ")
		shiny_hunt = shiny_hunt[:-1]

		if(shiny_hunt == "Type Null"):
				shiny_hunt = "Type: Null"

		if(shiny_hunt == "none"):
			await ctx.send("You haven't set your shiny yet!", components=[
                                    							create_actionrow(
                                        							create_button(style=ButtonStyle.green, label="Set It", custom_id="get_shiny")
                                        						)
                                    						  ])
		else:
			await ctx.send(f"You are currently shiny hunting {shiny_hunt}", components=[
                                    											create_actionrow(
                                        											create_button(style=ButtonStyle.green, label="Change It", custom_id="get_shiny")
                                        										)
                                    										  ])

	@cog_ext.cog_component()
	async def get_shiny(self, ctx):

		def check(m):
			return m.author.id == ctx.author.id

		while True:
			await ctx.send(f"What do you want to shiny hunt <@{ctx.author.id}>?")
			message = await self.client.wait_for('message', check=check)
			messages = message.content.split(" ")
			message = ""
			for m in messages:
				message += m.capitalize() + " "
			message = message[:-1]

			if(message not in self.client.pokemon_in_game):
				await ctx.send("Please enter the correct pokemon name")
				continue
			break

		if(message == "Type: Null"):
				message = "Type Null"

		text_channel = self.client.ki_users[ctx.author.id]
		await text_channel.edit(name=f"{ctx.author.name}-{message}")

		if(message == "Type Null"):
			await ctx.send(f"<@{ctx.author.id}> you are now shiny hunting Type: Null")
		else:
			await ctx.send(f"<@{ctx.author.id}> you are now shiny hunting {message}")

	async def get_shinies(self):
		shinies = {}
		for user_id, text_channel in self.client.ki_users.items():
			shiny_list = text_channel.name.split("-")[1:]
			shiny = ""
			for sh in shiny_list:
				shiny += (sh.capitalize() + " ")
			shiny = shiny[:-1]

			if(shiny == "Type Null"):
				shiny = "Type: Null"

			shinies[user_id] = shiny

		return shinies

def setup(client):
	client.add_cog(shinyhunt(client))