#!/bin/bash

####################################################################################
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Darknet Setup░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Developed by Aarsyth░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░░░░░GitHub Repository: https://github.com/CyberOneTechnologies/░░░░░░░░░░░#
#░░░░░░░░░░░░░░░░░For support, reach out on Discord: Aarsyth#0563░░░░░░░░░░░░░░░░░░#
####################################################################################
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░█████╗░██╗░░░██╗██████╗░███████╗██████╗░░█████╗░███╗░░██╗███████╗░░░░░░░░░#
#░░░░░░░██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║██╔════╝░░░░░░░░░#
#░░░░░░░██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝██║░░██║██╔██╗██║█████╗░░░░░░░░░░░#
#░░░░░░░██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗██║░░██║██║╚████║██╔══╝░░░░░░░░░░░#
#░░░░░░░╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚███║███████╗░░░░░░░░░#
#░░░░░░░░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝░░░░░░░░░#
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
####################################################################################

# Set color variables for better readability
green=$(tput setaf 2)
yellow=$(tput setaf 3)
blue=$(tput setaf 4)
red=$(tput setaf 1)
reverse=$(tput rev)
bold=$(tput bold)
reset=$(tput sgr0)

# Function to install Docker
install_docker() {
    echo "${blue}${bold}Updating existing list of packages...${reset}"
    sudo apt-get update -y

    echo "${blue}${bold}Installing prerequisite packages...${reset}"
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

    echo "${blue}${bold}Adding GPG key for Docker...${reset}"
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

    echo "${blue}${bold}Adding Docker repository to APT sources...${reset}"
    echo "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" | sudo tee /etc/apt/sources.list.d/docker.list

    echo "${blue}${bold}Updating package database...${reset}"
    sudo apt-get update -y

    echo "${green}${bold}Installing Docker...${reset}"
    sudo apt-get install -y docker-ce
}

# Function to install Git
install_git() {
    echo "${green}${bold}Installing Git...${reset}"
    sudo apt-get install -y git
}

# Check if Docker is installed
if [[ $(which docker) && $(docker --version) ]]; then
    echo "${yellow}${bold}Docker is already installed. Skipping Docker installation...${reset}"
else
    echo "${red}${bold}Docker is not installed. Installing Docker...${reset}"
    install_docker
fi

# Check if Git is installed
if [[ $(which git) && $(git --version) ]]; then
    echo "${yellow}${bold}Git is already installed. Skipping Git installation...${reset}"
else
    echo "${red}${bold}Git is not installed. Installing Git...${reset}"
    install_git
fi

echo "${green}${bold}Done.${reset}"
