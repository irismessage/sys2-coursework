from pathlib import Path

workdir = Path()
for folder in sorted(workdir.glob("question*/")):
    if not folder.is_dir():
        continue
    
    print("### Screenshots")
    for screenshot in sorted(folder.iterdir()):
        if not screenshot.suffix == ".png":
            continue
        print(f"![]({screenshot})\n")
