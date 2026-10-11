import pcbnew, csv

board = pcbnew.GetBoard()

rows = []

for net in board.GetNetInfo().NetsByNetcode().values():

    netname = net.GetNetname()

    if not netname:
        continue

    pads = []

    for fp in board.GetFootprints():
        for pad in fp.Pads():
            if pad.GetNetname() == netname:
                pads.append(
                    f"{fp.GetReference()}:{pad.GetNumber()}"
                )

    pincount = len(pads)

    nettype = (
        "SINGLE" if pincount == 1 else
        "PAIR" if pincount == 2 else
        "MULTI"
    )

    rows.append([
        netname,
        pincount,
        nettype,
        ";".join(sorted(pads))
    ])

rows.sort(key=lambda r: (-r[1], r[0]))

outfile = r"C:\temp\net_report.csv"

with open(outfile, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow([
        "NetName",
        "PinCount",
        "NetType",
        "Pads"
    ])
    w.writerows(rows)

print(f"Report written: {outfile}")
print(f"Total nets: {len(rows)}")