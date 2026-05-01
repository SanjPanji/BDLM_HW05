import pytest
from prime_pack_spanji.core import is_prime, primes, checksum, pipeline


# --- is_prime tests ---

class TestIsPrime:
    def test_small_primes(self):
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
            assert is_prime(p), f"{p} should be prime"

    def test_small_composites(self):
        for c in [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 25, 49]:
            assert not is_prime(c), f"{c} should not be prime"

    def test_negative(self):
        assert not is_prime(-1)
        assert not is_prime(-7)

    def test_two_is_prime(self):
        assert is_prime(2)

    def test_one_is_not_prime(self):
        assert not is_prime(1)

    def test_zero_is_not_prime(self):
        assert not is_prime(0)

    def test_even_not_prime(self):
        assert not is_prime(100)
        assert not is_prime(1000)

    def test_larger_primes(self):
        assert is_prime(97)
        assert is_prime(101)
        assert is_prime(997)

    def test_larger_composites(self):
        assert not is_prime(100)
        assert not is_prime(999)  # 999 = 3 * 333

    def test_prime_43(self):
        # Specific check mentioned in the task as a typical mistake target
        assert is_prime(43)

    def test_prime_97(self):
        assert is_prime(97)

    def test_composite_91(self):
        # 91 = 7 * 13, common mistake to think it's prime
        assert not is_prime(91)


# --- primes tests ---

class TestPrimes:
    def test_length_10(self):
        assert len(primes(10)) == 10

    def test_length_1000(self):
        assert len(primes(1000)) == 1000

    def test_length_1(self):
        assert len(primes(1)) == 1

    def test_first_prime_is_2(self):
        assert primes(1) == [2]

    def test_first_five(self):
        assert primes(5) == [2, 3, 5, 7, 11]

    def test_not_one_in_list(self):
        # 1 is not prime — common mistake
        assert 1 not in primes(10)

    def test_primes_2_is_not_one_two(self):
        # primes(2) must be [2, 3], NOT [1, 2]
        assert primes(2) == [2, 3]

    def test_all_elements_are_prime(self):
        for p in primes(50):
            assert is_prime(p), f"{p} in primes(50) is not prime"

    def test_ascending_order(self):
        result = primes(20)
        assert result == sorted(result)

    def test_no_duplicates(self):
        result = primes(100)
        assert len(result) == len(set(result))


# --- checksum tests ---

class TestChecksum:
    def test_empty_list(self):
        assert checksum([]) == 0

    def test_single_element_1(self):
        # (0 + 1) * 113 = 113
        assert checksum([1]) == 113

    def test_known_example_from_spec(self):
        # [1, 2, 6, 24] -> 6,012,369 as per task description
        assert checksum([1, 2, 6, 24]) == 6_012_369

    def test_result_less_than_modulo(self):
        assert checksum(primes(1000)) < 10_000_007

    def test_result_non_negative(self):
        assert checksum([2, 3, 5, 7]) >= 0

    def test_order_matters(self):
        # checksum is order-dependent
        assert checksum([1, 2]) != checksum([2, 1])


# --- pipeline tests ---

class TestPipeline:
    def test_default_result(self):
        # Expected value from task description
        assert pipeline() == 7_785_816

    def test_returns_int(self):
        assert isinstance(pipeline(), int)

    def test_different_seed_different_result(self):
        r1 = pipeline(count=100, seed=42)
        r2 = pipeline(count=100, seed=99)
        assert r1 != r2

    def test_reproducible(self):
        assert pipeline(count=100, seed=42) == pipeline(count=100, seed=42)

    def test_result_in_valid_range(self):
        assert 0 <= pipeline() < 10_000_007
