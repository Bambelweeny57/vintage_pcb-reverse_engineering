# KiCad 10 Reverse Engineering Net Reconstruction Scripts

A collection of KiCad 10 Python scripts developed while reverse engineering a 2-layer PCB from imported Gerbers.

These scripts automate much of the tedious work involved in reconstructing a netlist from imported copper tracks and vias that have no original net information.

The workflow was developed while reconstructing a vintage computer motherboard but should be useful for many 2-layer Gerber-only reverse engineering projects.

---

## Files

    01_name_islands.py
    02_assign_pads.py
    03_rename_from_pads.py
    04_net_report.py

---

## Workflow

Run the scripts in the following order:

    01_name_islands.py
            ↓
    02_assign_pads.py
            ↓
    03_rename_from_pads.py
            ↓
    04_net_report.py
            ↓
      Excel Review
            ↓
     Manual Signal Naming

---

## 01_name_islands.py

### Purpose

Finds groups of electrically connected tracks and vias that do not currently belong to a net.

Each isolated copper island is assigned a unique automatically generated net name.

### Example Output

    AUTO_0001
    AUTO_0002
    AUTO_0003
    ...

### Result

Before:

    Unnamed Track
         │
        Via
         │
    Unnamed Track

After:

    AUTO_0001
         │
        Via
         │
    AUTO_0001

This creates a starting netlist from otherwise unnamed copper.

---

## 02_assign_pads.py

### Purpose

Assigns nets to component pads that physically touch tracks belonging to an existing net.

### Example

Before:

    Pad Net   = ""
    Track Net = AUTO_0042

After:

    Pad Net   = AUTO_0042
    Track Net = AUTO_0042

### Result

Component pins become connected to the reconstructed netlist.

This is the step that links the physical components into the connectivity graph.

---

## 03_rename_from_pads.py

### Purpose

Automatically renames simple point-to-point nets using the references and pin numbers of the first two connected pads.

### Example

Before:

    AUTO_0123

Connected Pads:

    U2 Pin 13
    U5 Pin 4

After:

    U2_13_U5_4

### Result

Anonymous AUTO_xxxx nets become meaningful connectivity names.

This makes tracing signals significantly easier during reverse engineering.

---

## 04_net_report.py

### Purpose

Generates a CSV report containing every net found on the board.

### Output File

    C:\temp\net_report.csv

### CSV Columns

| Column | Description |
|----------|----------|
| NetName | Current net name |
| PinCount | Number of connected pads |
| NetType | SINGLE, PAIR or MULTI |
| Pads | Complete list of connected pads |

### Example CSV

    NetName,PinCount,NetType,Pads
    GND,128,MULTI,...
    +5V,54,MULTI,...
    WKB,5,MULTI,U2:13;U2:4;U3:13;U3:4;U20:10
    U5_12_U7_9,2,PAIR,U5:12;U7:9
    AUTO_0421,1,SINGLE,MH1:1

### Net Types

MULTI

    More than two connected pads

Typically:

    Power rails
    Address buses
    Data buses
    Clock signals
    Reset signals
    Keyboard matrix signals
    Shared logic signals

PAIR

    Exactly two connected pads

Typically:

    Point-to-point connections

SINGLE

    One connected pad only

Typically:

    Mounting holes
    Test points
    Unconnected pads
    Missed assignments

### Why This Is Useful

Open the CSV in Excel and filter by NetType.

Review all MULTI nets first.

These are usually the nets that require manual identification and naming.

Once the MULTI nets have been named, most remaining nets are already sufficiently identified or are simple single-pin connections.

---

## Running the Scripts

Save all scripts somewhere accessible.

Example:

    C:\temp\01_name_islands.py
    C:\temp\02_assign_pads.py
    C:\temp\03_rename_from_pads.py
    C:\temp\04_net_report.py

Open:

    PCB Editor
    → Tools
    → Scripting Console

Run a script using:

    exec(open(r"C:\temp\01_name_islands.py").read())

Then:

    exec(open(r"C:\temp\02_assign_pads.py").read())

Then:

    exec(open(r"C:\temp\03_rename_from_pads.py").read())

Then:

    exec(open(r"C:\temp\04_net_report.py").read())

---

## Suggested Reverse Engineering Workflow

1. Import the Gerber files into KiCad.

2. Create or place component footprints.

3. Run 01_name_islands.py.

4. Run 02_assign_pads.py.

5. Run 03_rename_from_pads.py.

6. Run 04_net_report.py.

7. Open net_report.csv in Excel.

8. Filter for MULTI nets.

9. Identify and rename shared signals.

10. Review any remaining SINGLE nets.

11. Continue schematic capture using the reconstructed netlist.