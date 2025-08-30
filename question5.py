def find_duplicates(strings):
    seen = {}
    duplicates = []
    for s in strings:
        if s in seen:
            if seen[s] == 1:
                duplicates.append(s)
            seen[s] += 1
        else:
            seen[s] = 1
    return duplicates
my_list = ["ae86" , "aw11" , "ae86" , "fd3s" , "aw11" , "ae85" , "fc3s" , "fd3s"]
dupes = find_duplicates(my_list)
print("duplicates found on your list are these items: ", dupes)