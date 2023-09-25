# Windows 开发小技巧

python pip安装三方依赖

```bash
pip --no-cache-dir install <PackageName>
```

conda 环境迁移

```bash
# 进入环境
conda activate <EnvironmentName>
# 导出环境
conda env export --no-build --from-history > <EnvironmentName.yaml>
# 导入环境
conda env create -f <EnvironmentName.yaml>
```

conda 更新

```bash
conda update -n base -c defaults conda
```

conda 清理缓存

```bash
conda clean --all -y
```

npm/yarn/cnpm/pnpm 清理缓存

```bash
yarn cache clean
npm cache clean -f
```


