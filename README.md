# ChatGPT Auto-Reply Bot for Telegram  

ChatGPT-based bot that automatically responds to incoming messages in Telegram.  
Works via **ProxyAPI** and **Telegram Client API**.  

## Features  
- Automatically replies to all incoming messages  
- Uses **ProxyAPI** for generating responses  
- Works through **Telegram Client API** for seamless messaging  
- Supports natural conversation and contextual replies  
- Can be customized for different reply styles  
- Works 24/7 without manual intervention  

## Installation  

### 1. Clone the repository  
```bash
git clone https://github.com/your-repo/chatgpt-telegram-bot.git
cd chatgpt-telegram-bot
```

### 2. Install dependencies  
Make sure you have **Python 3.8+** installed. Then, install required packages:  
```bash
pip install -r requirements.txt
```

## Getting API Credentials  

### 1. Get Telegram API ID and Hash  
To interact with Telegram, you need to obtain API credentials:  
1. Go to [Telegram's API Development Page](https://my.telegram.org/apps).  
2. Log in with your Telegram account.  
3. Click "Create New Application" and fill in the details.  
4. After submission, you will get:  
   - **API ID**  
   - **API Hash**  

### 2. Generate a Telegram Session String  
To generate a session string, run the script **generate_session.py** located in the repository:

```bash
python generate_session.py
```

Follow the on-screen instructions to log in and retrieve your **session string**.

### 3. Register and Get ProxyAPI Key  
1. Visit [ProxyAPI's website](https://proxyapi.com/) (or another chosen provider).  
2. Sign up and log in to your account.    
3. Retrieve your **ProxyAPI Key** from the dashboard.  

## Running the Bot  
```bash
python bot.py
```

## Usage  
Once the bot is running, it will automatically respond to any incoming messages in Telegram chats.  
You can customize response behavior through **ProxyAPI** settings.  
