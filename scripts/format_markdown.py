import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

CODE_PREFIXES = (
    "#include",
    "using",
    "int ",
    "long",
    "float",
    "double",
    "char",
    "return",
    "cout",
    "cin",
    "void",
    "std::",
    "for",
    "while",
    "do",
    "if",
    "else",
    "switch",
    "case",
    "break",
    "continue",
    "const",
    "class",
    "struct",
    "public",
    "private",
    "protected",
    "auto",
    "namespace",
    "main",
    "printf",
    "scanf",
)


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9\s-]", "", text.lower())
    slug = re.sub(r"\s+", "-", slug).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug or "section"


def is_heading(line: str) -> bool:
    return bool(re.match(r"^#+\s", line.strip()))


def is_code_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped in {"{", "}"}:
        return True
    return stripped.startswith(CODE_PREFIXES) or stripped.endswith(";") or stripped.startswith("//")


def normalize_title(line: str) -> str:
    title = line.lstrip("# ").strip()
    return f"# {title}"


def add_overview(body_lines: list[str]) -> list[str]:
    if not body_lines:
        return []
    while body_lines and not body_lines[0].strip():
        body_lines = body_lines[1:]
    if not body_lines:
        return []
    first = body_lines[0].strip().lower()
    if is_heading(body_lines[0]) and first.startswith("## overview"):
        return body_lines
    if is_heading(body_lines[0]):
        return body_lines
    result = ["## Overview", ""]
    return result + body_lines


def build_toc(lines: list[str]) -> list[str]:
    toc = []
    for line in lines:
        if is_heading(line):
            level = len(line) - len(line.lstrip("#"))
            if level < 2:
                continue
            title = line.lstrip("# ").strip()
            indent = "  " * (level - 2)
            toc.append(f"{indent}- [{title}](#{slugify(title)})")
    return toc


def strip_existing_toc(content: list[str]) -> list[str]:
    cleaned: list[str] = []
    i = 0
    while i < len(content):
        line = content[i]
        stripped = line.strip().lower()
        if stripped == "## table of contents":
            i += 1
            while i < len(content) and (content[i].strip().startswith("-") or not content[i].strip()):
                i += 1
            continue
        cleaned.append(line)
        i += 1
    return cleaned


def collect_code_block(content: list[str], start_index: int) -> tuple[list[str], int]:
    code_lines: list[str] = []
    i = start_index
    while i < len(content) and not content[i].strip():
        i += 1
    while i < len(content):
        candidate = content[i]
        if candidate.strip() == "":
            if (i + 1 < len(content)) and is_code_line(content[i + 1]):
                code_lines.append(candidate)
                i += 1
                continue
            break
        lowered_candidate = candidate.strip().lower()
        if is_heading(candidate) or lowered_candidate == "example" or lowered_candidate.startswith("## example"):
            break
        if not is_code_line(candidate):
            break
        code_lines.append(candidate)
        i += 1
    return code_lines, i


def format_file(path: Path) -> None:
    raw_lines = path.read_text(encoding="utf-8").splitlines()
    if not raw_lines:
        return

    idx = 0
    while idx < len(raw_lines) and not raw_lines[idx].strip():
        idx += 1
    if idx == len(raw_lines):
        return

    title_line = normalize_title(raw_lines[idx])
    content = strip_existing_toc(raw_lines[idx + 1 :])

    transformed: list[str] = []
    example_count = 0
    i = 0
    while i < len(content):
        line = content[i]
        stripped = line.strip()
        lowered = stripped.lower()
        if lowered == "example":
            example_count += 1
            transformed.append(f"## Example {example_count}")
            transformed.append("")
            code_lines, i = collect_code_block(content, i + 1)
            if code_lines:
                transformed.append("```cpp")
                transformed.extend(code_lines)
                transformed.append("```")
                transformed.append("")
            continue
        if lowered.startswith("## example"):
            transformed.append(line)
            transformed.append("")
            code_lines, i = collect_code_block(content, i + 1)
            if code_lines:
                transformed.append("```cpp")
                transformed.extend(code_lines)
                transformed.append("```")
                transformed.append("")
            continue
        transformed.append(line)
        i += 1

    body_lines = [l.rstrip() for l in transformed if l is not None]
    body_lines = add_overview(body_lines)

    toc_lines = build_toc([title_line] + body_lines)

    final_lines = [title_line, "", "## Table of Contents", ""]
    final_lines.extend(toc_lines)
    if toc_lines:
        final_lines.append("")
    final_lines.extend(body_lines)

    path.write_text("\n".join(final_lines).rstrip("\n") + "\n", encoding="utf-8")


def main() -> None:
    for md_path in REPO_ROOT.rglob("*.md"):
        if md_path.is_dir():
            continue
        format_file(md_path)


if __name__ == "__main__":
    main()
