from aiogram import Bot,Dispatcher,F,Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,File,Video,PhotoSize
import aiogram
import keyboards as kb 
from backend.database.core import is_user_exists,create_user,is_user_subbed

router = Router()

welcome_text = """Welcome to Character AI – Your Portal to Endless Conversations!

Here, you can create and talk to unique AI characters with their own personalities, knowledge, and stories. From historical figures and fictional heroes to your own custom creations – anything is possible.

What can you do here?
✨ Chat with anyone: Philosophers, anime characters, celebrities, or original personas.
✨ Create your own: Design a character's personality, backstory, and voice in minutes.
✨ Explore limitless worlds: Dive into roleplay, seek advice, practice languages, or just have fun.

Start your journey by typing a character's name or browsing the community library. The only limit is your imagination."""

@router.message(CommandStart())
async def start_handler(message:Message):
    user_id = message.from_user.id
    user_ex = await is_user_exists(str(user_id))
    if not user_ex:
        await create_user(str(user_id))
    await message.answer(welcome_text,reply_markup=kb.main_keyborad)

@router.messgae(F.text == "Profile")
async def profile_handler(message:Message):
    user_id = str(message.from_user.id)
    user_subbed = await  is_user_subbed(user_id)
    username = str(message.from_user.username)
    profile_text = f"""Profile of {username}
                       Subscription : {user_subbed}
        """
    if not user_subbed:
        await message.answer(
            text = profile_text,
            reply_markup=kb.profile_key_board
        )
    else:
        await message.asnwer(text = profile_text)


sub_text = """Устали от ограничений? Переходите на Премиум!

Станьте хозяином своего виртуального мира. Только для Премиум-пользователей:

    🧬 Ваши персонажи: Дайте волю фантазии — создавайте и обучайте AI-персонажей с любым характером и историей.

    🚫 Никакой рекламы: Чистый и непрерывный диалог. Только вы и ваши персонажи.

    ♾️ Общение без границ: Забудьте про лимиты сообщений. Общайтесь 24/7, развивайте сюжеты и отношения без остановки.

Откройте все возможности — оформите подписку!
Всего зя 10$ в месяц !"""        

@router.message(F.text == "Subscribe")
async def subscribe_handler(message:Message):
    await message.answer(text = sub_text,reply_markup=kb.subscribe_keyboard)

@router.message(F.text == "Back")
async def back_handler(message:Message):
    pass            
        