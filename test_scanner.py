from repository.scanner import scan_repository

def test_scan_repository_lists_files(tmp_path):
    (tmp_path / "hello.py").write_text("print('hello')", encoding="utf-8")
    results = scan_repository(str(tmp_path))
    assert any(item["path"] == "hello.py" for item in results)
