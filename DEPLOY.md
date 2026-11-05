# GitHub 云端上线与验收

**仓库**：https://github.com/disdorqin/knowledge-sources （公开、仅保存元数据）

## 建立记录

- 2026-11-05：用户已在 GitHub 创建空仓库 `disdorqin/knowledge-sources`，默认分支 `main`。
- 本仓库只引用 22 个第三方公开资源；未 Fork、Submodule 或复制外部正文。
- 初始目录与治理规范由已授权的 GitHub 连接写入：内容提交 `484ed1532cc43192b86b917ccf829d2792fb45f1`，远端目录、8 个 Topic 和 22 个链接检查通过；以 GitHub 当前默认分支内容和提交记录为上线事实来源。
- OpenViking 外部入口仍是提案，**没有**因本仓库上线而自动发布到 OpenViking。

## 上线后验收

1. 打开仓库根目录的 README，能看到 8 个 Topic。
2. `catalog.json` 存在，唯一来源数为 22，各 Topic 链接可用。
3. 至少检查 `topics/life-safety.md`、`topics/social-relationships.md`、`topics/computer-foundations.md` 可远程读回。
4. `python scripts/validate_catalog.py` PASS（静态结构校验，不等于 22 个上游项目的内容均经过独立科学验证）。
5. 没有第三方仓库全文、个人隐私、OpenViking 私有科研资料与明文密钥。
6. 记录首次成功远程提交的 SHA；后续变更由 Git 历史追踪。

## 日后更新

优先在 GitHub 仓库的 `topics/*.md` 和 `catalog.json` 中更新描述与原始链接。对新增项目先做重合检查；不执行上游安装脚本或批量 Fork。详见 GOVERNANCE、CONTRIBUTING 和 MAINTENANCE。
