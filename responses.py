from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup",):
        return "hey hows it going?"

    if user_message in ("who are you", "do i know you",):
        return "iam Nezuko"

    # if user_message in ("time", "time?"):
    #     now = datetime.now()
    #     datetime = now.strftime("%d/%m/%y, %H:%M:%S")
    #
    #     return str(datetime)

    return  "wrong command senpai"

