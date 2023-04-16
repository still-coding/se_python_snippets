#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flet as ft
from game import Game
from time import sleep


def main(page: ft.Page):
    page.title = "Heroes and Monsters"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1000

    game = None
    
    lv_info = ft.ListView(expand=True, spacing=0, height=300, auto_scroll=True)
    pb_hero = ft.ProgressBar(width=400, color=ft.colors.RED, value=0)
    pb_monster = ft.ProgressBar(width=400, color=ft.colors.RED, value=0)
    txt_hero = ft.Text("hero", text_align=ft.TextAlign.CENTER, width=400)
    txt_monster = ft.Text("monster", text_align=ft.TextAlign.CENTER, width=400)

    def dd_heroes_select(e):
        game.select_hero_by_class_name(dd_heroes.value)
        pb_hero.value, txt_hero.value = game.get_hero_status()
        page.update()


    def btn_new_game_click(e):
        nonlocal game
        game = Game()
        lv_info.controls.clear()
        dd_heroes.options.clear()
        dd_heroes.options = list(map(ft.dropdown.Option, game.get_heroes_list()))
        dd_heroes.value = dd_heroes.options[0].key
        pb_hero.value, txt_hero.value = game.get_hero_status()
        pb_monster.value, txt_monster.value = game.get_monster_status()
        page.update()


    def btn_create_monster_click(e):
        game.create_monster()
        pb_monster.value, txt_monster.value = game.get_monster_status()
        page.update()

    in_progress = False

    def btn_start_click(e):
        nonlocal in_progress
        if in_progress:
            in_progress = False
            btn_start.text = "Start"
            page.update()
            return
        i = 0
        in_progress = True
        btn_start.text = "Stop"
        while in_progress and game.game_continues():
            lv_info.controls.append(
                ft.Text(
                    game.hero_move() if i % 2 else game.monster_move(),
                    text_align=ft.TextAlign.CENTER,
                    width=400,
                )
            )
            pb_hero.value, txt_hero.value = game.get_hero_status()
            pb_monster.value, txt_monster.value = game.get_monster_status()
            page.update()
            sleep(1)
            i += 1

    btn_start = ft.ElevatedButton(text="Start", width=450, on_click=btn_start_click)
    dd_heroes = ft.Dropdown(on_change=dd_heroes_select)

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.ElevatedButton(
                            text="New Game", width=450, on_click=btn_new_game_click
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Row(
                                    [ft.Text("Select hero"), dd_heroes],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                pb_hero,
                                txt_hero,
                            ],
                            spacing=50,
                        ),
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            text="Create Monster",
                                            on_click=btn_create_monster_click,
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    width=400,
                                    height=64,
                                ),
                                pb_monster,
                                txt_monster,
                            ],
                            spacing=50,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [btn_start],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row([lv_info], alignment=ft.MainAxisAlignment.CENTER),
            ],
            spacing=50,
        )
    )


ft.app(target=main)
