# ADBProject 📱👨🏻‍💻
A Python script that executes ADB commands to perform certain tasks in an Android Pixel Emulator. The script uses the `pure-python-adb` library (`ppadb`). Once the script is executed, a pdf file is automatically generated containing screenshots of the effects of each of the actions that the phone took. Some of the executed commands perform the following actions on the phone or emulator:

- Toggle bluetooth and wifi. 
- Launch an app. 🚀
- Press and hold three apps on the home screen. 🏠
- Toggle the rotation lock setting. 🔐
- Create a new contact and store it in memory. 💾
- Download the `.apk` contained in this repo.
- Delete the `.apk` contained in this repo.

## How to run the project?

In order to run the project, you need to install:
- Python
- `pure-python-adb` python's library.
- `fpdf` python's library
- Android's Google Pixel Emulator.

Once you installed everything on the list above, you have to follow the steps below:
- Open the project on `PyCharm`, or your preferred IDE.
- Launch 🚀 the Android's Google Pixel Emulator, and leave it on the home screen.
- Execute the `main.py` file.

Once the script finishes running, the pdf file generated can be found in the `root`of the project with the following name: `reporte.pdf` 


