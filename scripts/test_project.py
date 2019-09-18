import allure


class TestAll:

    @allure.step("测试脚本")
    def test_011(self):
        allure.attach("项目一", "成功")
        assert True

    def test_012(self):
        allure.attach("项目二", "失败")
        assert False

