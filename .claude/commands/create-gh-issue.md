# Issue: Fix five-in-a-row game bugs and missing features

## 问题描述 / Problem Description

当前五子棋游戏 (`five_in_a_row.py`) 存在以下问题：

### 1. **游戏结束后未让玩家选择先手** / Game doesn't ask who starts after win
当一方获胜后，新一轮游戏没有让玩家选择谁先手，直接让 X 方继续开局。

**预期行为：** 应该询问"X 还是 O 先手？(x/o)"，然后让用户选择。

### 2. **坐标输入顺序不明确** / Coordinate input order unclear
提示信息 `Enter row and column` 可能让人困惑，因为通常用户习惯 "行 列" 的格式，但需要明确说明。

### 3. **缺少悔棋功能** / No undo feature
游戏过程中无法撤销上一步操作。

### 4. **提示信息不统一** / Inconsistent prompts
中文提示（如"继续游戏？(y/n):"）与英文提示混用，建议统一为中文或增加翻译注释。

---

## Expected Behavior

1. 获胜后询问新对局由哪方先手
2. 清晰标明行列输入顺序
3. 支持悔棋功能 (例如按 u 键)
4. 统一提示语言或添加中文翻译

---

## Acceptance Criteria

- [ ] 新增：游戏结束后询问先手玩家 (x/o/u 选 O/x/重新开始)
- [ ] 优化：改进坐标输入提示
- [ ] 新增：添加悔棋功能
- [ ] 优化：统一提示信息语言
