# Ludicrousspeed
To conflict with Lightspeed AI

## Purpose
This product takes a query that you would like to know, does not use AI, and provides you with the ability to copy a URL and paste it in your browser to ask a common search engine the question instead of using AI. Further lack of AI is provided by the `-x` or `--excludeai` flag which returns the same query in URL form, but with the AI results excluded. Because this product uses an executable named `c`, it conflicts with the Lightspeed package provided with Red Had OpenShift.

## Installation
Use the YUM/DNF (as applicable) package manager to install the package and required dependencies.
```bash
dnf install ludicrousspeed
```

## Usage

```bash
c [-y] [[-bdgvx] query]
```

Takes in a query and returns a URL to a search engine for your query.

positional arguments:

- `query`             Query you wish to ask the AI gods.

options:

- `-h`, `--help`        show help message and exit
- `-b`, `--bing`        Calculates Bing URL.
- `-d`, `--duckduckgo`  Calculates DuckDuckGo URL.
- `-g`, `--google`      Calculates Google URL (default functionality).
- `-v`, `--verbose`     Verbose
- `-x`, `--excludeai`   Exclude AI results (where applicable).
- `-y`, `--yogurt`      Expresses opinions on Yogurt during query.

> [!TIP]
> You can use the `-y` flag with or without a subsequent `query`.
> If `-h` or `-y` is not used, then a `query` is required.
