![Function_](https://user-images.githubusercontent.com/87334808/131955642-16f62d1b-2dfc-4cdb-9b89-278679c91616.png)
# Function
An open-source Discord bot with everyday functionality.

Constantly having to search for commonly used pieces of information in different places can be frustrating, so make it easy and do everything in your own Discord server!
- Add the bot to your server [here](https://discord.com/api/oauth2/authorize?client_id=864234598191202335&permissions=259846043712&scope=bot%20applications.commands).
- Check out the code in action on Replit [here](https://replit.com/@YashT11/FunctionDiscordBot#main.py) (always running!). 
- [![Run on Repl.it](https://repl.it/badge/github/YashTelang/Function)](https://repl.it/github/YashTelang/Function) Clone and run the code yourself! Run command: *python main.py*.

## Commands

###### Greetings
- `-hello`: Says hello.
- `-bye`: Says bye.
- `-good morning`: Says good morning.
- `-good afternoon`: Says good afternoon.
- `-good evening`: Says good evening.

###### Time
- `-settimezone [timezone]`: Sets the timezone to **[timezone]**. A list of timezones can be found [here](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568).
- `-time`: After setting a timezone, gives the time.

###### Weather
- `-setlocation [location]`: Sets the location to **[location]**, which can be any city in the world. 
- `-weather`: Gives the current temperature in °F, humidity, pressure, and report.
- `-temperature`: Gives the current temperature in °F.
- `-humidity`: Gives the current humidity in %.
- `-pressure`: Gives the current pressure in atm.
- `-report`: Gives the current weather report.

###### News
- `-news source [source]`: Gives recent news from **[source]**.
- `-news about [topic]`: Gives recent news about **[topic]**.

###### Stocks
- `-stock [ticker]`: Gives history of **[ticker]** from the past 5 days.

## APIs Used
- [discord.py](https://discordpy.readthedocs.io/en/stable/api.html)
- [pytz](http://pytz.sourceforge.net/)
- [newsapi-python](https://github.com/mattlisiv/newsapi-python)
- [yfinance](https://github.com/ranaroussi/yfinance)
- [Flask](https://palletsprojects.com/p/flask/)

## Contact
Feel free to give suggestions or contact me at ytelang11@gmail.com!
