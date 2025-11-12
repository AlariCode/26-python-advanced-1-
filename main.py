
import gc


a = []
b = [a]
a.append(b)

print(gc.get_stats())
gc.collect()
