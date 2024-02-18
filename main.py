import ota
import wifi


def conn_wifi(ssid: str, password: str):
    print(f"Connecting to: {ssid}")
    wifi.radio.connect(ssid, password)
    print(f"Connected to: {ssid}")


def main():    
    settings = ota.get_thingsboard_settings()
    conn_wifi(settings["wifi_ssid"], settings["wifi_password"])
    tb_ota = ota.OverTheAirUpdate(tb_url=settings["thingsboard_url"], 
                                  tb_port=settings["thingsboard_port"], 
                                  tb_device_access_token=settings["thingsboard_device_token"])

    while True:
        try:
            if tb_ota.is_new_firmware_available():
                # New firmware is available, let's download it.
                tb_ota.download_firmware_files()
            else:
                # Add your custom code here.
                pass
        except ConnectionError as e:
            # Handle request connection errors here, for example you might try to reconnect to Wi-Fi (Optional).
            pass   
        except ota.OverTheAirUpdateError as e:
            # Handle exceptions related to the firmware download process (Optional).
            pass   


if __name__ == '__main__':
    main()
