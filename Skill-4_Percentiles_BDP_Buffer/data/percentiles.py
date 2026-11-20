# percentiles.py - latency percentiles of the baseline RTT measurements
import statistics, sys
vals = sorted(float(x) for x in open(sys.argv[1]) if x.strip())
def pct(p):                       # linear-interpolated percentile
    k = (len(vals) - 1) * p / 100
    lo, hi = int(k), min(int(k) + 1, len(vals) - 1)
    return vals[lo] + (vals[hi] - vals[lo]) * (k - lo)
print(f"samples : {len(vals)}")
print(f"min     : {vals[0]:.3f} ms")
print(f"mean    : {statistics.mean(vals):.3f} ms")
print(f"stdev   : {statistics.stdev(vals):.3f} ms")
for p in (50, 90, 95, 99):
    print(f"p{p:<6} : {pct(p):.3f} ms")
print(f"max     : {vals[-1]:.3f} ms")
print(f"mean/p50 = {statistics.mean(vals)/pct(50):.2f}   p99/p50 = {pct(99)/pct(50):.2f}")
