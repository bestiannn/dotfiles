from libqtile.command.client import InteractiveCommandClient

client = InteractiveCommandClient()

screens = []
groups = []

for i in range(1, 7):
    if client.group[str(i)].info()["screen"] != None:
        screens.append(client.group[str(i)].info()["screen"])
        groups.append(client.group[str(i)].info()["name"])

if len(screens) == 2:
    client.group[groups[0]].toscreen(screens[1])
    client.group[groups[1]].toscreen(screens[0])