import pathlib
import re
import sys

_thisdir = pathlib.Path(__file__).parent.resolve()
_importdir = (_thisdir.parent.parent / "autobaba").resolve()
sys.path.insert(0, str(_importdir))
import solutionformat as sf
sys.path.remove(str(_importdir))

filenametrans = {
    "?": "(q)",
}

atrans = (
    (
        """Ghost Guard, 100 with RNG & 114 without
(D2R2U2R1U1R5U3L2D1U1R1D2R2D1R1D1L4R2D2L3U1D1R2U1L1D1L1U2D1R3U1L2R1U1L1R5U1R1D1L1D1R1D1R1U3W1U1W1U1W1U1D1R2U2W1L2W1L1W1L1W1L1D2L1W1U1)
&
(D2R2U2L1U1R5W1R1W1D1R1U2L1D1R1D3L3U1D1R3U1L1U1L1D1R1D1L1R2U6L2D3U3R1D3R1L5U1L2D1R1W1R1W1R1W1R1W1R1W1R1D1R1W1U1W1U1W1U1W1U1W1U1D1R2U2L1W1L1W1L1W1L1W1L1D2L1W1U1)"""
        ,
        """Ghost Guard, 100?
(D2R2U2R1U1R5U3L2D1U1R1D2R2D1R1D1L4R2D2L3U1D1R2U1L1D1L1U2D1R3U1L2R1U1L1R5U1R1D1L1D1R1D1R1U3W1U1W1U1W1U1D1R2U2W1L2W1L1W1L1W1L1D2L1W1U1)

Ghost Guard, 114
(D2R2U2L1U1R5W1R1W1D1R1U2L1D1R1D3L3U1D1R3U1L1U1L1D1R1D1L1R2U6L2D3U3R1D3R1L5U1L2D1R1W1R1W1R1W1R1W1R1W1R1D1R1W1U1W1U1W1U1W1U1W1U1D1R2U2L1W1L1W1L1W1L1W1L1D2L1W1U1)"""
    ),
    (
        """Broken, 45 with RNG & 61 without
(L1D4R5W1R1W1D1R1U4L1D3R1U7L1U1L1D5L2U1D1U1D1) 
&
(L1D4R2D1R1U2D1R3U6R1U1L1U1L1D6L1D1L6D1R6D1R1U1W1U10)"""
        ,
        """Broken, 45?
(L1D4R5W1R1W1D1R1U4L1D3R1U7L1U1L1D5L2U1D1U1D1) 

Broken, 61
(L1D4R2D1R1U2D1R3U6R1U1L1U1L1D6L1D1L6D1R6D1R1U1W1U10)"""
    ),
    (
        "(U4R3U2L1U1R1D4L3U1L1D6U4R5U4L1U1W4R3L4D6L1D2L7U3D3R3U1R7U7R5D3U3L5D7R7D1R1U2D1R2U2L5U3L2U2R2D4U4L5D10L2D3L4D1R5D1R1U2L1U1R2L3U2L1U4Reset)"
    ,
        "(U4R3U2L1U1R1D4L3U1L1D6U4R5U4L1U1W4R3L4D6L1D2L7U3D3R3U1R7U7R5D3U3L5D7R7D1R1U2D1R2U2L5U3L2U2R2D4U4L5D10L2D3L4D1R5D1R1U2L1U1R2L3U2L1U4Z1)"
    ),
    (
        "Hazel Den, 54 with RNG, obviously",
        "Hazel Den, 54?"
    ),
    (
        """Mutual Feelings (Baba+Flag), 77 with RNG & 95 without
(U4R4U1R1D2U1R1U1R1D2L2D3L7U2R5U3R2D3R1D1L9D1L1U1R1U1L1U1L1D2W1D1U2R7)
&
(R5U1L2U3D1L3U1R6U1R3D1U1L2D1W1D1R1U1R1D2U3R1D3U3R1D3R1D1L8U1L4D1L1D1R1U2R2D1R1D1L1U2L1W1D2R7D1R1U1)"""
        ,
        """Mutual Feelings (Baba+Flag), 77?
(U4R4U1R1D2U1R1U1R1D2L2D3L7U2R5U3R2D3R1D1L9D1L1U1R1U1L1U1L1D2W1D1U2R7)

Mutual Feelings (Baba+Flag), 95
(R5U1L2U3D1L3U1R6U1R3D1U1L2D1W1D1R1U1R1D2U3R1D3U3R1D3R1D1L8U1L4D1L1D1R1U2R2D1R1D1L1U2L1W1D2R7D1R1U1)"""
    ),
    (
        "Heavy Words, 135 (R4D1L2R1L3U1L4D3R1D1L2R1U4R4D1L1U1L3D3L1D1R2L1U7L5U1L1R1L2D1R2L1R1L1R2U1R2D3L2D1R1L1R1L1R2U1R2D4R1D1L1U4R3D1L1U1L2D3R1D1L1U5L2D1R2D3R1D1R6)"
        ,
        """Heavy Words, 135
(R4D1L2R1L3U1L4D3R1D1L2R1U4R4D1L1U1L3D3L1D1R2L1U7L5U1L1R1L2D1R2L1R1L1R2U1R2D3L2D1R1L1R1L1R2U1R2D4R1D1L1U4R3D1L1U1L2D3R1D1L1U5L2D1R2D3R1D1R6)"""
    ),
    (
        "Lock The Door, 103 (R2D2L1D2R1L1U2R1D1L3D3U3L1D3R2D1L2R6D1R1U4R1L7U1L1D5R1D1L1U1L2D1R1L1U5L1R1D3R1D1R1U3R1U1L2U4R7U2R3)"
        ,
        """Lock The Door, 103
(R2D2L1D2R1L1U2R1D1L3D3U3L1D3R2D1L2R6D1R1U4R1L7U1L1D5R1D1L1U1L2D1R1L1U5L1R1D3R1D1R1U3R1U1L2U4R7U2R3)"""
    )
)

