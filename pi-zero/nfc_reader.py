import subprocess

def read_nfc():
    try:
        # Uses libnfc utilities installed on raspbian
        output = subprocess.check_output(["nfc-poll"], stderr=subprocess.STDOUT)
        for line in output.decode().splitlines():
            if "UID" in line:
                uid = line.split(":")[-1].strip()
                return f"nfc://{uid}"
    except:
        return "NFC_ERROR"
