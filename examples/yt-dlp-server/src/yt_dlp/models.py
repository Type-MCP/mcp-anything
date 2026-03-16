"""Data models for yt-dlp MCP server."""

from dataclasses import dataclass
from typing import Any


@dataclass
class IdentityParams:
    """Parameters for identity."""
    x: str

@dataclass
class ACastChannelIeSuitableParams:
    """Parameters for a_cast_channel_ie_suitable."""
    url: str

@dataclass
class AddAcceptEncodingHeaderParams:
    """Parameters for add_accept_encoding_header."""
    headers: str
    supported_encodings: str

@dataclass
class AesCbcDecryptParams:
    """Parameters for aes_cbc_decrypt."""
    data: str
    key: str
    iv: str

@dataclass
class AesCbcEncryptParams:
    """Parameters for aes_cbc_encrypt."""
    data: str
    key: str
    iv: str
    padding_mode: str | None = None

@dataclass
class AesCbcEncryptBytesParams:
    """Parameters for aes_cbc_encrypt_bytes."""
    data: str
    key: str
    iv: str

@dataclass
class AesCtrDecryptParams:
    """Parameters for aes_ctr_decrypt."""
    data: str
    key: str
    iv: str

@dataclass
class AesCtrEncryptParams:
    """Parameters for aes_ctr_encrypt."""
    data: str
    key: str
    iv: str

@dataclass
class AesDecryptParams:
    """Parameters for aes_decrypt."""
    data: str
    expanded_key: str

@dataclass
class AesDecryptTextParams:
    """Parameters for aes_decrypt_text."""
    data: str
    password: str
    key_size_bytes: str

@dataclass
class AesEcbDecryptParams:
    """Parameters for aes_ecb_decrypt."""
    data: str
    key: str
    iv: str | None = None

@dataclass
class AesEcbEncryptParams:
    """Parameters for aes_ecb_encrypt."""
    data: str
    key: str
    iv: str | None = None

@dataclass
class AesEncryptParams:
    """Parameters for aes_encrypt."""
    data: str
    expanded_key: str

@dataclass
class AesGcmDecryptAndVerifyParams:
    """Parameters for aes_gcm_decrypt_and_verify."""
    data: str
    key: str
    tag: str
    nonce: str

@dataclass
class AgeRestrictedParams:
    """Parameters for age_restricted."""
    content_limit: str
    age_limit: str

@dataclass
class AluraCourseIeSuitableParams:
    """Parameters for alura_course_ie_suitable."""
    url: str

@dataclass
class AndereTijdenIeSuitableParams:
    """Parameters for andere_tijden_ie_suitable."""
    url: str

@dataclass
class ArgsToStrParams:
    """Parameters for args_to_str."""
    args: str

@dataclass
class Aria2cFdAria2cRpcParams:
    """Parameters for aria2c_fd_aria2c_rpc."""
    rpc_port: str
    rpc_secret: str
    method: str
    params: str | None = None

@dataclass
class Aria2cFdSupportsManifestParams:
    """Parameters for aria2c_fd_supports_manifest."""
    manifest: str

@dataclass
class ArteTvCategoryIeSuitableParams:
    """Parameters for arte_tv_category_ie_suitable."""
    url: str

@dataclass
class AssSubtitlesTimecodeParams:
    """Parameters for ass_subtitles_timecode."""
    seconds: str

@dataclass
class AwsIdpAuthenticateParams:
    """Parameters for aws_idp_authenticate."""
    username: str
    password: str

@dataclass
class BandcampAlbumIeSuitableParams:
    """Parameters for bandcamp_album_ie_suitable."""
    url: str

@dataclass
class BaseUrlParams:
    """Parameters for base_url."""
    url: str

@dataclass
class BbcieSuitableParams:
    """Parameters for bbcie_suitable."""
    url: str

@dataclass
class BbvtvLiveIeSuitableParams:
    """Parameters for bbvtv_live_ie_suitable."""
    url: str

@dataclass
class BiliIntlBaseIeJson2srtParams:
    """Parameters for bili_intl_base_ie_json2srt."""
    json: str

@dataclass
class BilibiliBaseIeExtractFormatsParams:
    """Parameters for bilibili_base_ie_extract_formats."""
    play_info: str

