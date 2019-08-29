#Create the service file
sudo touch /etc/systemd/system/jokebot.servicebot.service

#Edit the service file, adding the contents of pybot.service here
sudo vim /etc/systemd/system/jokebot.service

#Enable the service (this will cause it to start on boot)
sudo systemctl enable jokebot

#Start the service so it starts running now
sudo service jokebot start

#If you make a change to your code, restart the service so the changes are picked up
sudo service jokebot restart