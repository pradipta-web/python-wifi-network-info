import subprocess
import re


def get_wifi_info():
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10
        )

        if result.returncode != 0:
            print("Unable to retrieve Wi-Fi information.")
            return

        output = result.stdout

        if not output.strip():
            print("No Wi-Fi information available.")
            return

        info = {}

        fields = {
            "Name": ["SSID"],
            "State": ["State", "Status"],
            "Radio Type": ["Radio type", "Jenis radio"],
            "Authentication": ["Authentication", "Autentikasi"],
            "Encryption": ["Cipher", "Enkripsi"],
            "Signal": ["Signal", "Sinyal"],
            "Channel": ["Channel", "Saluran"],
            "Receive Rate": ["Receive rate (Mbps)", "Receive rate"],
            "Transmit Rate": ["Transmit rate (Mbps)", "Transmit rate"]
        }

        for line in output.splitlines():
            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            for display_name, aliases in fields.items():
                if key.lower() in [alias.lower() for alias in aliases]:
                    info[display_name] = value

        print("\n" + "=" * 45)
        print("       WIFI NETWORK INFORMATION")
        print("=" * 45)

        if not info:
            print("No Wi-Fi interface information found.")
        else:
            for key in fields:
                value = info.get(key, "Not available")
                print(f"{key:<20}: {value}")

        print("=" * 45)

    except subprocess.TimeoutExpired:
        print("Request timed out.")

    except FileNotFoundError:
        print("The netsh command is not available.")

    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    get_wifi_info()