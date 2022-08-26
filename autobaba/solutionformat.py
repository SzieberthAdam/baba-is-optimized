import re

def compress1(solution1):
    """does a level 1 compress a oneliner solution; drops 1s after direction characters"""
    return "".join(((t[0] if t[1] == 1 else f'{t[0]}{t[1]}') for t in split1_2(solution1)))


def sectionize1(solution1, compress=True, section_length=4):
    """sectionize a oneliner solution; adds dashes after certain number of move definitions"""
    sections = []
    section = []
    for i, t in enumerate(split1_2(solution1), 1):
        s = t[0] if (compress and t[1] == 1) else f'{t[0]}{t[1]}'
        section.append(s)
        if not i % section_length:
            sections.append(section)
            section = []
    if section:
        sections.append(section)
        section = []
    return "-".join(["".join(section) for section in sections])


def decompress1(solution1):
    """converts a oneliner solution to its decompressed format; adds leftout 1s; without dashes"""
    return "".join(f'{t[0]}{t[1]}' for t in split1_2(solution1))


def ensure1_v1(solution1):
    """ensures version 1 oneliner solution format; with explicit 1s and without dashes"""
    return decompress1(solution1)


def ensure1_v2(solution1):
    """ensures version 2 oneliner solution format; without 1s and with dashes"""
    return sectionize1(solution1)


def split1_1(solution1):
    """splits a oneliner solution sting to substrings (does not add leftout 1s)"""
    return tuple(re.findall("[UDLRWXZ]\d*", solution1))


def split1_2(solution1):
    """splits a oneliner solution to tuple of tuples; second tuple has (direction::string, count::int) format"""
    return tuple((s[0], int("".join(s[1:]) or "1")) for s in split1_1(solution1))


def steps1(solution1):
    """calculates the number of steps of a oneliner solution"""
    return sum(t[1] for t in split1_2(solution1))


def convert1tox(solution1):
    """converts a oneliner solution to a one input per line format"""
    steps = []
    for t in split1_2(solution1):
        for i in range(t[1]):
            steps.append(t[0])
    return "\n".join(steps)


def splitx_1(solutionx):
    result = []
    program = [s for s in program_text.strip().split("\n") if s]
    lastaction = None
    lastactioncount = 0
    for s in program:
        command, _, comment = s.partition("#")
        command = command.rstrip()
        comment = comment.lstrip()
        while command[0] not in "UDLRWXZ":
            if command[0] in "?":
                result.append("#random-dependent")
                command = command[1:]
                continue
            if command[0] in "w":
                result.append("#win-next")
                command = command[1:]
                continue
            raise AssertionError
        assert command[0] in "UDLRWXZ"
        result.append(command[0])
        command = command[1:]
        while command[0]:
            if command[0] in "y":
                result.append("#not-is-you")
                command = command[1:]
                continue
            raise AssertionError
    return tuple(result)


def splitx_2(solutionx):
    result = []
    lastaction = None
    lastactioncount = 0
    for action in splitx_1(solutionx):
        if action not in "UDLRWXZ":
            continue
        if action == lastaction:
            lastactioncount += 1
        else:
            if lastaction is not None:
                result.append((lastaction, lastactioncount))
            lastaction = action
            lastactioncount = 1
    if lastaction is not None::
        result.append((lastaction, lastactioncount))
    return tuple(result)


def convertxto1_v1(solutionx):
    """converts a one input per line solution to a oneliner (version 1) format"""
    return "".join(f'{t[0]}{t[1]}' for t in splitx_2(solutionx))


def convertxto1_v2(solutionx):
    """converts a one input per line solution to a oneliner (version 2) format"""
    return sectionize1(convertxto1_v1(solutionx))
