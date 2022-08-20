import re


def d2solutionkey(d):
    if d["levelcode"]:
        s = f'{d["levelcode"]}, {d["levelname"]}, {d["solution-steps"]}{"?" * d["solution-rng"]}'
    else:
        s = f'{d["levelname"]}, {d["solution-steps"]}{"?" * d["solution-rng"]}'
    return s


def d2solutionfilename(d):
    tr = {
        "?": "(q)",
    }
    solution_key = d.get("solution-key", d2solutionkey(d))
    s = "solutions/" + "".join([tr.get(c, c) for c in solution_key]) + ".txt"
    return s


def d2solutionurl(d):
    tr = {
        " ": "%20",
        ",": "%2C",
    }
    solution_filename = d.get("solution-filename", d2solutionfilename(d))
    s = "".join([tr.get(c, c) for c in solution_filename])
    return s


def readmemdtableline2d(s, d=None):
    m = re.search("^\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", s)
    if not m:
        return None
    L = m.groups()
    d = d or {}
    d["location"] = L[0]
    d["levelcode"] = L[1]
    d["levelname"] = L[2]
    m = re.search('\[(\d+)(\??)\]\((.+)\)', L[3])
    if m:
        d["solution-steps"] = int(m.group(1))
        d["solution-rng"] = bool(m.group(2))
        d["solution-url"] = m.group(3)
    elif L[3][-1] == "?":
        d["solution-steps"] = int(L[3][:-1])
        d["solution-rng"] = True
        d["solution-url"] = None
    else:
        d["solution-steps"] = int(L[3])
        d["solution-rng"] = False
        d["solution-url"] = None
    d["solution-key"] = d2solutionkey(d)
    d["solution-filename"] = d2solutionfilename(d)
    solution_url = d2solutionurl(d)
    if not d["solution-url"]:
        d["solution-url"] = d2solutionurl(d)
    else:
        assert d["solution-url"] == d2solutionurl(d)
        #print([d["solution-url"], d2solutionurl(d)])
    d["optimizedby"] = L[4]
    return d


def d2readmetableline(d):
    if d.get("solution-url"):
        s = f'| {d["location"]} | {d["levelcode"]} | {d["levelname"]} | [{d["solution-steps"]}{"?" * d["solution-rng"]}]({d["solution-url"]}) | {d["optimizedby"]} |'
    else:
        s = f'| {d["location"]} | {d["levelcode"]} | {d["levelname"]} | {d["solution-steps"]}{"?" * d["solution-rng"]} | {d["optimizedby"]} |'
    return s


def srefreshreadmemd(path):
    ignorestartswiths = ("| Location |", "| -------- |")
    with open(str(path), "r", encoding="utf8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if any(line.startswith(s) for s in ignorestartswiths):
            continue
        d = readmemdtableline2d(line)
        if d:
            new_line = d2readmetableline(d) + "\n"
            lines[i] = new_line
    s = "".join(lines)
    return s


def updatereadmemd(path):
    s = srefreshreadmemd(path)
    with open(str(path), "w", encoding="utf8") as f:
        f.write(s)
