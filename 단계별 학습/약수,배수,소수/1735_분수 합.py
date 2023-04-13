import sys
import math

input = sys.stdin.readline

Numerator1, Denominator1 = map(int, input().split())
Numerator2, Denominator2 = map(int, input().split())

AnsNumerator = (Numerator1*Denominator2)+(Denominator1*Numerator2)
AnsDenominator = (Denominator1*Denominator2)
Gcd = math.gcd(AnsNumerator,AnsDenominator)

while math.gcd(AnsNumerator,AnsDenominator) != 1:
    AnsNumerator = AnsNumerator // Gcd
    AnsDenominator = AnsDenominator // Gcd
    Gcd = math.gcd(int(AnsNumerator),int(AnsDenominator))

print(AnsNumerator, AnsDenominator)