btrans = (
    (
        """[L] Level Fall-8, Ghost Guard, 100?
D2R2U2R-UR5U3L2-DURD2-R2DRD-L4R2D2L3-UDR2U-LDLU2-DR3UL2-RULR5-URDL-DRDR-U3WUW-UWUD-R2U2WL2-WLWL-WLD2L-WU

[L] Level Fall-8, Ghost Guard, 114
D2R2U2L-UR5WR-WDRU2-LDRD3-L3UDR3-ULUL-DRDL-R2U6L2D3-U3RD3R-L5UL2D-RWRW-RWRW-RWRD-RWUW-UWUW-UWUD-R2U2LW-LWLW-LWLD2-LWU"""
        ,
        """[L] Level Fall-8, Ghost Guard, 100? | [L] Level Fall-8, Ghost Guard, 114
D2R2U2R-UR5U3L2-DURD2-R2DRD-L4R2D2L3-UDR2U-LDLU2-DR3UL2-RULR5-URDL-DRDR-U3WUW-UWUD-R2U2WL2-WLWL-WLD2L-WU | D2R2U2L-UR5WR-WDRU2-LDRD3-L3UDR3-ULUL-DRDL-R2U6L2D3-U3RD3R-L5UL2D-RWRW-RWRW-RWRD-RWUW-UWUW-UWUD-R2U2LW-LWLW-LWLD2-LWU"""
    ),
    (
        """[L] Level Chasm-Extra 3, Broken, 45?
LD4R5W-RWDR-U4LD3R-U7LUL-D5L2UD-UD

[L] Level Chasm-Extra 3, Broken, 61
LD4R2D-RU2DR3-U6RUL-ULD6L-DL6DR6-DRUW-U10"""
        ,
        """[L] Level Chasm-Extra 3, Broken, 45? | [L] Level Chasm-Extra 3, Broken, 61
LD4R5W-RWDR-U4LD3R-U7LUL-D5L2UD-UD | LD4R2D-RU2DR3-U6RUL-ULD6L-DL6DR6-DRUW-U10"""
    ),
    (
        """[L] Level Meta-8, Mutual Feelings, LEVEL IS BABA, LEVEL IS FLAG, 77?
U4R4UR-D2URU-RD2L2D3-L7U2R5U3-R2D3RD-L9DLU-RULU-LD2WD-U2R7

[L] Level Meta-8, Mutual Feelings, LEVEL IS BABA, LEVEL IS FLAG, 95
R5UL2U3-DL3UR6-UR3DU-L2DWD-RURD2-U3RD3U3-RD3RD-L8UL4D-LDRU2-R2DRD-LU2LW-D2R7DR-U"""
        ,
        """[L] Level Meta-8, Mutual Feelings, LEVEL IS BABA, LEVEL IS FLAG, 77? | [L] Level Meta-8, Mutual Feelings, LEVEL IS BABA, LEVEL IS FLAG, 95
U4R4UR-D2URU-RD2L2D3-L7U2R5U3-R2D3RD-L9DLU-RULU-LD2WD-U2R7 | R5UL2U3-DL3UR6-UR3DU-L2DWD-RURD2-U3RD3U3-RD3RD-L8UL4D-LDRU2-R2DRD-LU2LW-D2R7DR-U"""
    ),
)

