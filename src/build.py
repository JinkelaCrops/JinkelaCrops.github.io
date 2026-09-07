from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
(root / "assets").mkdir(exist_ok=True)
shutil.copyfile(root / "src/index.html", root / "index.html")
for name in ("site.css", "site.js"):
    shutil.copyfile(root / "src" / name, root / "assets" / name)
