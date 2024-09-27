from aiogram.fsm.state import State, StatesGroup
from aiogram import Bot

class StartSG(StatesGroup):
    start = State()

class MenuSG(StatesGroup):
    menu = State()

class MondaySG(StatesGroup):
    rasp = State()

class TuesdaySG(StatesGroup):
    rasp = State()

class WednesdaySG(StatesGroup):
    rasp = State()

class ThursdaySG(StatesGroup):
    rasp = State()

class FridaySG(StatesGroup):
    rasp = State()

class SaturdaySG(StatesGroup):
    rasp = State()

class HelpSG(StatesGroup):
    help = State()


class HelpSG(StatesGroup):
    help = State()