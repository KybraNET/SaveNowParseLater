# SaveNowParseLater

This tool acts as a worker and automates the (web) data extraction process, allowing you more time for parsing and analysis.

## Useful for
Extracting data from websites. It's especially useful for content delivery systems that renew their content frequently throughout the day. 

## How to Use:

  - Add the URLs and corresponding timer intervals to the config.txt file.
  - Set a different path in the WORKING_DIR constant if desired.
  - SaveNowParseLater will create a new directory in the specified path for each URL added to the config file.
  
  ```
    https://thewebsiteyouwannadownload.com 5
    https://anotherwebsite.org 3
   ```
   
## Nfo
- Use the dicWrite function in file.py to create a config.txt file automatically.
- worker.py is the main module and contains the entire functionality of SaveNowParseLater.
  

## Disclaimer:
   The mining of data is subject to the terms and conditions of the site you wish to mine and the laws of your jurisdiction. 
   The author assumes no liability for the use of the tool.
