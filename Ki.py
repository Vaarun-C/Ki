import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import os
import requests
import json
import time
from cogs import shinyhunt

client = commands.Bot(command_prefix = '.')
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True)

#Runs when Bot is ready
@client.event
async def on_ready():

	client.pokemon_in_game = ('Type: Null', 'Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran♀️','Nidorina','Nidoqueen','Nidoran♂️','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton',"Farfetch'd",'Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr.Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew','Chikorita','Bayleef','Meganium','Cyndaquil','Quilava','Typhlosion','Totodile','Croconaw','Feraligatr','Sentret','Furret','Hoothoot','Noctowl','Ledyba','Ledian','Spinarak','Ariados','Crobat','Chinchou','Lanturn','Pichu','Cleffa','Igglybuff','Togepi','Togetic','Natu','Xatu','Mareep','Flaaffy','Ampharos','Bellossom','Marill','Azumarill','Sudowoodo','Politoed','Hoppip','Skiploom','Jumpluff','Aipom','Sunkern','Sunflora','Yanma','Wooper','Quagsire','Espeon','Umbreon','Murkrow','Slowking','Misdreavus','Unown','Wobbuffet','Girafarig','Pineco','Forretress','Dunsparce','Gligar','Steelix','Snubbull','Granbull','Qwilfish','Scizor','Shuckle','Heracross','Sneasel','Teddiursa','Ursaring','Slugma','Magcargo','Swinub','Piloswine','Corsola','Remoraid','Octillery','Delibird','Mantine','Skarmory','Houndour','Houndoom','Kingdra','Phanpy','Donphan','Porygon2','Stantler','Smeargle','Tyrogue','Hitmontop','Smoochum','Elekid','Magby','Miltank','Blissey','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Celebi','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Poochyena','Mightyena','Zigzagoon','Linoone','Wurmple','Silcoon','Beautifly','Cascoon','Dustox','Lotad','Lombre','Ludicolo','Seedot','Nuzleaf','Shiftry','Taillow','Swellow','Wingull','Pelipper','Ralts','Kirlia','Gardevoir','Surskit','Masquerain','Shroomish','Breloom','Slakoth','Vigoroth','Slaking','Nincada','Ninjask','Shedinja','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Nosepass','Skitty','Delcatty','Sableye','Mawile','Aron','Lairon','Aggron','Meditite','Medicham','Electrike','Manectric','Plusle','Minun','Volbeat','Illumise','Roselia','Gulpin','Swalot','Carvanha','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Spoink','Grumpig','Spinda','Trapinch','Vibrava','Flygon','Cacnea','Cacturne','Swablu','Altaria','Zangoose','Seviper','Lunatone','Solrock','Barboach','Whiscash','Corphish','Crawdaunt','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Feebas','Milotic','Castform','Kecleon','Shuppet','Banette','Duskull','Dusclops','Tropius','Chimecho','Absol','Wynaut','Snorunt','Glalie','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Bagon','Shelgon','Salamence','Beldum','Metang','Metagross','Regirock','Regice','Registeel','Latias','Latios','Kyogre','Groudon','Rayquaza','Jirachi','Deoxys','Turtwig','Grotle','Torterra','Chimchar','Monferno','Infernape','Piplup','Prinplup','Empoleon','Starly','Staravia','Staraptor','Bidoof','Bibarel','Kricketot','Kricketune','Shinx','Luxio','Luxray','Budew','Roserade','Cranidos','Rampardos','Shieldon','Bastiodon','Burmy','Wormadam','Mothim','Combee','Vespiquen','Pachirisu','Buizel','Floatzel','Cherubi','Cherrim','Shellos','Gastrodon','Ambipom','Drifloon','Drifblim','Buneary','Lopunny','Mismagius','Honchkrow','Glameow','Purugly','Chingling','Stunky','Skuntank','Bronzor','Bronzong','Bonsly','MimeJr.','Happiny','Chatot','Spiritomb','Gible','Gabite','Garchomp','Munchlax','Riolu','Lucario','Hippopotas','Hippowdon','Skorupi','Drapion','Croagunk','Toxicroak','Carnivine','Finneon','Lumineon','Mantyke','Snover','Abomasnow','Weavile','Magnezone','Lickilicky','Rhyperior','Tangrowth','Electivire','Magmortar','Togekiss','Yanmega','Leafeon','Glaceon','Gliscor','Mamoswine','Porygon-Z','Gallade','Probopass','Dusknoir','Froslass','Rotom','Uxie','Mesprit','Azelf','Dialga','Palkia','Heatran','Regigigas','Giratina','Cresselia','Phione','Manaphy','Darkrai','Shaymin','Arceus','Victini','Snivy','Servine','Serperior','Tepig','Pignite','Emboar','Oshawott','Dewott','Samurott','Patrat','Watchog','Lillipup','Herdier','Stoutland','Purrloin','Liepard','Pansage','Simisage','Pansear','Simisear','Panpour','Simipour','Munna','Musharna','Pidove','Tranquill','Unfezant','Blitzle','Zebstrika','Roggenrola','Boldore','Gigalith','Woobat','Swoobat','Drilbur','Excadrill','Audino','Timburr','Gurdurr','Conkeldurr','Tympole','Palpitoad','Seismitoad','Throh','Sawk','Sewaddle','Swadloon','Leavanny','Venipede','Whirlipede','Scolipede','Cottonee','Whimsicott','Petilil','Lilligant','Basculin','Sandile','Krokorok','Krookodile','Darumaka','Darmanitan','Maractus','Dwebble','Crustle','Scraggy','Scrafty','Sigilyph','Yamask','Cofagrigus','Tirtouga','Carracosta','Archen','Archeops','Trubbish','Garbodor','Zorua','Zoroark','Minccino','Cinccino','Gothita','Gothorita','Gothitelle','Solosis','Duosion','Reuniclus','Ducklett','Swanna','Vanillite','Vanillish','Vanilluxe','Deerling','Sawsbuck','Emolga','Karrablast','Escavalier','Foongus','Amoonguss','Frillish','Jellicent','Alomomola','Joltik','Galvantula','Ferroseed','Ferrothorn','Klink','Klang','Klinklang','Tynamo','Eelektrik','Eelektross','Elgyem','Beheeyem','Litwick','Lampent','Chandelure','Axew','Fraxure','Haxorus','Cubchoo','Beartic','Cryogonal','Shelmet','Accelgor','Stunfisk','Mienfoo','Mienshao','Druddigon','Golett','Golurk','Pawniard','Bisharp','Bouffalant','Rufflet','Braviary','Vullaby','Mandibuzz','Heatmor','Durant','Deino','Zweilous','Hydreigon','Larvesta','Volcarona','Cobalion','Terrakion','Virizion','Tornadus','Thundurus','Reshiram','Zekrom','Landorus','Kyurem','Keldeo','Meloetta','Genesect','Chespin','Quilladin','Chesnaught','Fennekin','Braixen','Delphox','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Fletchling','Fletchinder','Talonflame','Scatterbug','Spewpa','Vivillon','Litleo','Pyroar','Flabébé','Floette','Florges','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Espurr','Meowstic','Honedge','Doublade','Aegislash','Spritzee','Aromatisse','Swirlix','Slurpuff','Inkay','Malamar','Binacle','Barbaracle','Skrelp','Dragalge','Clauncher','Clawitzer','Helioptile','Heliolisk','Tyrunt','Tyrantrum','Amaura','Aurorus','Sylveon','Hawlucha','Dedenne','Carbink','Goomy','Sliggoo','Goodra','Klefki','Phantump','Trevenant','Pumpkaboo','Gourgeist','Bergmite','Avalugg','Noibat','Noivern','Xerneas','Yveltal','Zygarde','Diancie','Hoopa','Volcanion','Rowlet','Dartrix','Decidueye','Litten','Torracat','Incineroar','Popplio','Brionne','Primarina','Pikipek','Trumbeak','Toucannon','Yungoos','Gumshoos','Grubbin','Charjabug','Vikavolt','Crabrawler','Crabominable','Oricorio','Cutiefly','Ribombee','Rockruff','Lycanroc','Wishiwashi','Mareanie','Toxapex','Mudbray','Mudsdale','Dewpider','Araquanid','Fomantis','Lurantis','Morelull','Shiinotic','Salandit','Salazzle','Stufful','Bewear','Bounsweet','Steenee','Tsareena','Comfey','Oranguru','Passimian','Wimpod','Golisopod','Sandygast','Palossand','Pyukumuku','Type:Null','Silvally','Minior','Komala','Turtonator','Togedemaru','Mimikyu','Bruxish','Drampa','Dhelmise','Jangmo-o','Hakamo-o','Kommo-o','Tapu Koko','Tapu Lele','Tapu Bulu','Tapu Fini','Cosmog','Cosmoem','Solgaleo','Lunala','Nihilego','Buzzwole','Pheromosa','Xurkitree','Celesteela','Kartana','Guzzlord','Necrozma','Magearna','Marshadow','Poipole','Naganadel','Stakataka','Blacephalon','Zeraora','Meltan','Melmetal','Grookey','Thwackey','Rillaboom','Scorbunny','Raboot','Cinderace','Sobble','Drizzile','Inteleon','Skwovet','Greedent','Rookidee','Corvisquire','Corviknight','Blipbug','Dottler','Orbeetle','Nickit','Thievul','Gossifleur','Eldegoss','Wooloo','Dubwool','Chewtle','Drednaw','Yamper','Boltund','Rolycoly','Carkol','Coalossal','Applin','Flapple','Appletun','Silicobra','Sandaconda','Cramorant','Arrokuda','Barraskewda','Toxel','Toxtricity','Sizzlipede','Centiskorch','Clobbopus','Grapploct','Sinistea','Polteageist','Hatenna','Hattrem','Hatterene','Impidimp','Morgrem','Grimmsnarl','Obstagoon','Perrserker','Cursola',"Sirfetch'd",'Mr.Rime','Runerigus','Milcery','Alcremie','Falinks','Pincurchin','Snom','Frosmoth','Stonjourner','Eiscue','Indeedee','Morpeko','Cufant','Copperajah','Dracozolt','Arctozolt','Dracovish','Arctovish','Duraludon','Dreepy','Drakloak','Dragapult','Zacian','Zamazenta','Eternatus','Kubfu','Urshifu','Zarude','Regieleki','Regidrago','Glastrier','Spectrier')

	#Initialize Discord channels
	for guild in client.guilds:
		if(guild.name == "Winston's server"):
			for text_channel in guild.text_channels:
				if(text_channel.id == 882574195513516072):
					client.motolist = text_channel
				elif(text_channel.id == 882574240891666472):
					client.spexlist = text_channel
				elif(text_channel.id == 882574582924574770):
					client.jefflist = text_channel
				elif(text_channel.id == 911646750547275816):
					client.gantherlist = text_channel
				elif(text_channel.id == 881875552028483594):
					client.pokemon_names_channel = text_channel
				elif(text_channel.id == 882583920963625010):
					client.spam_channel = text_channel
				elif(text_channel.id == 882872744323203072):
					client.command_channel = text_channel

		elif(guild.name == "The Bois"):
			for text_channel in guild.text_channels:
				if(text_channel.id == 792314109625499668):
					client.spawn_channel = text_channel
				elif(text_channel.id == 851101277920559154):
					client.incense_channel = text_channel

	#Initialize ids
	client.moto_id = 730020582393118730
	client.ganther_id = 730028657581490176
	client.jeff_id = 730023436939952139
	client.spex_id = 729997258656972820
	client.poketwo_id = 716390085896962058
	
	client.winston_status = False
	client.shiny = False
	client.shiny_hunt = shinyhunt.shinyhunt(client)

	client.ki_users = {
		client.moto_id: client.motolist,
		client.jeff_id: client.jefflist,
		client.spex_id: client.spexlist,
		client.ganther_id: client.gantherlist
	}

	print('ready')

