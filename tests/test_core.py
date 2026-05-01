import pytest
from prime_pack_spanji2.core import is_prime, primes, checksum, pipeline


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
        assert not is_prime(999)

    def test_prime_43(self):
        assert is_prime(43)

    def test_prime_97(self):
        assert is_prime(97)

    def test_composite_91(self):
        assert not is_prime(91)

    def test_returns_bool(self):
        assert isinstance(is_prime(2), bool)
        assert isinstance(is_prime(4), bool)

    def test_prime_4(self):
        assert not is_prime(4)

    def test_prime_9(self):
        assert not is_prime(9)

    def test_prime_2_only_even(self):
        # 2 is the only even prime
        assert is_prime(2)
        assert not is_prime(4)
        assert not is_prime(6)


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

    def test_first_ten(self):
        assert primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_not_one_in_list(self):
        assert 1 not in primes(10)

    def test_primes_2_is_not_one_two(self):
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

    def test_returns_list(self):
        assert isinstance(primes(5), list)

    def test_1000th_prime(self):
        # 1000th prime is 7919
        assert primes(1000)[-1] == 7919

    def test_100th_prime(self):
        # 100th prime is 541
        assert primes(100)[-1] == 541


class TestChecksum:
    def test_empty_list(self):
        assert checksum([]) == 0

    def test_single_element_1(self):
        assert checksum([1]) == 113

    def test_single_element_2(self):
        assert checksum([2]) == 226

    def test_known_example_from_spec(self):
        assert checksum([1, 2, 6, 24]) == 6_012_369

    def test_result_less_than_modulo(self):
        assert checksum(primes(1000)) < 10_000_007

    def test_result_non_negative(self):
        assert checksum([2, 3, 5, 7]) >= 0

    def test_order_matters(self):
        assert checksum([1, 2]) != checksum([2, 1])

    def test_modulo_applied(self):
        # Result must always be less than 10_000_007
        assert checksum([10_000_000] * 100) < 10_000_007

    def test_two_elements(self):
        # (0+1)*113=113, (113+2)*113=12995
        assert checksum([1, 2]) == 12995


class TestPipeline:
    def test_default_result(self):
        assert pipeline() == 7_785_816

    def test_explicit_params(self):
        assert pipeline(count=1000, seed=100) == 7_785_816

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

    def test_different_count(self):
        r1 = pipeline(count=100, seed=100)
        r2 = pipeline(count=200, seed=100)
        assert r1 != r2
