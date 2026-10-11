import pcbnew

b = pcbnew.GetBoard()
items = [t for t in b.GetTracks() if t.GetNetname() == ""]

visited = set()
netnum = 1

for seed in items:

    if id(seed) in visited:
        continue

    island = []
    queue = [seed]

    while queue:

        cur = queue.pop()

        if id(cur) in visited:
            continue

        visited.add(id(cur))
        island.append(cur)

        if type(cur).__name__ == "PCB_VIA":

            vp = cur.GetPosition()

            for o in items:

                if id(o) in visited:
                    continue

                if type(o).__name__ == "PCB_TRACK":

                    s = o.GetStart()
                    e = o.GetEnd()

                    if ((s.x == vp.x and s.y == vp.y) or
                        (e.x == vp.x and e.y == vp.y)):
                        queue.append(o)

        else:

            s = cur.GetStart()
            e = cur.GetEnd()
            layer = cur.GetLayer()

            for o in items:

                if id(o) in visited:
                    continue

                if type(o).__name__ == "PCB_VIA":

                    vp = o.GetPosition()

                    if ((vp.x == s.x and vp.y == s.y) or
                        (vp.x == e.x and vp.y == e.y)):
                        queue.append(o)

                elif type(o).__name__ == "PCB_TRACK":

                    if o.GetLayer() != layer:
                        continue

                    os = o.GetStart()
                    oe = o.GetEnd()

                    if (
                        (os.x == s.x and os.y == s.y) or
                        (oe.x == s.x and oe.y == s.y) or
                        (os.x == e.x and os.y == e.y) or
                        (oe.x == e.x and oe.y == e.y)
                    ):
                        queue.append(o)

    if island:

        net = pcbnew.NETINFO_ITEM(b, f"AUTO_{netnum:04d}")
        b.Add(net)

        for x in island:
            x.SetNet(net)

        print(f"AUTO_{netnum:04d} size={len(island)}")

        netnum += 1

pcbnew.Refresh()

print("Done")