#Runs whenever a message is posted on Discord
@client.event
async def on_message(message):

	#Check if Muxus says Winston is rate limited
	if((message.author.id == 882580519542468639) and (message.channel.id == client.command_channel.id) and (message.content == 'Rate Limited')):
		await client.spawn_channel.send("Winston is being rate limited right now... Try that again after a few seconds")
		await client.command_channel.purge(limit=1) #Remove the rate limited message afterwards
		return

	#Check to see if messsage if from poketwo in the spawn channel
	if((message.author.id == client.poketwo_id) and (message.channel.id == client.spawn_channel.id)):

		if(client.winston_status == False):
			return

		try:

			#Get the message from poketwo
			pokemon_spawn_message = (await message.channel.fetch_message(message.id)).embeds[0]

			#Check if it is a spawn message
			if ('wild pokémon has appeared!' in pokemon_spawn_message.to_dict().get('title')):
	
				pokemon_names = await catch()
				not_caught = []
				for name in pokemon_names:
					#Check if pokemon is uncaught
					not_caught.extend(await check(name))

				not_caught = set(not_caught)
				not_caught = list(not_caught)

				is_shiny = await client.shiny_hunt.get_shinies()
				for name in pokemon_names:
					for user, shiny_pokemon in is_shiny.items():
						if(name == shiny_pokemon):
							await client.spawn_channel.send(f"<@{user}> your shiny has spawned")
							client.shiny = True

				if(client.shiny):
					await client.command_channel.send("Stop Spam")
					await client.spawn_channel.send("Session terminated")
					client.shiny = False
					return

				#If everyone has caught it, ask winston to catch it
				if(len(not_caught) == 0):
					for name in pokemon_names:
						await client.pokemon_names_channel.send(name)			
				else:

					await client.command_channel.send("Stop Spam")
					#Otherwise send prompt to catch the pokemon
					for name in not_caught:
						await client.spawn_channel.send(f"Wait <@{name}>, needs to catch this")
					await client.spawn_channel.send("Session terminated")


				if(len(pokemon_names) == 1):
					#Get URL and name from image
					directory = pokemon_names[0]
					pokemon_URL = pokemon_spawn_message.image.url

					await client.spawn_channel.send(f"Downloading image to E:/Projects/Ki/Images/{directory}")
					await client.command_channel.send(f"Download {pokemon_URL} {directory}")


		except IndexError:
			return

	#Runs on_message alongside other commands
	await client.process_commands(message)

