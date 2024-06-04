# Botnet Script

## Overview

This script is designed to perform UDP and TCP flood attacks based on parameters fetched from a remote server. It continuously monitors the server for updated attack parameters and executes the specified attack when instructed. **Note: This script is for educational purposes only. Unauthorized use of this script against any system without permission is illegal and unethical.**

## Features

- Fetches attack parameters from a remote server.
- Supports both UDP and TCP flood attacks.
- Multi-threaded for higher attack throughput.
- Continuously monitors the server for updated parameters.

## How It Works

### Initialization

The script begins by fetching attack parameters from a specified URL. The parameters include the target IP address, port, attack type (UDP or TCP), the number of packets to send, the number of threads to use, and a control flag to start or stop the attack.

### Setup a HTTP C2

### Editing the Url

Open the script and **_edit_** url parameter as your server.
The parameters will be fetched from url.
```python
url="http://duvi.duckdns.org/"
```

### Creating index.html

Create a html file for attack parameters. Parameter format should be like this:

```html
P<ip_address>P<port>P<attack_type>P<times>P<threads>P<attack_flag>
```

### Parameter Format

```
P<ip_address>P<port>P<attack_type>P<times>P<threads>P<attack_flag>
```

- `ip_address`: The target IP address.
- `port`: The target port number.
- `attack_type`: 'u' for UDP attack, 't' for TCP attack.
- `times`: The number of packets to send in each burst.
- `threads`: The number of threads to use.
- `attack_flag`: 'atc' to start the attack, any other value to stop.

### Main Loop

The script continuously monitors the server every **10** seconds for updated parameters. If the `attack_flag` is set to 'atc', the attack is initiated or continued; otherwise, it stops.

### Example

Here's a simplified example of the server response:

```
P192.168.1.1P80PuP100P5Patc
```

- IP Address: 192.168.1.1
- Port: 80
- Attack Type: UDP
- Packets per Thread: 100
- Threads: 5
- Attack Flag: 'atc' (start the attack)

##  Step-by-Step Setup Instructions

1. **Clone the Repository or Download the Script**

    Open your terminal or command prompt and run the following command to clone the repository:
    ```bash
    git clone https://github.com/Menesay/Python-Botnet.git
    ```
    Alternatively, you can download the script directly from the repository.

2. **Ensure You Have Python 3 Installed**

    Verify that Python 3 is installed on your system by running:
    ```bash
    python --version
    ```
    If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

3. **Install PyInstaller**

    PyInstaller is a tool that converts Python scripts into standalone executables. Install it using pip:
    ```bash
    pip install pyinstaller
    ```

4. **Convert the Script to an Executable**

    Navigate to the directory containing the script (`bot.py`) and run the following command:
    ```bash
    pyinstaller --onefile bot.py
    ```
    This will generate an executable file in the `dist` folder within your current directory.

5. **Run the Executable**

    Navigate to the `dist` folder and run the executable:
    - On Windows:
      ```bash
      ./dist/bot.exe
      ```
    - On macOS/Linux:
      ```bash
      ./dist/bot
      ```

## Disclaimer

This script is intended for educational purposes only. Unauthorized use against any system without explicit permission is strictly prohibited and may result in severe legal consequences. The author is not responsible for any misuse of this script.
