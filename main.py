import os

from discord.ext.commands import Bot, when_mentioned
from discord import Thread


class MyBot(Bot):
    async def on_thread_update(self, before: Thread, after: Thread):
        if before.archived is False or after.archived is True:
            return

        channel = await after.guild.fetch_channel(after.parent_id)
        await channel.send(f"unarchived thread -> {after.mention}")


def main(token: str) -> None:
    bot = MyBot(when_mentioned)
    bot.run(token)


if __name__ == "__main__":
    token = os.getenv("DISCORD_BOT_TOKEN")
    main(token)