async def catch():

	possible_pokemon = []

	#Function to check if message is from Poketwo
	def check(m):
		return m.author.id == client.poketwo_id

	await client.command_channel.send("Hint")

	#Get message from discord and check if it is from Poketwo
	message = await client.wait_for('message', check=check)
	hint = message.content.split(" ")[-1]
	hint = hint[:-1]
	hint = hint.replace("\\", "")

	for pokemon in client.pokemon_in_game:
		if(len(pokemon) == len(hint)):
			possible_pokemon.append(pokemon)

	letter_count = 0
	while(letter_count < len(hint)):
		if(hint[letter_count] != "_"):
			count = 0
			while (count < len(possible_pokemon)):
				if(possible_pokemon[count][letter_count] != hint[letter_count]):
					possible_pokemon.remove(possible_pokemon[count])
					count = count - 1
				count += 1
		letter_count += 1
	return possible_pokemon

#Checks pokemon name with user's list of pokemon
async def check(name):

	pokemon = []
	uncaught = []

	for user_id, channel in client.ki_users.items():
		messages = await channel.history(limit=1000).flatten() #Get user's saved list of pokemon
		for message in messages:
			pokemon.append(message.content)
		if name in pokemon:
			uncaught.append(user_id) #Save and return the users who haven't caught the pokemon
		pokemon = []

	return uncaught

#Send numbers from start till end
@slash.slash(
	name="numbers",
	description="Sends numbers from start till end",
	guild_ids=[760880935557398608],
	options=[
		create_option(
			name="start",
			description="Starting number",
			option_type=4,
			required=True
		),
		create_option(
			name="end",
			description="Ending number",
			option_type=4,
			required=True
		)
	]
)

async def numbers(ctx:SlashContext, start, end):
	s = ""

	if(end < start):
		for i in range(int(start), int(end)-1, -1):
			s += str(i) + " "
	else:
		for i in range(int(start), int(end)+1):
			s += str(i) + " "

	await ctx.send(s)

#Load all cogs in cogs folder
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

#Run the bot
client.run(os.environ['TOKEN'])