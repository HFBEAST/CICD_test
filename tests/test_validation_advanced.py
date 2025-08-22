# tests/test_validation_advanced.py
"""
高级验证测试 - 更深入的环境检查
"""

import os
import sys
import platform
import json
import pytest
from pathlib import Path


class TestSystemInfo:
    """系统信息验证"""

    def test_display_system_info(self):
        """显示系统信息用于调试"""
        info = {
            "操作系统": platform.system(),
            "系统版本": platform.version(),
            "Python版本": sys.version,
            "当前目录": os.getcwd(),
            "用户": os.environ.get('USER', os.environ.get('USERNAME', '未知')),
            "CI环境": os.environ.get('CI', 'False')
        }

        print("\n系统信息:")
        print("-" * 40)
        for key, value in info.items():
            print(f"{key}: {value}")
        print("-" * 40)

        # 在CI环境中的特殊检查
        if os.environ.get('CI') == 'true':
            assert os.environ.get('GITHUB_ACTIONS') == 'true', "应该在GitHub Actions中运行"
            print("✓ 在GitHub Actions环境中运行")


class TestDependencyVersions:
    """依赖版本验证"""

    def test_critical_dependencies(self):
        """验证关键依赖的版本"""
        import flask
        import werkzeug

        # 定义最低版本要求
        min_versions = {
            'flask': '2.0.0',
            'werkzeug': '2.0.0'
        }

        # 检查Flask版本
        flask_version = flask.__version__
        print(f"Flask版本: {flask_version}")
        assert self._compare_versions(flask_version, min_versions['flask']) >= 0, \
            f"Flask版本太低，需要>={min_versions['flask']}"

    def _compare_versions(self, v1, v2):
        """比较版本号"""
        from packaging import version
        return version.parse(v1) >= version.parse(v2)


class TestFileEncoding:
    """文件编码验证"""

    def test_python_files_encoding(self):
        """验证Python文件使用UTF-8编码"""
        project_root = Path(__file__).parent.parent
        python_files = list(project_root.glob("**/*.py"))

        encoding_issues = []
        for file_path in python_files:
            if '.venv' in str(file_path) or 'venv' in str(file_path):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    f.read()
            except UnicodeDecodeError:
                encoding_issues.append(str(file_path))

        if encoding_issues:
            pytest.fail(f"以下文件不是UTF-8编码: {encoding_issues}")

        print(f"✓ 检查了{len(python_files)}个Python文件，全部使用UTF-8编码")


class TestAPIEndpoints:
    """API端点验证"""

    @pytest.fixture
    def client(self):
        """创建测试客户端"""
        from src.app import app
        app.config['TESTING'] = True
        return app.test_client()

    def test_health_endpoint(self, client):
        """验证健康检查端点"""
        response = client.get('/health')
        assert response.status_code == 200

        data = response.get_json()
        assert 'status' in data
        assert data['status'] == 'healthy'
        print("✓ 健康检查端点正常")

    def test_home_endpoint(self, client):
        """验证首页端点"""
        response = client.get('/')
        assert response.status_code == 200

        data = response.get_json()
        assert 'message' in data
        print(f"✓ 首页消息: {data['message']}")