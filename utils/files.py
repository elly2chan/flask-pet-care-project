import json
import os
from pathlib import Path
from typing import Optional

from config import ROOT_DIR


def get_absolute_file_path(path: str | Path) -> str:
    """
    Get absolute path.

    :param path: relative path
    :return:
    """
    _path = Path(path)
    return os.path.join(ROOT_DIR, _path)


def get_json_file_content(path: str | Path, encoding: Optional[str] = "utf-8") -> dict | list:
    """
    Get JSON file content.

    :param path:
    :param encoding:
    :return:
    """
    with open(get_absolute_file_path(path), encoding=encoding) as f:
        return json.load(f)
