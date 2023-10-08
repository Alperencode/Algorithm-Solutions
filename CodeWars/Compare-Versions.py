def compare_versions(version1, version2):
    if not ("." in (version1 and version2)):
        return (False if version1 < version2 else True)
    version1, version2 = version1.split("."), version2.split(".")

    for index, item in enumerate(version2):
        try:
            if int(item) > int(version1[index]):
                return False
        except Exception:
            return False
    return True

# Testcases
# compare_versions("11", "10") True
# compare_versions("11", "11") True
# compare_versions("10.4.6", "10.4") True
# compare_versions("10.4", "10.4.8") False
# compare_versions("10.4", "11") False
# compare_versions("10.4", "10.10") False
# compare_versions("10.4.9", "10.5") False

# Status - Passed
