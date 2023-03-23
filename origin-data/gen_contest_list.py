#!/usr/bin/env python3

from os import path
import os
import json
import time

dist = "../data/contest_list.json"
pathname = "../data"
contest_list = {}


def json_output(data):
    return json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def json_input(path):
    with open(path, 'r') as f:
        return json.load(f)


def mkdir(_path):
    if not path.exists(_path):
        os.makedirs(_path)


def get_timestamp(dt):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return int(timestamp)


def output(filename, data):
    with open(filename, 'w') as f:
        f.write(json_output(data))


def dfs(contest_list, pathname, board_link):
    config_path = path.join(pathname, "config.json")
    if os.path.isfile(config_path):
        config = json_input(config_path)
        contest_list['config'] = {}
        contest_list['config']['contest_name'] = config['contest_name']
        contest_list['config']['start_time'] = config['start_time']
        contest_list['config']['end_time'] = config['end_time']
        contest_list['config']['frozen_time'] = config['frozen_time']

        if 'link' in config.keys():
            contest_list['config']['link'] = config['link']

        if 'logo' in config.keys():
            contest_list['config']['logo'] = config['logo']

        contest_list['board_link'] = board_link
    else:
        for _path in os.listdir(pathname):
            if not _path in ['contest_list.json', '.DS_Store']:
                contest_list[_path] = {}
                dfs(contest_list[_path], path.join(
                    pathname, _path), path.join(board_link, _path))


def work(contest_list, pathname):
    dfs(contest_list, pathname, '/')
    output(dist, contest_list)


work(contest_list, pathname)
