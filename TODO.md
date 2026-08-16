# Walk Into The Frame：待办

## P0｜跑通 scene-distillation zine MVP

- [ ] 用现有的楼梯/建筑场景照 + 人物照跑通一张平衡场景拼贴海报。
- [ ] 建立 Distillation Card：semantic nucleus、情绪残留、主导手势、材质、舍弃清单。
- [ ] 测试默认的平衡场景拼贴，并记录主体 45–65%、留白 30–45% 的效果。
- [ ] 只有在用户明确要求极简时，测试不对称岛、撕纸窗口、方向漂移等稀疏构图。
- [ ] 测试三种人物 cameo：剪纸块、干墨轮廓、错落碎片。
- [ ] 测试 Standard Accent Mode 与精确触发的 `单色块模式`。
- [ ] 检查主体/景的比例、关系锚点、接触/遮挡、视觉隐喻、眼线路径和人物层级。
- [ ] 检查拼贴感：主纸窗、辅助纸片、边界、接缝、重叠、断裂和外围留白是否可见。
- [ ] 检查米白底纸是否稳定，天空/海水/墙面是否被正确抽取为独立层而非整张底色。
- [ ] 测试用户提供地点后的短手写 `@Place` 标记，并验证未提供地点时不会自行添加地理信息。
- [ ] 记录失败类型：仍像照片、满版插画、装饰过多、人物太写实、色彩失控、无关图标、文字变形。
- [ ] 固化最终 prompt、recipe、创作想法和艺术指导的返回格式。

## P1｜把方法做成稳定 skill

- [ ] 为 reference routing 增加场景图/人物图/风格图的角色判断。
- [ ] 为不同场景建立 source-derived composition family 选择规则。
- [ ] 为 cut-paper、dry-print、broken contour、colored-pencil fragment 写独立配方。
- [ ] 增加人物 cameo 的 `barely-there / relational-subtle / noticeable` 三档；默认使用 relational-subtle。
- [ ] 为凳子、窗户、台阶、门、栏杆、船、桌子和路径建立关系锚点示例。
- [ ] 增加 `balanced-scene-collage / sparse-distillation` 两种构图模式。
- [ ] 增加 `standard-accent / solid-color-block` 两套色彩检查。
- [ ] 为每次生成保存输入角色、保留等级、Distillation Card、prompt 和质量结果。
- [ ] 用自然风景、建筑、人文街景三类素材做前向测试。
- [ ] 运行 skill-creator 的 quick validation 和 Markdown 链接检查。

## P2｜视频与 Live Photo（后续阶段）

- [ ] 只对通过质量门的 zine 海报编写图生视频 motion prompt。
- [ ] 用 Kling 网页端测试纸张、印刷纹理、植物、光影和人物小动作。
- [ ] 需要批量处理时再评估视频 API、轮询、下载和成本统计。
- [ ] 用 ffmpeg 裁切最短稳定源片，统一输出 1–3 秒 MP4。
- [ ] 再研究 Apple Photos 可导入的 Live Photo 封装和真实设备验证。

## P3｜发布体验

- [ ] 添加脱敏 before/after 示例，并明确标注 AI 生成。
- [ ] 选择开源许可证并建立 frontmatter/Markdown 校验。
- [ ] 记录模型名称与价格的更新时间，不把临时价格写成永久承诺。
- [ ] 发布第一个 scene-distillation 版本 tag：`v0.2.0-scene-distillation`。
