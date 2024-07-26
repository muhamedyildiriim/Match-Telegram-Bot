# MatchPlus-Telegram-Bot

## Description
The **Football Match Scheduler Bot** is a Telegram bot designed to provide daily updates on upcoming football matches from various leagues, including the Champions League, UEFA Europa League, UEFA Conference League, English Premier League, and Turkish Super Lig. The bot fetches match data from "onefootball.com" and sends a compiled message to a designated Telegram group at 12:00 PM, keeping users informed about the matches scheduled for that day.

## Features
- **Daily Match Updates**: Get daily updates for popular football leagues.
- **Seamless Integration**: Easily integrates with Telegram for distributing match information.
- **Accurate Data**: Match data is sourced from "onefootball.com" for accurate and up-to-date information.

## Technical Details
### Dependencies
- Python
- BeautifulSoup
- Requests
- Schedule
- pymongo
- python-telegram-bot

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/football-match-scheduler-bot.git
    cd football-match-scheduler-bot
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure the `config.ini` file:
    - Open the `config.ini` file in a text editor.
    - Replace the placeholders with your Telegram bot token and group ID.
    ```ini
    [telegram]
    bot_token = YOUR_TELEGRAM_BOT_TOKEN
    group_id = YOUR_TELEGRAM_GROUP_ID
    ```

4. Run the bot:
    ```bash
    python main.py
    ```

### Usage
- The bot will automatically fetch match data from "onefootball.com" and send updates to the configured Telegram group at 12:00 PM daily.
- Users will receive notifications about upcoming matches, including the date, time, and scores.

## How It Works
1. **Data Scraping**: The bot uses the BeautifulSoup library to scrape match data from "onefootball.com".
2. **Database Storage**: Match information is stored in a MongoDB database.
3. **Telegram Integration**: The bot uses the python-telegram-bot library to send messages to a Telegram group at a scheduled time using the `schedule` library.

## Configuration
- Ensure the `config.ini` file is correctly set up with your Telegram bot token and group ID.
- Adjust the schedule timing if needed by modifying the `main.py` file.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or support, please contact [muhamedyildiriim@gmail.com].

