def convert_language_code(input_file, output_file):
    """
    Converts all en-US language codes in a TMX file to en-UK.
    Works with SDL-generated TMX files.
    """

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    replacements = {
        'xml:lang="en-US"': 'xml:lang="en-UK"',
        'srclang="en-US"': 'srclang="en-UK"',
        'adminlang="en-US"': 'adminlang="en-UK"',
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Conversion complete! Saved as: {output_file}")


if __name__ == "__main__":
    input_file = "sample_tmx/original_en-US.tmx"
    output_file = "sample_tmx/converted_en-UK_python.tmx"
    convert_language_code(input_file, output_file)
