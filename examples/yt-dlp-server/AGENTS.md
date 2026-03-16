# yt-dlp MCP Server

MCP server for yt-dlp (with 200 capabilities)

## Available Tools

### identity

IDENTITY

Parameters:
- `x` (string): 
### a_cast_channel_ie_suitable

Suitable

Parameters:
- `url` (string): 
### add_accept_encoding_header

Add accept encoding header

Parameters:
- `headers` (HTTPHeaderDict): 
- `supported_encodings` (Iterable): 
### aes_cbc_decrypt

Decrypt with aes in CBC mode

Parameters:
- `data` (string): 
- `key` (string): 
- `iv` (string): 
### aes_cbc_encrypt

Encrypt with aes in CBC mode

Parameters:
- `data` (string): 
- `key` (string): 
- `iv` (string): 
- `padding_mode` (string, optional):  (default: pkcs7)
### aes_cbc_encrypt_bytes

Aes cbc encrypt bytes

Parameters:
- `data` (string): 
- `key` (string): 
- `iv` (string): 
### aes_ctr_decrypt

Decrypt with aes in counter mode

Parameters:
- `data` (string): 
- `key` (string): 
- `iv` (string): 
### aes_ctr_encrypt

Encrypt with aes in counter mode

Parameters:
- `data` (string): 
- `key` (string): 
- `iv` (string): 
### aes_decrypt

Decrypt one block with aes

Parameters:
- `data` (string): 
- `expanded_key` (string): 
### aes_decrypt_text

Decrypt text

Parameters:
- `data` (string): 
- `password` (string): 
- `key_size_bytes` (string): 
### aes_ecb_decrypt

Decrypt with aes in ECB mode

Parameters:
- `data` (string): 
- `key` (string): 
- `iv` (string, optional): 
### aes_ecb_encrypt

Encrypt with aes in ECB mode. Using PKCS#7 padding

Parameters:
- `data` (string): 
- `key` (string): 
- `iv` (string, optional): 
### aes_encrypt

Encrypt one block with aes

Parameters:
- `data` (string): 
- `expanded_key` (string): 
### aes_gcm_decrypt_and_verify

Decrypt with aes in GBM mode and checks authenticity using tag

Parameters:
- `data` (string): 
- `key` (string): 
- `tag` (string): 
- `nonce` (string): 
### age_restricted

Returns True iff the content should be blocked 

Parameters:
- `content_limit` (string): 
- `age_limit` (string): 
### alura_course_ie_suitable

Suitable

Parameters:
- `url` (string): 
### andere_tijden_ie_suitable

Suitable

Parameters:
- `url` (string): 
### args_to_str

Args to str

Parameters:
- `args` (string): 
### aria2c_fd_aria2c_rpc

Aria2c rpc

Parameters:
- `rpc_port` (string): 
- `rpc_secret` (string): 
- `method` (string): 
- `params` (string, optional): 
### aria2c_fd_supports_manifest

Supports manifest

Parameters:
- `manifest` (string): 
### arte_tv_category_ie_suitable

Suitable

Parameters:
- `url` (string): 
### ass_subtitles_timecode

Ass subtitles timecode

Parameters:
- `seconds` (string): 
### aws_idp_authenticate

Authenticate with a username and password. 

Parameters:
- `username` (string): 
- `password` (string): 
### bandcamp_album_ie_suitable

Suitable

Parameters:
- `url` (string): 
### base_url

Base url

Parameters:
- `url` (string): 
### bbcie_suitable

Suitable

Parameters:
- `url` (string): 
### bbvtv_live_ie_suitable

Suitable

Parameters:
- `url` (string): 
### bili_intl_base_ie_json2srt

Json2srt

Parameters:
- `json` (string): 
### bilibili_base_ie_extract_formats

Extract formats

Parameters:
- `play_info` (string): 
### bilibili_base_ie_is_logged_in

Is logged in

### bilibili_base_ie_json2srt

Json2srt

Parameters:
- `json_data` (string): 
### bilibili_collection_list_ie_suitable

Suitable

