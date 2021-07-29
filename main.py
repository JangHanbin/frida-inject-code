import frida
import sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message))
    else:
        print(message)


PACKAGE_NAME = ""

jscode ="""

var il2cpp = Module.getBaseAddress("libil2cpp.so");

console.log("[*] libil2cpp.so_base : " + il2cpp);
console.log(" ")
console.log(" ")



"""
try:
    print("[*] Get Device")

    android_device = frida.get_usb_device(1)
    print("    " + str(android_device))

    # for spawn application
    # pid = android_device.spawn(PACKAGE_NAME)
    # process = android_device.attach(pid)

    process = android_device.attach(PACKAGE_NAME)

    script = process.create_script(jscode)
    script.on('message', on_message)

    print('[*] Running Hook')
    script.load()
    sys.stdin.read()

except Exception as e:
    print(e)