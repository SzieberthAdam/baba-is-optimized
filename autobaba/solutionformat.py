import re

def compress1_1(solution1):
    return "".join(((t[0] if t[1] == 1 else f'{t[0]}{t[1]}') for t in split1_2(solution1)))

def compress1_2(solution1, section_length=4):
    sections = []
    section = []
    for i, t in enumerate(split1_2(solution1), 1):
        s = t[0] if t[1] == 1 else f'{t[0]}{t[1]}'
        section.append(s)
        if not i % section_length:
            sections.append(section)
            section = []
    if section:
        sections.append(section)
        section = []
    return "-".join(["".join(section) for section in sections])


def split1_1(solution1):
    return tuple(re.findall("[UDLRWXZ]\d*", solution1))

def split1_2(solution1):
    return tuple((s[0], int("".join(s[1:]) or "1")) for s in split1_1(solution1))

def steps1(solution1):
    return sum(t[1] for t in split1_2(solution1))


def convert1tox(solution1):
    steps = []
    for t in split1_2(solution1):
        for i in range(t[1]):
            steps.append(t[0])
    return "\n".join(steps)