nametrans = {
    "Where Do I Go": "Where Do I Go?",
    "Now What Is This": "Now What Is This?",
    "But Where’s the Key": "But Where's the Key",
    "Hostile Environment (Flag)": "Hostile Environment, LEVEL IS FLAG",
    "Fragile Existence (Baba)": "Fragile Existence, LEVEL IS BABA",
    "Baba Doesn’t Respond": "Baba Doesn't Respond",
    "Turn The Corner (Baba)": "Turn The Corner, LEVEL IS BABA",
    "A Way Out (End)": "A Way Out?, FLAG IS END",
    "A Way Out (Win)": "A Way Out?",
    "Written Instructions (Win)": "Written Instructions",
    "Written Instructions (text_win)": "Written Instructions, LEVEL WRITE WIN",
    "Cleaning Service (Skull)": "Cleaning Service, LEVEL IS SKULL",
    "Crushers (Text)": "Crushers, LEVEL IS TEXT",
    "Living Lands (Me)": "Living Lands, LEVEL IS ME",
    "Booby Trap (Baba)": "Booby Trap, LEVEL IS BABA",
    "Avalanche (Baba)": "Avalanche, LEVEL IS BABA",
    "Booby Trap (Flag+Belt)": "Booby Trap, LEVEL IS BELT, LEVEL IS FLAG",
    "Mutual Feelings (Baba+Flag)": "Mutual Feelings, LEVEL IS BABA, LEVEL IS FLAG",
    "Booby Trap (Text+Flag)": "Booby Trap, LEVEL IS FLAG, LEVEL IS TEXT",
    "Tangle (Baba)": "Tangle, LEVEL IS BABA",
    "Breaking and Entering (Text)": "Breaking and Entering, LEVEL IS TEXT",
    "Return of Scenic Pond": "The Return of Scenic Pond",
    "The End (Done)": "The End, ALL IS DONE"
}

locationtrans = {
    "THE LAKE"       : "1. The Lake",
    "SOLITARY ISLAND": "2. Solitary Island",
    "TEMPLE RUINS"   : "3. Temple Ruins",
    "FOREST OF FALL" : "4. Forest of Fall",
    "DEEP FOREST"    : "5. Deep Forest",
    "ROCKET TRIP"    : "6. Rocket Trip",
    "FLOWER GARDEN"  : "7. Flower Garden",
    "CHASM"          : "8. Chasm",
    "VOLCANIC CAVERN": "9. Volcanic Cavern",
    "MOUNTAINTOP"    : "10. Mountaintop",
}

with (_thisdir.parent /"README.md").open("r", encoding="utf8") as f:
    _r = tuple(s.strip() for s in f.readlines())

