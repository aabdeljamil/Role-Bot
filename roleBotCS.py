import discord
import asyncio
import time

TOKEN = ''

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_raw_reaction_add(payload):
    pinCount = 0

    bot_id = 803760636436807690
    reaction = payload
    user = payload.member
    msgToPin = None

    if payload.user_id == bot_id:
        return

    if reaction.emoji == '📌':
        pinCount = reaction.count

    if pinCount >= 3:
        chnl = discord.utils.get(payload.member.guild.text_channels, id=payload.channel_id)
        #following is done to get a reference to the message, so that I can call the pin() method on it
        #there probably is a more efficient way than searching the whole history of the channel, but oh well
        async for mesag in chnl.history(limit=None):
            if mesag.id == payload.message_id:
                msgToPin = mesag
                
        if not msgToPin.pinned:
            await msgToPin.pin()
            return
        else:
            await chnl.send('Already Pinned!')
            return

    Channel = client.get_channel(801703288340217906) #role assignment channel

    if reaction.channel_id != Channel.id:
        return

    one = client.get_emoji(801910714088030209)
    two = client.get_emoji(801911644015558676)
    three = client.get_emoji(801911651691266099)
    four = client.get_emoji(801911660675596298)
    five = client.get_emoji(801911668090601552)
    six = client.get_emoji(801911675095089193)
    seven = client.get_emoji(801911681839267881)
    eight = client.get_emoji(801911688470855730)
    nine = client.get_emoji(801911695794241576)
    ten = client.get_emoji(801911705050546246)
    eleven = client.get_emoji(801911711220629514)
    twelve = client.get_emoji(801911717742903366)
    thirteen = client.get_emoji(801920602525007872)
    fourteen = client.get_emoji(801920612339679273)
    fifteen = client.get_emoji(801920618445668383)
    sixteen = client.get_emoji(801920624645505074)
    seventeen = client.get_emoji(801920634615496767)
    eighteen = client.get_emoji(801920644413390857)
    nineteen = client.get_emoji(801920651567824896)
    twenty = client.get_emoji(801920672749060096)
    twentyone = client.get_emoji(801920683218829324)
    twentytwo = client.get_emoji(801920689594564698)
    twentythree = client.get_emoji(801920696313315378)
    twentyfour = client.get_emoji(801920708338647111)
    twentyfive = client.get_emoji(801920716781781003)
    twentysix = client.get_emoji(801920724507689050)
    twentyseven = client.get_emoji(801920732350382110)
    twentyeight = client.get_emoji(801920747294687232)
    twentynine = client.get_emoji(801920754391580722)
    thirty = client.get_emoji(801920761517309983)
    thirtyone = client.get_emoji(801920770733244436)
    thirtytwo = client.get_emoji(801920789725184050)
    thirtythree = client.get_emoji(801920797840244806)
    thirtyfour = client.get_emoji(801920804710514699)
    thirtyfive = client.get_emoji(801920811408818218)
    thirtysix = client.get_emoji(801920818035949600)
    thirtyseven = client.get_emoji(801920825153552454)
    thirtyeight = client.get_emoji(801920833068466216)
    thirtynine = client.get_emoji(801920841326657626)

    if reaction.emoji == one:
        Role = discord.utils.get(user.guild.roles, id=801916281455771658)
        await user.add_roles(Role)
    elif reaction.emoji == two:
        Role = discord.utils.get(user.guild.roles, id=801916369691475969)
        await user.add_roles(Role)
    elif reaction.emoji == three:
        Role = discord.utils.get(user.guild.roles, id=801916539279507517)
        await user.add_roles(Role)
    elif reaction.emoji == four:
        Role = discord.utils.get(user.guild.roles, id=801916574914969600)
        await user.add_roles(Role)
    elif reaction.emoji == five:
        Role = discord.utils.get(user.guild.roles, id=801916608469139456)
        await user.add_roles(Role)
    elif reaction.emoji == six:
        Role = discord.utils.get(user.guild.roles, id=801916631063855194)
        await user.add_roles(Role)
    elif reaction.emoji == seven:
        Role = discord.utils.get(user.guild.roles, id=801916654924726284)
        await user.add_roles(Role)
    elif reaction.emoji == eight:
        Role = discord.utils.get(user.guild.roles, id=801702304080199731)
        await user.add_roles(Role)
    elif reaction.emoji == nine:
        Role = discord.utils.get(user.guild.roles, id=801702359440424980)
        await user.add_roles(Role)
    elif reaction.emoji == ten:
        Role = discord.utils.get(user.guild.roles, id=801702451534495765)
        await user.add_roles(Role)
    elif reaction.emoji == eleven:
        Role = discord.utils.get(user.guild.roles, id=801702476494798868)
        await user.add_roles(Role)
    elif reaction.emoji == twelve:
        Role = discord.utils.get(user.guild.roles, id=801702500658970640)
        await user.add_roles(Role)
    elif reaction.emoji == thirteen:
        Role = discord.utils.get(user.guild.roles, id=801916744045166692)
        await user.add_roles(Role)
    elif reaction.emoji == fourteen:
        Role = discord.utils.get(user.guild.roles, id=801916765847420959)
        await user.add_roles(Role)
    elif reaction.emoji == fifteen:
        Role = discord.utils.get(user.guild.roles, id=801898049583710209)
        await user.add_roles(Role)
    elif reaction.emoji == sixteen:
        Role = discord.utils.get(user.guild.roles, id=801916908646432798)
        await user.add_roles(Role)
    elif reaction.emoji == seventeen:
        Role = discord.utils.get(user.guild.roles, id=801916936237482025)
        await user.add_roles(Role)
    elif reaction.emoji == eighteen:
        Role = discord.utils.get(user.guild.roles, id=801916954654146583)
        await user.add_roles(Role)
    elif reaction.emoji == nineteen:
        Role = discord.utils.get(user.guild.roles, id=801846843259748372)
        await user.add_roles(Role)
    elif reaction.emoji == twenty:
        Role = discord.utils.get(user.guild.roles, id=801702554915831818)
        await user.add_roles(Role)
    elif reaction.emoji == twentyone:
        Role = discord.utils.get(user.guild.roles, id=801917149027369010)
        await user.add_roles(Role)
    elif reaction.emoji == twentytwo:
        Role = discord.utils.get(user.guild.roles, id=801702577041178624)
        await user.add_roles(Role)
    elif reaction.emoji == twentythree:
        Role = discord.utils.get(user.guild.roles, id=801830345527918622)
        await user.add_roles(Role)
    elif reaction.emoji == twentyfour:
        Role = discord.utils.get(user.guild.roles, id=801916129395081287)
        await user.add_roles(Role)
    elif reaction.emoji == twentyfive:
        Role = discord.utils.get(user.guild.roles, id=801917191310016533)
        await user.add_roles(Role)
    elif reaction.emoji == twentysix:
        Role = discord.utils.get(user.guild.roles, id=801917237237514242)
        await user.add_roles(Role)
    elif reaction.emoji == twentyseven:
        Role = discord.utils.get(user.guild.roles, id=801917261005717605)
        await user.add_roles(Role)
    elif reaction.emoji == twentyeight:
        Role = discord.utils.get(user.guild.roles, id=801835762659753994)
        await user.add_roles(Role)
    elif reaction.emoji == twentynine:
        Role = discord.utils.get(user.guild.roles, id=801917315871408128)
        await user.add_roles(Role)
    elif reaction.emoji == thirty:
        Role = discord.utils.get(user.guild.roles, id=801917332456472696)
        await user.add_roles(Role)
    elif reaction.emoji == thirtyone:
        Role = discord.utils.get(user.guild.roles, id=801917394485379102)
        await user.add_roles(Role)
    elif reaction.emoji == thirtytwo:
        Role = discord.utils.get(user.guild.roles, id=801917429050769438)
        await user.add_roles(Role)
    elif reaction.emoji == thirtythree:
        Role = discord.utils.get(user.guild.roles, id=801891776293634059)
        await user.add_roles(Role)
    elif reaction.emoji == thirtyfour:
        Role = discord.utils.get(user.guild.roles, id=801917471841583105)
        await user.add_roles(Role)
    elif reaction.emoji == thirtyfive:
        Role = discord.utils.get(user.guild.roles, id=801830423214424065)
        await user.add_roles(Role)
    elif reaction.emoji == thirtysix:
        Role = discord.utils.get(user.guild.roles, id=801917445547229184)
        await user.add_roles(Role)
    elif reaction.emoji == thirtyseven:
        Role = discord.utils.get(user.guild.roles, id=801702603833868298)
        await user.add_roles(Role)
    elif reaction.emoji == thirtyeight:
        Role = discord.utils.get(user.guild.roles, id=801917573251072050)
        await user.add_roles(Role)
    elif reaction.emoji == thirtynine:
        Role = discord.utils.get(user.guild.roles, id=801917633116766248)
        await user.add_roles(Role)



