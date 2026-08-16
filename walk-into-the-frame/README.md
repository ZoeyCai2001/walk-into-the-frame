# Walk Into The Frame

### 走进自己的 zine

把摄影者轻轻放回自己的记忆里，但不把照片原样搬进 zine。

`Walk Into The Frame` 是一个面向摄影师的 Codex skill：输入一张风景或人文照片，再加一张自己的照片，将场景提炼为稀疏的纸面海报、拼贴、版画或编辑性 zine，并把摄影者抽象成同一视觉系统中的小型视觉元素。

```text
两张照片 → 蒸馏语义 → 确定命题 → 选择隐喻 → 纸面重编排 → 人物 cameo → zine 海报
```

它不追求把真实人脸无损贴回照片，也不把原照片完整画成插画。目标是让“我曾经在这里”成为一张有留白、有材料感、可以独立成立的视觉记忆。视频和 Live Photo 是后续阶段：只对已经确认的 zine 海报做轻微动效。

## 使用方式

```text
用 $walk-into-the-frame 把这两张照片重新编排成一张平衡的米白纸底拼贴海报。
从风景照里提取门、台阶和暖光，从我的照片里提取草帽、米色穿搭和摄影者身份。
把场景拆成独立的门、台阶和植物纸片层，不要保留照片像素；让人物通过台阶、门、窗户、凳子或路径等具体关系融入画面，不使用固定人物比例。
如果地点由我提供，请在留白处加一个短小手写的 `@Place` 标记。
```

## 方法来源

这个 skill 采用“先观察、再提取关系、最后重新编排”的工作方式，参考了 [gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) 的场景蒸馏思路，以及 [scene-distillation-zine-v1-3](https://github.com/liuyutian198-stack/scene-distillation-zine-v1-3) 和 [gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) 的纸面海报系统：照片提供事实，创作决定如何删除、隐喻和留白。

## 项目结构

- [SKILL.md](SKILL.md)：触发条件、工作流、提示词契约和质量门
- [references/zine-recipes.md](references/zine-recipes.md)：风格配方和失败修复
- [ARCHITECTURE.md](ARCHITECTURE.md)：当前静态图优先架构与后续视频路线
- [TODO.md](TODO.md)：实施清单
- [references/video-tools.md](references/video-tools.md)：视频阶段的历史调研与交接说明
- [scripts/compose_photo_pairs.py](../scripts/compose_photo_pairs.py)：按 `N-1`/`N-2` 批量导出原图与 zine 图对照拼贴

## 对照图批量导出

将原图命名为 `N-1`、生成图命名为 `N-2`，运行：

```bash
python3 scripts/compose_photo_pairs.py \
  "/path/to/chosed" \
  "/path/to/chosed/composites"
```

横图会按“原图上、生成图下”排列，竖图会按“原图左、生成图右”排列。脚本只按共同边缩放，
保持原比例，并从生成图取样米白纸底作为外层画布。
