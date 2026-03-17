from point import Point


class TestPoint:
    def test_distance_ok(self):
        # GIVEN
        p1 = Point(0, 0)
        p2 = Point(3, 4)

        # WHEN
        d = p1.distance(p2)

        # THEN
        assert d == 5

    def test_eq_true(self):
        # GIVEN
        p1 = Point(3, 4)
        p2 = Point(3, 4)

        # WHEN
        res = p1 == p2

        # THEN
        assert res is True

    def test_eq_false(self):
        # GIVEN
        p1 = Point(1, 2)
        p2 = Point(3, 2)

        # WHEN
        res = p1 == p2

        # THEN
        assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