@dataclass
class BilibiliBaseIeJson2srtParams:
    """Parameters for bilibili_base_ie_json2srt."""
    json_data: str

@dataclass
class BilibiliCollectionListIeSuitableParams:
    """Parameters for bilibili_collection_list_ie_suitable."""
    url: str

@dataclass
class BlockParseParams:
    """Parameters for block_parse."""
    parser: str

@dataclass
class BlockProductParams:
    """Parameters for block_product."""
    block_x: str
    block_y: str

@dataclass
class BlockWriteIntoParams:
    """Parameters for block_write_into."""
    stream: str

@dataclass
class BoolOrNoneParams:
    """Parameters for bool_or_none."""
    v: str
    default: str | None = None

@dataclass
class BoxParams:
    """Parameters for box."""
    box_type: str
    payload: str

@dataclass
class BreaklineStatusPrinterPrintAtLineParams:
    """Parameters for breakline_status_printer_print_at_line."""
    text: str
    pos: str

@dataclass
class BugReportsMessageParams:
    """Parameters for bug_reports_message."""
    before: str | None = None

@dataclass
class BuildFragmentsListParams:
    """Parameters for build_fragments_list."""
    boot_info: str

@dataclass
class BunnyCdnFdPingThreadParams:
    """Parameters for bunny_cdn_fd_ping_thread."""
    stop_event: str
    url: str
    headers: str
    secret: str
    context_id: str

@dataclass
class BunnyCdnFdRealDownloadParams:
    """Parameters for bunny_cdn_fd_real_download."""
    filename: str
    info_dict: str

@dataclass
class BytesToIntlistParams:
    """Parameters for bytes_to_intlist."""
    bs: str

@dataclass
class BytesToLongParams:
    """Parameters for bytes_to_long."""
    s: str

@dataclass
class CacheLoadParams:
    """Parameters for cache_load."""
    section: str
    key: str
    dtype: str | None = None
    default: str | None = None
    min_ver: str | None = None

@dataclass
class CacheStoreParams:
    """Parameters for cache_store."""
    section: str
    key: str
    data: str
    dtype: str | None = None

@dataclass
class CaesarParams:
    """Parameters for caesar."""
    s: str
    alphabet: str
    shift: str

@dataclass
class CallinIeTryGetUserNameParams:
    """Parameters for callin_ie_try_get_user_name."""
    d: str

@dataclass
class CandidatePluginPathsParams:
    """Parameters for candidate_plugin_paths."""
    candidate: str

@dataclass
class CbcieSuitableParams:
    """Parameters for cbcie_suitable."""
    url: str

@dataclass
class CheckExecutableParams:
    """Parameters for check_executable."""
    exe: str
    args: str | None = None

@dataclass
class ChromeCookieDecryptorDecryptParams:
    """Parameters for chrome_cookie_decryptor_decrypt."""
    encrypted_value: str

@dataclass
class CiscoLiveSearchIeSuitableParams:
    """Parameters for cisco_live_search_ie_suitable."""
    url: str

@dataclass
class CleanHeadersParams:
    """Parameters for clean_headers."""
    headers: str

@dataclass
class CleanHtmlParams:
    """Parameters for clean_html."""
    html: str

@dataclass
class CleanPodcastUrlParams:
    """Parameters for clean_podcast_url."""
    url: str

@dataclass
class CleanPotParams:
    """Parameters for clean_pot."""
    po_token: str

@dataclass
class CleanProxiesParams:
    """Parameters for clean_proxies."""
    proxies: dict
    headers: str

@dataclass
class CliBoolOptionParams:
    """Parameters for cli_bool_option."""
    params: str
    command_option: str
    param: str
    true_value: str | None = None
    false_value: str | None = None
    separator: str | None = None

@dataclass
class CliConfigurationArgsParams:
    """Parameters for cli_configuration_args."""
    argdict: str
    keys: str
    default: str | None = None
    use_compat: str | None = None

@dataclass
class CliOptionParams:
    """Parameters for cli_option."""
    params: str
    command_option: str
    param: str
    separator: str | None = None

@dataclass
class CliValuelessOptionParams:
    """Parameters for cli_valueless_option."""
    params: str
    command_option: str
    param: str
    expected_value: str | None = None

@dataclass
class CompatEtreeFromstringParams:
    """Parameters for compat_etree_fromstring."""
    text: str

