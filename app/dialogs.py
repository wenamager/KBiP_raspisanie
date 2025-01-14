from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Row, Column
from aiogram.types import Message, User
from aiogram_dialog.widgets.input import TextInput, ManagedTextInput
from aiogram_dialog.widgets.media import StaticMedia
from aiogram.types import ContentType, CallbackQuery, Message
from aiogram import Bot
from app import states
from app import getters
import asyncio
from main import bot
import random
import config

bot = bot

start_message = '''
👋 Привет <b>{username}</b>!

🏆 Этот бот сделан для просмотра расписания КБиП
'''


async def start_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.MenuSG.menu)

async def to_monday(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.MondaySG.rasp)

async def to_tuesday(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.TuesdaySG.rasp)

async def to_wensday(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.WednesdaySG.rasp)

async def to_thursday(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.ThursdaySG.rasp)

async def to_friday(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.FridaySG.rasp)

async def to_help(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.HelpSG.help)

async def to_saturday(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.SaturdaySG.rasp)

async def to_help(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=states.HelpSG.help)

# async def to_profile(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.start(state=states.ProfileSG.profile)

# async def to_bet(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.start(state=states.StavkaSG.home)

# async def to_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.start(state=states.MenuSG.menu)


# async def to_gift(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.start(state=states.GiftSG.gift)

# async def to_home(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.start(state = states.StavkaSG.home)

# async def to_help(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.start(state=states.HelpSG.help)

# async def to_promo(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.start(state=states.PromoSG.promo)

# async def to_adminka(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     if str(callback.from_user.id) != str(config.ADMIN_ID):
#         print(callback.from_user.id)
#         await callback.message.answer("<b>Вы не админ!</b>")
#         return
#     await dialog_manager.start(state=states.AdminkaSG.adminka)


# async def to_subscribe(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.start(state=states.SubscribeSG.subscribe)

# async def to_instruction(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.start(state=states.InstructionSG.instruction)

# async def go_back(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.back()

# async def go_next(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     await dialog_manager.next()


# async def add_balance_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str):
#     amount = float(text)
#     invoice = await cryptopay.create_invoice(amount, message.from_user.id)
#     asyncio.create_task(cryptopay.check_payment(bot, message.from_user.id, invoice['invoice_id'], amount))
#     await message.answer(f"Оплатите счет: {invoice['url']}")
#     await dialog_manager.start(state=states.BalanceSG.pull_balance)

# async def gift_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str):
#     unicode = message.text.split(' ')[0]
#     value = message.text.split(' ')[1]
#     await requests.add_unicode(unicode, int(value))
#     await message.answer("<b>Промокод успешно добавлен!</b>")

    
# promocodes_1 = ['xYzQpRt', 'aBcDrLM', 'jKlMnOp', 'qRsTuVw', 'zXyAbCd', 'pQrStUv', 'mNoPqRs', 'eFgHiJk', 'tUvWxYz', 'aBcDsKl']
# promocodes_3 = ['kLmNoPq', 'rStUvWx', 'xYzAbCd', 'jKlMKTy', 'pQrQoBa', 'eFgTcHk', 'tUvFgKla', 'aBcDaSm', 'mNoGkLw', 'qRsTDfg']
# promocodes_5 = ['zXyAbCd', 'kLmGep', 'rStUQdh', 'xYzMNt', 'jKlMGnM', 'pQrQeTa', 'eFgMeHT', 'tUvQjLaS', 'aBcKoP', 'mNoPbWk']
# async def check_promo_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str):
#     promocode = await requests.get_unicode(message.text)
#     if not promocode:
#         await message.answer("Такого промокода нет!")
#         await dialog_manager.start(state=states.MenuSG.menu)
#         return
#     else:
#         is_activated = await requests.check_promocode(message.from_user.id, message.text)
#         if is_activated:
#             await message.answer("Вы уже ввели данный промокод!")
#         else:
#             await requests.add_promocode(message.from_user.id, message.text)
#             await requests.add_subscribe(message.from_user.id, promocode)
#             await message.answer(f"<b>Вы получили {promocode} бесплатных игр!</b>")
#             await dialog_manager.start(state=states.MenuSG.menu)
    # if text in promocodes_1:
    #     is_activated = await requests.check_promocode(message.from_user.id, message.text)
    #     if is_activated:
    #         await message.answer("Вы уже ввели данный промокод!")
    #         await dialog_manager.start(state=states.MenuSG.menu)
    #         return
    #     await requests.add_promocode(message.from_user.id, message.text)
    #     await requests.add_subscribe(message.from_user.id, 1)
    #     await message.answer("<b>Вы получили 1 бесплатную игру!</b>")
    # elif text in promocodes_3:
    #     is_activated = await requests.check_promocode(message.from_user.id, message.text)
    #     if is_activated:
    #         await message.answer("Вы уже ввели данный промокод!")
    #         await dialog_manager.start(state=states.MenuSG.menu)
    #         return
    #     await requests.add_promocode(message.from_user.id, message.text)
    #     await requests.add_subscribe(message.from_user.id, 3)
    #     await message.answer("<b>Вы получили 3 бесплатных игр!</b>")
    # elif text in promocodes_5:
    #     is_activated = await requests.check_promocode(message.from_user.id, message.text)
    #     if is_activated:
    #         await message.answer("Вы уже ввели данный промокод!")
    #         await dialog_manager.start(state=states.MenuSG.menu)
    #         return
    #     await requests.add_promocode(message.from_user.id, message.text)
    #     await requests.add_subscribe(message.from_user.id, 5)
    #     await message.answer("<b>Вы получили 5 бесплатных игр!</b>")
    # else:
    #     await message.answer('Такого промокода нет!.')
    # await dialog_manager.start(state=states.MenuSG.menu)

