
# Tradingview screenshots to twitter

## This is a work in progress...

This project is for Poolsifi. This will send screenshots of charts (where an entry/exit happened) to Twitter.
An alert will notify the app that a screenshot has to be taken.

Things to keep in mind:

- when using our **desktop**, use this to open the chrome profile:
    ```
    CHROME_PROFILE_PATH = 'C:\\Users\\Puja\\AppData\\Local\\Google\\Chrome\\User Data'
    DRIVER_PATH = 'C:\\Users\\Puja\\chromedriver'

    # put this in the __init__ method
    # if google asks to sign in, just sign in manually (it's a 1 time thing)
    chrome_options.add_argument('--profile-directory=Profile 2')
    chrome_options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
    ```

- when using our **home laptop**, use this to open the chrome profile:
    ```
    CHROME_PROFILE_PATH = 'C:\\Users\\pripuja\\AppData\\Local\\Google\\Chrome\\User Data'
    DRIVER_PATH = "C:\\Users\\pripuja\\Desktop\\Python\\chromedriver"

    # put this in the __init__ method
    chrome_options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
    ```

- do not move/click anything on the selenium controlled browser
- make sure that any other chrome browser is closed otherwise it wont work
- please use the dassamaara gmail id to login to tradingview as the chart on that account has been set up in a specific way & it is a pro account (this app needs to be run on a pro app)
    - the background has the symbol & timeframe watermark
    - the bars are a medium sized and are a 100 bars from the right
    - the indicators on the chart: Signal on the top and Screener below it
    - an alarm set up based on Screener
- make sure that when the selenium controlled browser is opened, no other tab is manually opened