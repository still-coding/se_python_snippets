#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flet as ft


def main(page: ft.Page):
    page.title = "Heroes and Monsters"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1000
    
    lv_info = ft.ListView(expand=True, spacing=0, height=300, auto_scroll=True)
    pb_hero = ft.ProgressBar(width=400, color=ft.colors.RED, value=0)
    pb_monster = ft.ProgressBar(width=400, color=ft.colors.RED, value=0)
    txt_hero = ft.Text("hero", text_align=ft.TextAlign.CENTER, width=400)
    txt_monster = ft.Text("monster", text_align=ft.TextAlign.CENTER, width=400)

    def dd_heroes_select(e):
        pass

    def btn_new_game_click(e):
        pass

    def btn_create_monster_click(e):
        pass

    def btn_start_click(e):
        pass

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
