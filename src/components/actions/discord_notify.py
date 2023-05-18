from components.actions.base.action import Action
import logging
from discord_webhook import DiscordWebhook, DiscordEmbed

# lo lascio qui per ora
DISCORD_WEBHOOKS = [
    'https://discord.com/api/webhooks/1107723354850471967/WLmfV_8pK-AcG7c9So3tmArVmQevF4nGc2ylhb15XPTvflyWXGCILfjumLU-fZzwwQIw'
]

class DiscordNotify(Action):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def send_to_discord(self, url, data):
        discord_webhook = DiscordWebhook(url=url)
        embed = DiscordEmbed(
            title='Signal', description='Signal received from webhook', color=242424)
        discord_webhook.add_embed(embed)
        response = discord_webhook.execute()

    def run(self, *args, **kwargs):
        super().run(*args, **kwargs)
        self.logger.info(f"{self.name} ---> SendToDiscord action has run!")
        print("dio cane")
        data = self.validate_data()
        """
        foreach discord url in settings:
            send data to discord
        """
        for url in DISCORD_WEBHOOKS:
            self.send_to_discord(url, data)
        print('Data from webhook:', data)
