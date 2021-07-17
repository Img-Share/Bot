To run the bot, put your discord bot id thing in .env
To run Img.Hub (beta):
If on Windows, install Flask via pip:
"pip install Flask"
then run web.py
If on Linux or macOS, install pip, on Debian based distros like Ubuntu, you can run:
"sudo apt install -y python3 python3-pip"
then, use pip to install Flask:
"pip install Flask"
lastly, run web.py, on most distros, you can run "env python3 web.py"
**Note**: These instructions are only for development, please use a production WSGI server like UWSGI or Gunicorn in production.
to make #allmemes and #allpets work,
1. open terminal and type sudo nano /usr/local/bin/amazon-sync
2. put in: 
while true
do
 ls /path/to/meme/folder /path/to/meme.txt/file
 ls /path/to/pet/folder/ > /path/to/pet.txt/file
 sleep 120
done
3. execute sudo chmod +x /usr/local/bin/amazon-sync  
4. whenever you want to start the bot, type amazon-sync in terminal
