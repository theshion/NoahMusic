import asyncio
from AnonXMusic import app as Yumikoo
from pyrogram import filters


SPAM_CHATS = []


@Yumikoo.on_message(filters.command(["tagall", "all"]) | filters.command("@all", "") & filters.group)
async def tag_all_users(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ") 
        return                  
    if replied:
        SPAM_CHATS.append(message.chat.id)      
        usernum= 0
        usertxt = ""
        async for m in Yumikoo.get_chat_members(message.chat.id): 
            if message.chat.id not in SPAM_CHATS:
                break       
            usernum += 1
            usertxt += f"⬝ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 3:
                await replied.reply_text(usertxt)
                await asyncio.sleep(1)
                usernum = 0
                usertxt = ""
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]
        
        SPAM_CHATS.append(message.chat.id)
        usernum= 0
        usertxt = ""
        async for m in Yumikoo.get_chat_members(message.chat.id):       
            if message.chat.id not in SPAM_CHATS:
                break 
            usernum += 1
            usertxt += f"⬝ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 3:
                await Yumikoo.send_message(message.chat.id,f'{text}\n{usertxt}')
                await asyncio.sleep(1)
                usernum = 0
                usertxt = ""                          
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass        
           
@Yumikoo.on_message(filters.command("cancel") & ~filters.private)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try :
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴄᴛɪᴏɴ ʜᴀꜱ ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ\nɴᴏ ᴘʀᴏᴄᴇꜱꜱ ɪꜱ ᴏɴɢᴏɪɴɢ")     
                                     
    else :
        await message.reply_text("ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴄᴛɪᴏɴ ʜᴀꜱ ʙᴇᴇɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴛᴏᴘᴘᴇᴅ\nɴᴏ ᴘʀᴏᴄᴇss ɪꜱ ᴏɴɢᴏɪɴɢ")  
        return       


