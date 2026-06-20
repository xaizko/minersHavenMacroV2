import mss

with mss.mss() as sct:
    for i, mon in enumerate(sct.monitors):
        print(f"{i}: left={mon['left']}, top={mon['top']}, width={mon['width']}, height={mon['height']}")