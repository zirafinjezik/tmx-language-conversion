def convert_language_code(input_file, output_file):
    """
    Converts all en-US language codes in a TMX file to en-GB.
    Works with SDL-generated TMX files.
    """

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    replacements = {
        'xml:lang="en-US"': 'xml:lang="en-GB"',
        'srclang="en-US"': 'srclang="en-GB"',
        'adminlang="en-US"': 'adminlang="en-GB"',
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Conversion complete! Saved as: {output_file}")


if __name__ == "__main__":
    input_file = "sample_tmx/original_en-US.tmx"
    output_file = "sample_tmx/converted_en-GB_python.tmx"
    convert_language_code(input_file, output_file)
