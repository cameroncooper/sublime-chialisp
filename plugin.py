import os
from LSP.plugin.core.typing import Tuple
from lsp_utils import NpmClientHandler


def plugin_loaded() -> None:
    LspChialispPlugin.setup()


def plugin_unloaded() -> None:
    LspChialispPlugin.cleanup()


class LspChialispPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'chialisp-language-server'
    server_binary_path = os.path.join(server_directory, 'runner', 'runner.js')
    skip_npm_install = True

    @classmethod
    def minimum_node_version(cls) -> Tuple[int, int, int]:
        return (14, 16, 0)
