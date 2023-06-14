# book-viewer
## Input
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
        ]
    ],
    [
        "chapter2",
        [
            "paragraph1",
            "paragraph2"
        ]
    ],
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
        ]
    ],
    [
        "chapter2",
        [
            "paragraph1",
            "paragraph2"
        ]
    ],
]
)
```
## Usage
### json format
**CANNOT CORS (Cross-Origin Resource Sharing)**
```text
./index.html?json=<json_url>
```
Example: https://hellowhatas.github.io/book-viewer/?json=example/龙王：世界的重启.json  
Example: https://hellowhatas.github.io/book-viewer/?json=example/Cycle_of_the_Werewolf.json  

content string in json file is can contain html elements  
Example: https://hellowhatas.github.io/book-viewer/?json=example/grad-cam.json  
Example: https://hellowhatas.github.io/book-viewer/?json=example/Skeleton_Crew.json  
Example: https://hellowhatas.github.io/book-viewer/?json=example/math.json  

### js format
**CAN CORS (Cross-Origin Resource Sharing) via JSONP**
```text
./index.html?js=<js_url>
```
Example: https://hellowhatas.github.io/book-viewer/?js=example/grad-cam.js  

## Shortcut keys
- `ArrowRight`: next chapter
- `ArrowLeft`: previous chapter
- `-`: reduce font size
- `=`: increase font size