@client.event
async def on_raw_reaction_remove(payload):

    guild = client.get_guild(747979512041439313) #cs server

    user = discord.utils.get(guild.members, id=payload.user_id)

    Channel = client.get_channel(801703288340217906) #role assignment channel

    one = client.get_emoji(801910714088030209)
    two = client.get_emoji(801911644015558676)
    three = client.get_emoji(801911651691266099)
    four = client.get_emoji(801911660675596298)
    five = client.get_emoji(801911668090601552)
    six = client.get_emoji(801911675095089193)
    seven = client.get_emoji(801911681839267881)
    eight = client.get_emoji(801911688470855730)
    nine = client.get_emoji(801911695794241576)
    ten = client.get_emoji(801911705050546246)
    eleven = client.get_emoji(801911711220629514)
    twelve = client.get_emoji(801911717742903366)
    thirteen = client.get_emoji(801920602525007872)
    fourteen = client.get_emoji(801920612339679273)
    fifteen = client.get_emoji(801920618445668383)
    sixteen = client.get_emoji(801920624645505074)
    seventeen = client.get_emoji(801920634615496767)
    eighteen = client.get_emoji(801920644413390857)
    nineteen = client.get_emoji(801920651567824896)
    twenty = client.get_emoji(801920672749060096)
    twentyone = client.get_emoji(801920683218829324)
    twentytwo = client.get_emoji(801920689594564698)
    twentythree = client.get_emoji(801920696313315378)
    twentyfour = client.get_emoji(801920708338647111)
    twentyfive = client.get_emoji(801920716781781003)
    twentysix = client.get_emoji(801920724507689050)
    twentyseven = client.get_emoji(801920732350382110)
    twentyeight = client.get_emoji(801920747294687232)
    twentynine = client.get_emoji(801920754391580722)
    thirty = client.get_emoji(801920761517309983)
    thirtyone = client.get_emoji(801920770733244436)
    thirtytwo = client.get_emoji(801920789725184050)
    thirtythree = client.get_emoji(801920797840244806)
    thirtyfour = client.get_emoji(801920804710514699)
    thirtyfive = client.get_emoji(801920811408818218)
    thirtysix = client.get_emoji(801920818035949600)
    thirtyseven = client.get_emoji(801920825153552454)
    thirtyeight = client.get_emoji(801920833068466216)
    thirtynine = client.get_emoji(801920841326657626)

    if payload.channel_id != Channel.id:
        return

    if payload.emoji == one:
        Role = discord.utils.get(user.guild.roles, id=801916281455771658)
        await user.remove_roles(Role)
    elif payload.emoji == two:
        Role = discord.utils.get(user.guild.roles, id=801916369691475969)
        await user.remove_roles(Role)
    elif payload.emoji == three:
        Role = discord.utils.get(user.guild.roles, id=801916539279507517)
        await user.remove_roles(Role)
    elif payload.emoji == four:
        Role = discord.utils.get(user.guild.roles, id=801916574914969600)
        await user.remove_roles(Role)
    elif payload.emoji == five:
        Role = discord.utils.get(user.guild.roles, id=801916608469139456)
        await user.remove_roles(Role)
    elif payload.emoji == six:
        Role = discord.utils.get(user.guild.roles, id=801916631063855194)
        await user.remove_roles(Role)
    elif payload.emoji == seven:
        Role = discord.utils.get(user.guild.roles, id=801916654924726284)
        await user.remove_roles(Role)
    elif payload.emoji == eight:
        Role = discord.utils.get(user.guild.roles, id=801702304080199731)
        await user.remove_roles(Role)
    elif payload.emoji == nine:
        Role = discord.utils.get(user.guild.roles, id=801702359440424980)
        await user.remove_roles(Role)
    elif payload.emoji == ten:
        Role = discord.utils.get(user.guild.roles, id=801702451534495765)
        await user.remove_roles(Role)
    elif payload.emoji == eleven:
        Role = discord.utils.get(user.guild.roles, id=801702476494798868)
        await user.remove_roles(Role)
    elif payload.emoji == twelve:
        Role = discord.utils.get(user.guild.roles, id=801702500658970640)
        await user.remove_roles(Role)
    elif payload.emoji == thirteen:
        Role = discord.utils.get(user.guild.roles, id=801916744045166692)
        await user.remove_roles(Role)
    elif payload.emoji == fourteen:
        Role = discord.utils.get(user.guild.roles, id=801916765847420959)
        await user.remove_roles(Role)
    elif payload.emoji == fifteen:
        Role = discord.utils.get(user.guild.roles, id=801898049583710209)
        await user.remove_roles(Role)
    elif payload.emoji == sixteen:
        Role = discord.utils.get(user.guild.roles, id=801916908646432798)
        await user.remove_roles(Role)
    elif payload.emoji == seventeen:
        Role = discord.utils.get(user.guild.roles, id=801916936237482025)
        await user.remove_roles(Role)
    elif payload.emoji == eighteen:
        Role = discord.utils.get(user.guild.roles, id=801916954654146583)
        await user.remove_roles(Role)
    elif payload.emoji == nineteen:
        Role = discord.utils.get(user.guild.roles, id=801846843259748372)
        await user.remove_roles(Role)
    elif payload.emoji == twenty:
        Role = discord.utils.get(user.guild.roles, id=801702554915831818)
        await user.remove_roles(Role)
    elif payload.emoji == twentyone:
        Role = discord.utils.get(user.guild.roles, id=801917149027369010)
        await user.remove_roles(Role)
    elif payload.emoji == twentytwo:
        Role = discord.utils.get(user.guild.roles, id=801702577041178624)
        await user.remove_roles(Role)
    elif payload.emoji == twentythree:
        Role = discord.utils.get(user.guild.roles, id=801830345527918622)
        await user.remove_roles(Role)
    elif payload.emoji == twentyfour:
        Role = discord.utils.get(user.guild.roles, id=801916129395081287)
        await user.remove_roles(Role)
    elif payload.emoji == twentyfive:
        Role = discord.utils.get(user.guild.roles, id=801917191310016533)
        await user.remove_roles(Role)
    elif payload.emoji == twentysix:
        Role = discord.utils.get(user.guild.roles, id=801917237237514242)
        await user.remove_roles(Role)
    elif payload.emoji == twentyseven:
        Role = discord.utils.get(user.guild.roles, id=801917261005717605)
        await user.remove_roles(Role)
    elif payload.emoji == twentyeight:
        Role = discord.utils.get(user.guild.roles, id=801835762659753994)
        await user.remove_roles(Role)
    elif payload.emoji == twentynine:
        Role = discord.utils.get(user.guild.roles, id=801917315871408128)
        await user.remove_roles(Role)
    elif payload.emoji == thirty:
        Role = discord.utils.get(user.guild.roles, id=801917332456472696)
        await user.remove_roles(Role)
    elif payload.emoji == thirtyone:
        Role = discord.utils.get(user.guild.roles, id=801917394485379102)
        await user.remove_roles(Role)
    elif payload.emoji == thirtytwo:
        Role = discord.utils.get(user.guild.roles, id=801917429050769438)
        await user.remove_roles(Role)
    elif payload.emoji == thirtythree:
        Role = discord.utils.get(user.guild.roles, id=801891776293634059)
        await user.remove_roles(Role)
    elif payload.emoji == thirtyfour:
        Role = discord.utils.get(user.guild.roles, id=801917471841583105)
        await user.remove_roles(Role)
    elif payload.emoji == thirtyfive:
        Role = discord.utils.get(user.guild.roles, id=801830423214424065)
        await user.remove_roles(Role)
    elif payload.emoji == thirtysix:
        Role = discord.utils.get(user.guild.roles, id=801917445547229184)
        await user.remove_roles(Role)
    elif payload.emoji == thirtyseven:
        Role = discord.utils.get(user.guild.roles, id=801702603833868298)
        await user.remove_roles(Role)
    elif payload.emoji == thirtyeight:
        Role = discord.utils.get(user.guild.roles, id=801917573251072050)
        await user.remove_roles(Role)
    elif payload.emoji == thirtynine:
        Role = discord.utils.get(user.guild.roles, id=801917633116766248)
        await user.remove_roles(Role)



