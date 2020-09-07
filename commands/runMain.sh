BLUE=`tput setaf 4`
echo "${BLUE}$(tput bold) Please Wait! Booting Up!"
echo "${BLUE}$(tput bold)Starting services..."
osascript -e 'tell app "Terminal"
   do script "sh ~/evabot/commands/runRasaBackend.sh"
end tell'
echo "${BLUE}$(tput bold)Started services [1/4] \r"
osascript -e 'tell app "Terminal"
   do script "sh ~/evabot/commands/runRasaActionServer.sh"
end tell'
echo "${BLUE}$(tput bold)Started services [2/4] \r"
osascript -e 'tell app "Terminal"
   do script "sh ~/evabot/commands/runRasaServer.sh"
end tell'
echo "${BLUE}$(tput bold)Started services [3/4] \r"
osascript -e 'tell app "Terminal"
   do script "sh ~/evabot/commands/runRasaFrontend.sh"
end tell'
echo "${BLUE}$(tput bold)Started services [4/4] \r"
echo "Please wait configuring services..." && sleep 18 && echo "All services up and Running!!" && echo " $(tput sgr0)"