# async def subscribe1_handler(callback: CallbackQuery, widget: ManagedTextInput, dialog_manager: DialogManager):
#     user_balance = await requests.check_balance(callback.from_user.id)
#     if user_balance >= 25:
#         await requests.add_subscribe(callback.from_user.id, 1)
#         await requests.add_balance(callback.from_user.id, -25)
#         await callback.message.answer("Вы успешно приобрели подписку!")
#     else:
#         await callback.message.answer("Недостаточно средств на балансе!")
#     await dialog_manager.start(state=states.SubscribeSG.subscribe)

# async def subscribe3_handler(callback: CallbackQuery, widget: ManagedTextInput, dialog_manager: DialogManager):
#     user_balance = await requests.check_balance(callback.from_user.id)
#     if user_balance >= 50:
#         await requests.add_subscribe(callback.from_user.id, 3)
#         await requests.add_balance(callback.from_user.id, -50)
#         await callback.message.answer("Вы успешно приобрели подписку!")
#     else:
#         await callback.message.answer("Недостаточно средств на балансе!")
#     await dialog_manager.start(state=states.SubscribeSG.subscribe)

# async def subscribe5_handler(callback: CallbackQuery, widget: ManagedTextInput, dialog_manager: DialogManager):
#     user_balance = await requests.check_balance(callback.from_user.id)
#     if user_balance >= 100:
#         await requests.add_subscribe(callback.from_user.id, 5)
#         await requests.add_balance(callback.from_user.id, -100)
#         await callback.message.answer("Вы успешно приобрели подписку!")
#     else:
#         await callback.message.answer("Недостаточно средств на балансе!")
#     await dialog_manager.start(state=states.SubscribeSG.subscribe)

# async def stavka_handler(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     subscribe = await requests.check_subscribe(callback.from_user.id)
#     if subscribe <= 0:
#         await callback.message.answer("<b>У вас нету активной подписки!</b>")
#         await dialog_manager.start(states.StavkaSG.home)
#     else:
#         await requests.remove_subscribe(callback.from_user.id, 1)
#         stavka_id = button.widget_id  # Извлекаем ID ставки из ID кнопки
#         await requests.set_stavka(callback.from_user.id, stavka_id)
#         await dialog_manager.start(states.ShowStavkaSG.show_stavka)

start_dialog = Dialog(
    Window(
        Format(start_message),
        Button(
            Const("Начать!"), 
            id='start_menu',
            on_click=start_menu
            ),
        state=states.StartSG.start,
    ),
    getter=getters.user_getter
)   


menu_dialog = Dialog(
    Window(
        Const('Выберите день недели:'),
        Column(
            Button(Const('Понедельник'), id='monday', on_click=to_monday),
            Button(Const('Вторник'), id='tuesday', on_click=to_tuesday),
            Button(Const('Среда'), id='wensday', on_click=to_wensday),
            Button(Const('Четверг'), id='thursday', on_click=to_thursday),
            Button(Const('Пятница'), id='friday', on_click=to_friday),
            Button(Const('Суббота'), id='saturday', on_click=to_saturday),
        ),
        Button(Const('📨 Техническая поддержка'), id='help', on_click = to_help),
        state=states.MenuSG.menu,
    ),
)  