Parameters:
- `url` (string): 
### block_parse

Parse

Parameters:
- `parser` (string): 
### block_product

Block product

Parameters:
- `block_x` (string): 
- `block_y` (string): 
### block_write_into

Write into

Parameters:
- `stream` (string): 
### bool_or_none

Bool or none

Parameters:
- `v` (string): 
- `default` (string, optional): 
### box

Box

Parameters:
- `box_type` (string): 
- `payload` (string): 
### breakline_status_printer_print_at_line

Print at line

Parameters:
- `text` (string): 
- `pos` (string): 
### bug_reports_message

Bug reports message

Parameters:
- `before` (string, optional):  (default: ;)
### build_fragments_list

Return a list of (segment, fragment) for each fragment in the video 

Parameters:
- `boot_info` (string): 
### bunny_cdn_fd_ping_thread

Ping thread

Parameters:
- `stop_event` (string): 
- `url` (string): 
- `headers` (string): 
- `secret` (string): 
- `context_id` (string): 
### bunny_cdn_fd_real_download

Real download

Parameters:
- `filename` (string): 
- `info_dict` (string): 
### bytes_to_intlist

Bytes to intlist

Parameters:
- `bs` (string): 
### bytes_to_long

bytes_to_long(string) : long

Parameters:
- `s` (string): 
### cache_enabled

Enabled

### cache_load

Load

Parameters:
- `section` (string): 
- `key` (string): 
- `dtype` (string, optional):  (default: json)
- `default` (string, optional): 
- `min_ver` (string, optional): 
### cache_store

Store

Parameters:
- `section` (string): 
- `key` (string): 
- `data` (string): 
- `dtype` (string, optional):  (default: json)
### caesar

Caesar

Parameters:
- `s` (string): 
- `alphabet` (string): 
- `shift` (string): 
### callin_ie_try_get_user_name

Try get user name

Parameters:
- `d` (string): 
### candidate_plugin_paths

Candidate plugin paths

Parameters:
- `candidate` (string): 
### cbcie_suitable

Suitable

Parameters:
- `url` (string): 
### check_executable

Checks if the given binary is installed somewhere in PATH, and returns its name.

Parameters:
- `exe` (string): 
- `args` (string, optional):  (default: [])
### chrome_cookie_decryptor_decrypt

Decrypt

Parameters:
- `encrypted_value` (string): 
### cisco_live_search_ie_suitable

Suitable

Parameters:
- `url` (string): 
### clean_headers

Clean headers

Parameters:
- `headers` (HTTPHeaderDict): 
### clean_html

Clean an HTML snippet into a readable string

Parameters:
- `html` (string): 
### clean_podcast_url

Clean podcast url

Parameters:
- `url` (string): 
### clean_pot

Clean pot

Parameters:
- `po_token` (string): 
### clean_proxies

Clean proxies

Parameters:
- `proxies` (object): 
- `headers` (HTTPHeaderDict): 
### cli_bool_option

Cli bool option

Parameters:
- `params` (string): 
- `command_option` (string): 
- `param` (string): 
- `true_value` (string, optional):  (default: true)
- `false_value` (string, optional):  (default: false)
- `separator` (string, optional): 
### cli_configuration_args

Cli configuration args

Parameters:
- `argdict` (string): 
- `keys` (string): 
- `default` (string, optional):  (default: [])
- `use_compat` (string, optional):  (default: True)
### cli_option

Cli option

Parameters:
- `params` (string): 
- `command_option` (string): 
- `param` (string): 
- `separator` (string, optional): 
### cli_valueless_option

Cli valueless option

Parameters:
- `params` (string): 
- `command_option` (string): 
- `param` (string): 
- `expected_value` (string, optional):  (default: True)
### compat_etree_fromstring

Compat etree fromstring

Parameters:
- `text` (string): 
### compat_ord

Compat ord

Parameters:
- `c` (string): 
### compat_setenv

Compat setenv

Parameters:
- `key` (string): 
- `value` (string): 
- `env` (string, optional): 
### compat_shlex_quote

Compat shlex quote

