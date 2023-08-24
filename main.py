from scrapy.cmdline import execute
import os

# print(os.getcwd())
os.chdir("./CCE")


def to_scrapy_command(parameters: dict, spider_name: str):
    command = ["scrapy", "crawl", spider_name]
    for key, value in parameters.items():
        command.append("-a")
        command.append(f"{key}={value}")

    return command


parameters = dict(
    searchlist='["gobierno"]',
    category="transparencia justicia y legalidad",
    from_date='2022-08-20',
    to_date='2022-11-25',
)


command = to_scrapy_command(parameters, spider_name="CCESpider")
execute(argv=command + ["-o news.json"])
