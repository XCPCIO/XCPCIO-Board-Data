import os

from xcpcio_board_spider import utils

import common

DATA_DIR = os.getenv(
    "DATA_DIR", "../../../../data/ccpc/9th/jiangsu-and-xiangtan-warmup")
FETCH_JS_URI = os.getenv(
    "FETCH_JS_URI", "../../../../data/provincial-contest/2023/jiangsu-warmup")
FETCH_XT_URI = os.getenv(
    "FETCH_XT_URI", "../../../../data/ccpc/9th/xiangtan-invitational-warmup")


def get_contest():
    c = common.get_basic_contest()

    c.contest_name = "2023 年 CCPC 江苏省赛 & 全国邀请赛（湖南）- 热身赛"
    c.problem_quantity = 4
    c.start_time = utils.get_timestamp_second("2023-05-27 14:00:00")
    c.end_time = utils.get_timestamp_second("2023-05-27 16:00:00")

    c.fill_problem_id().fill_balloon_color()

    return c


def main():
    c = get_contest()
    common.work(c, DATA_DIR, FETCH_JS_URI, FETCH_XT_URI)


if __name__ == "__main__":
    main()
