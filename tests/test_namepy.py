from subprocess import check_output

from namepy import name


class TestNamepy:

    def test_namepy(self):
        assert name() is not None

    def test_cmd_namepy(self):
        result = check_output('namepy', shell=True)
        assert result is not None and '-' in result