Parameters:
- `s` (string): 
### config_all_args

All args

### config_append_config

Append config

Parameters:
- `label` (string, optional): 
### config_init

Init

Parameters:
- `args` (string, optional): 
- `filename` (string, optional): 
### config_read_file

Read file

Parameters:
- `filename` (string): 
- `default` (string, optional):  (default: [])
### cookie_jar_to_list

Cookie jar to list

Parameters:
- `cookie_jar` (string): 
### cookie_to_dict

Cookie to dict

Parameters:
- `cookie` (string): 
### create_connection

Create connection

Parameters:
- `address` (string): 
- `timeout` (string, optional): 
- `source_address` (string, optional): 
- `_create_socket_func` (string, optional): 
### create_mapping_re

Create mapping re

Parameters:
- `supported` (string): 
### create_socks_proxy_socket

Create socks proxy socket

Parameters:
- `dest_addr` (string): 
- `proxy_args` (string): 
- `proxy_ip_addr` (string): 
- `timeout` (string): 
- `source_address` (string): 
### cue_block_as_json

As json

### cue_block_from_json

From json

Parameters:
- `json` (string): 
### cue_block_hinges

Hinges

Parameters:
- `other` (string): 
### cue_block_parse

Parse

Parameters:
- `parser` (string): 
### cue_block_write_into

Write into

Parameters:
- `stream` (string): 
### curl_cffi_preference

Curl cffi preference

Parameters:
- `rh` (string): 
- `request` (string): 
### curl_cffi_response_adapter_read

Read

Parameters:
- `amt` (string, optional): 
### curl_cffi_response_reader_close

Close

### curl_cffi_response_reader_read

Read

Parameters:
- `size` (string, optional): 
### curl_cffirh_send

Send

Parameters:
- `request` (Request): 
### current_git_head

Current git head

### dash_segments_fd_real_download

Real download

Parameters:
- `filename` (string): 
- `info_dict` (string): 
### data_parser_expect_bytes

Expect bytes

Parameters:
- `expected_value` (string): 
- `message` (string): 
### data_parser_read_bytes

Read bytes

Parameters:
- `num_bytes` (string): 
### data_parser_read_double

Read double

Parameters:
- `big_endian` (string, optional):  (default: False)
### data_parser_read_uint

Read uint

Parameters:
- `big_endian` (string, optional):  (default: False)
### data_parser_skip

Skip

Parameters:
- `num_bytes` (string): 
- `description` (string, optional):  (default: unknown)
### data_parser_skip_to

Skip to

Parameters:
- `offset` (string): 
- `description` (string, optional):  (default: unknown)
### data_parser_skip_to_end

Skip to end

Parameters:
- `description` (string, optional):  (default: unknown)
### date_formats

Date formats

Parameters:
- `day_first` (string, optional):  (default: True)
### date_from_str

Return a date object from a string using datetime_from_str

Parameters:
- `date_str` (string): 
- `format` (string, optional):  (default: %Y%m%d)
- `strict` (string, optional):  (default: False)
### date_range_day

Returns a range that only contains the given day

Parameters:
- `day` (string): 
### datetime_add_months

Increment/Decrement a datetime object by months.

Parameters:
- `dt_` (string): 
- `months` (string): 
### datetime_from_str

Return a datetime object from a string.

Parameters:
- `date_str` (string): 
- `precision` (string, optional):  (default: auto)
- `format` (string, optional):  (default: %Y%m%d)
### datetime_round

Round a datetime object's time to a specific precision

Parameters:
- `dt_` (string): 
- `precision` (string, optional):  (default: day)
### daum_clip_ie_suitable

Suitable

Parameters:
- `url` (string): 
### daum_playlist_ie_suitable

Suitable

Parameters:
- `url` (string): 
### debugger_write

Write

Parameters:
- `level` (string, optional):  (default: 100)
### decode_argument

DecodeArgument

Parameters:
- `b` (string): 
### decode_filename

DecodeFilename

Parameters:
- `b` (string): 
- `for_subprocess` (string, optional):  (default: False)
### decode_option