monday_dialog = Dialog(
    Window(
        Const('Расписание на понедельник:\n'),
        Format("{main_pairs}"),
        Button(Const('◀️ Назад'), id='back', on_click=start_menu),
        state=states.MondaySG.rasp,
        getter=getters.monday
    ),
)  

tuesday_dialog = Dialog(
    Window(
        Const('Расписание на вторник:\n'),
        Format("{main_pairs}"),
        Button(Const('◀️ Назад'), id='back', on_click=start_menu),
        state=states.TuesdaySG.rasp,
        getter=getters.tuesday
    ),
)  

wednesday_dialog = Dialog(
    Window(
        Const('Расписание на среду:\n'),
        Format("{main_pairs}"),
        Button(Const('◀️ Назад'), id='back', on_click=start_menu),
        state=states.WednesdaySG.rasp,
        getter=getters.wednesay
    ),
)  

thursday_dialog = Dialog(
    Window(
        Const('Расписание на четверг:\n'),
        Format("{main_pairs}"),
        Button(Const('◀️ Назад'), id='back', on_click=start_menu),
        state=states.ThursdaySG.rasp,
        getter=getters.thursday
    ),
)  

friday_dialog = Dialog(
    Window(
        Const('Расписание на пятницу:\n'),
        Format("{main_pairs}"),
        Button(Const('◀️ Назад'), id='back', on_click=start_menu),
        state=states.FridaySG.rasp,
        getter=getters.friday
    ),
)  

saturday_dialog = Dialog(
    Window(
        Const('Расписание на субботу:\n'),
        Format("{main_pairs}"),
        Button(Const('◀️ Назад'), id='back', on_click=start_menu),
        state=states.SaturdaySG.rasp,
        getter=getters.saturday
    ),
)  


# profile_dialog = Dialog(
#     Window(
#         StaticMedia(path='profile.jpg', type=ContentType.PHOTO),
#         Format(text='👤 <b>{username}</b>'),
#         Format(text='⭐️ ID: <b>{id}</b>'),
#         Format(text='🎟 Подписка: <b>{subscribe}</b> игр'),
#         Format(text='💳 Баланс: <b>{balance}$</b>'),
#         Button(Const('💵 Пополнить баланс'), id='add_balance', on_click = go_next),
#         Button(Const('🎟 Оформить подписку'), id='subscribe', on_click = to_subscribe),  
#         Button(Const('📨 Техническая поддержка'), id='help', on_click = to_help),
#         Button(Const('⚙️ Админ-панель'), id='admin', on_click = to_adminka),
#         Button(Const('◀️ Назад'), id='back', on_click=to_menu),
#         getter=getters.user_getter,
#         state=states.ProfileSG.profile,
#     ),
#     Window(
#         Const("Введите сумму пополения: "),
#         TextInput(
#             id = 'sum_input',
#             on_success=add_balance_handler,
#         ),
#         state=states.ProfileSG.balance,
#     ),
# ) 


# pull_balance_dialog = Dialog(
#     Window(
#         Const(text='Вернуться: '),
#         Button(Const('◀️ Назад'),id='back',on_click=to_profile,),
#         TextInput(
#             id = 'sum_input',
#             on_success=add_balance_handler,
#         ),
#         state=states.BalanceSG.pull_balance,
#     ),
# ) 


help_dialog = Dialog (
     Window(
         Const(text='По всем вопросам: @wenaxera'),
         Button(Const('◀️ Назад'),id='back',on_click=start_menu),
         state=states.HelpSG.help
     ),
 )


# instruction_dialog = Dialog (
#     Window(
#         Const(text='Инструкция:\nhttps://telegra.ph/Instrukciya-kak-polzovatsya-football-predict-bot-09-21'),
#         Button(Const('◀️ Назад'),id='back',on_click=to_menu),
#         state=states.InstructionSG.instruction
#     ),
# )

# promo_dialog = Dialog (
#     Window(
#         Const(text='Введите промокод: '),
#         Button(Const('◀️ Назад'),id='back',on_click=to_menu,),
#         TextInput(
#             id = 'promo_input',
#             on_success=check_promo_handler,
#         ),
#         state=states.PromoSG.promo,
#     ),
# )

