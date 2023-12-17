# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald


def old_macdonald(name):
    return name[:3].capitalize() + name[3:].capitalize() # name[:3] is the first 3 letters of the name, name[3:] is the rest of the name

print(old_macdonald('macdonald'))  # MacDonald