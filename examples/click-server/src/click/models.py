"""Data models for click MCP server."""

from dataclasses import dataclass
from typing import Any


@dataclass
class AddCompletionClassParams:
    """Parameters for add_completion_class."""
    name: str | None = None

@dataclass
class ArgumentAddToParserParams:
    """Parameters for argument_add_to_parser."""
    parser: str
    ctx: str

@dataclass
class ArgumentGetErrorHintParams:
    """Parameters for argument_get_error_hint."""
    ctx: str

@dataclass
class ArgumentGetUsagePiecesParams:
    """Parameters for argument_get_usage_pieces."""
    ctx: str

@dataclass
class ArgumentMakeMetavarParams:
    """Parameters for argument_make_metavar."""
    ctx: str

@dataclass
class AugmentUsageErrorsParams:
    """Parameters for augment_usage_errors."""
    ctx: str
    param: str | None = None

@dataclass
class BashCompleteFormatCompletionParams:
    """Parameters for bash_complete_format_completion."""
    item: str

@dataclass
class BatchParams:
    """Parameters for batch."""
    iterable: str
    batch_size: int

@dataclass
class BoolParamTypeConvertParams:
    """Parameters for bool_param_type_convert."""
    value: str
    param: str
    ctx: str

@dataclass
class BoolParamTypeStrToBoolParams:
    """Parameters for bool_param_type_str_to_bool."""
    value: str

@dataclass
class BytesIoCopyWriteParams:
    """Parameters for bytes_io_copy_write."""
    b: str

@dataclass
class ChoiceConvertParams:
    """Parameters for choice_convert."""
    value: str
    param: str
    ctx: str

@dataclass
class ChoiceGetInvalidChoiceMessageParams:
    """Parameters for choice_get_invalid_choice_message."""
    value: str
    ctx: str

@dataclass
class ChoiceGetMetavarParams:
    """Parameters for choice_get_metavar."""
    param: str
    ctx: str

@dataclass
class ChoiceGetMissingMessageParams:
    """Parameters for choice_get_missing_message."""
    param: str
    ctx: str

@dataclass
class ChoiceNormalizeChoiceParams:
    """Parameters for choice_normalize_choice."""
    choice: str
    ctx: str

@dataclass
class ChoiceShellCompleteParams:
    """Parameters for choice_shell_complete."""
    ctx: str
    param: str
    incomplete: str

@dataclass
class CliRunnerGetDefaultProgNameParams:
    """Parameters for cli_runner_get_default_prog_name."""
    cli: str

@dataclass
class CliRunnerIsolatedFilesystemParams:
    """Parameters for cli_runner_isolated_filesystem."""
    temp_dir: str | None = None

@dataclass
class CliRunnerMakeEnvParams:
    """Parameters for cli_runner_make_env."""
    overrides: str | None = None

@dataclass
class ClickExceptionShowParams:
    """Parameters for click_exception_show."""
    file: str | None = None

@dataclass
class CommandParams:
    """Parameters for command."""
    name: str

@dataclass
class CommandCollectUsagePiecesParams:
    """Parameters for command_collect_usage_pieces."""
    ctx: str

@dataclass
class CommandCollectionAddSourceParams:
    """Parameters for command_collection_add_source."""
    group: str

@dataclass
class CommandCollectionGetCommandParams:
    """Parameters for command_collection_get_command."""
    ctx: str
    cmd_name: str

@dataclass
class CommandCollectionListCommandsParams:
    """Parameters for command_collection_list_commands."""
    ctx: str

@dataclass
class CommandFormatEpilogParams:
    """Parameters for command_format_epilog."""
    ctx: str
    formatter: str

@dataclass
class CommandFormatHelpParams:
    """Parameters for command_format_help."""
    ctx: str
    formatter: str

@dataclass
class CommandFormatHelpTextParams:
    """Parameters for command_format_help_text."""
    ctx: str
    formatter: str

@dataclass
class CommandFormatOptionsParams:
    """Parameters for command_format_options."""
    ctx: str
    formatter: str

@dataclass
class CommandFormatUsageParams:
    """Parameters for command_format_usage."""
    ctx: str
    formatter: str

@dataclass
class CommandGetHelpParams:
    """Parameters for command_get_help."""
    ctx: str

@dataclass
class CommandGetHelpOptionParams:
    """Parameters for command_get_help_option."""
    ctx: str

@dataclass
class CommandGetHelpOptionNamesParams:
    """Parameters for command_get_help_option_names."""
    ctx: str

@dataclass
class CommandGetParamsParams:
    """Parameters for command_get_params."""
    ctx: str

@dataclass
class CommandGetShortHelpStrParams:
    """Parameters for command_get_short_help_str."""
    limit: int | None = None

@dataclass
class CommandGetUsageParams:
    """Parameters for command_get_usage."""
    ctx: str

@dataclass
class CommandMakeContextParams:
    """Parameters for command_make_context."""
    info_name: str
    args: list
    parent: str | None = None

@dataclass
class CommandMakeParserParams:
    """Parameters for command_make_parser."""
    ctx: str

@dataclass
class CommandShellCompleteParams:
    """Parameters for command_shell_complete."""
    ctx: str
    incomplete: str

@dataclass
class CommandToInfoDictParams:
    """Parameters for command_to_info_dict."""
    ctx: str

@dataclass
class ConfirmParams:
    """Parameters for confirm."""
    text: str
    default: bool | None = None
    abort: bool | None = None
    prompt_suffix: str | None = None
    show_default: bool | None = None
    err: bool | None = None

@dataclass
class ConsoleStreamWriteParams:
    """Parameters for console_stream_write."""
    x: str

@dataclass
class ConsoleStreamWritelinesParams:
    """Parameters for console_stream_writelines."""
    lines: str