@dataclass
class CompatOrdParams:
    """Parameters for compat_ord."""
    c: str

@dataclass
class CompatSetenvParams:
    """Parameters for compat_setenv."""
    key: str
    value: str
    env: str | None = None

@dataclass
class CompatShlexQuoteParams:
    """Parameters for compat_shlex_quote."""
    s: str

@dataclass
class ConfigAppendConfigParams:
    """Parameters for config_append_config."""
    label: str | None = None

@dataclass
class ConfigInitParams:
    """Parameters for config_init."""
    args: str | None = None
    filename: str | None = None

@dataclass
class ConfigReadFileParams:
    """Parameters for config_read_file."""
    filename: str
    default: str | None = None

@dataclass
class CookieJarToListParams:
    """Parameters for cookie_jar_to_list."""
    cookie_jar: str

@dataclass
class CookieToDictParams:
    """Parameters for cookie_to_dict."""
    cookie: str

@dataclass
class CreateConnectionParams:
    """Parameters for create_connection."""
    address: str
    timeout: str | None = None
    source_address: str | None = None
    create_socket_func: str | None = None

@dataclass
class CreateMappingReParams:
    """Parameters for create_mapping_re."""
    supported: str

@dataclass
class CreateSocksProxySocketParams:
    """Parameters for create_socks_proxy_socket."""
    dest_addr: str
    proxy_args: str
    proxy_ip_addr: str
    timeout: str
    source_address: str

@dataclass
class CueBlockFromJsonParams:
    """Parameters for cue_block_from_json."""
    json: str

@dataclass
class CueBlockHingesParams:
    """Parameters for cue_block_hinges."""
    other: str

@dataclass
class CueBlockParseParams:
    """Parameters for cue_block_parse."""
    parser: str

@dataclass
class CueBlockWriteIntoParams:
    """Parameters for cue_block_write_into."""
    stream: str

@dataclass
class CurlCffiPreferenceParams:
    """Parameters for curl_cffi_preference."""
    rh: str
    request: str

@dataclass
class CurlCffiResponseAdapterReadParams:
    """Parameters for curl_cffi_response_adapter_read."""
    amt: str | None = None

@dataclass
class CurlCffiResponseReaderReadParams:
    """Parameters for curl_cffi_response_reader_read."""
    size: str | None = None

@dataclass
class CurlCffirhSendParams:
    """Parameters for curl_cffirh_send."""
    request: str

@dataclass
class DashSegmentsFdRealDownloadParams:
    """Parameters for dash_segments_fd_real_download."""
    filename: str
    info_dict: str

@dataclass
class DataParserExpectBytesParams:
    """Parameters for data_parser_expect_bytes."""
    expected_value: str
    message: str

@dataclass
class DataParserReadBytesParams:
    """Parameters for data_parser_read_bytes."""
    num_bytes: str

@dataclass
class DataParserReadDoubleParams:
    """Parameters for data_parser_read_double."""
    big_endian: str | None = None

@dataclass
class DataParserReadUintParams:
    """Parameters for data_parser_read_uint."""
    big_endian: str | None = None

@dataclass
class DataParserSkipParams:
    """Parameters for data_parser_skip."""
    num_bytes: str
    description: str | None = None

@dataclass
class DataParserSkipToParams:
    """Parameters for data_parser_skip_to."""
    offset: str
    description: str | None = None

@dataclass
class DataParserSkipToEndParams:
    """Parameters for data_parser_skip_to_end."""
    description: str | None = None

@dataclass
class DateFormatsParams:
    """Parameters for date_formats."""
    day_first: str | None = None

@dataclass
class DateFromStrParams:
    """Parameters for date_from_str."""
    date_str: str
    format: str | None = None
    strict: str | None = None

@dataclass
class DateRangeDayParams:
    """Parameters for date_range_day."""
    day: str

@dataclass
class DatetimeAddMonthsParams:
    """Parameters for datetime_add_months."""
    dt: str
    months: str

@dataclass
class DatetimeFromStrParams:
    """Parameters for datetime_from_str."""
    date_str: str
    precision: str | None = None
    format: str | None = None

@dataclass
class DatetimeRoundParams:
    """Parameters for datetime_round."""
    dt: str
    precision: str | None = None

