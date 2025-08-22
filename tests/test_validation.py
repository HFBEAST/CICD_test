# tests/test_validation.py
"""
前期验证测试 - 用于确认环境配置正确
这个文件应该最先运行，确保基础环境没问题
"""

import sys
import os
import pytest


class TestEnvironmentValidation:
    """环境验证测试类"""

    def test_python_version(self):
        """验证Python版本是否正确"""
        print(f"当前Python版本: {sys.version}")
        assert sys.version_info >= (3, 10), "需要Python 3.10或更高版本"
        assert sys.version_info < (4, 0), "不支持Python 4.x"

    def test_import_basic_modules(self):
        """验证基础模块能否导入"""
        try:
            import flask
            print(f"✓ Flask版本: {flask.__version__}")
        except ImportError:
            pytest.fail("无法导入Flask")

        try:
            import pytest
            print(f"✓ Pytest版本: {pytest.__version__}")
        except ImportError:
            pytest.fail("无法导入Pytest")

    def test_project_structure(self):
        """验证项目结构是否正确"""
        # 获取项目根目录
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # 检查必要的目录
        assert os.path.exists(os.path.join(project_root, 'src')), "src目录不存在"
        assert os.path.exists(os.path.join(project_root, 'tests')), "tests目录不存在"
        assert os.path.exists(os.path.join(project_root, '.github')), ".github目录不存在"

        # 检查必要的文件
        assert os.path.exists(os.path.join(project_root, 'requirements.txt')), "requirements.txt不存在"
        assert os.path.exists(os.path.join(project_root, 'README.md')), "README.md不存在"

        print("✓ 项目结构验证通过")

    def test_src_module_import(self):
        """验证src模块能否正确导入"""
        try:
            from src import app
            assert app is not None
            print("✓ src.app模块导入成功")
        except ImportError as e:
            pytest.fail(f"无法导入src.app: {e}")


class TestBasicFunctionality:
    """基础功能验证测试"""

    def test_flask_app_exists(self):
        """验证Flask应用是否存在"""
        from src.app import app
        assert app is not None
        assert app.name == 'src.app' or app.name == 'app'
        print(f"✓ Flask应用名称: {app.name}")

    def test_basic_routes_exist(self):
        """验证基础路由是否存在"""
        from src.app import app

        # 获取所有注册的路由
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append(rule.endpoint)

        print(f"已注册的路由: {routes}")

        # 验证必要的路由
        assert 'home' in routes or 'index' in routes, "首页路由不存在"
        assert 'health' in routes, "健康检查路由不存在"

    def test_app_can_start(self):
        """验证应用能否启动"""
        from src.app import app

        # 创建测试客户端
        client = app.test_client()
        assert client is not None

        # 测试根路径
        response = client.get('/')
        assert response.status_code in [200, 404], f"意外的状态码: {response.status_code}"
        print(f"✓ 应用可以启动，根路径返回: {response.status_code}")


class TestDevelopmentTools:
    """开发工具验证测试"""

    def test_pytest_config(self):
        """验证pytest配置"""
        import pytest

        # 检查pytest.ini是否存在
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pytest_ini = os.path.join(project_root, 'pytest.ini')

        if os.path.exists(pytest_ini):
            print("✓ pytest.ini配置文件存在")
        else:
            print("⚠ pytest.ini不存在（可选）")

    def test_code_quality_tools(self):
        """验证代码质量工具"""
        tools_status = {}

        try:
            import flake8
            tools_status['flake8'] = flake8.__version__
        except ImportError:
            tools_status['flake8'] = '未安装'

        try:
            import black
            tools_status['black'] = black.__version__
        except ImportError:
            tools_status['black'] = '未安装'

        try:
            import mypy
            tools_status['mypy'] = mypy.__version__
        except ImportError:
            tools_status['mypy'] = '未安装'

        print("代码质量工具状态:")
        for tool, status in tools_status.items():
            print(f"  {tool}: {status}")


# 标记这些测试应该最先运行
pytestmark = pytest.mark.validation


def test_critical_validation():
    """关键验证 - 这个测试必须通过"""
    assert True, "这个测试应该总是通过"
    print("\n" + "=" * 50)
    print("🚀 基础验证开始")
    print("=" * 50)