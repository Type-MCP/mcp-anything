# click MCP Server

MCP server for click (CLI application, with 50 capabilities)

## Available Tools

### add_completion_class

Register a :class:`ShellComplete` subclass under the given name.

Parameters:
- `name` (string, optional): Name to register the class under. Defaults to the
### argument_add_to_parser

Add to parser

Parameters:
- `parser` (_OptionParser): 
- `ctx` (Context): 
### argument_get_error_hint

Get error hint

Parameters:
- `ctx` (Context): 
### argument_get_usage_pieces

Get usage pieces

Parameters:
- `ctx` (Context): 
### argument_human_readable_name

Human readable name

### argument_make_metavar

Make metavar

Parameters:
- `ctx` (Context): 
### augment_usage_errors

Context manager that attaches extra information to exceptions.

Parameters:
- `ctx` (Context): 
- `param` (Parameter, optional): 
### bash_complete_format_completion

Format completion

Parameters:
- `item` (CompletionItem): 
### batch

Batch

Parameters:
- `iterable` (Iterable): 
- `batch_size` (integer): 
### bool_param_type_convert

Convert

Parameters:
- `value` (Any): 
- `param` (Parameter): 
- `ctx` (Context): 
### bool_param_type_str_to_bool

Convert a string to a boolean value.

Parameters:
- `value` (string): 
### bytes_io_copy_write

Write

Parameters:
- `b` (ReadableBuffer): 
### choice_convert

For a given value from the parser, normalize it and find its

Parameters:
- `value` (Any): 
- `param` (Parameter): 
- `ctx` (Context): 
### choice_get_invalid_choice_message

Get the error message when the given choice is invalid.

Parameters:
- `value` (Any): The invalid value.
- `ctx` (Context): 
### choice_get_metavar

Get metavar

Parameters:
- `param` (Parameter): 
- `ctx` (Context): 
### choice_get_missing_message

Message shown when no choice is passed.

Parameters:
- `param` (Parameter): 
- `ctx` (Context): 
### choice_normalize_choice

Normalize a choice value, used to map a passed string to a choice.

Parameters:
- `choice` (ParamTypeValue): 
- `ctx` (Context): 
### choice_shell_complete

Complete choices that start with the incomplete value.

Parameters:
- `ctx` (Context): Invocation context for this command.
- `param` (Parameter): The parameter that is requesting completion.
- `incomplete` (string): Value being completed. May be empty.
### choice_to_info_dict

To info dict

### clear

Clears the terminal screen.  This will have the effect of clearing

### cli_runner_get_default_prog_name

Given a command object it will return the default program name

Parameters:
- `cli` (Command): 
### cli_runner_isolated_filesystem

A context manager that creates a temporary directory and

Parameters:
- `temp_dir` (string, optional): Create the temporary directory under this
### cli_runner_make_env

Returns the environment overrides for invoking a script.

Parameters:
- `overrides` (Mapping, optional): 
### click_exception_show

Show

Parameters:
- `file` (IO, optional): 
### command

Command

Parameters:
- `name` (_AnyCallable): 
### command_collect_usage_pieces

Returns all the pieces that go into the usage line and returns

Parameters:
- `ctx` (Context): 
### command_collection_add_source

Add a group as a source of commands.

Parameters:
- `group` (Group): 
### command_collection_get_command

Get command

Parameters:
- `ctx` (Context): 
- `cmd_name` (string): 
### command_collection_list_commands

List commands

Parameters:
- `ctx` (Context): 
### command_format_epilog

Writes the epilog into the formatter if it exists.

Parameters:
- `ctx` (Context): 
- `formatter` (HelpFormatter): 
### command_format_help

Writes the help into the formatter if it exists.

Parameters:
- `ctx` (Context): 
- `formatter` (HelpFormatter): 
### command_format_help_text

Writes the help text to the formatter if it exists.

Parameters:
- `ctx` (Context): 
- `formatter` (HelpFormatter): 
### command_format_options

Writes all the options into the formatter if they exist.

Parameters:
- `ctx` (Context): 
- `formatter` (HelpFormatter): 
### command_format_usage

Writes the usage line into the formatter.

Parameters:
- `ctx` (Context): 
- `formatter` (HelpFormatter): 
### command_get_help

Formats the help into a string and returns it.

Parameters:
- `ctx` (Context): 
### command_get_help_option

Returns the help option object.

Parameters:
- `ctx` (Context): 
### command_get_help_option_names

Returns the names for the help option.

Parameters:
- `ctx` (Context): 
### command_get_params

Get params

Parameters:
- `ctx` (Context): 
### command_get_short_help_str

Gets short help for the command or makes it by shortening the

Parameters:
- `limit` (integer, optional):  (default: 45)
### command_get_usage

Formats the usage line into a string and returns it.

Parameters:
- `ctx` (Context): 
### command_make_context

This function when given an info name and arguments will kick

Parameters:
- `info_name` (string): the info name for this invocation.  Generally this
- `args` (array): the arguments to parse as list of strings.
- `parent` (Context, optional): the parent context if available.
### command_make_parser

Creates the underlying option parser for this command.

Parameters:
- `ctx` (Context): 
### command_shell_complete

Return a list of completions for the incomplete value. Looks

Parameters:
- `ctx` (Context): Invocation context for this command.
- `incomplete` (string): Value being completed. May be empty.
### command_to_info_dict

To info dict

Parameters:
- `ctx` (Context): 
### composite_param_type_arity

Arity

### confirm

Prompts for confirmation (yes/no question).

Parameters:
- `text` (string): the question to ask.
- `default` (boolean, optional): The default value to use when no input is given. If (default: False)
- `abort` (boolean, optional): if this is set to `True` a negative answer aborts the (default: False)
- `prompt_suffix` (string, optional): a suffix that should be added to the prompt. (default: : )
- `show_default` (boolean, optional): shows or hides the default value in the prompt. (default: True)
- `err` (boolean, optional): if set to true the file defaults to ``stderr`` instead of (default: False)
### confirmation_option

Add a ``--yes`` option which shows a prompt before continuing if

### console_stream_name

Name

### console_stream_write

Write

Parameters:
- `x` (AnyStr): 
### console_stream_writelines

Writelines

Parameters:
- `lines` (Iterable): 

## Available Resources

- `app://click/status` — Current status and version of click
- `app://click/commands` — Available commands and tools in click
- `docs://click/tool-index` — Complete index of all click tools with parameters and usage
- `docs://click/argument` — Documentation for click argument capabilities
- `docs://click/bash_complete` — Documentation for click bash_complete capabilities
- `docs://click/bool_param_type` — Documentation for click bool_param_type capabilities
- `docs://click/bytes_io_copy` — Documentation for click bytes_io_copy capabilities
- `docs://click/choice` — Documentation for click choice capabilities

## Available Prompts

- `use_click` — Guide for using click tools effectively
- `debug_click` — Diagnose issues with click operations

## Usage

This server runs over stdio. Add it to your MCP client config:

```json
{
  "mcpServers": {
    "click": {
      "command": "mcp-click"
    }
  }
}
```
