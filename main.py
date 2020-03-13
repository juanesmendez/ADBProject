from fpdf import FPDF
from ppadb.client import Client as AdbClient
from time import sleep


GOOGLE_MAPS_ACTIVITY = "com.google.android.apps.maps/com.google.android.maps.MapsActivity"
PHONE = "com.google.android.dialer/com.google.android.dialer.extensions.GoogleDialtactsActivity"
APK_NAME = "app-release.apk"
ANDMIN = "com.andminuniandes/com.interfaz.MainActivity"


def check_event_count(n, count):
    return True if n == count else False


def take_screenshot(device, file_name):
    result = device.screencap()
    with open(f"./images/{file_name}.png", "wb") as fp:
        fp.write(result)


def installAPK(device):
    # Launch all app menu
    device.shell("input tap 540 1550")
    sleep(1)
    # Screenshot of all app menu without apk installed
    take_screenshot(device, "apk_uninstalled")
    # Install APK
    device.install(APK_NAME)
    sleep(4)
    # Screenshot of all app menu with apk installed
    take_screenshot(device, "apk_installed")


def uninstallAPK(device):
    device.shell("input keyevent 3")
    # Uninstall apk
    device.uninstall("com.andminuniandes")
    sleep(1)
    device.shell("input tap 540 1550")
    sleep(1)
    # Screenshot of all app menu without apk installed
    take_screenshot(device, "apk_uninstalled_2")


def event_one(device):
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {GOOGLE_MAPS_ACTIVITY}")
    sleep(2)  # Sleep, so that there is time to take the screenshot if the command is delayed
    take_screenshot(device, "google_maps_1")

def event_two(device):
    sleep(1)
    # For going back 'home'
    device.shell("input keyevent 3")
    # For long pressing the app icons
    # print(device.shell("wm density"))
    device.shell("input touchscreen swipe 200 1700 200 1700 2000")
    sleep(2)
    take_screenshot(device, "long_press_1")

    device.shell("input keyevent 3")

    device.shell("input touchscreen swipe 350 1700 350 1700 2000")
    sleep(2)
    take_screenshot(device, "long_press_2")

    device.shell("input keyevent 3")

    device.shell("input touchscreen swipe 500 1700 500 1700 2000")
    sleep(2)
    take_screenshot(device, "long_press_3")


def event_three(device):
    device.shell("input keyevent 3")
    # Check the wifi status of the emulator
    print(device.shell("dumpsys wifi | grep 'Wi-Fi is'"))


def event_four(device):
    # Activating device rotation lock
    device.shell("input touchscreen swipe 400 20 400 800 1000")
    take_screenshot(device, "rotation_lock_1")

    sleep(1)
    print(device.shell(
        "content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0"))
    # Screenshot of lock working
    sleep(2)
    take_screenshot(device, "rotation_lock_2")


def event_five(device):
    device.shell("input keyevent 3")
    sleep(2)

    # Launch the contacts app and add a new contact
    device.shell("input keyevent 207")
    sleep(1)  # Sleep, so that there is time to take the screenshot if the command is delayed
    take_screenshot(device, "contacts_1")

    device.shell(
        "am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Bo Lawson' -e phone 123456789")
    device.shell("input keyevent 122")
    sleep(2)  # Sleep, so that there is time to take the screenshot if the command is delayed
    take_screenshot(device, "contacts_2")

    # print(device.shell("wm size"))
    device.shell("input tap 900 80")
    sleep(2)
    take_screenshot(device, "contacts_3")

    device.shell("input keyevent 4")
    sleep(1)
    take_screenshot(device, "contacts_4")


def event_six(device):
    device.shell("input keyevent 3")
    # QUESTION 2
    # Launch first app available in home screen
    sleep(1)
    take_screenshot(device, "home_3")

    # Launches an app (Check if I wanna open Google Maps)
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {GOOGLE_MAPS_ACTIVITY}")
    sleep(2)
    take_screenshot(device, "google_maps_2")


def event_seven(device):
    # Lower device volume
    device.shell("input keyevent 25")
    device.shell("input keyevent 25")
    take_screenshot(device, "volume")
    # Sleep for the volume widget to dissapear without causing any trouble
    sleep(4)


def event_eight(device):
    # Launch any app with text input and write my name (Telephone)
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {PHONE}")
    sleep(2)
    take_screenshot(device, "phone")

    # Input name
    device.shell("input tap 500 90")
    sleep(1)
    take_screenshot(device, "phone_2")

    device.shell("input text 'Juan Esteban Mendez'")
    sleep(3)
    take_screenshot(device, "phone_3")


def event_nine(device):
    # Turn bluetooth on (It is not supported on emulator)
    # The following line must be uncommented when the script is run using a real device
    # device.shell("am start -a android.bluetooth.adapter.action.REQUEST_ENABLE")
    return

