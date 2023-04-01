from modules import Json

def gen_CONFIG():
    CONFIG: dict[str, dict] = {
        "HOST" : "",
        "PORT" : "",
        "DEBUG" : "",
    }

    CONFIG["HOST"] = input("Your server HOST:\n> ")
    CONFIG["PORT"] = int(input("Your server PORT:\n> "))
    CONFIG["DEBUG"] = bool(input("Debug mode:\n> "))

    Json.dump_nowait("config.json", CONFIG)