@dataclass
class DaumClipIeSuitableParams:
    """Parameters for daum_clip_ie_suitable."""
    url: str

@dataclass
class DaumPlaylistIeSuitableParams:
    """Parameters for daum_playlist_ie_suitable."""
    url: str

@dataclass
class DebuggerWriteParams:
    """Parameters for debugger_write."""
    level: str | None = None

@dataclass
class DecodeArgumentParams:
    """Parameters for decode_argument."""
    b: str

@dataclass
class DecodeFilenameParams:
    """Parameters for decode_filename."""
    b: str
    for_subprocess: str | None = None

@dataclass
class DecodeOptionParams:
    """Parameters for decode_option."""
    optval: str

@dataclass
class DecodeBaseParams:
    """Parameters for decode_base."""
    value: str
    digits: str

@dataclass
class DecodeBase64Params:
    """Parameters for decode_base64."""
    text: str

@dataclass
class DecodeBaseNParams:
    """Parameters for decode_base_n."""
    string: str
    n: str | None = None
    table: str | None = None

@dataclass
class DecodePackedCodesParams:
    """Parameters for decode_packed_codes."""
    code: str

@dataclass
class DecodePngParams:
    """Parameters for decode_png."""
    png_data: str

@dataclass
class DeprecationWarningParams:
    """Parameters for deprecation_warning."""
    msg: str
    printer: str | None = None
    stacklevel: str | None = None

@dataclass
class DetectExeVersionParams:
    """Parameters for detect_exe_version."""
    output: str
    version_re: str | None = None
    unrecognized: str | None = None

@dataclass
class DetermineExtParams:
    """Parameters for determine_ext."""
    url: str
    default_ext: str | None = None

@dataclass
class DetermineFileEncodingParams:
    """Parameters for determine_file_encoding."""
    data: str

@dataclass
class DetermineProtocolParams:
    """Parameters for determine_protocol."""
    info_dict: str

@dataclass
class Dfxp2srtParams:
    """Parameters for dfxp2srt."""
    dfxp_data: str

@dataclass
class DictGetParams:
    """Parameters for dict_get."""
    d: str
    key_or_keys: str
    default: str | None = None
    skip_false_values: str | None = None

@dataclass
class DirsInZipParams:
    """Parameters for dirs_in_zip."""
    archive: str

@dataclass
class EinsUndEinsTvLiveIeSuitableParams:
    """Parameters for eins_und_eins_tv_live_ie_suitable."""
    url: str

@dataclass
class EncodeArgumentParams:
    """Parameters for encode_argument."""
    s: str

@dataclass
class EncodeFilenameParams:
    """Parameters for encode_filename."""
    s: str
    for_subprocess: str | None = None

@dataclass
class EncodeBaseNParams:
    """Parameters for encode_base_n."""
    num: str
    n: str | None = None
    table: str | None = None

@dataclass
class EncodeCompatStrParams:
    """Parameters for encode_compat_str."""
    string: str
    encoding: str | None = None
    errors: str | None = None

@dataclass
class EncodeDataUriParams:
    """Parameters for encode_data_uri."""
    data: str
    mime_type: str

@dataclass
class ErrorToCompatStrParams:
    """Parameters for error_to_compat_str."""
    err: str

@dataclass
class ErrorToStrParams:
    """Parameters for error_to_str."""
    err: str

@dataclass
class EscapeHtmlParams:
    """Parameters for escape_html."""
    text: str

@dataclass
class EscapeRfc3986Params:
    """Parameters for escape_rfc3986."""
    s: str

@dataclass
class EspnArticleIeSuitableParams:
    """Parameters for espn_article_ie_suitable."""
    url: str

@dataclass
class EwetvLiveIeSuitableParams:
    """Parameters for ewetv_live_ie_suitable."""
    url: str

@dataclass
class ExecPpParseCmdParams:
    """Parameters for exec_pp_parse_cmd."""
    cmd: str
    info: str

@dataclass
class ExpandPathParams:
    """Parameters for expand_path."""
    s: str

@dataclass
class Ext2mimetypeParams:
    """Parameters for ext2mimetype."""
    ext_or_url: str

@dataclass
class ExternalFdAvailableParams:
    """Parameters for external_fd_available."""
    path: str | None = None

