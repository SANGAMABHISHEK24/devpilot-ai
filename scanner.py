from pathlib import Path

IGNORED_DIRS = {
    ".git", ".venv", "venv", "__pycache__", "node_modules",
    ".pytest_cache", "dist", "build"
}

def scan_repository(root: str, max_files: int = 500) -> list[dict]:
    """List source files without reading or executing their contents."""
    root_path = Path(root).expanduser().resolve()

    if not root_path.exists() or not root_path.is_dir():
        raise ValueError("Repository path must be an existing directory")

    results = []
    for path in root_path.rglob("*"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.is_file():
            results.append({
                "path": str(path.relative_to(root_path)),
                "suffix": path.suffix.lower(),
                "size_bytes": path.stat().st_size,
            })
            if len(results) >= max_files:
                break

    return results
