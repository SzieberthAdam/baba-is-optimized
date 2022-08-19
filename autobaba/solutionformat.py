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
    return "".join(f'{t[0]}{t[1]}' for t in split1_2(s1))


def split1_1(solution1):
    """splits a oneliner solution sting to substrings (does not add leftout 1s)"""
    return tuple(re.findall("[UDLRWXZ]\d*", solution1))


def split1_2(solution1):
    """splits a oneliner solution to tuple of tuples; second tuple has (direction::string, count::int) format"""
    return tuple((s[0], int("".join(s[1:]) or "1")) for s in split1_1(solution1))


def steps1(solution1):
    """calculates the nuber of steps of a oneliner solution"""
    return sum(t[1] for t in split1_2(solution1))


def convert1tox(solution1):
    """converts a oneliner solution to a one input per line format"""
    steps = []
    for t in split1_2(solution1):
        for i in range(t[1]):
            steps.append(t[0])
    return "\n".join(steps)
