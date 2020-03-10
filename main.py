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

    # Screenshot of the homescreen
    result = device.screencap()
    with open(f"./images/home_1.png", "wb") as fp:
        fp.write(result)


    # Launch all app menu
    device.shell("input tap 540 1550")
    sleep(1)
    # Screenshot of all app menu without apk installed
    result = device.screencap()
    with open(f"./images/apk_uninstalled.png", "wb") as fp:
        fp.write(result)

    device.install(APK_NAME)
    sleep(4)
    #Screenshot of all app menu with apk installed
    result = device.screencap()
    with open(f"./images/apk_installed.png", "wb") as fp:
        fp.write(result)

    sleep(1)
    # Launch the installed app
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {ANDMIN}")
    sleep(1)
    # Screenshot of AndMin App open
    result = device.screencap()
    with open(f"./images/andmin.png", "wb") as fp:
        fp.write(result)

    sleep(1)  # Sleep, so that there is time to take the screenshot if the command is delayed
    device.shell("input keyevent 3")
    sleep(2)
    # For accessing the package name of the app that is open
    # ans = device.shell("dumpsys window windows | grep Focus")
    # print(ans)
    # print(ans.split("\n"))

    # Screenshot of the homescreen
    result = device.screencap()
    with open(f"./images/home_2.png", "wb") as fp:
        fp.write(result)

    # Launches an app (Check if I wanna open Google Maps)
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {GOOGLE_MAPS_ACTIVITY}")
    sleep(2)  # Sleep, so that there is time to take the screenshot if the command is delayed
    result = device.screencap()
    with open(f"./images/google_maps_1.png", "wb") as fp:
        fp.write(result)

    sleep(1)

    # For going back 'home'
    device.shell("input keyevent 3")
    # For long pressing the app icons
    print(device.shell("wm density"))
    # device.shell("input touchscreen swipe 170 187 170 187 2000")

    # Check the wifi status of the emulator
    print(device.shell("dumpsys wifi | grep 'Wi-Fi is'"))

    # Activating device rotation lock
    device.shell("input touchscreen swipe 400 20 400 800 1000")
    result = device.screencap()
    with open(f"./images/rotation_lock_1.png", "wb") as fp:
        fp.write(result)

    sleep(1)
    print(device.shell(
        "content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0"))
    # Screenshot of lock working
    sleep(2)
    result = device.screencap()
    with open(f"./images/rotation_lock_2.png", "wb") as fp:
        fp.write(result)
    sleep(1)
    device.shell("input keyevent 3")
    sleep(2)

    # Launch the contacts app and add a new contact
    device.shell("input keyevent 207")
    sleep(1)  # Sleep, so that there is time to take the screenshot if the command is delayed
    result = device.screencap()
    with open(f"./images/contacts_1.png", "wb") as fp:
        fp.write(result)

    device.shell(
        "am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Bo Lawson' -e phone 123456789")
    device.shell("input keyevent 122")
    sleep(2)  # Sleep, so that there is time to take the screenshot if the command is delayed
    result = device.screencap()
    with open(f"./images/contacts_2.png", "wb") as fp:
        fp.write(result)


    print(device.shell("wm size"))
    device.shell("input tap 900 80")
    sleep(2)
    result = device.screencap()
    with open(f"./images/contacts_3.png", "wb") as fp:
        fp.write(result)

    device.shell("input keyevent 4")
    sleep(1)
    result = device.screencap()
    with open(f"./images/contacts_4.png", "wb") as fp:
        fp.write(result)

    device.shell("input keyevent 3")

    # QUESTION 2
    #Launch first app available in home screen
    sleep(1)
    result = device.screencap()
    with open(f"./images/home_3.png", "wb") as fp:
        fp.write(result)

    # Launches an app (Check if I wanna open Google Maps)
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {GOOGLE_MAPS_ACTIVITY}")
    sleep(2)
    result = device.screencap()
    with open(f"./images/google_maps_2.png", "wb") as fp:
        fp.write(result)

    # Lower device volume
    device.shell("input keyevent 25")
    device.shell("input keyevent 25")
    result = device.screencap()
    with open(f"./images/volume.png", "wb") as fp:
        fp.write(result)

    sleep(4)
    # Launch any app with text input and write my name (Telephone)
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {PHONE}")
    sleep(2)
    result = device.screencap()
    with open(f"./images/phone.png", "wb") as fp:
        fp.write(result)

    # Input name
    device.shell("input tap 500 90")
    sleep(1)
    result = device.screencap()
    with open(f"./images/phone_2.png", "wb") as fp:
        fp.write(result)

    device.shell("input text 'Juan Esteban Mendez'")
    sleep(3)
    result = device.screencap()
    with open(f"./images/phone_3.png", "wb") as fp:
        fp.write(result)
    # Turn bluetooth on (It is not supported on emulator)

    # Launch contacts app and add a new contact

    device.shell("input keyevent 207")
    sleep(2)
    result = device.screencap()
    with open(f"./images/contacts_5.png", "wb") as fp:
        fp.write(result)

    device.shell(
        "am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Pedro Rosales' -e phone 3112142706")
    sleep(2)
    result = device.screencap()
    with open(f"./images/contacts_6.png", "wb") as fp:
        fp.write(result)

    device.shell("input tap 900 80")
    sleep(2)
    result = device.screencap()
    with open(f"./images/contacts_7.png", "wb") as fp:
        fp.write(result)

    device.shell("input keyevent 4")
    sleep(2)
    result = device.screencap()
    with open(f"./images/contacts_8.png", "wb") as fp:
        fp.write(result)

    device.shell("input keyevent 3")

    #Uninstall apk
    device.uninstall("com.andminuniandes")
    sleep(1)
    device.shell("input tap 540 1550")
    sleep(1)
    # Screenshot of all app menu without apk installed
    result = device.screencap()
    with open(f"./images/apk_uninstalled_2.png", "wb") as fp:
        fp.write(result)




