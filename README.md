# Wi-Fi Network Information Tool

A lightweight Python-based tool that displays information about the currently connected Wi-Fi network on Windows.

This project uses the built-in Windows `netsh` command to retrieve wireless network interface information.

## Features

- Display Wi-Fi connection status.
- Show connected Wi-Fi name (SSID).
- Display Wi-Fi radio type.
- Show authentication and encryption methods.
- Display signal strength.
- Show Wi-Fi channel.
- Display receive and transmit rates.
- Support for English and Indonesian Windows command output.

## Built With

- Python 3
- Subprocess
- Regular Expressions
- Windows Netsh Command

## Requirements

- Windows 10 or Windows 11
- Python 3.9 or newer
- Active Wi-Fi adapter

No additional Python packages are required.

## Project Structure

```text
python-wifi-network-info/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pradipta-web/python-wifi-network-info.git
```

### 2. Navigate to the Project Directory

```bash
cd python-wifi-network-info
```

### 3. Run the Application

```bash
py main.py
```

## Example Output

```text
=============================================
       WIFI NETWORK INFORMATION
=============================================
Name                : MyWiFi
State               : Connected
Radio Type          : 802.11ac
Authentication      : WPA2-Personal
Encryption          : CCMP
Signal              : 95%
Channel              : 6
Receive Rate         : 433 Mbps
Transmit Rate        : 433 Mbps
=============================================
```

*Note: The output above is an example. Actual information depends on your Wi-Fi adapter and network configuration.*

## Platform Compatibility

This tool is designed specifically for Windows systems because it uses the Windows `netsh wlan` command.

## Limitations

- Only displays information from the local Wi-Fi interface.
- Does not support Wi-Fi password retrieval.
- Some information may not be available depending on the wireless adapter.
- Requires a working Windows WLAN service.

## Author

**Kinervaaa**

GitHub: [@pradipta-web](https://github.com/pradipta-web)

---

If you find this project useful, feel free to give it a ⭐!