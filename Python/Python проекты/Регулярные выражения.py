import re

regexp = re.compile(r"(?P<phone>(?P<country>(\+\d{1,3}-)?)(\d{3}-)?\d{3}-\d{4})")
lines = ["223-457-8900", "457-7891", "+17-457-7892", "+1-224-457-7893", "479 7989"]


def add_country_code(match_obj):
    # print("country:",match_obj.group("country"), type(match_obj.group("country")))
    if not match_obj.group("country"):
        #     print("none")
        return "+1-" + match_obj.group("phone")
    else:
        return match_obj.group("phone")


for line in lines:
    print(regexp.sub(add_country_code, line))
