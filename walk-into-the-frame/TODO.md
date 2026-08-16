# Walk Into The Frame：待办

## P0｜先跑通静态 zine MVP

- [ ] 用现有的楼梯场景照 + 人物照跑通第一组测试。
- [ ] 选择三种对照风格：手绘旅行明信片、彩铅观察稿、纸张拼贴。
- [ ] 为每种风格记录 scene facts、visual grammar 和人物 cameo 方案。
- [ ] 用图像生成/编辑模型完成 `scene image + person image → zine still`。
- [ ] 检查场景是否仍可辨、人物是否属于同一媒介、人物是否过于突出。
- [ ] 记录失败类型：场景漂移、风格混杂、人物太大、身份线索丢失、文字变形、解剖异常。
- [ ] 形成一套可重复的静帧 prompt 模板。

## P1｜把方法做成可复用 skill

- [ ] 根据真实测试结果调整 `SKILL.md` 中的风格选择和失败修复规则。
- [ ] 为手绘明信片、彩铅、拼贴、线稿/限色、Risograph、photo-relic editorial 写独立配方。
- [ ] 增加 `barely-there / subtle / noticeable` 三档人物存在感。
- [ ] 增加 `preserve-composition / editorial-reframe` 两种构图策略。
- [ ] 为每次生成保存输入角色、风格配方、prompt 和质量检查结果。
- [ ] 确认人物照片只在用户授权范围内使用，不将 API key 或原始肖像提交到仓库。
- [ ] 运行 skill-creator 的 quick validation，并用三类场景做前向测试。

## P2｜视频与 Live Photo（后续阶段）

- [ ] 只对通过质量门的 zine 静帧编写图生视频 motion prompt。
- [ ] 用 Kling 网页端测试纸张、植物、光影和人物小动作。
- [ ] 需要批量处理时再评估视频 API、轮询、下载和成本统计。
- [ ] 用 ffmpeg 裁切最短稳定源片，统一输出 1–3 秒 MP4。
- [ ] 再研究 Apple Photos 可导入的 Live Photo 封装和真实设备验证。

## P3｜发布体验

- [ ] 添加脱敏 before/after 示例，并明确标注 AI 生成。
- [ ] 选择开源许可证并建立 Markdown/frontmatter 校验。
- [ ] 记录模型名称与价格的更新时间，不把临时价格写成永久承诺。
- [ ] 发布第一个静态图优先版本 tag：`v0.1.0-zine-mvp`。
