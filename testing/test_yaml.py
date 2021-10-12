import yaml

with open("../datas/add.yml") as f:
    print(yaml.safe_load(f))