@dataclass
class ExternalFdCanDownloadParams:
    """Parameters for external_fd_can_download."""
    info_dict: str
    path: str | None = None

@dataclass
class ExternalFdRealDownloadParams:
    """Parameters for external_fd_real_download."""
    filename: str
    info_dict: str

@dataclass
class ExternalFdSupportsParams:
    """Parameters for external_fd_supports."""
    info_dict: str

@dataclass
class ExtractAttributesParams:
    """Parameters for extract_attributes."""
    html_element: str

@dataclass
class ExtractBasicAuthParams:
    """Parameters for extract_basic_auth."""
    url: str

@dataclass
class ExtractBoxDataParams:
    """Parameters for extract_box_data."""
    data: str
    box_sequence: str

@dataclass
class ExtractCookiesFromBrowserParams:
    """Parameters for extract_cookies_from_browser."""
    browser_name: str
    profile: str | None = None
    logger: str | None = None
    keyring: str | None = None
    container: str | None = None

@dataclass
class ExtractTimezoneParams:
    """Parameters for extract_timezone."""
    date_str: str
    default: str | None = None

@dataclass
class F4mFdRealDownloadParams:
    """Parameters for f4m_fd_real_download."""
    filename: str
    info_dict: str

@dataclass
class FFmpegConcatPpConcatFilesParams:
    """Parameters for f_fmpeg_concat_pp_concat_files."""
    in_files: str
    out_file: str

@dataclass
class FFmpegExtractAudioPpRunFfmpegParams:
    """Parameters for f_fmpeg_extract_audio_pp_run_ffmpeg."""
    path: str
    out_path: str
    codec: str
    more_opts: str

@dataclass
class FFmpegFdAvailableParams:
    """Parameters for f_fmpeg_fd_available."""
    path: str | None = None

@dataclass
class FFmpegFdCanMergeFormatsParams:
    """Parameters for f_fmpeg_fd_can_merge_formats."""
    info_dict: str
    params: str

@dataclass
class FFmpegFdOnProcessStartedParams:
    """Parameters for f_fmpeg_fd_on_process_started."""
    proc: str
    stdin: str

@dataclass
class FFmpegPostProcessorConcatFilesParams:
    """Parameters for f_fmpeg_post_processor_concat_files."""
    in_files: str
    out_file: str
    concat_opts: str | None = None

@dataclass
class FFmpegPostProcessorForceKeyframesParams:
    """Parameters for f_fmpeg_post_processor_force_keyframes."""
    filename: str
    timestamps: str

@dataclass
class FFmpegPostProcessorGetAudioCodecParams:
    """Parameters for f_fmpeg_post_processor_get_audio_codec."""
    path: str

@dataclass
class FFmpegPostProcessorGetMetadataObjectParams:
    """Parameters for f_fmpeg_post_processor_get_metadata_object."""
    path: str
    opts: str | None = None

@dataclass
class FFmpegPostProcessorGetStreamNumberParams:
    """Parameters for f_fmpeg_post_processor_get_stream_number."""
    path: str
    keys: str
    value: str

@dataclass
class FFmpegPostProcessorGetVersionsParams:
    """Parameters for f_fmpeg_post_processor_get_versions."""
    downloader: str | None = None

@dataclass
class FFmpegPostProcessorGetVersionsAndFeaturesParams:
    """Parameters for f_fmpeg_post_processor_get_versions_and_features."""
    downloader: str | None = None

@dataclass
class FFmpegPostProcessorRunFfmpegParams:
    """Parameters for f_fmpeg_post_processor_run_ffmpeg."""
    path: str
    out_path: str
    opts: str

@dataclass
class FFmpegPostProcessorRunFfmpegMultipleFilesParams:
    """Parameters for f_fmpeg_post_processor_run_ffmpeg_multiple_files."""
    input_paths: str
    out_path: str
    opts: str

@dataclass
class FFmpegPostProcessorStreamCopyOptsParams:
    """Parameters for f_fmpeg_post_processor_stream_copy_opts."""
    copy: str | None = None
    ext: str | None = None

@dataclass
class FFmpegSinkFdRealConnectionParams:
    """Parameters for f_fmpeg_sink_fd_real_connection."""
    sink: str
    info_dict: str

