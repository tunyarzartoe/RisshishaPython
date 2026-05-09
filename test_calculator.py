import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'python-basic'))

import calculator

# Test add function
result_add = calculator.add(2, 3)
print(f"add(2, 3) = {result_add}")
assert result_add == 5, f"Expected 5, got {result_add}"

# Test mul function
result_mul = calculator.mul(4, 5)
print(f"mul(4, 5) = {result_mul}")
assert result_mul == 20, f"Expected 20, got {result_mul}"

print("All tests passed!")