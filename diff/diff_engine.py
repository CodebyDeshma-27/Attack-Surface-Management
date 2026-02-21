def diff_scans(old, new):
    old_set = {(o["host"], o["port"], o["service"], o["version"]) for o in old}
    new_set = {(n["host"], n["port"], n["service"], n["version"]) for n in new}

    added = new_set - old_set
    removed = old_set - new_set

    return {
        "added": list(added),
        "removed": list(removed)
    }
