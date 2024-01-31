# Freshman Orientation Camp 2024 Bot

This repository contains the source code for the Telegram bot [@FOC24Bot](https://t.me/FOC24Bot).

Made in Python 3.11.5 using the [python-telegram-bot](https://python-telegram-bot.org/) module.

## Table of Contents

1. [Features](#features)
    1. [Commands](#commands)
1. [Compilation](#compilation)
1. [Tasklist](#tasklist)
1. [Notes](#notes)

## Features

The bot currently supports the following features:

### Commands:

> `/start` - Begins the interaction with the user
>
> `/hello` - Replies to the user with a message with the format: *Hello, {username}!*.
>
> `/help` - Replies to the user with a list of commands, their descriptions and arguments (if any).
>
> `/enable` - Sets bot status to active, allows execution of many other commands by users
>
> `/disable` - Sets bot status to inactive, stops execution of many commands by users

## Compilation

## Tasklist

- [x] Create script to start the bot with the necessary configurations.
- [ ] Implement logging module
- [x] Create database and an interface for managing the database.
- [x] Add basic commands to the bot
- [ ] Containerize the code to prepare for cloud hosting