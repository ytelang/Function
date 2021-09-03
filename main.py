import discord
import os
import pytz
import json
import requests
from datetime import datetime
datetime
from newsapi import NewsApiClient
import yfinance as yf
from keep_alive import keep_alive

#client is Discord
client = discord.Client()

#bot has started
@client.event
async def on_ready():
  print('{0.user}'.format(client) + ' has landed!')

#responses to messages (commands)
@client.event
async def on_message(message):
  if message.author == client.user:
    return

#greetings
  if message.content.startswith('-hello'):
    await message.channel.send('Hi there!')

  if message.content.startswith('-good morning'):
    await message.channel.send('Good morning!')

  if message.content.startswith('-good afternoon'):
    await message.channel.send('Good afternoon!')

  if message.content.startswith('-good evening'):
    await message.channel.send('Good evening!')

  if message.content.startswith('-bye'):
    await message.channel.send('Bye!')

#time   
  if message.content.startswith('-settimezone'):
    location = message.content[13:]
    tz = pytz.timezone(location) 
    global datetime
    datetime = datetime.now(tz)
    await message.channel.send('Time zone set!')
    
  if message.content.startswith('-time'):
    await message.channel.send('The time is: ' + datetime.strftime('%H:%M:%S') + '.')

#weather
  if message.content.startswith('-setlocation'):
    global city
    city = message.content[13:]
    weatherURL = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + os.environ['WeatherAPI']
    response = requests.get(weatherURL)
    if response.status_code == 200:
      data = response.json()
      main = data['main']
      global temperature
      temperature = round(1.8 * (round(main['temp']) - 273) + 32)
      global humidity
      humidity = main['humidity']
      global pressure
      pressure = round(main['pressure']/10)
      global report
      report = data['weather']
      await message.channel.send('Location set!')
    else:
      await message.channel.send('Error!')

  if message.content.startswith('-weather'):
    await message.channel.send('The temperature in ' + city + ' is: ' + str(temperature) + ' °F. Humidity is at ' + str(humidity) + '%, and pressure is at ' + str(pressure) + ' atm. Current report: ' + str(report[0]['description']) + '.')

  if message.content.startswith('-temperature'):
    await message.channel.send('The temperature in ' + city + ' is: ' + str(temperature) + ' °F.')

  if message.content.startswith('-humidity'):
    await message.channel.send('Humidity is at ' + str(humidity) + '%.')

  if message.content.startswith('-pressure'):
    await message.channel.send('Pressure is at ' + str(pressure) + ' kPa.')
    
  if message.content.startswith('-report'):
    await message.channel.send('Current report: ' + str(report[0]['description']) + '.')

#news
  api = NewsApiClient(api_key=os.environ['NewsAPI'])
  if message.content.startswith('-news source'):
    source = message.content[13:]
    await message.channel.send(str(api.get_top_headlines(sources=source))[:2000])

  if message.content.startswith('-news about'):
    search = message.content[11:]
    await message.channel.send(str(api.get_everything(q=search))[:2000])

#stocks
  if message.content.startswith('-stock'):
    stock = yf.Ticker(message.content[7:])
    await message.channel.send(stock.history(period = '5d'))

keep_alive()
client.run(os.environ['TOKEN'])