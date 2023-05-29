# Darknet Project

This project provides a Docker containerized Python application for open source intelligence gathering on the darknet.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. **Docker**

2. **Git**

The script `install_docker.sh` is provided in the root directory to install Docker and Git. If these are not installed on your Kali Linux system, you can run this script to install them. 

**- Before running the script, you may need to make it executable with the following command:**
```
chmod +x install_docker.sh
```

**- Then, you can run the script with this command:**
```
./install_docker.sh
```

# Installation

**- Clone the repository to your local machine:**
```
git clone https://github.com/CyberOneTechnologies/Darknet.git
```

**-Navigate to the Darknet directory:**
```
cd Darknet
```

**-Build the Docker image:**
```
docker build -t darknet .
```

**-Run the Docker container:**
```
docker run -it darknet
```

# Usage
This will run the Python application inside the Docker container, which will start a Tor connection, perform a search on the darknet, and then stop the Tor connection.

Please note that the actual functionality of performing searches on the darknet has not yet been implemented.

# Troubleshooting
If you're having trouble building the Docker image, ensure you have a stable internet connection and that you're able to access Docker Hub.

If the Docker container is not running properly, ensure that Docker is installed correctly and that you're able to run other Docker containers.

# Legal Disclaimer
This tool is provided for educational and research purposes only. The usage of this tool for illegal activities is strictly prohibited. The authors and organization involved in the creation and maintenance of this tool are not responsible for any misuse or damage caused by this tool.
