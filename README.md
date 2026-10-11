<p align="center">
<img src="images/banner.png
</p>

# Vintage PCB Reverse Engineering

A collection of workflows, tools, notes and projects related to the reverse engineering, preservation and reconstruction of vintage computer hardware.

The goal of this repository is to document practical techniques that help turn surviving boards, Gerbers, photographs and schematics into maintainable modern design files.

Many historic computer projects exist only as aging hardware, incomplete documentation or archived manufacturing data. Reverse engineering allows these designs to be preserved, studied, repaired and reproduced for future generations.

---

## Objectives

This repository aims to:

- Preserve vintage computer hardware designs.
- Document reverse engineering methodologies.
- Share repeatable KiCad workflows.
- Reconstruct netlists from Gerbers.
- Recreate schematics from surviving boards.
- Document lessons learned.
- Help others avoid repeating dead ends.
- Support the vintage computing community.

---

## Current Projects

### OSI 600D Superboard II

Reverse engineering work based on Gerber data provided by Grant ("Kayball") for a modified Ohio Scientific 600D Superboard II motherboard featuring Cherry keyboard switches and ROM modifications.

This project became the catalyst for developing a repeatable KiCad net reconstruction workflow.

---

## Reverse Engineering Workflow

One of the biggest challenges when working from Gerbers is that the copper geometry exists but all net information has been lost.

To address this, the repository includes a complete KiCad 10 workflow for reconstructing connectivity information:

    Unnamed Copper
          ↓
    Auto Named Islands
          ↓
    Pad Assignment
          ↓
    Automatic Point-To-Point Naming
          ↓
    CSV Analysis
          ↓
    Manual Signal Identification

The workflow can dramatically reduce the effort required to reconstruct a usable netlist.

See:

    Reverse_Engineering_Workflows/
    └── KiCad10_Net_Reconstruction/

for details.

---

## Philosophy

The purpose of reverse engineering is not merely to clone hardware.

It is to capture and preserve design intent.

Tracks, vias and components can often be reconstructed from Gerbers or scans, but understanding why a design works and documenting that knowledge is equally important.

Where possible this repository favours:

- Open documentation
- Reproducible workflows
- KiCad source files
- Learning by doing
- Community collaboration

---

## Tools

Current workflows primarily use:

- KiCad 10
- Python
- Excel
- Gerber imports
- Visual schematic reconstruction

Additional tooling and automation may be added over time.

---

## Contributions

Contributions are welcome.

If you have experience reverse engineering vintage hardware, improving KiCad workflows or preserving historical computer designs, feel free to raise an issue or submit a pull request.

---

## Acknowledgements

Special thanks to the vintage computing community and the many enthusiasts who preserve rare hardware, documentation and manufacturing data that would otherwise be lost.

Additional thanks to Grant ("Kayball") for making available the OSI 600D Superboard II Gerber data that inspired the initial workflow development.

---

## License

Unless otherwise noted, documentation and scripts in this repository are released under the MIT License.