DecodeOption

Parameters:
- `optval` (string): 
### decode_base

Decode base

Parameters:
- `value` (string): 
- `digits` (string): 
### decode_base64

Decode base64

Parameters:
- `text` (string): 
### decode_base_n

Convert given base-n string to int

Parameters:
- `string` (string): 
- `n` (string, optional): 
- `table` (string, optional): 
### decode_packed_codes

Decode packed codes

Parameters:
- `code` (string): 
### decode_png

Decode png

Parameters:
- `png_data` (string): 
### deprecation_warning

Deprecation warning

Parameters:
- `msg` (string): 
- `printer` (string, optional): 
- `stacklevel` (string, optional):  (default: 0)
### detect_exe_version

Detect exe version

Parameters:
- `output` (string): 
- `version_re` (string, optional): 
- `unrecognized` (string, optional):  (default: present)
### determine_ext

Determine ext

Parameters:
- `url` (string): 
- `default_ext` (string, optional):  (default: unknown_video)
### determine_file_encoding

Detect the text encoding used

Parameters:
- `data` (string): 
### determine_protocol

Determine protocol

Parameters:
- `info_dict` (string): 
### dfxp2srt

@param dfxp_data A bytes-like object containing DFXP data

Parameters:
- `dfxp_data` (string): 
### dict_get

Dict get

Parameters:
- `d` (string): 
- `key_or_keys` (string): 
- `default` (string, optional): 
- `skip_false_values` (string, optional):  (default: True)
### dirs_in_zip

Dirs in zip

Parameters:
- `archive` (string): 
### eins_und_eins_tv_live_ie_suitable

Suitable

Parameters:
- `url` (string): 
### encode_argument

EncodeArgument

Parameters:
- `s` (string): 
### encode_filename

EncodeFilename

Parameters:
- `s` (string): 
- `for_subprocess` (string, optional):  (default: False)
### encode_base_n

Convert given int to a base-n string

Parameters:
- `num` (string): 
- `n` (string, optional): 
- `table` (string, optional): 
### encode_compat_str

Encode compat str

Parameters:
- `string` (string): 
- `encoding` (string, optional): 
- `errors` (string, optional):  (default: strict)
### encode_data_uri

Encode data uri

Parameters:
- `data` (string): 
- `mime_type` (string): 
### error_to_compat_str

Error to compat str

Parameters:
- `err` (string): 
### error_to_str

Error to str

Parameters:
- `err` (string): 
### escape_html

EscapeHTML

Parameters:
- `text` (string): 
### escape_rfc3986

Escape non-ASCII characters as suggested by RFC 3986

Parameters:
- `s` (string): 
### espn_article_ie_suitable

Suitable

Parameters:
- `url` (string): 
### ewetv_live_ie_suitable

Suitable

Parameters:
- `url` (string): 
### exec_pp_parse_cmd

Parse cmd

Parameters:
- `cmd` (string): 
- `info` (string): 
### expand_path

Expand shell variables and ~

Parameters:
- `s` (string): 
### ext2mimetype

Ext2mimetype

Parameters:
- `ext_or_url` (string): 
### external_fd_exe_name

EXE NAME

### external_fd_available

Available

Parameters:
- `path` (string, optional): 
### external_fd_can_download

Can download

Parameters:
- `info_dict` (string): 
- `path` (string, optional): 
### external_fd_exe

Exe

### external_fd_get_basename

Get basename

### external_fd_real_download

Real download

Parameters:
- `filename` (string): 
- `info_dict` (string): 
### external_fd_supports

Supports

Parameters:
- `info_dict` (string): 
### extract_attributes

Given a string for an HTML element such as

Parameters:
- `html_element` (string): 
### extract_basic_auth

Extract basic auth

Parameters:
- `url` (string): 
### extract_box_data

Extract box data

Parameters:
- `data` (string): 
- `box_sequence` (string): 
### extract_cookies_from_browser

Extract cookies from browser

