# 自动删除修改时间超过N天的文件以及目录

[![author](https://img.shields.io/badge/Author-Alice-orange)](https://t.me/FairyAlicePro) [![github](https://img.shields.io/badge/Github-AliceEngineerPro-green)](https://github.com/AliceEngineerPro) [![github](https://img.shields.io/badge/GitBook-AliceEngineerProGitBook-green)](https://interestingbooks.gitbook.io/) [![type](https://img.shields.io/badge/Type-README-blue)](https://github.com/AliceEngineerPro) [![editor](https://img.shields.io/badge/Editor-PyCharm-yellow)](https://github.com/AliceEngineerPro) [![file](https://img.shields.io/badge/Language-Markdown-orange)](https://github.com/AliceEngineerPro) [![version](https://img.shields.io/badge/Version-Release-blue)](https://github.com/AliceEngineerPro) [![docs](https://img.shields.io/badge/Docs-Passing-brightgreen)](https://github.com/AliceEngineerPro) [![](https://img.shields.io/badge/%E7%AD%89%E6%88%91%E4%BB%A3%E7%A0%81%E7%BC%96%E6%88%90-%E5%A8%B6%E4%BD%A0%E4%B8%BA%E5%A6%BB%E5%8F%AF%E5%A5%BD@-red)](https://github.com/AliceEngineerPro)

## 一.修改配置文件

1. 在项目跟目录找到`application.ini`

2. 参数说明

   - `file_path`: 文件路径, 多个文件路径使用`;`(分号,半角英文)隔开
   - `file_ext`: 文件扩展名, 多个文件扩展名使用`;`(分号,半角英文)隔开
   - `modify_timeout_day`: 修改时间超过N天的文件以及目录

   ```ini
   [service]
   file_path = /var/cache; /var/log; /var/cache; /var/log
   file_ext = .*
   modify_timeout_day = 7
   ```

3. 项目运行

## 二.项目运行



