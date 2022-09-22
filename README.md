# SaveNowParseLater

A Web data scientist often extracts data from (HTML) websites. Many websites are content delivery systems, whose content is renewed several times within a day. In order for the scientist to have a certain amount of data, this tool should help him. Then he can focus more on parsing. This tool acts as a worker and brings the necessary basic functionality. The mining of data is subject to the terms and conditions of the site you wish to mine and the laws of your jurisdiction. The author assumes no liability for the use of the tool.

How To USE:
- Add Data to config.txt. You need to add the url and the minutes set the cyclic timer. like that
https://thewebsiteyouwannadownload.com 5
https://anotherwebsite.org 3

- You can set a different path in first Constant->WORKING_DIR for saving 
the config.txt and all the downloaded html files. SaveNowParseLater create 
a new directory in that path for each URL you added to config file. 

Info:
- If you dont like to add values to config file by own you can use the dicWrite function in file.py for saving own dictionay
- worker.py is Main! If you want to entire functionality of the SaveNowParseLater than just import that module

Its just some simple tool but if you like that tool please leave a Star :)
Iam not sure when it's possible to continue with these repo, because i have lot work load in my private repos/ business