r = {}
for i, line in enumerate(_r):
    m = re.search("^\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.+?)\|$", line)
    if not m:
        continue
    parts = (i,) +tuple(s.strip() for s in m.groups())
    key = (parts[3], parts[4])
    assert key not in r
    r[key] = parts
rmatch = {key[0].upper(): key[0] for key in r}
lmatch = {s.upper(): s for s in set(t[1] for t in r.values())}
lmatch["NULL"] = "Null"


with pathlib.Path("Baba Optimized Run.txt").open("r", encoding="utf8") as f:
    s_a1 = s_a0 = f.read()
    for t in atrans:
        s_a1 = s_a1.replace(t[0], t[1])
    a = tuple(s.strip() for s in s_a1.split("\n") if s.strip())

state = 0

b = []
c = []

def save():
    s_b = "\n\n".join(b)
    for t in btrans:
        s_b = s_b.replace(t[0], t[1])
    with pathlib.Path("out-walkthrough.txt").open("w", encoding="utf8") as f:
        f.write(s_b)
    s_c = "\n".join([t[1] for t in sorted(c)])
    with pathlib.Path("out-mdtable.txt").open("w", encoding="utf8") as f:
        f.write(s_c)


def getfilename(parts, steps, rng):
    if parts[2]:
        out_filename0 = f'{parts[2]}, {parts[3]}, {steps}{"?" * rng}.txt'
    else:
        out_filename0 = f'{parts[3]}, {steps}{"?" * rng}.txt'
    out_filename1 = "".join([filenametrans.get(c, c) for c in out_filename0])
    return out_filename1

i = 0

while True:
    line = a[i]
    if line == "Totals":
        break
    i += 1
    line_ = line.lower()
    if state == 0:
        if line_.startswith("section"):
            continue
        m0 = re.search("^(.+), (\d+)(\??)$", line)
        if m0:
            level, steps, rng = m0.groups()
            rng = bool(rng)
            level = nametrans.get(level, level)
            if level.endswith(" (Win)"):
                level = level[:-6]
            steps = int(steps)
            if level.upper() in rmatch:
                state = 1
                continue
            else:
                raise Exception
        line_mod = line.replace("Return to Map", "X1")
        m0 = re.search("^(.+), (\d+) \(([UDLRWXZ0-9]+)\)$", line_mod)
        if m0:
            location, steps, solution1 = m0.groups()
            location = lmatch[locationtrans.get(location.upper(), location).upper()]
            steps = int(steps)
            steps_calculated = sf.steps1(solution1)
            assert steps_calculated == steps
            b_line = f'[T] {location}, {steps}'
            b.append(f'{b_line}\n{sf.ensure1_v2(solution1)}')
            save()
            continue
        raise Exception
    elif state == 1:
        parts = r[(rmatch[level.upper()], f'{steps}{"?" * rng}')]
        m1 = re.search("^\(([UDLRWXZ0-9]+)\)$", line)
        if m1:
            solution1 = m1.groups()[0]
            steps_calculated = sf.steps1(solution1)
            assert steps_calculated == steps
            if parts[2]:
                b_line = f'[L] {parts[2]}, {parts[3]}, {steps}{"?" * rng}'
            else:
                b_line = f'[L] {parts[3]}, {steps}{"?" * rng}'
            b.append(f'{b_line}\n{sf.ensure1_v2(solution1)}')
            c_line = f'| {parts[1]} | {parts[2]} | {parts[3]} | {steps}{"?" * rng} | {parts[5]} |'
            c.append((parts[0], c_line))
            save()
            out_filename = getfilename(parts, steps, rng)
            out_path = _thisdir / "solutions" / out_filename
            with out_path.open("w") as f:
                f.write(sf.ensure1_v2(solution1))
            out_path = _thisdir / "solutions-multiline" / out_filename
            with out_path.open("w") as f:
                f.write(sf.convert1tox(solution1))
            state = 0
        else:
            raise Exception
    else:
        raise Exception
