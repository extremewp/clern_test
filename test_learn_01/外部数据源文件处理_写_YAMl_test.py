# 文本地址
# https://pyyaml.org/wiki/PyYAMLDocumentation
import yaml

print(yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
""", Loader=yaml.FullLoader))
