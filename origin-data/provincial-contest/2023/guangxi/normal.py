import os

from xcpcio_board_spider import utils

import common

DATA_DIR = os.getenv(
    "DATA_DIR", "../../../../data/provincial-contest/2023/guangxi")


def get_contest():
    c = common.get_basic_contest()

    c.contest_name = "2023 年第六届广西大学生程序设计竞赛（正式赛）"
    c.problem_quantity = 13
    c.start_time = utils.get_timestamp_second("2023-06-04 09:00:00")
    c.end_time = utils.get_timestamp_second("2023-06-04 14:00:00")

    c.fill_problem_id().fill_balloon_color()

    return c


def main():
    common.work(DATA_DIR, get_contest(), 59040)


main()