def event_ten(device):
    # Launch contacts app and add a new contact
    device.shell("input keyevent 207")
    sleep(2)
    take_screenshot(device, "contacts_5")

    device.shell(
        "am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Pedro Rosales' -e phone 3112142706")
    sleep(2)
    take_screenshot(device, "contacts_6")

    device.shell("input tap 900 80")
    sleep(2)
    take_screenshot(device, "contacts_7")
    device.shell("input keyevent 4")
    sleep(2)
    take_screenshot(device, "contacts_8")


def execute_event(num, device):
    switcher = {
        1: event_one,
        2: event_two,
        3: event_three,
        4: event_four,
        5: event_five,
        6: event_six,
        7: event_seven,
        8: event_eight,
        9: event_nine,
        10: event_ten
    }
    # Get the function from the switcher dictionary
    func = switcher.get(num, lambda: "Invalid event id")
    # Execute the function
    func(device)


def main(n):
    eventCount = 0

    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("emulator-5554")

    # Screenshot of the homescreen
    device.shell("input keyevent 3")
    take_screenshot(device, "home_1")

    #Install APK
    installAPK(device)

    sleep(1)
    # Launch the installed app
    device.shell(f"am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n {ANDMIN}")
    sleep(1)
    # Screenshot of AndMin App open
    take_screenshot(device, "andmin")

    sleep(1)  # Sleep, so that there is time to take the screenshot if the command is delayed
    device.shell("input keyevent 3")
    sleep(2)
    # For accessing the package name of the app that is open
    # ans = device.shell("dumpsys window windows | grep Focus")
    # print(ans)
    # print(ans.split("\n"))

    # Screenshot of the homescreen
    take_screenshot(device, "home_2")

    while eventCount < n:
        execute_event(eventCount + 1, device)
        eventCount += 1

    device.shell("input keyevent 3")

    return device

def writeHeader(pdf):
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Midterm ADB", ln=1, align="C")
    pdf.cell(200, 5, txt="Juan Esteban Mendez", ln=1, align="L")
    pdf.cell(200, 5, txt="Student code: 201531707", ln=1, align="L")
    pdf.cell(200, 10, txt="Emulator: Pixel_2_API_26", ln=1, align="L")


def writeInstallAPK(pdf):
    pdf.cell(200, 10, txt="1. Install an android apk through ADB on either an emulator or an actual device", ln=1,
             align="L")
    pdf.set_x(80)
    pdf.image(f"./images/home_1.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10, txt="Command: adb install app-release.apk", ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/apk_uninstalled.png", w=60)
    pdf.image(f"./images/apk_installed.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(200, 10,
                   txt="Command: adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.andminuniandes/com.interfaz.MainActivity")
    pdf.set_x(80)
    pdf.image(f"./images/andmin.png", w=60)


