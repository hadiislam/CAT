if [ -e  /usr/lib/sudo ];then
  if [ -e /usr/bin/apt-get ];then
    if [ ! -e /usr/bin/python3 ];then
       sudo apt-get update
       sudo apt-get upgrade -y
       sudo apt-get install python -y
       sudo apt-get install python3 -y
     fi
  fi
else
  if [ -d /usr/bin ];then
    if [ -e /usr/bin/apt-get ];then
      if [ ! -e /usr/bin/python3 ];then
       apt-get update
       apt -get upgrade -y
       apt-get install python -y
       apt-get install python3 -y
      fi
    fi
  fi
fi
if [ -d /data/data/com.termux/files/usr/bin ]; then
  if [ ! -e /data/data/com.termux/files/usr/bin/python3 ];then
    pkg update
    pkg upgrade -y
    pkg install python -y
    pkg install python3 -y
  fi
fi
if [ -e  /usr/lib/sudo ];then
  if [ -e /usr/bin/yum ];then
    if [ ! -e /usr/bin/python3 ];then
       sudo yum update
       sudo yum upgrade -y
       sudo yum install python -y
       sudo yum install python3 -y
     fi
  fi
else
  if [ -d /usr/bin ];then
    if [ -e /usr/bin/yum ];then
      if [ ! -e /usr/bin/python3 ];then
       yum update
       yum upgrade -y
       yum install python -y
       yum install python3 -y
      fi
    fi
  fi
fi
if [ -e  /usr/bin/brew ];then
  if [ ! -e /usr/bin/python3 ];then
     brew install python -y
     brew install python3 -y
   fi
fi
if [ -e  /usr/bin/brew ];then
  if [ ! -e /usr/bin/python ];then
     brew install python -y
     brew install python3 -y
   fi
fi
if [ -e  /usr/bin/apk ];then
  if [ ! -e /usr/bin/python ];then
     apk install python -y
     apk install python3 -y
   fi
fi
if [ -e  /usr/bin/apk ];then
  if [ ! -e /usr/bin/python3 ];then
     apk install python -y
     apk install python3 -y
   fi
fi
python3 install.py
exit
