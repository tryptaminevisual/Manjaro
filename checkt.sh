#! /bin/bash

GREEN='\033[0;32m' # Green Color
NC='\033[0m' # No Color

if whereis $(< /home/florens/Scripts/WebCheck/cfile.txt) | grep -q '/usr/bin/'; then
  echo -e "All Tools found! [${GREEN}✓${NC}]"
fi

# Remeber to add a new grep -q {PATH}