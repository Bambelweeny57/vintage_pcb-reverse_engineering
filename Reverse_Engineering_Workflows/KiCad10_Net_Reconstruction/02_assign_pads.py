import pcbnew

board = pcbnew.GetBoard()
tracks = [t for t in board.GetTracks() if t.GetNetname() != ""]
footprints = board.GetFootprints()

count = sum(
    1
    for fp in footprints
    for pad in fp.Pads()
    if pad.GetNetname() == ""
    for track in tracks
    if track.HitTest(pad.GetPosition())
    and (pad.SetNet(track.GetNet()) or True)
)

if count > 0:
    pcbnew.Refresh()

print(f"Success! Automatically assigned nets to {count} pads.")