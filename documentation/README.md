# Understanding TMX Structure

TMX (Translation Memory eXchange) is an XML-based standard for exchanging translation memory data.

A TMX file contains:
- `<header>` — metadata including source language (srclang)
- `<body>` — translation units (TUs)
- `<tu>` — a translation unit
- `<tuv>` — a translation variant with a language code
- `<seg>` — the actual text segment

This repo demonstrates how to safely modify the language code in both the header and the TUV elements.
