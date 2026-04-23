"""
Unit tests for speed/feed calculations.
Run: python -m pytest tests/ -v
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))
from speed_feed_calc import calc_rpm, calc_feed_rate, calc_mrr, taylor_tool_life

def test_rpm_formula():
    N = calc_rpm(305, 50)
    assert abs(N - 1943.0) < 2.0, f"RPM calc wrong: {N}"

def test_rpm_small_diameter():
    N = calc_rpm(100, 10)
    expected = (100 * 1000) / (math.pi * 10)
    assert abs(N - expected) < 0.1

def test_feed_rate_turning():
    Vf = calc_feed_rate(1943, 0.25, n_teeth=1)
    assert abs(Vf - 485.75) < 1.0

def test_feed_rate_milling_4_teeth():
    Vf = calc_feed_rate(2000, 0.10, n_teeth=4)
    assert abs(Vf - 800.0) < 0.1

def test_milling_feed_uses_tooth_count():
    Vf_1 = calc_feed_rate(2000, 0.10, n_teeth=1)
    Vf_4 = calc_feed_rate(2000, 0.10, n_teeth=4)
    assert abs(Vf_4 - 4 * Vf_1) < 0.01, "Feed rate must scale with tooth count"

def test_mrr_positive():
    mrr = calc_mrr(486, 2.0, 50)
    assert mrr > 0

def test_taylor_tool_life_decreases_with_speed():
    T_slow = taylor_tool_life(100, "4140 Steel", "carbide_coated")
    T_fast = taylor_tool_life(200, "4140 Steel", "carbide_coated")
    assert T_fast is not None and T_slow is not None
    assert T_slow > T_fast, "Tool life should decrease as speed increases"

def test_taylor_returns_none_for_unknown_combo():
    T = taylor_tool_life(150, "ABS", "ceramic")
    assert T is None

print("All tests defined. Run: python -m pytest tests/ -v")
