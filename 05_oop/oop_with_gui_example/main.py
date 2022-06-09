import toga
from toga.style.pack import Pack, COLUMN, ROW, CENTER
from game import Game
from asyncio import sleep, create_task


def build(app):

    game = None

    def update_monster():
        pb_monster.value, label_monster.text  = game.get_monster_status()

    def update_hero():
        pb_hero.value, label_hero.text  = game.get_hero_status()

    def button_new_game_press(widget):
        nonlocal game
        game = Game()
        mt_input_info.clear()
        selection_hero.items = game.get_heroes_list()
        update_hero()
        update_monster()

    def button_monster_press(widget):
        game.create_monster()
        update_monster()

    def selection_hero_select(widget):
        game.select_hero_by_class_name(widget.value)
        update_hero()

    async def play():
        i = 0
        while game.game_continues():
            mt_input_info.value += game.hero_move() if i % 2 else game.monster_move()
            update_monster()
            update_hero()
            await sleep(1)
            i += 1
        button_start.label = 'Start'
        nonlocal in_progress
        in_progress = False

    task = None
    in_progress = False

    def button_start_press(widget):
        nonlocal task, in_progress
        if in_progress:
            task.cancel()
            in_progress = False
            widget.label = 'Start'
        else:
            task = create_task(play())
            in_progress = True
            widget.label = 'Stop'


    style_flex = Pack(flex=1, padding=10)
    style_row = Pack(direction=ROW, flex=1, padding=10)
    style_col = Pack(direction=COLUMN, flex=1, padding=10)
    style_pb = Pack(direction=COLUMN, width=250, height=20, padding=10)
    style_more_pad = Pack(text_align=CENTER, flex=1, padding=20)

    button_new_game = toga.Button('New Game', style=style_more_pad, on_press=button_new_game_press)

    label_select = toga.Label('Select hero:', style=style_flex)
    selection_hero = toga.Selection(style=style_flex, on_select=selection_hero_select)

    pb_hero = toga.ProgressBar(max=100, running=False, value=0, style=style_col)
    label_hero = toga.Label('hero', style=style_more_pad)

    button_monster = toga.Button('Create Monster', style=style_flex, on_press=button_monster_press)
    pb_monster = toga.ProgressBar(max=100, running=False, value=0, style=style_col)
    label_monster = toga.Label('monster', style=style_more_pad)

    button_start = toga.Button("Start", style=style_more_pad, on_press=button_start_press)
    mt_input_info = toga.MultilineTextInput("", style=style_more_pad, readonly=True)


    box_hero_row1 = toga.Box(style=style_row, children=[label_select, selection_hero])
    box_hero_row2 = toga.Box(style=style_row, children=[pb_hero])
    box_hero = toga.Box(style=style_col, children=[box_hero_row1, box_hero_row2, label_hero])

    box_monster_row1 = toga.Box(style=style_row, children=[button_monster])
    box_monster_row2 = toga.Box(style=style_row, children=[pb_monster])
    box_monster = toga.Box(style=style_col, children=[box_monster_row1, box_monster_row2, label_monster])

    box_hero_and_monster = toga.Box(style=style_row, children=[box_hero, box_monster])

    return toga.Box(children=[button_new_game, box_hero_and_monster, button_start, mt_input_info], style=style_col)


def main():
    return toga.App('Heroes and Monsters', 'org.surgu.asoiu.heroesandmonsters', startup=build)


if __name__ == '__main__':
    main().main_loop()
