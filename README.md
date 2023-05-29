# Darknet Project

This project provides a Docker containerized Python application for open source intelligence gathering on the darknet.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

**1. Install Docker on Kali Linux:**

Docker is not included by default on Kali Linux. You can install it by using the following commands in your terminal.

First, update your existing list of packages:
```
sudo apt-get update
```

Next, install a few prerequisite packages which let apt use packages over HTTPS:
```
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
```

Then add the GPG key for the official Docker repository to your system:
```
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```

Add the Docker repository to APT sources:
```
sudo echo "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" > /etc/apt/sources.list.d/docker.list
```

Update the package database with the Docker packages from the newly added repo:
```
sudo apt-get update
```

Finally, install Docker:
```
sudo apt-get install docker-ce
```

**2. Install Git on Kali Linux:**

Git is usually included by default on Kali Linux, but if it is not, you can install it by using the following command in your terminal:
```
sudo apt-get install git
```

After installing Docker and Git, you can proceed with the rest of the instructions for cloning the repository and running the Docker container.

### Installation

- Clone the repository to your local machine:

```
git clone https://github.com/CyberOneTechnologies/Darknet.git
```

- Navigate to the Darknet directory:

```
cd Darknet
```

- Build the Docker image:

```
docker build -t darknet .
```

- Run the Docker container:

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
