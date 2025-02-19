# Notes for developers

### For open_tv.py
1. `SYMBOL_INPUTS` in `open_tv.py` should be the number of inputs in the screener which will be filled with symbols by Python. There are currently a total of 20 symbol inputs in the screener. Only a couple of them will get filled (currently, 5 of them will get filled). So, don't give this constant a value of the total symbol inputs. To change how many symbols can get filled, go to the screener's code in Pine Script.

2. In `open_tv.py`, specify the timeframe of the chart. It is in the `CHART_TIMEFRAME` constant. This is the timeframe which the entries run on. The value of the constant should be a string and one of these options (The spelling must be correct):![Alt text](media/chart-tf.png) 

4. In `open_tv.py`, make sure the `USED_SYMBOLS_INPUT` constant is the name of the "Used Symbols" input in the screener

5. In `open_tv.py`, make sure the `LAYOUT_NAME` constant is set to the name of the layout on Tradingview which is meant for the screener.

6. In `open_tv.py`, the constant `SCREENER_REUPLOAD_TIMEOUT` has to have a value for the number of seconds it should wait for the screener to be re-uploaded on the chart. 

### For send_to_socials/send_to_discord.py
1. `BI_REPORT_LINK` should be the shortened link of the latest Trade Stats Power BI Report. Use Bitly to shorten it.

### For resources/categories.py
In Poolsifi's server, there are 5 categories: CURRENCIES, US STOCKS, INDIAN STOCKS, CRYPTO and INDICES. 
In each category, there are 3 channels: strategy-1, exits and before-and-after.
The instructions below will show you what you need to do for each category and its channels. 

**For the CURRENCIES category:**
- `CURRENCIES_WEBHOOK_NAME` in categories.py should be "Currencies". 
- `CURRENCIES_ENTRY_WEBHOOK_LINK` in categories.py should be the webhook link of the strategy-1 channel.
- `CURRENCIES_EXIT_WEBHOOK_LINK` in categories.py should be the webhook link of the exits channel.
- `CURRENCIES_BEFORE_AFTER_WEBHOOK_LINK` in categories.py should be the webhook link of the before-and-after channel.

**For the US STOCKS category:**
- `US_STOCKS_WEBHOOK_NAME` in categories.py should be "US Stocks". 
- `US_STOCKS_ENTRY_WEBHOOK_LINK` in categories.py should be the webhook link of the strategy-1 channel.
- `US_STOCKS_EXIT_WEBHOOK_LINK` in categories.py should be the webhook link of the exits channel.
- `US_STOCKS_BEFORE_AFTER_WEBHOOK_LINK` in categories.py should be the webhook link of the before-and-after channel.

**For the INDIAN STOCKS category:**
- `INDIAN_STOCKS_WEBHOOK_NAME` in categories.py should be "Indian Stocks". 
- `INDIAN_STOCKS_ENTRY_WEBHOOK_LINK` in categories.py should be the webhook link of the strategy-1 channel.
- `INDIAN_STOCKS_EXIT_WEBHOOK_LINK` in categories.py should be the webhook link of the exits channel.
- `INDIAN_STOCKS_BEFORE_AFTER_WEBHOOK_LINK` in categories.py should be the webhook link of the before-and-after channel.

**For the CRYPTO category:**
- `CRYPTO_WEBHOOK_NAME` in categories.py should be "Crypto". 
- `CRYPTO_ENTRY_WEBHOOK_LINK` in categories.py should be the webhook link of the strategy-1 channel.
- `CRYPTO_EXIT_WEBHOOK_LINK` in categories.py should be the webhook link of the exits channel.
- `CRYPTO_BEFORE_AFTER_WEBHOOK_LINK` in categories.py should be the webhook link of the before-and-after channel.

**For the INDICES category:**
- `INDICES_WEBHOOK_NAME` in categories.py should be "Indices". 
- `INDICES_ENTRY_WEBHOOK_LINK` in categories.py should be the webhook link of the strategy-1 channel.
- `INDICES_EXIT_WEBHOOK_LINK` in categories.py should be the webhook link of the exits channel.
- `INDICES_BEFORE_AFTER_WEBHOOK_LINK` in categories.py should be the webhook link of the before-and-after channel.

