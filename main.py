# from ppadb.client import Client as AdbClient
#
# client = AdbClient(host="127.0.0.1", port=5037)
# device = client.device("emulator-5554")
# result = device.screencap()
#
# with open("screen.png", "wb") as fp:
#     fp.write(result)

from fpdf import FPDF
from ppadb.client import Client as AdbClient
from time import sleep


GOOGLE_MAPS_ACTIVITY = "com.google.android.apps.maps/com.google.android.maps.MapsActivity"
PHONE = "com.google.android.dialer/com.google.android.dialer.extensions.GoogleDialtactsActivity"
APK_NAME = "app-release.apk"
ANDMIN = "com.andminuniandes/com.interfaz.MainActivity"




def main():
    img_id = 1

    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("emulator-5554")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Midterm ADB", ln=1, align="C")
    pdf.cell(200, 5, txt="Juan Esteban Mendez", ln=1, align="L")
    pdf.cell(200, 5, txt="Codigo: 201531707", ln=1, align="L")

    pdf.cell(200, 20, txt="1. Install an android apk through ADB on either an emulator or an actual device", ln=1,
             align="L")


    # Launch all app menu
    device.shell("input tap 540 1550")
    device.install(APK_NAME)
    sleep(4)
    # Launch the installed app
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {ANDMIN}")
    sleep(1)  # Sleep, so that there is time to take the screenshot if the command is delayed
    device.shell("input keyevent 3")

    pdf.cell(200, 20, txt="QUESTION 1", ln=1, align="L")

    # For accessing the package name of the app that is open
    # ans = device.shell("dumpsys window windows | grep Focus")
    # print(ans)
    # print(ans.split("\n"))

    # Screenshot of the homescreen
    result = device.screencap()
    with open(f"./images/image_{img_id}.png", "wb") as fp:
        fp.write(result)

    pdf.image(f"./images/image_{img_id}.png", w=50, h=100)
    img_id += 1

    pdf.cell(200, 10, txt="1. Go to the home menu and click on the first app available on the launcher, all via ADB.",
             ln=1, align="L")
    pdf.cell(200, 10,
             txt="Command: adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.google.android.apps.maps/com.google.android.maps.MapsActivity",
             ln=1, align="L")
    # Launches an app (Check if I wanna open Google Maps)
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {GOOGLE_MAPS_ACTIVITY}")
    sleep(1)  # Sleep, so that there is time to take the screenshot if the command is delayed
    result = device.screencap()
    with open(f"./images/image_{img_id}.png", "wb") as fp:
        fp.write(result)

    pdf.image(f"./images/image_{img_id}.png", w=50, h=100)
    img_id += 1

    pdf.cell(200, 20,
             txt="2. Go to the home menu and long tap the first 3 apps available on the launcher, all via ADB.", ln=1,
             align="L")

    # For going back 'home'
    device.shell("input keyevent 3")
    # For long pressing the app icons
    print(device.shell("wm density"))
    # device.shell("input touchscreen swipe 170 187 170 187 2000")

    # Check the wifi status of the emulator
    pdf.cell(200, 20, txt="3. Using ADB, verify the device's current WiFi status (on/off) ", ln=1, align="L")
    print(device.shell("dumpsys wifi | grep 'Wi-Fi is'"))

    # Activating device rotation lock
    # Falta tomar screenshot antes y despues de eso activado
    pdf.cell(200, 20, txt="4.Using ADB, activate the device's rotation lock.  ", ln=1, align="L")
    device.shell("input touchscreen swipe 400 20 400 800 1000")
    sleep(1)
    print(device.shell(
        "content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0"))
    device.shell("input keyevent 3")
    sleep(2)

    # Launch the contacts app and add a new contact
    pdf.cell(200, 20, txt="5. Using ADB, launch the contacts app and add a new contact to the contact's list.", ln=1,
             align="L")
    # device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {CONTACTS_ACTIVITY}")
    device.shell("input keyevent 207")
    sleep(1)  # Sleep, so that there is time to take the screenshot if the command is delayed
    result = device.screencap()
    with open(f"./images/image_{img_id}.png", "wb") as fp:
        fp.write(result)

    pdf.image(f"./images/image_{img_id}.png", w=50, h=100)
    img_id += 1

    device.shell(
        "am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Bo Lawson' -e phone 123456789")
    device.shell("input keyevent 122")

    print(device.shell("wm size"))
    device.shell("input tap 900 80")
    device.shell("input keyevent 4")
    device.shell("input keyevent 3")

    # QUESTION 2
    # Launches an app (Check if I wanna open Google Maps)
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {GOOGLE_MAPS_ACTIVITY}")
    # Lower device volume
    device.shell("input keyevent 25")
    device.shell("input keyevent 25")
    sleep(4)
    # Launch any app with text input and write my name (Telephone)
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {PHONE}")
    # Input name
    sleep(2)
    device.shell("input tap 500 90")
    sleep(1)
    device.shell("input text 'Juan Esteban Mendez'")
    # Turn bluetooth on (It is not supported on emulator)

    # Launch contacts app and add a new contact

    device.shell("input keyevent 207")
    device.shell(
        "am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Pedro Rosales' -e phone 3112142706")
    device.shell("input tap 900 80")

    sleep(1)
    device.shell("input keyevent 4")
    device.shell("input keyevent 3")

    #Uninstall apk
    device.uninstall("com.andminuniandes")

    pdf.output("report.pdf")


if __name__ == "__main__":
    main()