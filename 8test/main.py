import re
from pprint import pprint


def var3(data):
    pattern = r"set *(.*?) *is *#\((.*?)\)"
    parsed = re.findall(pattern, data)
    return {key: list(map(int, value.replace(' ', '').split('.')))
            for key, value in parsed}


data3 = (
    "\\begin\\begin set leat is #( 123 . 6436 . 805 ). \end,"
    "\\begin set tiquso is #(760 . 6334 . 634634). \end, "
    "\\begin set tebeen is #( 52423 . 5252 . 338 . 3642347 ). \end, \end"
)

pprint(var3(data3), sort_dicts=False)
#https://github.com/manticgaga