# to_subscribe_dialog = Dialog(
#     Window(
#         Const(text='Выберите нужный тариф: '),
#         Button(Format('25$ за одну игру'), id='subscribe_1', on_click=subscribe1_handler),
#         Button(Format('50$ за три игры'), id='subscribe_3', on_click=subscribe3_handler),
#         Button(Format('100$ за пять игр'), id='subscribe_5', on_click=subscribe5_handler),
#         Button(Const('◀️ Назад'),id='back',on_click=to_profile),
#         state = states.SubscribeSG.subscribe
#     )
# )


# def create_stavka_buttons(stavki:dict):
#     print(stavki)
#     buttons = []
#     i = 0
#     for stavka in stavki['stavki']:
#         i += 1
#         buttons.append(
#             Button(
#                 Format(f"{stavka['detail']}"),  # Динамическое название кнопки
#                 id=f"{stavka['id']}",  # Уникальный ID кнопки для каждой ставки
#                 on_click=stavka_handler  # Хендлер, который будет обрабатывать нажатие
#             )
#         )
#     return buttons


# home_dialog = Dialog(
#     Window(
#         StaticMedia(path='bet.jpg', type=ContentType.PHOTO),
#         Column(
#             # Используем данные, полученные через getter для создания кнопок
#             *create_stavka_buttons(getters.stavki_getter())
#         ),
#         Button(Const('◀️ Назад'),id='back',on_click=to_menu),
#         state=states.StavkaSG.home
#     )
# )


# async def stavka_getter_by_id(dialog_manager: DialogManager, event_from_user: User,**kwargs):
#         match_id = await requests.get_stavka(event_from_user.id)
#         matches = getters.stavki_getter()['stavki']
#         result = {

#         }
#         chances = [
#             20,30,40,60,70,80,90
#         ]
#         for match in matches:
#             if match['id'] == match_id:
#                 result['match'] = match['detail']
#                 comand_1 = match['detail'].split('-')[0]
#                 comand_2 = match['detail'].split('-')[1]
#                 if len(comand_1) > len(comand_2):
#                     comand_1 = comand_1.split(' ')
#                     print(f"SPLITTED : {comand_1}")
#                     if len(comand_1[len(comand_1)-1]) <= 1:
#                         comand_1 = comand_1[len(comand_1)-2]
#                     else:
#                         comand_1 = comand_1[len(comand_1)-1]
#                 else:
#                     comand_2 = comand_2.split()
#                     print(f"SPLITTED_2 : {comand_2}")
#                     comand_2 = comand_2[0]
#                 result['comand_1'] = comand_1           
#                 result['comand_2'] = comand_2
#                 chance1 = chances[random.randint(0,6)]
#                 chance2 = 100 - chance1
#                 result['chance1'] = chance1
#                 result['chance2'] = chance2

#                 if chance1 > chance2:
#                     result['final'] = f'Мы рекомендуем ставить на <b>{comand_1}</b>!'
#                 else:
#                     result['final'] = f'Мы рекомендуем ставить на <b>{comand_2}</b>!'
#         return result

        

# show_stavka_dialog = Dialog(
#     Window(
#         Format('⚽️ Матч: <b>{match}</b>\n'),
#         Format('💫Команда 1: <b>{comand_1}</b>\n🔎Шанс победы: <b>{chance1}%</b>\n'),                                        
#         Format('💫Команда 2: <b>{comand_2}</b>\n🔎Шанс победы: <b>{chance2}%</b>\n'),
#         Format('<b>{final}</b>'),
#         Button(Const('◀️ Назад'),id='back',on_click=to_bet),
#         state=states.ShowStavkaSG.show_stavka,
#         getter=stavka_getter_by_id
#     )
# )


# adminka_dialog = Dialog(
#     Window(
#         Format('Пользователей в боте: <b>{users}</b>'),                                  
#         Button(Const('🎁 Добавить промокод'),id='gift',on_click=to_gift),
#         # Button(Const('Рассылка'),id='gift',on_click=to_gift),
#         Button(Const('◀️ Назад'),id='back',on_click=to_profile), 
#         state=states.AdminkaSG.adminka,
#         getter=getters.get_users
#     )
# )

# gift_dialog = Dialog (
#     Window(
#         Const(text='Введите промокод и количество бонусных игр: \nПример: promocode123 5'),
#         Button(Const('◀️ Назад'),id='back',on_click=to_adminka),
#         TextInput(
#             id = 'promo_input',
#             on_success=gift_handler,
#         ),
#         state=states.GiftSG.gift,
#     ),
# )