from cx_Freeze import setup, Executable
import os

# Inclure des fichiers supplémentaires (dossiers de classes et fichiers JSON)
include_files = [
    ("classes/", "classes/")
]

# Configuration de cx_Freeze
setup(
    name="Game App",
    version="1.0",
    description="Application de gestion de jeux",
    options={
        "build_exe": {
            "packages": ["os"],
            "include_files": include_files,
        }
    },
    executables=[Executable("main.py", base=None)]
)
