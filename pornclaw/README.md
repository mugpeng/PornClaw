# PornClaw

PornClaw 是一个面向内容站点的系列推荐引擎原型。用户输入一个数据源 URL，系统抓取最近内容、聚合成系列、结合显式偏好和反馈，输出可解释的 Top 5 推荐。

## 第一阶段目标

- 本地运行 Web 应用
- 输入单个数据源 URL
- 抓取近期内容并落库
- 聚合到系列层级
- 支持显式标签偏好、自然语言偏好、候选反馈、推荐反馈
- 输出带理由的 Top 5 推荐

## 核心流程图

```text
用户输入 URL + 标签偏好 + 自然语言偏好
  -> source adapter 抓取最近条目
  -> normalize 清洗标题 / 标签
  -> aggregate 聚合为系列
  -> 候选反馈补充画像
  -> recommend 规则打分
  -> explain 生成推荐理由
  -> 推荐结果页反馈影响下一轮排序
```

## 技术栈

- Python 3.11
- FastAPI
- Jinja2
- SQLite
- SQLAlchemy
- requests + BeautifulSoup
- pytest
- Docker Compose

## 目录结构

```text
pornclaw/
  app/
  tests/
  scripts/
  Dockerfile
  docker-compose.yml
  requirements.txt
  README.md
```

## 本地运行

```bash
cd pornclaw
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/init_db.py
uvicorn app.main:app --reload
```

浏览器打开 `http://127.0.0.1:8000`，首页默认已填入演示数据源 `demo://seed`。

## Docker 启动

```bash
cd pornclaw
docker compose up --build
```

访问 `http://127.0.0.1:8000`。

## Demo Source 方案

- 默认使用 `demo://seed`，由 `DemoSourceAdapter` 读取内置静态 HTML，保证首版闭环稳定可演示。
- 同一个 adapter 也支持解析简单的外部静态 HTML 卡片结构；如果结构不符会返回明确错误。

## 测试

```bash
pytest
```

## 未来迭代方向

- 增加更多 source adapter
- 优化系列归并规则
- 增加偏好解析测试与解释测试
- 引入更精细的多样性控制和召回策略
