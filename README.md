<h1 align="center">
cOTA
  <br>
</h1>

<h4 align="center">
CircuitPython Over-the-air (OTA) updates via ThingsBoard and GitHub for seamless device management.   
<br>
 </h4>

## Features
-   Enable automatic firmware updates on microcontrollers using CircuitPython over Wi-Fi.
-   Utilize a GitHub-Repository as your firmware repository.
-   Upload and distribute OTA updates for your microcontrollers using ThingsBoard.
-   Monitor firmware downloads, verify updates, and track errors with ease.
-   Ensure data integrity by verifying file hashes during firmware download.

## How To Use

1. Download and move the following files and folder to your microcontroller:

<a name="repofiles"></a>

* `main.py` 
* `boot.py` 
* `settings.toml`
* `lib` 

2. Edit the `settings.toml` file and fill in your Wi-Fi and ThingsBoard credentials.
3. Add your own modules to the microcontroller and edit the content of the `main.py` file e.g. as follows:
   
	```py
	from your_module import your_custom_function
	
	...
	
	if tb_ota.is_new_firmware_available():
	    # New firmware is available, let's download it.
	    tb_ota.download_firmware_files()
	else:
	    # Add your custom code or call your functions here, e.g.:
	    your_custom_function()
	    ...
	```
 
4. Perform a hard reset, similar to hitting the RESET button, on the microcontroller and make sure the device is connected to Wi-Fi.
5. Ensure that your ThingsBoard device is associated with a profile, typically the `default` profile which is preconfigured.
6. Create a public GitHub-Repository which contains a `main` branch.
7. Push the code or modules that need to be saved or overwritten on the microcontroller to your GitHub repository.
8. In ThingsBoard, add a new OTA package under `Advanced features` > `OTA updates`. Add a custom firmware- title and version number as well as the device profile and make sure the `Package type` is set to `Firmware`. Now change to `Use external URL` and add the URL to your GitHub repo under `Direct URL`.
9. Under `profiles` you now have to add the firmware-package to a specific profile to actually update the firmware of the device(s). **The microcontroller will now download the files in your GitHub repo and save it on the filesystem**.
10. After making modifications to your code in the repository, revisit step 8 and ensure that you either update the firmware title or version when you create a new OTA package on ThingsBoard. This step is crucial for enabling the microcontroller to detect the updated firmware.

> **Important**
> Make sure your code is inside the `main` branch. Other branch names will cause problems.

## Details

When the microcontroller detects new firmware, it will download all files from the repository and completely replace the contents of the microcontroller's filesystem with the content of the repository. This process involves removing the entire filesystem (excluding the [repository files](#repofiles)) on the microcontroller before saving the repository files.

The `Client attributes` and `Shared attributes` sections of a specific device within ThingsBoard store details regarding the currently installed firmware and the uploaded firmware.
You can also import a [predefined dashboard](https://github.com/thingsboard/thingsboard/blob/master/application/src/main/data/json/demo/dashboards/firmware.json) to view the firmware download progress in ThingsBoard.

## License

This project is licensed under the terms of the MIT license.
