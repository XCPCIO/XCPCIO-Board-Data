import os

from xcpcio_board_spider import utils

import common

DATA_DIR = os.getenv(
    "DATA_DIR", "../../../../data/ccpc/9th/final")
FETCH_URI = os.getenv(
    "FETCH_URI", "./raw/formal")


def get_contest():
    c = common.get_basic_contest()

    c.contest_name = "第 9 届 CCPC 中国大学生程序设计竞赛总决赛"
    c.problem_quantity = 13
    c.start_time = utils.get_timestamp_second("2024-03-31 9:00:00")
    c.end_time = utils.get_timestamp_second("2024-03-31 14:00:00")

    c.fill_problem_id().fill_balloon_color()

    c.medal = {
        "official": {
            "gold": 12,
            "silver": 24,
            "bronze": 37,
        },
    }

    return c


def main():
    c = get_contest()
    common.work(DATA_DIR, FETCH_URI, c)


if __name__ == "__main__":
    main()
