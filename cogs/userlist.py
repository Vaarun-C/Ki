#Cog with commands to manage the custom list of pokemon of user

import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

class userlist(commands.Cog):

	server_ids = [760880935557398608]

	def __init__(self, client):
		self.client = client

	#Manage User's list
	@cog_ext.cog_slash( name="mylist",
						guild_ids=server_ids,
						description="Manage my list of Pokemon",
						options=[
							create_option(
								name="manage",
								description="Manage my list",
								option_type=3,
								required=True,
								choices=[
									create_choice(
										name="Make my list",
										value="Make"
									),
									create_choice(
										name="Show my list",
										value="Show"
									),
									create_choice(
										name="Clear my list",
										value="Clear"
									)
								]
							)
						]
					  )
	async def mylist(self, ctx, manage: str):
		if(manage == "Make"):
			await self.makeList(ctx)
		elif(manage == "Show"):
			await self.showList(ctx)
		elif(manage == "Clear"):
			await self.clearList(ctx)

	#Makes list of Pokemon
	async def makeList(self, ctx):
	
		#Function to check if message is from Poketwo
		def check(m):
			return m.author.id == self.client.poketwo_id
	
		list_of_pokemon = []
		count = 0
	
		while (True):
	
			if(count == 0):
				await ctx.send('Open list of pokemon')
			else:
				await ctx.send('Go to next page')
	
			#Get message from discord and check if it is from Poketwo
			message = await self.client.wait_for('message', check=check)
	
			#Get embeds from message
			message_content = (message.embeds[0]).to_dict()
	
			#Get the number of Pokemon from footer
			if(count == 0):
				number_of_pokemon_string = (((message_content.get('footer')).get('text')).split(' '))[-1]
				number_of_pokemon = int(number_of_pokemon_string[:-1])
	
			#Get the names of pokemon and append them to list_of_pokemon
			list_of_embeds = message_content.get('fields')
			list_of_embeds.pop(-1)
	
			for embed in list_of_embeds:
				list_of_pokemon.append(embed.get('name')[embed.get('name').index(" "):embed.get('name').index("#")])	

			count += 1
	
			#If count is greater than number of pages in list, stop
			if(count > int(number_of_pokemon/20)):
				break
	
		count = 1
		e = discord.Embed()
		channel = self.client.ki_users.get(ctx.author.id)

		#Store user's list in embeds
		for pokemon in list_of_pokemon:
			e.add_field(name=count, value=pokemon, inline=True)
			count += 1
			if ((count % 25) == 0):
				await channel.send(embed = e)
				e = discord.Embed()

		await channel.send(embed = e)	
		await ctx.send(f'{ctx.author.name}, your list of pokemon is successfully stored')	

	#Clears user's list
	async def clearList(self, ctx):
	
		await ctx.send("Clearing list...")
	
		#Clear respective user's saved list
		channel = self.client.ki_users.get(ctx.author.id)
		await channel.purge(limit=1000)
		await ctx.send(f'{ctx.author.name} your list is cleared')
	
	#Shows user's saved list of Pokemon					
	async def showList(self, ctx):
		
		channel = self.client.ki_users.get(ctx.author.id)
		messages = await channel.history(limit = 1000, oldest_first = True).flatten()

		if(len(messages) == 0):
			await ctx.send("List is empty")
		else:
			for message in messages:
				await ctx.send(embed = message.embeds[0])

def setup(client):
	client.add_cog(userlist(client))