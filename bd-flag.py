#usr/bin/bash
clear
bi='\033[34;1m' #biru
i='\033[32;1m' #ijo
pur='\033[35;1m' #purple
cy='\033[36;1m' #cyan
me='\033[31;1m' #merah
pu='\033[37;1m' #putih
ku='\033[33;1m' #kuning

# Jangan Recode Ya gayn

echo
echo
echo
    echo $i"       [•]"$me"─────────────────────────────────────────── "$i"[•]"
     echo $i"        |"$cy"        BANGLADESH DARK TERMUX ASSOCIATE      "$i"|"
     echo $i"        |"$me"───────────────────────────────────────────── "$i"|"
     echo $i"        |"$pu"    Auther :"$bi" BD Termux Team                   "$i"|"
     echo $i"        |"$pu"    Facebook :"$bi" Tanjim Abubokor                "$i"|"
     echo $i"        |"$pu"    Contact WhatsApp :"$bi" 01631596698            "$i"|"
     echo $i"        |"$pu"   Contact Gmail :"$bi" bdtermuxteam23@gmail.com   "$i"|"
    echo $i"       [•]"$me"────────────────────────────────────────────"$i"[•]"
echo


echo
echo
echo
echo $cy"       ░█▀▀"$i"░░░█▀█░░░"$me"█▀▀░░░"$ku"█▀▀░░░"$cy"█▀▄░░░"$i"█▀█░░░"$bi"█▀█░░░"$pur"█░█"
echo $bi"       ░█▀▀░░░"$cy"█▀█░░░█░░░░░"$bi"█▀▀░░░"$i"█"$cy"▀▄░░░█░"$me"█░░░█░█░░░"$ku"█▀▄"
echo $pur"       ░▀░░░░░▀░▀░░░▀"$bi"▀▀░░░▀▀"$i"▀░░░▀▀░░░░"$me"▀▀▀░░░"$cy"▀▀▀░░░▀░"$bi"▀"
echo







echo
echo
echo
      echo $ku"        ★"$i"##########################################"$ku"★"
      echo $ku"        ★"$cy"   |"$me"1"$cy"|"$pur"  Facebook Auto Tools"$ku"               ★"
      echo $ku"        ★"$cy"   |"$me"2"$cy"|"$pur"  Facebook Hack [Phishing]"$ku"          ★"
      echo $ku"        ★"$cy"   |"$me"3"$cy"|"$pur"  Facebook Hack [BruteForse]"$ku"        ★"
      echo $ku"        ★"$cy"   |"$me"4"$cy"|"$pur"  Facebook Auto Report"$ku"              ★"
      echo $ku"        ★"$i"##########################################"$ku"★"
echo
    


echo
echo
echo
echo $i"        [5] Install All Packages" 
echo $me"        [0] EXIT"
echo
    


echo $me"╔═══"$bi"["$i"BD"$bi"]"$me"══════"$bi"["$i""Termux Team""$bi"]"
echo $me"║"
read -p"╚═══➣➣ " pil


if [ $pil = 1 ]
then
clear
toilet -f pagga "W A I T" | lolcat
sleep 1
git clone https://github.com/ciku370/OSIF
cd OSIF	
pip2 install -r requirements.txt
python2 osif.py
fi

if [ $pil = 2 ]
then
clear
toilet -f pagga "W A I T" | lolcat
sleep 1
pkg install git python php curl openssh grep && git clone -b Termux-Support-Branch https://github.com/DarkSecDevelopers/HiddenEye.git && chmod 777 HiddenEye && cd HiddenEye && pip install -r requirements.txt && pip install requests && python HiddenEye.py 
fi

if [ $pil = 3 ]
then
clear
toilet -f pagga "W A I T" | lolcat
sleep 1
git clone https://github.com/tanjim750/Facebook-BruteForce.git
cd Facebook-BruteForce    
pip3 install requests bs4
pip install mechanize
python3 fb.py
fi

if [ $pil = 5 ]
then
clear
apt update && apt upgrade
apt install python2
pkg install python3
pkg install python2 -y
pkg install python
pkg install git -y
pip2 install urllib3 chardet certifi idna requests
pkg install openssh 
pip2 install mechanize
pkg install curl
pkg install ruby
pkg install gem
gem install lolcat
pkg install git
pkg install php
pkg install ruby cowsay toilet figlet
pkg install neofetch
pkg install nano
toilet -f pagga "S U C C E S S" | lolcat
fi


if [ $pil = 0 ]
then
clear
figlet -f slant "E X I T"|lolcat
sleep 2
echo $cy" Thanks for support us "
sleep 2
exit
fi

if [ $pil = 4 ]
then
clear
toilet -f pagga "W A I T" | lolcat
sleep 1
git clone https://github.com/IlayTamvan/Report 
cd Report
unzip Report.zip
python2 Report.py
fi




