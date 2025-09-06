import time
import asyncio
from plyer import notification
# plyer does not work on MacOS
import pync  # Library for terminal notification
from desktop_notifier import DesktopNotifier, Urgency, Button, ReplyField, DEFAULT_SOUND


async def start_notification_app():

    while True:

        # notification.notify(title="Please drink some water",
        #                     message="You need to drink some water.... Its been an hour")

        # pync.notify("Please Drink Water",
        #            title="!!!REMINDER!!!", sound="Horn")

        notifier = DesktopNotifier(app_name="Reminder App")
        await notifier.send(
            title="Please Drink Water",
            message="Hey Asim, Dont forget to drink some water",
            urgency=Urgency.Critical,
            on_dispatched=lambda: print("Notification showing"),
            sound=DEFAULT_SOUND,
        )
        time.sleep(10)


if __name__ == "__main__":
    asyncio.run(start_notification_app())
   # start_notification_app()
