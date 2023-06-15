import datetime
BOOK = [
    [
        "Square",
        [
            f"<center>{datetime.date.today()}</center>",
            *[f"<li>{x}^2 = {x**2}</li>" for x in range(100)]
        ]
    ]
]