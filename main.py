import wifi
import ota
from custom import say_hello


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
                tb_ota.download_firmware_files()
            else:
                # Custom code comes here
                say_hello()  
        except ConnectionError as e:
            # Custom code comes here 
            pass   
        except ota.OverTheAirUpdateError as e:
            # Custom code comes here
            pass   


if __name__ == '__main__':
    main()
