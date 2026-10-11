import pcbnew

b = pcbnew.GetBoard()

for net in b.GetNetInfo().NetsByNetcode().values():

    name = net.GetNetname()

    if not name.startswith("AUTO_"):
        continue

    pads = []

    for fp in b.GetFootprints():
        for pad in fp.Pads():
            if pad.GetNetname() == name:
                pads.append(
                    (
                        fp.GetReference().replace("",""),
                        str(pad.GetNumber())
                    )
                )

    if len(pads) < 2:
        continue

    pads = sorted(pads)

    newname = f"{pads[0][0]}_{pads[0][1]}_{pads[1][0]}_{pads[1][1]}"

    try:
        net.SetNetname(newname)
        print(f"{name} -> {newname}")
    except:
        pass

pcbnew.Refresh()

print("Finished")