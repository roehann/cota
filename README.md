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
3. Perform a hard reset, similar to hitting the RESET button, on the microcontroller and make sure the device is connected to Wi-Fi and that your script is running.
4. Create a public GitHub-Repository which contains a `main` branch.
5. Push the modules that need to be copied to or modified on the microcontroller to your GitHub repository. **Please note that the microcontroller will delete everything from the local filesystem, except for the previously named [files and folder](#repofiles), after downloading these repository files**. For example, it is not mandatory to define the `boot.py` or `settings.toml` file in your repository; however, they can be updated if needed. You can also look into [this](https://github.com/roehann/cota-example) repo that features a minimal working example which you can use for your repo.
6. Ensure that your ThingsBoard device is associated with a profile, typically the `default` profile which is preconfigured. In the following example, the `ota_profile` profile is utilized, but you also have the option to create your own profile under `Profiles` > `Device profiles` and adding your created profile to your device under `Entities` > `Devices` like so:

	![ota_change_device_profile_blur](https://github.com/roehann/cota/assets/72553816/be34f3b7-d7a8-4bea-8109-28a6e1352f4f)
   
7. In ThingsBoard, add a new OTA package under `Advanced features` > `OTA updates`. Add a custom firmware- title and version number as well as the device profile and make sure the `Package type` is set to `Firmware`. Now change to `Use external URL` and add the URL to your GitHub repo under `Direct URL`. It should look something like this:
   
    ![ota_add_package_example](https://github.com/roehann/cota/assets/72553816/98dc7288-73e9-4c31-8a90-22c4660d7ffa)

8. Within the `profiles` > `Device profiles` section, you must now incorporate the firmware package into a designated profile to effectively update the firmware of the device(s), like so:

	![firmware_to_profile](https://github.com/roehann/cota/assets/72553816/9f294110-0abd-409f-bdf5-d3025ae47c08)
   
	Subsequently, the microcontroller will proceed to download the files from your GitHub repository and store them in the filesystem.
	You can also import a [predefined dashboard](https://github.com/thingsboard/thingsboard/blob/master/application/src/main/data/json/demo/dashboards/firmware.json) to view the firmware download progress in ThingsBoard.
10. After making modifications to your code in the repository, revisit step 8 and ensure that you either update the firmware title or version when you create a new OTA package on ThingsBoard. This step is crucial for enabling the microcontroller to detect the updated firmware.

> **Important**
> Make sure your code is inside the `main` branch. Other branch names will cause problems.

## Details

The `Client attributes` and `Shared attributes` sections of a specific device within ThingsBoard store details regarding the currently installed firmware and the uploaded firmware.

After pushing your files to your repository, please note that it may take some time for the GitHub API to reflect these updates. Hence, after pushing the files to your repository and immediately publishing the package via ThingsBoard, the file hashes may not initially match, potentially resulting in errors on the microcontroller. These errors can be caught using the `OverTheAirUpdateError` exception handler in the `main.py` file. However, after a few minutes, the hash values should be updated and the errors resolved.

## License

This project is licensed under the terms of the MIT license.
