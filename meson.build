project('grad-project',
    version: '1.0.beta',
    meson_version: '>= 1.0.0'
)

gnome = import('gnome')
python = import('python')

py_installation = python.find_installation('python3')

PROJECT_NAME = 'CAU.GRADPROJECT.SmartFinder'
APPLICATION_ID = 'CAU.GRADPROJECT.SmartFinder'

PYTHON_DIR = py_installation.get_path('purelib')
PKGDATA_DIR = join_paths(get_option('prefix'), get_option('datadir'), APPLICATION_ID)
PKGLIB_DIR = join_paths(get_option('prefix'), get_option('libdir'), APPLICATION_ID)

glib_dep = dependency('glib-2.0')
dependency('gobject-introspection-1.0')
dependency('gtk4')
dependency('libadwaita-1')
dependency('libsoup-3.0')
dependency('tracker-sparql-3.0')
dependency('pango')
dependency('pygobject-3.0')
dependency('py3cairo')

subdir('data')

install_subdir(
    'src',
    install_dir: py_installation.get_install_dir()
)

bin_config = configuration_data()
bin_config.set('application_id', APPLICATION_ID)
bin_config.set('project_name', PROJECT_NAME)
bin_config.set('pkgdatadir', PKGDATA_DIR)
bin_config.set('localedir', join_paths(get_option('prefix'), get_option('datadir'), 'locale'))
bin_config.set('pythondir', PYTHON_DIR)
bin_config.set('version', meson.project_version())

bin_config.set('local_build', 'False')

configure_file(
    input: 'grad-project.in',
    output: 'grad-project',
    configuration: bin_config,
    install_dir: get_option('bindir')
)

local_config = configuration_data()
local_config.set('application_id', APPLICATION_ID)
local_config.set('project_name', PROJECT_NAME)
local_config.set('pkgdatadir', join_paths(meson.current_build_dir(), 'data'))
local_config.set('localedir', join_paths(get_option('prefix'), get_option('datadir'), 'locale'))
local_config.set('pythondir', meson.current_source_dir())
local_config.set('version', meson.project_version())

local_config.set('local_build', 'True')

configure_file(
    input: 'grad-project.in',
    output: 'local-project',
    configuration: local_config,
)

gnome.post_install(
    glib_compile_schemas: true,
    gtk_update_icon_cache: true,
    update_desktop_database: true
)