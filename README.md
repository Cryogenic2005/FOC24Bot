# Freshman Orientation Camp 2024 Bot

This repository contains the source code for the Telegram bot [@FOC24Bot](https://t.me/FOC24Bot).

Made in Python 3.11.5 using the [python-telegram-bot](https://python-telegram-bot.org/) module.

---

## Table of Contents

1. [Features](#features)
    1. [Commands](#commands)
1. [Compilation](#compilation)
1. [Tasklist](#tasklist)
1. [Notes](#notes)

---

## Features

The bot currently supports the following features:


### Commands:

> `/start` - Begins the interaction with the user
>
> `/hello` - Replies to the user with a message with the format: *Hello, {username}!*.
>
> `/help` - Replies to the user with a list of commands, their descriptions and arguments (if any).
>
> `/passOn [Optional:message]` - Replies with the previous message associated with the last execution of the command (the bot will inform the user if no message was saved previously). Then, save the message passed to this command (if any) for the next execution of the command.

---

## Compilation

---

## Tasklist

- [ ] Create script to start the bot with the necessary configurations.
- [ ] Implement logging module
- [ ] Create database and an interface for managing the database.
- [ ] Add basic commands to the bot
- [ ] Containerize the code to prepare for cloud hosting

---

## Notes

I am making this bot for 2 main purposes:

- Practice using the python-telegram-bot Python module to code a bot.
- Practice maintaining a clean codebase.

If all goes well, I will also:

- Try migrating the bot to the cloud.

- Run this bot for the Freshman Orientation Camp 2024 for event management purposes.