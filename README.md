# book-viewer
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
### js format
for JSONP
```json
mainfunc(
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
)
```
## Usage
### python (json) format
```text
./index.html?py=<python_url>
```
**CANNOT CORS (Cross-Origin Resource Sharing)**  
**Example:** https://hellowhatas.github.io/book-viewer/?py=example/math.py  
**Example:** https://hellowhatas.github.io/book-viewer/?py=example/square.py  
### json format
**CANNOT CORS (Cross-Origin Resource Sharing)**
```text
./index.html?json=<json_url>
```
**Example:** https://hellowhatas.github.io/book-viewer/?json=example/龙王：世界的重启.json  
**Example:** https://hellowhatas.github.io/book-viewer/?json=example/Cycle_of_the_Werewolf.json  

content string in json file is can contain html elements  
**Example:** https://hellowhatas.github.io/book-viewer/?json=example/grad-cam.json  
**Example:** https://hellowhatas.github.io/book-viewer/?json=example/Skeleton_Crew.json  
**Example:** https://hellowhatas.github.io/book-viewer/?json=example/math.json  

### js format
**CAN CORS (Cross-Origin Resource Sharing) via JSONP**
```text
./index.html?js=<js_url>
```
**Example:** https://hellowhatas.github.io/book-viewer/?js=example/grad-cam.js  

## Shortcut keys
- `ArrowRight`: next chapter
- `ArrowLeft`: previous chapter
- `-`: reduce font size
- `=`: increase font size

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
