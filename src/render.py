import os
from jinja2 import Environment, FileSystemLoader
from src.config import config

def run():

    # 创建Jinja2环境
    env = Environment(loader=FileSystemLoader('.'))

    # 加载模板
    template = env.get_template('src/template.html')

    # 渲染模板并提供数据
    rendered_html = template.render(data=config)

    # 创建目录
    os.makedirs('docs', exist_ok=True)

    # 将渲染后的HTML写入文件
    with open('docs/index.html', 'w', encoding='utf-8') as file:
        file.write(rendered_html)