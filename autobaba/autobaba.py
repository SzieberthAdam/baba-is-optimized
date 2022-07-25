import codecs
import pathlib
import sys

_thisdir = pathlib.Path(__file__).parent.resolve()

direction_fstr = """Send, {{{KEY} down}}
Sleep %KeyDownTime%
Send, {{{KEY} up}}
Sleep %BabaStepRelax%"""

key_dict = {
    "L": "Left",
    "R": "Right",
    "U": "Up",
    "D": "Down",
    ".": "Space",
}

key_dict2 = {
    "?": "",
    "y": "Sleep %NotYouRelax%",
    "t": "Sleep %TeleportRelax%",
    "w": "Sleep %WinRelax%",
}

baba_joiner = "\n\n"

if __name__ == "__main__":

    usage = """Usage: python autobaba.py [autobaba.txt] [templatefile.ahk]"""
    txt_missing = """ERROR: unable to locate autobaba TXT file"""
    ahk_missing = """ERROR: unable to locate autobaba AHK template file"""
    parse_error = """ERROR: unable to parse TXT file: {0}"""

    if len(sys.argv) == 1:
        txt_path = pathlib.Path("autobaba.txt")
    else:
        try:
            txt_path = pathlib.Path(sys.argv[1])
        except (IndexError, ValueError):
            print(usage)
            sys.exit(101)

    if not txt_path.is_file():
        print(txt_missing)
        print(usage)
        sys.exit(110)

    if len(sys.argv) == 3:
        try:
            ahk_path = pathlib.Path(sys.argv[2])
        except (IndexError, ValueError):
            print(usage)
            sys.exit(102)
        if not ahk_path.is_file():
            print(ahk_missing)
            print(usage)
            sys.exit(120)

    else:
        ahk_path = _thisdir / "autobaba-template.ahk"
        if not ahk_path.is_file():
            print(ahk_missing)
            sys.exit(20)

    if 3 < len(sys.argv):
        print(usage)
        sys.exit(109)

    with txt_path.open("rb") as f:
        program_bytes = f.read()

    if program_bytes.startswith(codecs.BOM_UTF8):
        program_text = program_bytes.decode("utf-8-sig")
    else:
        program_text = program_bytes.decode("utf-8")

    with ahk_path.open("rb") as f:
        ahk_bytes = f.read()

    if ahk_bytes.startswith(codecs.BOM_UTF8):
        ahk_text = ahk_bytes.decode("utf-8-sig")
    else:
        ahk_text = ahk_bytes.decode("utf-8")

    program = [s for s in program_text.strip().split("\n") if s]

    #print(program)

    baba = []

    for s in program:
        command, _, comment = s.partition("#")
        command = command.rstrip()
        comment = comment.lstrip()
        for c in command:
            if c.upper() in key_dict:
                key_key = c.upper()
                key = key_dict[key_key]
                direction_str = direction_fstr.format(KEY=key)
                baba.append(direction_str)
            elif c in key_dict2:
                baba.append(key_dict2[c])
            else:
                print(parse_error.format(c))
                sys.exit(200)

    baba_str = baba_joiner.join(baba)

    out_txt = ahk_text.replace("{{baba}}", baba_str).replace("\r\n", "\n")

    #print(out_txt)

    out_txt_path = txt_path.with_suffix(".ahk")

    with out_txt_path.open("w", encoding="utf8") as f:
        f.write(out_txt)
