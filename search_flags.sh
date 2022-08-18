#!/bin/bash
#Author: Iulian Bancau
clear

echo "
  1. Search for file
  2. Search files containing text

Enter your option:"

COLOR_RED='\033[0;31m'
COLOR_GREEN='\033[0;32m'
COLOR_U_YELLOW='\033[4;33m'
COLOR_NC='\033[0m'

read optionNumber

if [ "$optionNumber" -eq 1 ]
then
    clear
    
      echo "Enter filename:"
      read fileName
      
      echo "Enter path to search in:"
      read filePath

      echo "Searching for $fileName in $filePath...\n\n${COLOR_U_YELLOW}Results:"
      
      echo "${COLOR_GREEN}"
      find $filePath -name $fileName 2>/dev/null || echo "No other results :("
      echo "${COLOR_NC}"
    
elif [ "$optionNumber" -eq 2 ]
then
    clear
    
      echo "Enter search text:"
      read searchText
        
      echo "Enter path to search in:"
      read filePath
    
      echo "Searching for text \"$searchText\" in $filePath...\n\n${COLOR_U_YELLOW}Results:"
      
      echo "${COLOR_GREEN}"
      grep -Ril "$searchText" $filePath || echo "No results :("
      echo "${COLOR_NC}"
    
else
    echo Invalid option
fi

