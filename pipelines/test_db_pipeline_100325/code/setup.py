from setuptools import setup, find_packages
setup(
    name = 'test_db_pipeline_100325',
    version = '1.0',
    packages = find_packages(include = ('test_db_pipeline_100325*', )) + ['prophecy_config_instances.test_db_pipeline_100325'],
    package_dir = {'prophecy_config_instances.test_db_pipeline_100325' : 'configs/resources/test_db_pipeline_100325'},
    package_data = {'prophecy_config_instances.test_db_pipeline_100325' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.4'],
    entry_points = {
'console_scripts' : [
'main = test_db_pipeline_100325.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
