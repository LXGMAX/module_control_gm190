import serial,re,time

port = "/dev/ttyS1"
brate = 115200

cmd_call = "AT+ZIPCALL=1\r\n"
cmd_at = "AT\r\n"

pat_at = r'\S[OK]+'
pat_call = r'\S[ZIPCALL]+'

s = serial.Serial(port, brate, timeout = 2)
s.flushInput()


def result(pat, rx):
    #print("result:", rx)
    r = re.findall(pat, rx)
    if len(r) > 0:
        print("succ", r)
        return True
    else:
        return False


def module_check():
    while True:
        s.write(cmd_at.encode("utf-8"))
        s.flushOutput()
        rx = s.read(s.in_waiting).decode("utf-8")
        #print("rx buff:", rx)
        if result(pat_at, rx) == True:
            break
    return True


try:
    module_check()
    time.sleep(1)
    s.flushInput()
    s.flushOutput()

    while True:
        w_bytes = s.write(cmd_call.encode("utf-8"))
        #s.flushInput()
        #s.flushOutput()
        rx = s.read(s.in_waiting).decode("utf-8")
        if result(pat_call, rx) == True:
            break
        else:
            print("err", rx)
            time.sleep(1)

    s.close()
    print("written:", w_bytes)

except Exception as e:
    print(e)
