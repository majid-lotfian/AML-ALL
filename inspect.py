from __future__ import annotations

from pathlib import Path
import pandas as pd


def inspect_large_csv(
    input_file: str,
    output_columns_file: str = "all_columns.txt",
    output_preview_file: str = "first_10_rows.csv",
    sep: str = ",",
    encoding: str | None = None,
    nrows_preview: int = 10,
) -> None:
    """
    Inspect a very large CSV file safely by:
    1. Reading only the header (column names)
    2. Reading only the first few rows

    This avoids loading the full dataset into memory.
    """

    input_path = Path(input_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    print(f"Input file found: {input_path}")
    print("-" * 60)

    # Step A: read only the header
    header_df = pd.read_csv(
        input_path,
        sep=sep,
        encoding=encoding,
        nrows=0
    )

    columns = list(header_df.columns)

    print("All column names:")
    for i, col in enumerate(columns, start=1):
        print(f"{i:4d}. {col}")

    print("-" * 60)
    print(f"Total number of columns: {len(columns)}")

    # Save all column names to a text file
    with open(output_columns_file, "w", encoding="utf-8") as f:
        for i, col in enumerate(columns, start=1):
            f.write(f"{i}\t{col}\n")

    print(f"Column list saved to: {output_columns_file}")

    # Step B: read only first few rows
    preview_df = pd.read_csv(
        input_path,
        sep=sep,
        encoding=encoding,
        nrows=nrows_preview,
        low_memory=False
    )

    print("-" * 60)
    print(f"First {nrows_preview} rows:")
    print(preview_df)

    # Save preview rows to a small CSV file
    preview_df.to_csv(output_preview_file, index=False)
    print(f"Preview rows saved to: {output_preview_file}")

    print("-" * 60)
    print("Inspection finished successfully.")


if __name__ == "__main__":
    INPUT_FILE = r"big_file.csv"   # change this
    SEPARATOR = ","                # use "\t" for TSV
    ENCODING = None                # e.g. "utf-8" or "latin1"

    inspect_large_csv(
        input_file=INPUT_FILE,
        output_columns_file="all_columns.txt",
        output_preview_file="first_10_rows.csv",
        sep=SEPARATOR,
        encoding=ENCODING,
        nrows_preview=10,
    )