@dataclass
class FFmpegSinkFdRealDownloadParams:
    """Parameters for f_fmpeg_sink_fd_real_download."""
    filename: str
    info_dict: str

@dataclass
class FFmpegThumbnailsConvertorPpConvertThumbnailParams:
    """Parameters for f_fmpeg_thumbnails_convertor_pp_convert_thumbnail."""
    thumbnail_filename: str
    target_ext: str

@dataclass
class FFmpegThumbnailsConvertorPpFixupWebpParams:
    """Parameters for f_fmpeg_thumbnails_convertor_pp_fixup_webp."""
    info: str
    idx: str | None = None

@dataclass
class FFmpegThumbnailsConvertorPpIsWebpParams:
    """Parameters for f_fmpeg_thumbnails_convertor_pp_is_webp."""
    path: str

@dataclass
class FancodeVodIeDownloadGqlParams:
    """Parameters for fancode_vod_ie_download_gql."""
    variable: str
    data: str
    note: str
    fatal: str | None = None
    headers: str | None = None

@dataclass
class Fc2LiveFdRealDownloadParams:
    """Parameters for fc2_live_fd_real_download."""
    filename: str
    info_dict: str

@dataclass
class FileDownloaderAddProgressHookParams:
    """Parameters for file_downloader_add_progress_hook."""
    ph: str

@dataclass
class FileDownloaderBestBlockSizeParams:
    """Parameters for file_downloader_best_block_size."""
    elapsed_time: str
    bytes: str

@dataclass
class FileDownloaderCalcEtaParams:
    """Parameters for file_downloader_calc_eta."""
    start_or_rate: str
    now_or_remaining: str
    total: str | None = None
    current: str | None = None

@dataclass
class FileDownloaderCalcPercentParams:
    """Parameters for file_downloader_calc_percent."""
    byte_counter: str
    data_len: str

@dataclass
class FileDownloaderCalcSpeedParams:
    """Parameters for file_downloader_calc_speed."""
    start: str
    now: str
    bytes: str

@dataclass
class FileDownloaderDownloadParams:
    """Parameters for file_downloader_download."""
    filename: str
    info_dict: str
    subtitle: str | None = None

@dataclass
class FileDownloaderFilesizeOrNoneParams:
    """Parameters for file_downloader_filesize_or_none."""
    unencoded_filename: str

@dataclass
class FileDownloaderFormatEtaParams:
    """Parameters for file_downloader_format_eta."""
    seconds: str

@dataclass
class FileDownloaderFormatPercentParams:
    """Parameters for file_downloader_format_percent."""
    percent: str

@dataclass
class FileDownloaderFormatRetriesParams:
    """Parameters for file_downloader_format_retries."""
    retries: str

@dataclass
class FileDownloaderFormatSecondsParams:
    """Parameters for file_downloader_format_seconds."""
    seconds: str

@dataclass
class FileDownloaderFormatSpeedParams:
    """Parameters for file_downloader_format_speed."""
    speed: str

@dataclass
class FileDownloaderParseBytesParams:
    """Parameters for file_downloader_parse_bytes."""
    bytestr: str

@dataclass
class FileDownloaderRealDownloadParams:
    """Parameters for file_downloader_real_download."""
    filename: str
    info_dict: str

@dataclass
class FileDownloaderReportDestinationParams:
    """Parameters for file_downloader_report_destination."""
    filename: str

@dataclass
class FileDownloaderReportResumingByteParams:
    """Parameters for file_downloader_report_resuming_byte."""
    resume_len: str

@dataclass
class FileDownloaderReportRetryParams:
    """Parameters for file_downloader_report_retry."""
    err: str
    count: str
    retries: str
    frag_index: str | None = None
    fatal: str | None = None

@dataclass
class FileDownloaderSanitizeOpenParams:
    """Parameters for file_downloader_sanitize_open."""
    filename: str
    open_mode: str

@dataclass
class FileDownloaderSlowDownParams:
    """Parameters for file_downloader_slow_down."""
    start_time: str
    now: str
    byte_counter: str

@dataclass
class FileDownloaderSupportsManifestParams:
    """Parameters for file_downloader_supports_manifest."""
    manifest: str

@dataclass
class FileDownloaderTempNameParams:
    """Parameters for file_downloader_temp_name."""
    filename: str

