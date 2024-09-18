import math


def load_from_user(prompt="", default=0):
    user_data = input(prompt)
    try:
        out_data = float(user_data)
    except:
        parsed = user_data.split("(")
        try:
            if len(parsed) == 2:
                if parsed[0] == "sqrt":
                    out_data = math.sqrt(float(parsed[1][:-1]))
                elif parsed[0] == "log":
                    out_data = math.log(float(parsed[1][:-1]))
                else:
                    out_data = default
            else:
                out_data = default 
        except:
            out_data = default
    finally:
        return out_data