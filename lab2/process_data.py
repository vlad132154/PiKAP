import json
import os
import sys

try:
    from .print_result import print_result
    from .cm_timer import cm_timer_1
    from .unique import Unique
    from .gen_random import gen_random
    from .field import field
except ImportError:
    from print_result import print_result
    from cm_timer import cm_timer_1
    from unique import Unique
    from gen_random import gen_random
    from field import field


path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(__file__), "data_light.json"
)

with open(path, encoding="utf-8") as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, "job-name"), ignore_case=True), key=str.lower)


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    return [f"{spec}, зарплата {salary} руб." for spec, salary in zip(arg, salaries)]


if __name__ == "__main__":
    with cm_timer_1():
        f4(f3(f2(f1(data))))