Parameters:
- `browser_name` (string): 
- `profile` (string, optional): 
- `logger` (string, optional): 
- `keyring` (string, optional): 
- `container` (string, optional): 
### extract_timezone

Extract timezone

Parameters:
- `date_str` (string): 
- `default` (string, optional): 
### f4m_fd_real_download

Real download

Parameters:
- `filename` (string): 
- `info_dict` (string): 
### f_fmpeg_concat_pp_concat_files

Concat files

Parameters:
- `in_files` (string): 
- `out_file` (string): 
### f_fmpeg_extract_audio_pp_run_ffmpeg

Run ffmpeg

Parameters:
- `path` (string): 
- `out_path` (string): 
- `codec` (string): 
- `more_opts` (string): 
### f_fmpeg_fd_available

Available

Parameters:
- `path` (string, optional): 
### f_fmpeg_fd_can_merge_formats

Can merge formats

Parameters:
- `info_dict` (string): 
- `params` (string): 
### f_fmpeg_fd_on_process_started

Override this in subclasses  

Parameters:
- `proc` (string): 
- `stdin` (string): 
### f_fmpeg_post_processor_available

Available

### f_fmpeg_post_processor_basename

Basename

### f_fmpeg_post_processor_check_version

Check version

### f_fmpeg_post_processor_concat_files

Use concat demuxer to concatenate multiple files having identical streams.

Parameters:
- `in_files` (string): 
- `out_file` (string): 
- `concat_opts` (string, optional): 
### f_fmpeg_post_processor_executable

Executable

### f_fmpeg_post_processor_force_keyframes

Force keyframes

Parameters:
- `filename` (string): 
- `timestamps` (string): 
### f_fmpeg_post_processor_get_audio_codec

Get audio codec

Parameters:
- `path` (string): 
### f_fmpeg_post_processor_get_metadata_object

Get metadata object

Parameters:
- `path` (string): 
- `opts` (string, optional):  (default: [])
### f_fmpeg_post_processor_get_stream_number

Get stream number

Parameters:
- `path` (string): 
- `keys` (string): 
- `value` (string): 
### f_fmpeg_post_processor_get_versions

Get versions

Parameters:
- `downloader` (string, optional): 
### f_fmpeg_post_processor_get_versions_and_features

Get versions and features

Parameters:
- `downloader` (string, optional): 
### f_fmpeg_post_processor_probe_available

Probe available

### f_fmpeg_post_processor_probe_basename

Probe basename

### f_fmpeg_post_processor_probe_executable

Probe executable

### f_fmpeg_post_processor_run_ffmpeg

Run ffmpeg

Parameters:
- `path` (string): 
- `out_path` (string): 
- `opts` (string): 
### f_fmpeg_post_processor_run_ffmpeg_multiple_files

Run ffmpeg multiple files

Parameters:
- `input_paths` (string): 
- `out_path` (string): 
- `opts` (string): 
### f_fmpeg_post_processor_stream_copy_opts

Stream copy opts

Parameters:
- `copy` (string, optional):  (default: True)
- `ext` (string, optional): 
### f_fmpeg_sink_fd_real_connection

Override this in subclasses 

Parameters:
- `sink` (string): 
- `info_dict` (string): 
### f_fmpeg_sink_fd_real_download

Real download

Parameters:
- `filename` (string): 
- `info_dict` (string): 
### f_fmpeg_thumbnails_convertor_pp_convert_thumbnail

Convert thumbnail

Parameters:
- `thumbnail_filename` (string): 
- `target_ext` (string): 
### f_fmpeg_thumbnails_convertor_pp_fixup_webp

Fixup webp

Parameters:
- `info` (string): 
- `idx` (string, optional): 
### f_fmpeg_thumbnails_convertor_pp_is_webp

Is webp

Parameters:
- `path` (string): 
### fancode_vod_ie_download_gql

Download gql

Parameters:
- `variable` (string): 
- `data` (string): 
- `note` (string): 
- `fatal` (string, optional):  (default: False)
- `headers` (string, optional): 
### fc2_live_fd_real_download

Real download

Parameters:
- `filename` (string): 
- `info_dict` (string): 
### file_downloader_fd_name

