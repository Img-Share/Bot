To run the bot, put your discord bot id thing in .env
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