def createPDF():
    print("CREATING PDF...")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Midterm ADB", ln=1, align="C")
    pdf.cell(200, 5, txt="Juan Esteban Mendez", ln=1, align="L")
    pdf.cell(200, 5, txt="Codigo: 201531707", ln=1, align="L")
    pdf.cell(200, 10, txt="Emulator: Pixel_2_API_26", ln=1, align="L")

    pdf.cell(200, 10, txt="1. Install an android apk through ADB on either an emulator or an actual device", ln=1,
             align="L")
    pdf.image(f"./images/home_1.png", w=60)
    pdf.cell(200, 5, txt="Command: adb install app-release.apk", ln=1, align="L")
    pdf.image(f"./images/apk_uninstalled.png", w=60)
    pdf.image(f"./images/apk_installed.png", w=60)
    pdf.multi_cell(200, 5, txt="Command: adb am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.andminuniandes/com.interfaz.MainActivity")
    pdf.image(f"./images/andmin.png", w=60)

    pdf.cell(200, 20, txt="QUESTION 1", ln=1, align="L")
    pdf.cell(200, 10, txt="1. Go to the home menu and click on the first app available on the launcher, all via ADB.",
             ln=1, align="L")
    pdf.cell(200, 10,
             txt="Command: adb shell input keyevent 3",
             ln=1, align="L")
    pdf.image(f"./images/home_2.png", w=60)
    pdf.multi_cell(200, 5,
             txt="Command: adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.google.android.apps.maps/com.google.android.maps.MapsActivity")
    pdf.image(f"./images/google_maps_1.png", w=60)

    pdf.cell(200, 20,
             txt="2. Go to the home menu and long tap the first 3 apps available on the launcher, all via ADB.", ln=1,
             align="L")

    pdf.cell(200, 20, txt="3. Using ADB, verify the device's current WiFi status (on/off) ", ln=1, align="L")

    pdf.cell(200, 20, txt="4. Using ADB, activate the device's rotation lock.  ", ln=1, align="L")
    pdf.cell(200, 20,
             txt="Command: adb shell input touchscreen swipe 400 20 400 800 1000",
             ln=1, align="L")
    pdf.image(f"./images/rotation_lock_1.png", w=60)
    pdf.multi_cell(200, 5,
             txt="Command: adb shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0")
    pdf.image(f"./images/rotation_lock_2.png", w=60)

    pdf.cell(200, 20, txt="5. Using ADB, launch the contacts app and add a new contact to the contact's list.", ln=1,
             align="L")
    pdf.cell(200, 20, txt="Command: adb shell input keyevent 207", ln=1,
             align="L")
    pdf.image(f"./images/contacts_1.png", w=60)
    pdf.multi_cell(200, 5, txt="Command: adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Bo Lawson' -e phone 123456789")
    pdf.image(f"./images/contacts_2.png", w=60)
    pdf.cell(200, 20, txt="Command: adb shell input tap 900 80", ln=1,
             align="L")
    pdf.image(f"./images/contacts_3.png", w=60)
    pdf.cell(200, 20, txt="Command: adb shell keyevent 4", ln=1,
             align="L")
    pdf.image(f"./images/contacts_4.png", w=60)

    pdf.cell(200, 20, txt="QUESTION 2", ln=1, align="L")
    pdf.cell(200, 10, txt="1. Go to the home menu and click on the first app available on the launcher, all via ADB.",
             ln=1, align="L")
    pdf.cell(200, 20, txt="Command: adb shell input keyevent 3", ln=1,
             align="L")
    pdf.image(f"./images/home_3.png", w=60)
    pdf.multi_cell(200, 5,
             txt="Command: adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.google.android.apps.maps/com.google.android.maps.MapsActivity")
    pdf.image(f"./images/google_maps_2.png", w=60)

    pdf.cell(200, 10, txt="2. Using ADB, lower the device's volume.",
             ln=1, align="L")
    pdf.cell(200, 10, txt="Command: adb shell keyevent 25",
             ln=1, align="L")
    pdf.image(f"./images/volume.png", w=60)

    pdf.cell(200, 10, txt="3. Using ADB, open the notes app (or any app with text input) and write your name.",
             ln=1, align="L")
    pdf.multi_cell(200, 5, txt="Command: adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.google.android.dialer/com.google.android.dialer.extensions.GoogleDialtactsActivity")
    pdf.image(f"./images/phone.png", w=50, h=100)
    pdf.cell(200, 10, txt="Command: adb shell input tap 500 90",
             ln=1, align="L")
    pdf.image(f"./images/phone_2.png", w=60)
    pdf.cell(200, 10, txt="Command: adb shell input text 'Juan Esteban Mendez'",
             ln=1, align="L")
    pdf.image(f"./images/phone_3.png", w=60)

    pdf.cell(200, 10, txt="4. Using ADB, turn on bluetooth.",
             ln=1, align="L")

    pdf.cell(200, 10, txt="5. Using ADB, launch the contacts app and add a new contact to the contact's list.",
             ln=1, align="L")
    pdf.cell(200, 10, txt="Command: adb shell input keyevent 207",
             ln=1, align="L")
    pdf.image(f"./images/contacts_5.png", w=60)
    pdf.multi_cell(200, 5, txt="Command: adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Pedro Rosales' -e phone 3112142706")
    pdf.image(f"./images/contacts_6.png", w=60)
    pdf.cell(200, 10, txt="Command: adb shell input tap 900 80",
             ln=1, align="L")
    pdf.image(f"./images/contacts_7.png", w=60)
    pdf.cell(200, 10, txt="Command: adb shell input keyevent 4",
             ln=1, align="L")
    pdf.image(f"./images/contacts_8.png", w=60)
    pdf.cell(200, 10, txt="Uninstall apk.",
             ln=1, align="L")
    pdf.cell(200, 10, txt="Command: adb uninstall com.andminuniandes",
             ln=1, align="L")
    pdf.image(f"./images/apk_uninstalled_2.png", w=60)


    pdf.output("report.pdf")


if __name__ == "__main__":
    main()
    createPDF()