def createPDF(n):
    eventCount = 0
    print("Creating PDF...")

    pdf = FPDF()
    pdf.add_page()

    writeHeader(pdf)

    writeInstallAPK(pdf)

    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 20, txt="QUESTION 1", ln=1, align="L")
    pdf.cell(200, 10, txt="1. Go to the home menu and click on the first app available on the launcher, all via ADB.",
             ln=1, align="L")
    pdf.cell(200, 10,
             txt="Command: adb shell input keyevent 3",
             ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/home_2.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(200, 10,
             txt="Command: adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.google.android.apps.maps/com.google.android.maps.MapsActivity")
    pdf.set_x(80)
    pdf.image(f"./images/google_maps_1.png", w=60)

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf

    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 20,
             txt="2. Go to the home menu and long tap the first 3 apps available on the launcher, all via ADB.", ln=1,
             align="L")
    pdf.multi_cell(200, 10, txt="Command: adb shell input touchscreen swipe 200 1700 200 1700 2000")
    pdf.set_x(80)
    pdf.image(f"./images/long_press_1.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10,
             txt="Command: adb shell input keyevent 3",
             ln=1, align="L")
    pdf.multi_cell(200, 10, txt="Command: adb shell input touchscreen swipe 350 1700 350 1700 2000")
    pdf.set_x(80)
    pdf.image(f"./images/long_press_2.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10,
             txt="Command: adb shell input keyevent 3",
             ln=1, align="L")
    pdf.multi_cell(200, 10, txt="Command: adb shell input touchscreen swipe 500 1700 500 1700 2000")
    pdf.set_x(80)
    pdf.image(f"./images/long_press_3.png", w=60)

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf

    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 20, txt="3. Using ADB, verify the device's current WiFi status (on/off) ", ln=1, align="L")
    pdf.cell(200, 10, txt="Command: dumpsys wifi | grep 'Wi-Fi is'", ln=1, align="L")
    pdf.multi_cell(200, 5, txt="The command shown above, was executed. It returns a string indicating if the wifi is enabled. In this case the command returned 'Wi-Fi is enabled'")

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf

    pdf.cell(200, 20, txt="4. Using ADB, activate the device's rotation lock.  ", ln=1, align="L")
    pdf.cell(200, 10,
             txt="Command: adb shell input touchscreen swipe 400 20 400 800 1000",
             ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/rotation_lock_1.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(200, 10,
             txt="Command: adb shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0")
    pdf.set_x(80)
    pdf.image(f"./images/rotation_lock_2.png", w=60)

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf

    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 20, txt="5. Using ADB, launch the contacts app and add a new contact to the contact's list.", ln=1,
             align="L")
    pdf.cell(200, 10, txt="Command: adb shell input keyevent 207", ln=1,
             align="L")
    pdf.set_x(80)
    pdf.image(f"./images/contacts_1.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(200, 10, txt="Command: adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Bo Lawson' -e phone 123456789")
    pdf.set_x(80)
    pdf.image(f"./images/contacts_2.png", w=60)
    pdf.cell(200, 20, txt="Command: adb shell input tap 900 80", ln=1,
             align="L")
    pdf.set_x(80)
    pdf.image(f"./images/contacts_3.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 20, txt="Command: adb shell keyevent 4", ln=1,
             align="L")
    pdf.set_x(80)
    pdf.image(f"./images/contacts_4.png", w=60)

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf

    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 20, txt="QUESTION 2", ln=1, align="L")
    pdf.cell(200, 10, txt="1. Go to the home menu and click on the first app available on the launcher, all via ADB.",
             ln=1, align="L")
    pdf.cell(200, 10, txt="Command: adb shell input keyevent 3", ln=1,
             align="L")
    pdf.set_x(80)
    pdf.image(f"./images/home_3.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(200, 10,
             txt="Command: adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.google.android.apps.maps/com.google.android.maps.MapsActivity")
    pdf.set_x(80)
    pdf.image(f"./images/google_maps_2.png", w=60)

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf

    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10, txt="2. Using ADB, lower the device's volume.", ln=1, align="L")
    pdf.cell(200, 10, txt="Command: adb shell keyevent 25", ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/volume.png", w=60)

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf

    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10, txt="3. Using ADB, open the notes app (or any app with text input) and write your name.", ln=1, align="L")
    pdf.multi_cell(200, 10, txt="Command: adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.google.android.dialer/com.google.android.dialer.extensions.GoogleDialtactsActivity")
    pdf.set_x(80)
    pdf.image(f"./images/phone.png", w=50, h=100)
    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10, txt="Command: adb shell input tap 500 90",ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/phone_2.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10, txt="Command: adb shell input text 'Juan Esteban Mendez'",
             ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/phone_3.png", w=60)

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf

    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10, txt="4. Using ADB, turn on bluetooth.",ln=1, align="L")
    pdf.cell(200, 10, txt="Command: adb shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE", ln=1, align="L")
    pdf.multi_cell(200, 5, txt="Given that for this report an emulator was used, a screenshot of the command working wasn't able to be taken. Although, if the script is ran with an actual android device, is is guaranteed it will work.")

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf

    pdf.cell(200, 10, txt="5. Using ADB, launch the contacts app and add a new contact to the contact's list.",
             ln=1, align="L")
    pdf.cell(200, 10, txt="Command: adb shell input keyevent 207",
             ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/contacts_5.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(200, 10, txt="Command: adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Pedro Rosales' -e phone 3112142706")
    pdf.set_x(80)
    pdf.image(f"./images/contacts_6.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10, txt="Command: adb shell input tap 900 80",
             ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/contacts_7.png", w=60)
    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10, txt="Command: adb shell input keyevent 4",
             ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/contacts_8.png", w=60)

    eventCount += 1
    if check_event_count(n, eventCount):
        return pdf


def finishPDF(pdf, n):
    print("Finishing PDF...")
    if n != 10:
        fileName = f"report_{n}_events.pdf"
    else:
        fileName = "report.pdf"

    pdf.set_x(pdf.l_margin)
    pdf.cell(200, 10, txt="Uninstall apk.",
             ln=1, align="L")
    pdf.cell(200, 10, txt="Command: adb uninstall com.andminuniandes",
             ln=1, align="L")
    pdf.set_x(80)
    pdf.image(f"./images/apk_uninstalled_2.png", w=60)

    pdf.output(fileName)


if __name__ == "__main__":
    n = int(input("Enter the parameter N (Maximum is 10 events):"))
    if n > 10 or n < 1:
        n = 10
    device = main(n)
    uninstallAPK(device)
    print("ADB commands execution finished")
    pdf = createPDF(n)
    finishPDF(pdf, n)