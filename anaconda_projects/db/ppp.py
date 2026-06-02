k = 50.0
h = 25.0
re = 500.0
rw = 0.1
P_res = 100.0
T = 310.0

beta = 0.00852702
mu_cP = fluid.mu(P_res)

C_prod = (beta * k * h) / (mu_cP * math.log(re / rw))

print(f"Коэффициент продуктивности при P_res = {P_res} атм:")
print(f"μ({P_res} атм) = {mu_cP:.6f} сП")
print(f"Формула: C = (β·k·h) / (μ·ln(re/rw))")
print(f"= ({beta}·{k}·{h}) / ({mu_cP:.6f}·ln({re}/{rw}))")
print(f"C = {C_prod:.4f} ст.м³/(сут·атм)")

def well_q_linear(P_res, P_bhp, C):
    if P_bhp >= P_res:
        return 0.0
    return max(0, C * (P_res - P_bhp))

P_bhp_range = np.linspace(0, P_res, 100)
q_ipr = [well_q_linear(P_res, p, C_prod) for p in P_bhp_range]

plt.figure(figsize=(10, 6))
plt.plot(q_ipr, P_bhp_range, 'b-', linewidth=2.5, label='IPR кривая')
plt.fill_between(q_ipr, P_bhp_range, alpha=0.15, color='steelblue')

plt.xlabel('Дебит q, ст.м³/сут', fontsize=12)
plt.ylabel('Забойное давление P_bhp, атм', fontsize=12)
plt.title(f'Кривая притока (IPR) — Скважина 1\nP_res = {P_res} атм, C = {C_prod:.2f}',
          fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)

plt.ylim(0, 100)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()