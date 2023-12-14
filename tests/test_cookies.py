def test_bake_project_app(cookies, bake_project_app_data):
    result = cookies.bake(extra_context=bake_project_app_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'go-app'

    # Check if the project directory exists
    assert result.project_path.is_dir()

    # Check if the project directory contains the required directories
    assert result.project_path.joinpath('.github').is_dir()
    assert result.project_path.joinpath('build').is_dir()
    assert result.project_path.joinpath('cmd').is_dir()
    assert result.project_path.joinpath('docs').is_dir()
    assert result.project_path.joinpath('internal').is_dir()
    assert result.project_path.joinpath('pkg').is_dir()
    assert result.project_path.joinpath('scripts').is_dir()
    assert result.project_path.joinpath('test').is_dir()

    # Check if the project directory contains the required files
    assert result.project_path.joinpath('.editorconfig').is_file()
    assert result.project_path.joinpath('.gitattributes').is_file()
    assert result.project_path.joinpath('.gitignore').is_file()
    assert result.project_path.joinpath('go.mod').is_file()
    assert result.project_path.joinpath('LICENSE').is_file()
    assert result.project_path.joinpath('make.bat').is_file()
    assert result.project_path.joinpath('Makefile').is_file()
    assert result.project_path.joinpath('README.md').is_file()


def test_bake_project_library(cookies, bake_project_library_data):
    result = cookies.bake(extra_context=bake_project_library_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'go-library'

    # Check if the project directory exists
    assert result.project_path.is_dir()

    # Check if the project directory contains the required directories
    assert result.project_path.joinpath('.github').is_dir()
    assert not result.project_path.joinpath('build').is_dir()
    assert result.project_path.joinpath('cmd').is_dir()
    assert result.project_path.joinpath('docs').is_dir()
    assert result.project_path.joinpath('internal').is_dir()
    assert result.project_path.joinpath('pkg').is_dir()
    assert result.project_path.joinpath('scripts').is_dir()
    assert result.project_path.joinpath('test').is_dir()

    # Check if the project directory contains the required files
    assert result.project_path.joinpath('.editorconfig').is_file()
    assert result.project_path.joinpath('.gitattributes').is_file()
    assert result.project_path.joinpath('.gitignore').is_file()
    assert result.project_path.joinpath('go.mod').is_file()
    assert result.project_path.joinpath('LICENSE').is_file()
    assert result.project_path.joinpath('make.bat').is_file()
    assert result.project_path.joinpath('Makefile').is_file()
    assert result.project_path.joinpath('README.md').is_file()
