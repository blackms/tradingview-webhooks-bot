from components.actions import Action
import logging


class SendToDiscord(Action):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def run(self, *args, **kwargs):
        super().run(*args, **kwargs)  # this is required
        self.logger.info(f"{self.name} ---> SendToDiscord action has run!")
        data = self.validate_data()
        print('Data from webhook:', data)
