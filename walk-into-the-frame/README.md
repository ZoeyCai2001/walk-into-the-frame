# Walk Into The Frame

### 走进自己的 zine

把摄影者轻轻放回自己的照片里，但先把照片重新编辑成一张有纸张、笔触和记忆感的 zine。

`Walk Into The Frame` 是一个面向摄影师的 Codex skill：输入一张风景或人文照片，再加一张自己的照片，将场景提炼为手绘、明信片、彩铅、拼贴、版画或安静的编辑设计，并把摄影者抽象成同一视觉语言中的小小参与者。

```text
两张照片 → 阅读场景 → 提取视觉事实 → 选择 zine 语法 → 抽象人物 → 融合成静态图
```

它不追求把真实人脸无损贴回照片，也不默认生成视频。目标是让“我曾经在这里”成为一张可信、克制、可以独立成立的视觉记忆。视频和 Live Photo 是后续阶段：只对已经确认的 zine 静帧做轻微动效。

## 使用方式

```text
用 $walk-into-the-frame 把这张楼梯照片做成一张手绘旅行明信片。
参考我的照片，把我抽象成一个背着相机、正在走上楼梯的小人物。
保留原来的楼梯、植物密度和向上的构图，不要写实脸，不要让人物成为主体。
```

## 方法来源

这个 skill 采用“先观察、再提取关系、最后重新编排”的工作方式，参考了 [gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) 的场景蒸馏思路，并吸收了 photo relic、极简海报和编辑性 zine 的方向：照片提供事实，创作决定如何保留。

## 项目结构

- [SKILL.md](SKILL.md)：触发条件、工作流、提示词契约和质量门
- [references/zine-recipes.md](references/zine-recipes.md)：风格配方和失败修复
- [ARCHITECTURE.md](ARCHITECTURE.md)：当前静态图优先架构与后续视频路线
- [TODO.md](TODO.md)：实施清单
- [references/video-tools.md](references/video-tools.md)：视频阶段的历史调研与交接说明
