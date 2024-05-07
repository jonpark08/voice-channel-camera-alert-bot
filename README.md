# Introduction

This Discord bot will notify the entire server when someone uses the camera/screen streaming feature on a specific voice channel.

# Configuration

Component without the ```#``` symbol must have a value entered. If the component has ```#``` in front of it, this is an optional function.

## Token ID

Server Token ID is required for this part. If you don't have one, generate one using this tutorial.

[Creating a Discord Bot & Getting a Token - Reactiflux](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)

```bash
[DEFAULT]
token: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Bot Token that has a length of 59 must be provided.
```

## Channel Information

```bash
[CHANNEL ID]
voice: XXXXXXXXXXXXXXXXXX
# The channel that will be monitored for any streaming event occured.
# Voice Channel ID that has a length of 18 digits must be provided.

alert: XXXXXXXXXXXXXXXXXXX
# Sends alert messages to specific chat channel.
# Chat Channel ID that has a length of 18 digits must be provided. Some has 19 digits.

#log:
# Optional Feature.
# Sends log messages to specific chat channel. Same result will be recorded on bot.log file.
# Chat Channel ID that has a length of 18 digits must be provided. Some has 19 digits.
```

## Message Timeout
```bash
[Time]
delete_timeout: XX
# Duration for how long the alert message will last after the streaming ends.
# Unit is in Seconds.
```