# littles_law.py - Little's Law check (values come from the experiment)
N, T = 5031, 10.0                      # UDP packets counted in Wireshark/tshark over T seconds
baseline_ms, loaded_ms = 0.259, 102.475   # ping RTTs
avg_backlog_bytes, avg_qlen_pkts = 64298.4, 51.82  # sampled from tc every 0.2 s
PKT = 1228                                  # bytes per queued packet (1200 + 8 UDP + 20 IP)
lam = N / T
W = (loaded_ms - baseline_ms) / 1000
print(f"N = {N} packets in T = {T:.0f} s  ->  lambda = {lam:.1f} packets/s")
print(f"W = loaded - baseline = {loaded_ms} - {baseline_ms} = {W*1000:.1f} ms = {W:.4f} s")
print(f"L = lambda x W = {lam:.1f} x {W:.4f} = {lam*W:.1f} packets  (Little's Law prediction)")
print(f"Measured average queue length: {avg_backlog_bytes/PKT:.1f} packets (backlog bytes / {PKT}), {avg_qlen_pkts:.1f} packets (tc qlen)")
print(f"Difference: {abs(lam*W - avg_qlen_pkts)/avg_qlen_pkts*100:.1f} %")
