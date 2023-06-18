# book-viewer on windows
## C++ Dependency
- C++ 17
- https://github.com/webview/webview  
  removed `private:` in [line 2007 of `webview.h`](https://github.com/webview/webview/blob/899018ad0e5cc22a18cd734393ccae4d55e3b2b4/webview.h#LL2007C1-L2007C1) to expose `m_webview`
- https://github.com/nlohmann/json
## Input
### python (json) format
The python code is executed using [brython](https://github.com/brython-dev/brython)  
`BOOK` indicates the input data
```py
BOOK = [
    # annotation
    {
        "tag":"script",
        "src": "<js_url>"
    },
    {
        "tag": "script",
        "innerText": r"""
                      multi lime js code
                      with escape char
                      """
    },
    [
        "chapter1",
        [
            r"paragraph1 with escape char",
            r"paragraph2 with escape char"
        ],
        r"// js code (page command 1) with escape char",
        r"// js code (page command 2) with escape char"
    ],
    [
        "chapter2",
        [
            r"paragraph1 with escape char",
            r"paragraph2 with escape char"
        ]
    ],
    r"// js code (every page command 1) with escape char",
    r"// js code (every page command 2) with escape char"
]
```
### json format
```json
[
    {
        "tag":"script",
        "src": "<js_url>"
    },
    {
        "tag": "script",
        "innerText": "// js code"
    },
    [
        "chapter1",
        [
            "paragraph1",
            "paragraph2"
        ],
        "// js code (page command 1)",
        "// js code (page command 2)"
    ],
    [
        "chapter2",
        [
            "paragraph1",
            "paragraph2"
        ]
    ],
    "// js code (every page command 1)",
    "// js code (every page command 2)"
]
```
## Usage
### python (json) format
```text
book-viewer.exe <path to py>
```

### json format
```text
book-viewer.exe <path to json>
```
## Shortcut keys
- `ArrowRight`: next chapter
- `ArrowLeft`: previous chapter
- `-`: reduce font size
- `=`: increase font size
- `F11` toggle fullscreen
## Advanced
### user scripts & links
**functions once** before the rendering of any chapter.
```json
[
    {
        "tag":"script",
        "src": "<js_url>"
    },
    {
        "tag": "script",
        "innerText": "// js code"
    },
    {
        "tag": "link",
        "rel": "stylesheet",
        "href": "<css_url>"
    },
]
```
### page commands
functions each time this page finishes writing.
```json
[
    [
        "chapter1",
        [
            "paragraph1",
            "paragraph2"
        ],
        "// js code (page command 1)",
        "// js code (page command 2)"
    ]
]
```
### each page commands
functions after [page commands](#page-commands) finishes on each page.
```json
[
    "// js code (every page command 1)",
    "// js code (every page command 2)"
]
```