### For database/local_db.py
1. `PWD` is supposed to be the password of our remote database. To edit that password, sign in to MongoDb and go to Data/base Access on the left. Click on the user (i.e. sammy) and edit the password.

### For exits.py
1. `self.col` is supposed to be the name of the collection where entries should be checked for exits.
2. The keys in the `self.last_checked_dates` dictionary should be the value of the category field in MongoDB documents (i.e. Currencies, US Stocks, Crypto etc...)

### For main.py
1. `SCREENER_SHORT` is supposed to be the shorttitle of the screener.
2. `DRAWER_SHORT` is supposed to be the shorttitle of the Trade Drawer indicator.
3. `SCREENER_NAME` is supposed to be the name of the screener (the name of the script).
4. `DRAWER_NAME` is supposed to be the name of the Trade Drawer indicator (the name of the script).
5. `INTERVAL_MINUTES` has to be set to the number of minutes Python should wait until it restarts all the inactive alerts
6. `START_FRESH` is like an on/off switch for starting fresh, deleting all alerts and setting up new alerts OR just opening TradingView, keeping the pre-existing alerts and waiting for alerts to come. If it's `True`, the application will open TradingView, delete all the alerts and start setting up all 260 alerts again. If it's `False`, the application will open TradingView, NOT delete the alerts but instead keep all the alerts that were made when the application was previously run. This variable was created so that I could do 2 things:
    - When I leave the application running, come back in the morning to find it frozen and find alerts in the Alerts log that are unread by the application, I would like to re-start the application and keep the alerts that were made when it ran previously without deleting all the alerts and therefore, keeping the alerts in the Alerts log. So, when I run the application with `START_FRESH` set to `False`, the application won't delete all the alerts, read the unread alerts that came when it was previously running and wait for new alerts.
    - Sometimes, when I think I need to start fresh, delete all the alerts and make new ones, I can set `START_FRESH` set to `True`.
7. `LINES_TO_KEEP` is the number of latest lines to keep in the log file. It keeps deleting the oldest logs and keeps the latest `LINES_TO_KEEP` lines. This was done to prevent the log file from slowing down the application.

### For Pinescript
1. In the Trade Drawer indicator, in Pinescript, the first 6 inputs have to be arranged in this order: dateTime, entry, sl, tp1, tp2, tp3

2. In Pine Script, the Get Exits indicator must have its first 7 inputs in this order: `entryTime`, `entryPrice`, `entryType`, `sl`, `tp1`, `tp2`, `tp3`

3. If the symbols in `symbol_settings.py` are rare and have prices like -5.0000000034782 or 0.00000389, go to the screener and fix the code in the alertMsg function to make it convert those prices into their correct string versions. Their string versions should be the exact same as the prices and should not be rounded off and the decimal places should not be cut off.

4. The Premium Screener and the Get Exits indicators on Tradingview must to be starred (so that they can appear in the Favorites dropdown)

5. Make sure that in the `timeframeToString` function, the timeframe of the entries is mentioned under the `switch` statement. Eg: If the timeframe of the entries is 1 hour, this statement should be there: `'60' => '1 hour'`

## Some errors which might happen on Tradingview
1. "Modify_study_limit_exceeding" error can happen on a script whose inputs are getting changed frequently. 
2. "Calculation timed out" error happens when the script exceeds the time limit for calculation
3. "Stopped - Calculation error" can happen in the alert

## Browser
1. Do not move/click anything on the selenium controlled browser
2. Make sure you are fine with it deleting any alerts and creating new ones
3. Make sure that any other chrome browser is closed otherwise it won't work
4. Make sure that when the selenium controlled browser is opened, no other tab is manually opened

## Tradingview
1. Please use the dassamaara gmail id to login to Tradingview as the chart on that account has been set up in a specific way
2. No popups or clicks should happen manually
3. In the alert settings, "On site Pop up" is unticked
4. the "Alerts log" must be maximized (although it doesn't have to be FULLY maximized) and not minimized. 
5. There must be a saved layout named "Screener" which has the following setup:
    - The bars are medium sized and the chart is a 100 bars from the right 
    - Premium Screener indicator & Trade Drawer indicator should be on the chart
    - Premium Screener should have 15-20 inputs (So that Python can click on it)
6. There must be a saved layout named "Exits" and the Get Exits indicator should be on it.
