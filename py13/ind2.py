#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def menu(food, **meal):
    print(f"Food: {food}")
    for meal, name in meal.items():
        print(f"{name}")


if __name__ == '__main__':
    menu(
        "Прием пищи",
        breakfast="Блинчики с творогом",
        dinner="Суп с грибами",
        supper="Рыба с овощами"
    )
    menu(
        "Прием пищи",
        breakfast="Овсяная каша"
    )
