import re

regexp = re.compile(r"((\+)?\d[- ])?"
                    r"(\()?(?P<city>[2-9][0-8]\d)(\))?[-. ]"
                    r"(?P<socket>[2-9]\d{2})[-. ]"
                    r"(?P<station>\d{4})")

telnumbers = ["+1-223-487-7879", "+1 223-456-7890", "1-223-456-7890", "+1 223 456-7890", "(223) 456-7890",
              "1 223 456 7890", "223.456.7890", "(223( 456-7890", "(223).456.7890", "+1-134-456-7890",
              "+1-198-456-7890", "+1-298-456-7890", "+1-288-456-7890", "+1 (223.456.7890", "+1-(223.456.7890",
              "1-223).456-7890"]


def normalize_number(match_obj):
    return "-".join(["+1", match_obj.group("city"), match_obj.group("socket"), match_obj.group("station")])


for i in range(len(telnumbers)):
    if regexp.search(telnumbers[i]):
        telnumbers[i] = regexp.sub(normalize_number, telnumbers[i])
    else:
        # raise ValueError("Номер недействителен")
        print("Номер недействителен")
        continue
    print(telnumbers[i])
