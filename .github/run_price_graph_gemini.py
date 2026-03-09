"""Run price_graph.py with Google Gemini instead of OpenAI."""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "langgraph" / "price_graph.py"

OPENAI_MODEL_LINE = 'model = ChatOpenAI(model="gpt-4o-mini", temperature=0)'

GEMINI_COMMENTED = """\
# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0,
#     google_api_key=os.environ["GEMINI_API_KEY"],
# )"""

GEMINI_UNCOMMENTED = """\
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.environ["GEMINI_API_KEY"],
)"""


def main():
    original = SCRIPT.read_text()

    patched = original.replace(OPENAI_MODEL_LINE, f"# {OPENAI_MODEL_LINE}")
    patched = patched.replace(GEMINI_COMMENTED, GEMINI_UNCOMMENTED)

    if patched == original:
        print("ERROR: patching had no effect — file may have changed", file=sys.stderr)
        return 1

    SCRIPT.write_text(patched)
    try:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], capture_output=True, text=True
        )
        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
        return result.returncode
    finally:
        SCRIPT.write_text(original)


if __name__ == "__main__":
    sys.exit(main())
