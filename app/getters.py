from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram.types import Message, User
import parser

main_times = [
        '8:00 - 8:45',
        '8:55 - 9:40',
        '9:50 - 10:35',
        '10:45 - 11:30',
        '12:00 - 12:45',
        '12:55 - 13:40',
        '14:00 - 14:45',
        '14:55 - 15:40',
        '15:50 - 16:35',
        '16:45 - 17:30',
        '17:40 - 18:25',
        '18:35 - 19:20',
        '19:30 - 20:15'
    ]

thursday_times = [
        '8:00 - 8:45',
        '8:55 - 9:40',
        '9:50 - 10:35',
        '10:45 - 11:30',
        '12:00 - 12:45',
        '12:55 - 13:40',
        '14:40 - 15:25',
        '15:35 - 16:20',
        '16:30 - 17:15',
        '17:25 - 18:10',
        '18:20 - 19:05',
        '19:15 - 20:00',
        '20:10 - 20:55'
    ]


async def user_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    return {
        'username': event_from_user.username,
        'id': event_from_user.id,
        }

async def monday(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    main_pairs = parser.start()
    pairs = main_pairs[0]
    message = ''
    i = 1
    for pare in pairs: 
        if pare['subject_name'] == '':
            i += 1
            continue
        message += f'-----------<b>{i}</b>-----------\n'
        message += '<b> ' + pare['subject_name'] + '</b>' + '\n'
        message += f'<b>{main_times}</b>\n'
        # message += '<b>   ' + f"{pare['teacher_1']}\n" + '</b>'
        message += f" Кабинет: <b>{pare['place']}</b>\n"
        i += 1
    return {
        'main_pairs': message
    }   

async def tuesday(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    main_pairs = parser.start()
    pairs = main_pairs[1]
    message = ''
    i = 1
    for pare in pairs: 
        if pare['subject_name'] == '':
            i += 1
            continue
        message += f'-----------<b>{i}</b>-----------\n'
        message += '<b> ' + pare['subject_name'] + '</b>' + '\n'
        message += f'<b>{main_times}</b>\n'
        # message += '<b>   ' + f"{pare['teacher_1']}\n" + '</b>'
        message += f" Кабинет: <b>{pare['place']}</b>\n"
        i += 1
    return {
        'main_pairs': message
    }     

async def wednesay(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    main_pairs = parser.start()
    pairs = main_pairs[2]
    message = ''
    i = 1
    for pare in pairs: 
        if pare['subject_name'] == '':
            i += 1
            continue
        message += f'-----------<b>{i}</b>-----------\n'
        message += '<b> ' + pare['subject_name'] + '</b>' + '\n'
        message += f'<b>{main_times}</b>\n'
        # message += '<b>   ' + f"{pare['teacher_1']}\n" + '</b>'
        message += f" Кабинет: <b>{pare['place']}</b>\n"
        i += 1
    return {
        'main_pairs': message
    }    

async def thursday(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    main_pairs = parser.start()
    pairs = main_pairs[3]
    message = ''
    i = 1
    for pare in pairs: 
        if pare['subject_name'] == '':
            i += 1
            continue
        message += f'-----------<b>{i}</b>-----------\n'
        message += '<b> ' + pare['subject_name'] + '</b>' + '\n'
        message += f'<b>{thursday_times}</b>\n'
        # message += '<b>   ' + f"{pare['teacher_1']}\n" + '</b>'
        message += f" Кабинет: <b>{pare['place']}</b>\n"
        i += 1
    return {
        'main_pairs': message
    }   

async def friday(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    main_pairs = parser.start()
    pairs = main_pairs[4]
    message = ''
    i = 1
    for pare in pairs: 
        if pare['subject_name'] == '':
            i += 1
            continue
        message += f'-----------<b>{i}</b>-----------\n'
        message += '<b> ' + pare['subject_name'] + '</b>' + '\n'
        message += f'<b>{main_times}</b>\n'
        # message += '<b>   ' + f"{pare['teacher_1']}\n" + '</b>'
        message += f" Кабинет: <b>{pare['place']}</b>\n"
        i += 1
    return {
        'main_pairs': message
    }   

async def saturday(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    times = [
        '8:00 - 8:45',
        '8:55 - 9:40',
        '9:50 - 10:35',
        '10:45 - 11:30',
        '11:40 - 12:25',
        '12:35 - 13:20',
        '13:40 - 14:25',
        '14:35 - 15:20',
        '15:30 - 16:15',
        '16:25 - 17:10',
        '17:20 - 18:05',
        '18:15 - 19:00',
        '19:10 - 19:55'
    ]
    main_pairs = parser.start()
    pairs = main_pairs[5]
    message = ''
    i = 1
    for pare in pairs: 
        if pare['subject_name'] == '':
            i += 1
            continue
        time = times[i-1]
        message += f'-----------<b>{i}</b>-----------\n'
        message += f'<b>{time}</b>\n'
        message += '<b> ' + pare['subject_name'] + '</b>' + '\n'
        # message += '<b>   ' + f"{pare['teacher_1']}\n" + '</b>'
        message += f" Кабинет: <b>{pare['place']}</b>\n"
        i += 1
    return {
        'main_pairs': message
    }   