@client.event
async def on_message(message):

    if message.author.bot:
        return

    failed = False
    noRoles = []

    cs = client.get_guild(747979512041439313)#cs guild

    moderatorRole = discord.utils.get(message.author.guild.roles, id=747979512041439315)

    if message.content.lower() == '>calendar spring 2021':
        file1 = discord.File('s2021.png')
        await message.channel.send(content=None, file=file1)
    elif message.content.lower() == '>calendar summer 2021':
        file1 = discord.File('sum2021a.png')
        file2 = discord.File('sum2021b.png')
        await message.channel.send(content=None, files=[file1, file2])
    elif message.content.lower() == '>calendar fall 2021':
        file1 = discord.File('f2021.png')
        await message.channel.send(content=None, file=file1)
    elif message.content.lower() == '>calendar spring 2022':
        file1 = discord.File('s2022.png')
        await message.channel.send(content=None, file=file1)
    elif message.content.lower() == '>calendar summer 2022':
        file1 = discord.File('sum2022a.png')
        file2 = discord.File('sum2022b.png')
        await message.channel.send(content=None, files=[file1, file2])
    elif message.content.lower() == '>calendar fall 2022':
        file1 = discord.File('f2022.png')
        await message.channel.send(content=None, file=file1)
    elif message.content.lower() == '>calendar spring 2023':
        file1 = discord.File('s2023.png')
        await message.channel.send(content=None, file=file1)
    elif message.content.lower() == '>calendar summer 2023':
        file1 = discord.File('sum2023a.png')
        file2 = discord.File('sum2023b.png')
        await message.channel.send(content=None, files=[file1, file2])


    elif message.content.lower() == '>del m':
        if moderatorRole not in message.author.roles:
            await message.channel.send('You do not have permission to do this')
            return

        await message.channel.send('Are you sure?')
        msg = await client.wait_for('message', timeout=60.0)
        if msg.content.lower() == 'y' or msg.content.lower() == 'yes':
            await message.channel.purge()

    elif message.content.lower() == '>remind users':
        if moderatorRole not in message.author.roles:
            await message.channel.send('You do not have permission to do this')
            return

        chnl = client.get_channel(802291569872338944)
        rolesChnl = client.get_channel(801703288340217906)

        membs = cs.members

        for memb in membs:
            if len(memb.roles) == 2:
                noRoles.append(memb)

        txt = "I noticed that you never assigned yourself class roles. Unless you aren't taking any CS classes \
            this semester, please go to the " + rolesChnl.mention + " channel and react to my message to assign \
                yourself the appropriate class roles. Oherwise, every class channel will remain hidden to you. Thanks!"

        for noRole in noRoles:
            '''
            if dm fails, send dm to me to let me know
            '''
            try:
                await noRole.send(txt)
            except (discord.errors.Forbidden, discord.errors.HTTPException) as e:
                abdallah = None
                for usr in cs.members:
                    if usr.name == 'abdallaha':
                        abdallah = usr
                txt1 = "role reminder failed for " + memb.mention + "[" + memb.name + "]"
                await abdallah.send(txt1)
                failed = True

        if failed:
            await message.channel.send("Role reminder failed")
        else:
            await message.channel.send("Role reminder sent")

        #instead of DM's, can send a message in server addressing everyone that hasn't chosen a role like so:
        '''
        for noRole in noRoles:
            txt += noRole.mention + ', '

            if len(txt) > 1950:
                await chnl.send(txt)
                txt = ''

        if txt != '':
            await chnl.send(txt)

        txt1 = "I noticed that you never assigned yourself class roles. Unless you aren't taking any CS classes \
            this semester, please go to the " + rolesChnl.mention + " channel and react to my message to assign \
                yourself the appropriate class roles. Oherwise, every class channel will remain hidden to you. Thanks!"

        await chnl.send(txt1)
        '''

    elif message.content.lower() == '>role assignment':
        if moderatorRole not in message.author.roles:
            await message.channel.send('You do not have permission to do this')
            return

        Channel = client.get_channel(801703288340217906)

        one = client.get_emoji(801910714088030209)
        two = client.get_emoji(801911644015558676)
        three = client.get_emoji(801911651691266099)
        four = client.get_emoji(801911660675596298)
        five = client.get_emoji(801911668090601552)
        six = client.get_emoji(801911675095089193)
        seven = client.get_emoji(801911681839267881)
        eight = client.get_emoji(801911688470855730)
        nine = client.get_emoji(801911695794241576)
        ten = client.get_emoji(801911705050546246)
        eleven = client.get_emoji(801911711220629514)
        twelve = client.get_emoji(801911717742903366)
        thirteen = client.get_emoji(801920602525007872)
        fourteen = client.get_emoji(801920612339679273)
        fifteen = client.get_emoji(801920618445668383)
        sixteen = client.get_emoji(801920624645505074)
        seventeen = client.get_emoji(801920634615496767)
        eighteen = client.get_emoji(801920644413390857)
        nineteen = client.get_emoji(801920651567824896)
        twenty = client.get_emoji(801920672749060096)
        twentyone = client.get_emoji(801920683218829324)
        twentytwo = client.get_emoji(801920689594564698)
        twentythree = client.get_emoji(801920696313315378)
        twentyfour = client.get_emoji(801920708338647111)
        twentyfive = client.get_emoji(801920716781781003)
        twentysix = client.get_emoji(801920724507689050)
        twentyseven = client.get_emoji(801920732350382110)
        twentyeight = client.get_emoji(801920747294687232)
        twentynine = client.get_emoji(801920754391580722)
        thirty = client.get_emoji(801920761517309983)
        thirtyone = client.get_emoji(801920770733244436)
        thirtytwo = client.get_emoji(801920789725184050)
        thirtythree = client.get_emoji(801920797840244806)
        thirtyfour = client.get_emoji(801920804710514699)
        thirtyfive = client.get_emoji(801920811408818218)
        thirtysix = client.get_emoji(801920818035949600)
        thirtyseven = client.get_emoji(801920825153552454)
        thirtyeight = client.get_emoji(801920833068466216)
        thirtynine = client.get_emoji(801920841326657626)

        text1 = "**React to this message to unlock channels and get your roles!**\nBased on the role(s) you pick, more text \
                and voice channels will become visible to you! To remove a role and hide its corresponding channels, just remove \
                your reaction to that role.\n\n" + str(one) + ' - CS100\n' + str(two) + ' - CS104\n' + str(three) + ' - CS105\n' \
                + str(four) + ' - CS110\n' + str(five) + ' - CS115\n' + str(six) + ' - CS116\n' + str(seven) + ' - CS201\n' \
                + str(eight) + ' - CS330\n' + str(nine) + ' - CS331\n' + str(ten) + ' - CS340\n' + str(eleven) + ' - CS350\n' \
                + str(twelve) + ' - CS351\n' + str(thirteen) + ' - CS397\n' + str(fourteen) + ' - CS401\n' \
                + str(fifteen) + ' - CS402\n' + str(sixteen) + ' - CS403\n' + str(seventeen) + ' - CS406\n' \
                + str(eighteen) + ' - CS411\n' + str(nineteen) + ' - CS422\n' + str(twenty) + ' - CS425\n'

        text2 = str(twentyone) + ' - CS429\n' + str(twentytwo) + ' - CS430\n' + str(twentythree) + ' - CS440\n' \
                + str(twentyfour) + ' - CS442\n' + str(twentyfive) + ' - CS443\n' + str(twentysix) + ' - CS445\n' \
                + str(twentyseven) + ' - CS447\n' + str(twentyeight) + ' - CS450\n' + str(twentynine) + ' - CS451\n' \
                + str(thirty) + ' - CS455\n' + str(thirtyone) + ' - CS456\n' + str(thirtytwo) + ' - CS458\n' \
                + str(thirtythree) + ' - CS470\n' + str(thirtyfour) + ' - CS480\n' + str(thirtyfive) + ' - CS481\n' \
                + str(thirtysix) + ' - CS482\n' + str(thirtyseven) + ' - CS484\n' + str(thirtyeight) + ' - CS485\n' \
                + str(thirtynine) + ' - CS487\n\nLet us know if you want a class added here.'

        emb1 = discord.Embed(title='Role Assignment', description=text1, colour=0x428df5)
        emb2 = discord.Embed(description=text2, colour=0x428df5)

        msg1 = await Channel.send(content=None, embed=emb1)
        msg2 = await Channel.send(content=None, embed=emb2)

        await msg1.add_reaction(one)
        await msg1.add_reaction(two)
        await msg1.add_reaction(three)
        await msg1.add_reaction(four)
        await msg1.add_reaction(five)
        await msg1.add_reaction(six)
        await msg1.add_reaction(seven)
        await msg1.add_reaction(eight)
        await msg1.add_reaction(nine)
        await msg1.add_reaction(ten)
        await msg1.add_reaction(eleven)
        await msg1.add_reaction(twelve)
        await msg1.add_reaction(thirteen)
        await msg1.add_reaction(fourteen)
        await msg1.add_reaction(fifteen)
        await msg1.add_reaction(sixteen)
        await msg1.add_reaction(seventeen)
        await msg1.add_reaction(eighteen)
        await msg1.add_reaction(nineteen)
        await msg1.add_reaction(twenty)

        await msg2.add_reaction(twentyone)
        await msg2.add_reaction(twentytwo)
        await msg2.add_reaction(twentythree)
        await msg2.add_reaction(twentyfour)
        await msg2.add_reaction(twentyfive)
        await msg2.add_reaction(twentysix)
        await msg2.add_reaction(twentyseven)
        await msg2.add_reaction(twentyeight)
        await msg2.add_reaction(twentynine)
        await msg2.add_reaction(thirty)
        await msg2.add_reaction(thirtyone)
        await msg2.add_reaction(thirtytwo)
        await msg2.add_reaction(thirtythree)
        await msg2.add_reaction(thirtyfour)
        await msg2.add_reaction(thirtyfive)
        await msg2.add_reaction(thirtysix)
        await msg2.add_reaction(thirtyseven)
        await msg2.add_reaction(thirtyeight)
        await msg2.add_reaction(thirtynine)

        await message.channel.send('Done')


@client.event
async def on_ready():

    for guild in client.guilds:
        print(client.user, 'connected to guild ', guild.name, '#', guild.id)


client.run(TOKEN)