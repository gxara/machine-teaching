def search(targetStr, character):
    found = False
    for eachChar in targetStr:
        if eachChar == character:
            found = True
    if not found:
        return False
    else:
        return True