FD NAME

### file_downloader_add_progress_hook

Add progress hook

Parameters:
- `ph` (string): 
### file_downloader_best_block_size

Best block size

Parameters:
- `elapsed_time` (string): 
- `bytes` (string): 
### file_downloader_calc_eta

Calc eta

Parameters:
- `start_or_rate` (string): 
- `now_or_remaining` (string): 
- `total` (string, optional): 
- `current` (string, optional): 
### file_downloader_calc_percent

Calc percent

Parameters:
- `byte_counter` (string): 
- `data_len` (string): 
### file_downloader_calc_speed

Calc speed

Parameters:
- `start` (string): 
- `now` (string): 
- `bytes` (string): 
### file_downloader_download

Download to a filename using the info from info_dict

Parameters:
- `filename` (string): 
- `info_dict` (string): 
- `subtitle` (string, optional):  (default: False)
### file_downloader_filesize_or_none

Filesize or none

Parameters:
- `unencoded_filename` (string): 
### file_downloader_format_eta

Format eta

Parameters:
- `seconds` (string): 
### file_downloader_format_percent

Format percent

Parameters:
- `percent` (string): 
### file_downloader_format_retries

Format retries

Parameters:
- `retries` (string): 
### file_downloader_format_seconds

Format seconds

Parameters:
- `seconds` (string): 
### file_downloader_format_speed

Format speed

Parameters:
- `speed` (string): 
### file_downloader_parse_bytes

Parse a string indicating a byte quantity into an integer.

Parameters:
- `bytestr` (string): 
### file_downloader_real_download

Real download process. Redefine in subclasses.

Parameters:
- `filename` (string): 
- `info_dict` (string): 
### file_downloader_report_destination

Report destination filename.

Parameters:
- `filename` (string): 
### file_downloader_report_resuming_byte

Report attempt to resume at given byte.

Parameters:
- `resume_len` (string): 
### file_downloader_report_retry

Report retry

Parameters:
- `err` (string): 
- `count` (string): 
- `retries` (string): 
- `frag_index` (string, optional): 
- `fatal` (string, optional):  (default: True)
### file_downloader_report_unable_to_resume

Report it was impossible to resume download.

### file_downloader_sanitize_open

Sanitize open

Parameters:
- `filename` (string): 
- `open_mode` (string): 
### file_downloader_slow_down

Sleep if the download speed is over the rate limit.

Parameters:
- `start_time` (string): 
- `now` (string): 
- `byte_counter` (string): 
### file_downloader_supports_manifest

Whether the downloader can download the fragments from the manifest.

Parameters:
- `manifest` (string): 
### file_downloader_temp_name

Returns a temporary filename for the given filename.

Parameters:
- `filename` (string): 

## Available Resources

- `app://yt-dlp/status` — Current status and version of yt-dlp
- `app://yt-dlp/commands` — Available commands and tools in yt-dlp
- `app://yt-dlp/config` — Current configuration of yt-dlp
- `docs://yt-dlp/tool-index` — Complete index of all yt-dlp tools with parameters and usage
- `docs://yt-dlp/a_cast_channel_ie` — Documentation for yt-dlp a_cast_channel_ie capabilities
- `docs://yt-dlp/alura_course_ie` — Documentation for yt-dlp alura_course_ie capabilities
- `docs://yt-dlp/andere_tijden_ie` — Documentation for yt-dlp andere_tijden_ie capabilities
- `docs://yt-dlp/aria2c_fd` — Documentation for yt-dlp aria2c_fd capabilities
- `docs://yt-dlp/arte_tv_category_ie` — Documentation for yt-dlp arte_tv_category_ie capabilities

## Available Prompts

- `use_yt_dlp` — Guide for using yt-dlp tools effectively
- `debug_yt_dlp` — Diagnose issues with yt-dlp operations

## Usage

This server runs over stdio. Add it to your MCP client config:

```json
{
  "mcpServers": {
    "yt-dlp": {
      "command": "mcp-yt-dlp"
    }
  }
}
```
