# [项目名称] - test

## 项目简介
# 技术栈：
  - DevOps/MLOps：Git + GitHub Actions（CI/CD）、Docker、DVC、MLflow（实验跟踪）


## 开发与部署流程（Commit → Build → Test → Staging → Prod）
### 1. 代码提交（Commit）
- 所有开发在 **feature分支**（如`feature/add-prediction-api`）进行，提交时需遵循规范：
  - 提交信息格式：`类型(模块): 描述`，例如：
    - `feat(api): 新增糖尿病风险预测接口`
    - `fix(test): 修复测试用例中的数据格式错误`
    - `docs(readme): 更新README中的部署流程`

### 2. 构建与测试（Build → Test）
- 触发条件：向 **dev/staging/main** 分支提PR时，GitHub Actions自动执行CI流程：
  1. **代码检查**：运行`black`（格式化）、`flake8`（ linting），确保代码规范；
  2. **测试执行**：运行`pytest`执行3类核心测试（见下方“测试说明”）；
  3. **容器构建**：构建Docker镜像，确保无运行时错误；
- 阻塞规则：CI失败（如测试不通过、镜像构建报错）时，PR **禁止合并**。

### 3. 环境晋升（Staging → Prod）
| 合并目标分支 | 触发操作 | 环境配置 | 输出结果 |
|--------------|----------|----------|----------|
| `staging`    | 自动部署到测试环境 | 使用GitHub Secrets中的 **STAGING_* 变量**（如`STAGING_DB_URL`），生成`staging.env` | 构建`staging`标签的Docker镜像 |
| `main`       | 自动部署到生产环境 | 使用GitHub Secrets中的 **PROD_* 变量**（如`PROD_API_KEY`），生成`prod.env` | 构建`prod`标签的Docker镜像 |


## 分支策略（Branching Scheme）
| 分支类型   | 命名规则          | 作用                                  | 合并路径                          |
|------------|-------------------|---------------------------------------|-----------------------------------|
| 主分支     | `main`            | 生产环境代码，永远可部署              | 仅从`staging`合并                 |
| 测试分支   | `staging`         | 预生产测试环境，验证功能稳定性        | 仅从`dev`合并                     |
| 开发分支   | `dev`             | 团队协作开发，集成已完成的功能        | 仅从`feature/*`合并               |
| 功能分支   | `feature/[功能名]`| 单个功能开发（如新增接口、优化模型）  | 完成后合并到`dev`，通过PR审核      |
| 修复分支   | `bugfix/[问题名]`  | 修复`dev/staging`的bug（如测试失败）  | 合并到对应分支（如`dev`或`staging`）|



## 快速开始（本地运行）
### 1. 克隆仓库
```bash
git clone https://github.com/[你的GitHub用户名]/[仓库名].git
cd [仓库名]
