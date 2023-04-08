Bitcoin Price Notifications With Python

As we all know, Bitcoin price is a fickle thing. You never really know where it’s going to be at the end of the day. So, instead of constantly checking various sites for the latest updates, let’s make a Python app to do the work for you.

For this, we’re going to use the popular automation website IFTTT. IFTTT (“if this, then that”) is a web service that bridges the gap between different apps and devices.

We’re going to create two IFTTT applets:

One for emergency notification when Bitcoin price falls under a certain threshold; and
another for regular Telegram updates on the Bitcoin price.
Both will be triggered by our Python app which will consume the data from the Coinmarketcap API.

An IFTTT applet is composed of two parts: a trigger and an action.

In our case, the trigger will be a webhook service provided by IFTTT. You can think of webhooks as “user-defined HTTP callbacks” and you can read more about them here.

Our Python app will make an HTTP request to the webhook URL which will trigger an action. Now, this is the fun part—the action could be almost anything you want. IFTTT offers a multitude of actions like sending an email, updating a Google Spreadsheet and even calling your phone.
