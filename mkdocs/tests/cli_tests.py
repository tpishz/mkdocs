#!/usr/bin/env python

import io
import logging
import unittest
from unittest import mock

from click.testing import CliRunner

from mkdocs import __main__ as cli


class CLITests(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_default(self, mock_serve):

        result = self.runner.invoke(cli.cli, ["serve"], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr=None,
            livereload='livereload',
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            watch_theme=False,
            watch=(),
        )

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_config_file(self, mock_serve):

        result = self.runner.invoke(
            cli.cli, ["serve", "--config-file", "mkdocs.yml"], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_serve.call_count, 1)
        args, kwargs = mock_serve.call_args
        self.assertTrue('config_file' in kwargs)
        self.assertIsInstance(kwargs['config_file'], io.BufferedReader)
        self.assertEqual(kwargs['config_file'].name, 'mkdocs.yml')

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_dev_addr(self, mock_serve):

        result = self.runner.invoke(
            cli.cli, ["serve", '--dev-addr', '0.0.0.0:80'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr='0.0.0.0:80',
            livereload='livereload',
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            watch_theme=False,
            watch=(),
        )

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_strict(self, mock_serve):

        result = self.runner.invoke(cli.cli, ["serve", '--strict'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr=None,
            livereload='livereload',
            config_file=None,
            strict=True,
            theme=None,
            use_directory_urls=None,
            watch_theme=False,
            watch=(),
        )

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_theme(self, mock_serve):

        result = self.runner.invoke(
            cli.cli, ["serve", '--theme', 'readthedocs'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr=None,
            livereload='livereload',
            config_file=None,
            strict=None,
            theme='readthedocs',
            use_directory_urls=None,
            watch_theme=False,
            watch=(),
        )

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_use_directory_urls(self, mock_serve):

        result = self.runner.invoke(
            cli.cli, ["serve", '--use-directory-urls'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr=None,
            livereload='livereload',
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=True,
            watch_theme=False,
            watch=(),
        )

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_no_directory_urls(self, mock_serve):

        result = self.runner.invoke(
            cli.cli, ["serve", '--no-directory-urls'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr=None,
            livereload='livereload',
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=False,
            watch_theme=False,
            watch=(),
        )

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_livereload(self, mock_serve):

        result = self.runner.invoke(cli.cli, ["serve", '--livereload'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr=None,
            livereload='livereload',
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            watch_theme=False,
            watch=(),
        )

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_no_livereload(self, mock_serve):

        result = self.runner.invoke(cli.cli, ["serve", '--no-livereload'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr=None,
            livereload='no-livereload',
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            watch_theme=False,
            watch=(),
        )

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_dirtyreload(self, mock_serve):

        result = self.runner.invoke(cli.cli, ["serve", '--dirtyreload'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr=None,
            livereload='dirty',
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            watch_theme=False,
            watch=(),
        )

    @mock.patch('mkdocs.commands.serve.serve', autospec=True)
    def test_serve_watch_theme(self, mock_serve):

        result = self.runner.invoke(cli.cli, ["serve", '--watch-theme'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        mock_serve.assert_called_once_with(
            dev_addr=None,
            livereload='livereload',
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            watch_theme=True,
            watch=(),
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_defaults(self, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['build'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        args, kwargs = mock_build.call_args
        self.assertTrue('dirty' in kwargs)
        self.assertFalse(kwargs['dirty'])
        mock_load_config.assert_called_once_with(
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            site_dir=None,
        )
        handler = logging._handlers.get('MkDocsStreamHandler')
        self.assertEqual(handler.level, logging.INFO)

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_clean(self, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['build', '--clean'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        args, kwargs = mock_build.call_args
        self.assertTrue('dirty' in kwargs)
        self.assertFalse(kwargs['dirty'])

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_dirty(self, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['build', '--dirty'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        args, kwargs = mock_build.call_args
        self.assertTrue('dirty' in kwargs)
        self.assertTrue(kwargs['dirty'])

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_config_file(self, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['build', '--config-file', 'mkdocs.yml'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        self.assertEqual(mock_load_config.call_count, 1)
        args, kwargs = mock_load_config.call_args
        self.assertTrue('config_file' in kwargs)
        self.assertIsInstance(kwargs['config_file'], io.BufferedReader)
        self.assertEqual(kwargs['config_file'].name, 'mkdocs.yml')

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_strict(self, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['build', '--strict'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            config_file=None,
            strict=True,
            theme=None,
            use_directory_urls=None,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_theme(self, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['build', '--theme', 'readthedocs'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            config_file=None,
            strict=None,
            theme='readthedocs',
            use_directory_urls=None,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_use_directory_urls(self, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['build', '--use-directory-urls'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=True,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_no_directory_urls(self, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['build', '--no-directory-urls'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=False,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_site_dir(self, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['build', '--site-dir', 'custom'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            site_dir='custom',
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_verbose(self, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['build', '--verbose'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        handler = logging._handlers.get('MkDocsStreamHandler')
        self.assertEqual(handler.level, logging.DEBUG)

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    def test_build_quiet(self, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['build', '--quiet'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_build.call_count, 1)
        handler = logging._handlers.get('MkDocsStreamHandler')
        self.assertEqual(handler.level, logging.ERROR)

    @mock.patch('mkdocs.commands.new.new', autospec=True)
    def test_new(self, mock_new):

        result = self.runner.invoke(cli.cli, ["new", "project"], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        mock_new.assert_called_once_with('project')

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_defaults(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['gh-deploy'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        g_args, g_kwargs = mock_gh_deploy.call_args
        self.assertTrue('message' in g_kwargs)
        self.assertEqual(g_kwargs['message'], None)
        self.assertTrue('force' in g_kwargs)
        self.assertEqual(g_kwargs['force'], False)
        self.assertTrue('ignore_version' in g_kwargs)
        self.assertEqual(g_kwargs['ignore_version'], False)
        self.assertEqual(mock_build.call_count, 1)
        b_args, b_kwargs = mock_build.call_args
        self.assertTrue('dirty' in b_kwargs)
        self.assertFalse(b_kwargs['dirty'])
        mock_load_config.assert_called_once_with(
            remote_branch=None,
            remote_name=None,
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_clean(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['gh-deploy', '--clean'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        args, kwargs = mock_build.call_args
        self.assertTrue('dirty' in kwargs)
        self.assertFalse(kwargs['dirty'])

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_dirty(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['gh-deploy', '--dirty'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        args, kwargs = mock_build.call_args
        self.assertTrue('dirty' in kwargs)
        self.assertTrue(kwargs['dirty'])

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_config_file(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['gh-deploy', '--config-file', 'mkdocs.yml'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        self.assertEqual(mock_load_config.call_count, 1)
        args, kwargs = mock_load_config.call_args
        self.assertTrue('config_file' in kwargs)
        self.assertIsInstance(kwargs['config_file'], io.BufferedReader)
        self.assertEqual(kwargs['config_file'].name, 'mkdocs.yml')

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_message(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['gh-deploy', '--message', 'A commit message'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        g_args, g_kwargs = mock_gh_deploy.call_args
        self.assertTrue('message' in g_kwargs)
        self.assertEqual(g_kwargs['message'], 'A commit message')
        self.assertEqual(mock_build.call_count, 1)
        self.assertEqual(mock_load_config.call_count, 1)

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_remote_branch(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['gh-deploy', '--remote-branch', 'foo'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            remote_branch='foo',
            remote_name=None,
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_remote_name(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['gh-deploy', '--remote-name', 'foo'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            remote_branch=None,
            remote_name='foo',
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_force(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['gh-deploy', '--force'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        g_args, g_kwargs = mock_gh_deploy.call_args
        self.assertTrue('force' in g_kwargs)
        self.assertEqual(g_kwargs['force'], True)
        self.assertEqual(mock_build.call_count, 1)
        self.assertEqual(mock_load_config.call_count, 1)

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_ignore_version(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['gh-deploy', '--ignore-version'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        g_args, g_kwargs = mock_gh_deploy.call_args
        self.assertTrue('ignore_version' in g_kwargs)
        self.assertEqual(g_kwargs['ignore_version'], True)
        self.assertEqual(mock_build.call_count, 1)
        self.assertEqual(mock_load_config.call_count, 1)

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_strict(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(cli.cli, ['gh-deploy', '--strict'], catch_exceptions=False)

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            remote_branch=None,
            remote_name=None,
            config_file=None,
            strict=True,
            theme=None,
            use_directory_urls=None,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_theme(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['gh-deploy', '--theme', 'readthedocs'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            remote_branch=None,
            remote_name=None,
            config_file=None,
            strict=None,
            theme='readthedocs',
            use_directory_urls=None,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_use_directory_urls(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['gh-deploy', '--use-directory-urls'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            remote_branch=None,
            remote_name=None,
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=True,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_no_directory_urls(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['gh-deploy', '--no-directory-urls'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            remote_branch=None,
            remote_name=None,
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=False,
            site_dir=None,
        )

    @mock.patch('mkdocs.config.load_config', autospec=True)
    @mock.patch('mkdocs.commands.build.build', autospec=True)
    @mock.patch('mkdocs.commands.gh_deploy.gh_deploy', autospec=True)
    def test_gh_deploy_site_dir(self, mock_gh_deploy, mock_build, mock_load_config):

        result = self.runner.invoke(
            cli.cli, ['gh-deploy', '--site-dir', 'custom'], catch_exceptions=False
        )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(mock_gh_deploy.call_count, 1)
        self.assertEqual(mock_build.call_count, 1)
        mock_load_config.assert_called_once_with(
            remote_branch=None,
            remote_name=None,
            config_file=None,
            strict=None,
            theme=None,
            use_directory_urls=None,
            site_dir='custom',
        )
