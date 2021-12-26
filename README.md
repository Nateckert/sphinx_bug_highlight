# Steps to reproduce the bug from scratch

```bat
pip install Sphinx==4.3.2
pip install PySide6==6.2.2.1

cd .\docs
sphinx-quickstart
```

Edit `docs\source\conf.py` to add: 

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

extensions = ['sphinx.ext.autodoc']
```

Build the doc from the root folder:

```bat
cd ..
scripts\build _doc.ps1
```