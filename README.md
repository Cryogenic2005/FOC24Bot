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

#### General purpose commands

> `/start` - Begins the interaction with the user
>
> `/hello` - Replies to the user with a message with the format: *Hello, {username}!*.
>
> `/help` - Replies to the user with a list of commands, their descriptions and arguments (if any).
>
> `/register` - Registers user in bot's database

#### Bot activity management commands

> `/enable` - Sets bot status to active, allows execution of many other commands by users
>
> `/disable` - Sets bot status to inactive, stops execution of many commands by users

#### Permission management commands

<u>Note:</u> Permission levels: User < Moderator < Admin < Owner

> `/check_perms @[username]`: Check the specified user's permission level
>
> `/grant @[username] [permission]`: Grant the specified user with the specified permission level. 
> 
> `/demote @[username] [permission]`: Demote the specified user to the specified permission level.

#### Game commands

> `/group [group-name]`: Get all images in the specified group name.

## Compilation

### 1. Python Version

First, ensure that you have the latest version of Python installed. (*This project was made with Python 3.11.5*)

### 2. Packages (*python-telegram-bot 20.7*) 

Second, check if you have installed the Python package *python-telegram-bot*. Also check if the package version is 20.7. Run the following command on your command line:

`pip show python-telegram-bot`

If not installed, run the following command:

`pip install python-telegram-bot`

### 3. Bot API Key

Follow the template and enter your bot's API key.

You can get it by following the instructions on the official [Telegram Bot API documentation](https://core.telegram.org/bots/features#botfather)

### 4. Running the bot

Change to your working directory and clone the repository to a folder with this command:

`git clone https://github.com/Cryogenic2005/FOC24Bot/`

Run the bot with the following command

`python main.py`

## Tasklist

- [x] Create script to start the bot with the necessary configurations.
- [ ] Implement logging module
- [x] Create database and an interface for managing the database.
- [x] Add basic commands to the bot
- [ ] Containerize the code to prepare for cloud hosting