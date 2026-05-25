import sys
import os

# 模拟一个本地的许可证知识库
LICENSE_DB = {
    "requests": ("Apache 2.0", "✅  包含专利授权条款，商业友好"),
    "flask": ("BSD-3-Clause", "✅  宽松许可，禁止用作者名义背书"),
    "django": ("BSD-3-Clause", "✅  宽松许可，商业友好"),
    "numpy": ("BSD-3-Clause", "✅  宽松许可，商业友好"),
    "gpl-lib": ("GPL-3.0", "⚠️  传染性许可证，衍生作品须以相同协议开源，商业项目需谨慎"),
    "urllib3": ("MIT", "✅  宽松许可，几乎无限制")
}

def check_requirements(file_path):
    if not os.path.exists(file_path):
        print(f"❌ 错误: 找不到文件 '{file_path}'")
        return

    print(f"🔍 正在扫描依赖文件: {file_path}\n" + "-" * 60)

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        package = line.strip().split('==')[0].lower()  # 简单提取包名
        if not package or package.startswith('#'):
            continue

        if package in LICENSE_DB:
            lic_type, risk_info = LICENSE_DB[package]
            status = "[✅ OK]" if "✅" in risk_info else "[⚠️ 注意]"
            # 格式化输出对齐
            print(f"{status:<9} {package:<15} -> {lic_type:<12} {risk_info.replace('✅', '').replace('⚠️', '').strip()}")
        else:
            print(f"[❔ 未知] {package:<15} -> ❓ 未在本地合规数据库中找到对应信息")

    print("-" * 60 + "\n🎯 扫描完成！请注意：本工具仅供合规参考，不构成法律意见。")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("💡 用法: python license_checker.py <requirements.txt路径>")
    else:
        check_requirements(sys.argv[1])