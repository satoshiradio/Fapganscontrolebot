# Fapganscontrolebot
A telegram bot which checks messages for fabulous geese. 


# Development instructions

## Getting this project up and running 

Clone this project and open its folder in a Terminal. 

Install the required libraries:
```
python3 -m pip install -r requirements.txt
```

Open the folder of this project in your favorite IDE (in PyCharm opening the root folder of this project is sufficient).

Create a local configuration file:
```
cp config.example.py config.py
```

## Register a bot for local testing

To do this, send the [BotFather](https://t.me/botfather) a `/newbot` command and follow the instructions. 
When you finished the registration your will receive a token to access the HTTP API. Copy this token to the `TOKEN` field under `BotConfig` in `config.py`

That's it!  
Now run `main.py` with either the command `python3 ./main.py` or by clicking in your IDE.
