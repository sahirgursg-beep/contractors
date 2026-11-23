import json
d = json.load(open('/tmp/n.json'))
rows = d if isinstance(d, list) else list(d.values())
print(type(d).__name__, len(d))
print(json.dumps(rows[:2], indent=1))
keys = set(); [keys.update(r.keys()) for r in rows if isinstance(r, dict)]; print(sorted(keys))
c = [r for r in rows if str(r.get('id', '')).startswith('23')]
print('construction', len(c))
print(json.dumps(c, indent=0)[:6000])
