import json

FILENAME = "sample-data.json"

with open(FILENAME, "r", encoding="utf-8") as f:
    data = json.load(f)

imdata = data.get("imdata", [])

print("Interface Status")
print("=" * 75)
print(f"{'DN':55} {'Description':15} {'Speed':8} {'MTU':6}")
print("-" * 75)

for item in imdata:
    obj = item.get("l1PhysIf", {})
    attrs = obj.get("attributes", {})

    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")

    print(f"{dn:55} {descr:15} {speed:8} {mtu:6}")