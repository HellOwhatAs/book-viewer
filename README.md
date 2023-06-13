# book-viewer
## Input
json format
```json
[
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
## Usage
```text
./index.html?json=<json_url>
```
Example: https://hellowhatas.github.io/book-viewer/?json=example/龙王：世界的重启.json
Example: https://hellowhatas.github.io/book-viewer/?json=example/Cycle_of_the_Werewolf.json

content string in json file is can contain html elements  
Example: https://hellowhatas.github.io/book-viewer/?json=example/grad-cam.json
Example: https://hellowhatas.github.io/book-viewer/?json=example/Skeleton_Crew.json

## Shortcut keys
- `ArrowRight`: next chapter
- `ArrowLeft`: previous chapter
- `-`: reduce font size
- `=`: increase font size
