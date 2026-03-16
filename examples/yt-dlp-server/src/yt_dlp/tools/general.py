"""general tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register general tools with the server."""

    @server.tool()
    async def identity(
        x: str,
    ) -> str:
        """IDENTITY"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("identity")

    @server.tool()
    async def aes_cbc_decrypt(
        data: str,
        key: str,
        iv: str,
    ) -> str:
        """Decrypt with aes in CBC mode"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_cbc_decrypt")

    @server.tool()
    async def aes_cbc_encrypt(
        data: str,
        key: str,
        iv: str,
        padding_mode: str | None = "pkcs7",
    ) -> str:
        """Encrypt with aes in CBC mode"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_cbc_encrypt")

    @server.tool()
    async def aes_cbc_encrypt_bytes(
        data: str,
        key: str,
        iv: str,
    ) -> str:
        """Aes cbc encrypt bytes"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_cbc_encrypt_bytes")

    @server.tool()
    async def aes_ctr_decrypt(
        data: str,
        key: str,
        iv: str,
    ) -> str:
        """Decrypt with aes in counter mode"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_ctr_decrypt")

    @server.tool()
    async def aes_ctr_encrypt(
        data: str,
        key: str,
        iv: str,
    ) -> str:
        """Encrypt with aes in counter mode"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_ctr_encrypt")

    @server.tool()
    async def aes_decrypt(
        data: str,
        expanded_key: str,
    ) -> str:
        """Decrypt one block with aes"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_decrypt")

    @server.tool()
    async def aes_decrypt_text(
        data: str,
        password: str,
        key_size_bytes: str,
    ) -> str:
        """Decrypt text"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_decrypt_text")

    @server.tool()
    async def aes_ecb_decrypt(
        data: str,
        key: str,
        iv: str | None = None,
    ) -> str:
        """Decrypt with aes in ECB mode"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_ecb_decrypt")

    @server.tool()
    async def aes_ecb_encrypt(
        data: str,
        key: str,
        iv: str | None = None,
    ) -> str:
        """Encrypt with aes in ECB mode. Using PKCS#7 padding"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_ecb_encrypt")

    @server.tool()
    async def aes_encrypt(
        data: str,
        expanded_key: str,
    ) -> str:
        """Encrypt one block with aes"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_encrypt")

    @server.tool()
    async def aes_gcm_decrypt_and_verify(
        data: str,
        key: str,
        tag: str,
        nonce: str,
    ) -> str:
        """Decrypt with aes in GBM mode and checks authenticity using tag"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("aes_gcm_decrypt_and_verify")

    @server.tool()
    async def age_restricted(
        content_limit: str,
        age_limit: str,
    ) -> str:
        """Returns True iff the content should be blocked"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("age_restricted")

    @server.tool()
    async def args_to_str(
        args: str,
    ) -> str:
        """Args to str"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("args_to_str")

    @server.tool()
    async def ass_subtitles_timecode(
        seconds: str,
    ) -> str:
        """Ass subtitles timecode"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("ass_subtitles_timecode")

    @server.tool()
    async def base_url(
        url: str,
    ) -> str:
        """Base url"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("base_url")

    @server.tool()
    async def block_product(
        block_x: str,
        block_y: str,
    ) -> str:
        """Block product"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("block_product")

    @server.tool()
    async def bool_or_none(
        v: str,
        default: str | None = None,
    ) -> str:
        """Bool or none"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("bool_or_none")

    @server.tool()
    async def box(
        box_type: str,
        payload: str,
    ) -> str:
        """Box"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("box")

    @server.tool()
    async def bug_reports_message(
        before: str | None = ";",
    ) -> str:
        """Bug reports message"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("bug_reports_message")

    @server.tool()
    async def build_fragments_list(
        boot_info: str,
    ) -> str:
        """Return a list of (segment, fragment) for each fragment in the video"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("build_fragments_list")

    @server.tool()
    async def bytes_to_intlist(
        bs: str,
    ) -> str:
        """Bytes to intlist"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("bytes_to_intlist")

    @server.tool()
    async def bytes_to_long(
        s: str,
    ) -> str:
        """bytes_to_long(string) : long"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("bytes_to_long")

    @server.tool()
    async def caesar(
        s: str,
        alphabet: str,
        shift: str,
    ) -> str:
        """Caesar"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("caesar")

    @server.tool()
    async def candidate_plugin_paths(
        candidate: str,
    ) -> str:
        """Candidate plugin paths"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("candidate_plugin_paths")

    @server.tool()
    async def check_executable(
        exe: str,
        args: str | None = "[]",
    ) -> str:
        """Checks if the given binary is installed somewhere in PATH, and returns its name."""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("check_executable")

    @server.tool()
    async def clean_headers(
        headers: str,
    ) -> str:
        """Clean headers"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("clean_headers")

    @server.tool()
    async def clean_html(
        html: str,
    ) -> str:
        """Clean an HTML snippet into a readable string"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("clean_html")

    @server.tool()
    async def clean_podcast_url(
        url: str,
    ) -> str:
        """Clean podcast url"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("clean_podcast_url")

    @server.tool()
    async def clean_pot(
        po_token: str,
    ) -> str:
        """Clean pot"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("clean_pot")

    @server.tool()
    async def clean_proxies(
        proxies: dict,
        headers: str,
    ) -> str:
        """Clean proxies"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("clean_proxies")

    @server.tool()
    async def cli_bool_option(
        params: str,
        command_option: str,
        param: str,
        true_value: str | None = "true",
        false_value: str | None = "false",
        separator: str | None = None,
    ) -> str:
        """Cli bool option"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("cli_bool_option")

    @server.tool()
    async def cli_configuration_args(
        argdict: str,
        keys: str,
        default: str | None = "[]",
        use_compat: str | None = "True",
    ) -> str:
        """Cli configuration args"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("cli_configuration_args")

    @server.tool()
    async def cli_option(
        params: str,
        command_option: str,
        param: str,
        separator: str | None = None,
    ) -> str:
        """Cli option"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("cli_option")

    @server.tool()
    async def cli_valueless_option(
        params: str,
        command_option: str,
        param: str,
        expected_value: str | None = "True",
    ) -> str:
        """Cli valueless option"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("cli_valueless_option")

    @server.tool()
    async def compat_etree_fromstring(
        text: str,
    ) -> str:
        """Compat etree fromstring"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("compat_etree_fromstring")

    @server.tool()
    async def compat_ord(
        c: str,
    ) -> str:
        """Compat ord"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("compat_ord")

    @server.tool()
    async def compat_setenv(
        key: str,
        value: str,
        env: str | None = None,
    ) -> str:
        """Compat setenv"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("compat_setenv")

    @server.tool()
    async def compat_shlex_quote(
        s: str,
    ) -> str:
        """Compat shlex quote"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("compat_shlex_quote")

    @server.tool()
    async def cookie_jar_to_list(
        cookie_jar: str,
    ) -> str:
        """Cookie jar to list"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("cookie_jar_to_list")

    @server.tool()
    async def cookie_to_dict(
        cookie: str,
    ) -> str:
        """Cookie to dict"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("cookie_to_dict")

    @server.tool()
    async def curl_cffi_preference(
        rh: str,
        request: str,
    ) -> str:
        """Curl cffi preference"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("curl_cffi_preference")

    @server.tool()
    async def current_git_head(
    ) -> str:
        """Current git head"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("current_git_head")

    @server.tool()
    async def date_formats(
        day_first: str | None = "True",
    ) -> str:
        """Date formats"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("date_formats")

    @server.tool()
    async def date_from_str(
        date_str: str,
        format: str | None = "%Y%m%d",
        strict: str | None = "False",
    ) -> str:
        """Return a date object from a string using datetime_from_str"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("date_from_str")

    @server.tool()
    async def datetime_add_months(
        dt: str,
        months: str,
    ) -> str:
        """Increment/Decrement a datetime object by months."""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("datetime_add_months")

    @server.tool()
    async def datetime_from_str(
        date_str: str,
        precision: str | None = "auto",
        format: str | None = "%Y%m%d",
    ) -> str:
        """Return a datetime object from a string."""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("datetime_from_str")

    @server.tool()
    async def datetime_round(
        dt: str,
        precision: str | None = "day",
    ) -> str:
        """Round a datetime object's time to a specific precision"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("datetime_round")

    @server.tool()
    async def decode_argument(
        b: str,
    ) -> str:
        """DecodeArgument"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("decode_argument")

    @server.tool()
    async def decode_filename(
        b: str,
        for_subprocess: str | None = "False",
    ) -> str:
        """DecodeFilename"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("decode_filename")

    @server.tool()
    async def decode_option(
        optval: str,
    ) -> str:
        """DecodeOption"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("decode_option")

    @server.tool()
    async def decode_base(
        value: str,
        digits: str,
    ) -> str:
        """Decode base"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("decode_base")

    @server.tool()
    async def decode_base64(
        text: str,
    ) -> str:
        """Decode base64"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("decode_base64")

    @server.tool()
    async def decode_base_n(
        string: str,
        n: str | None = None,
        table: str | None = None,
    ) -> str:
        """Convert given base-n string to int"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("decode_base_n")

    @server.tool()
    async def decode_packed_codes(
        code: str,
    ) -> str:
        """Decode packed codes"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("decode_packed_codes")

    @server.tool()
    async def decode_png(
        png_data: str,
    ) -> str:
        """Decode png"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("decode_png")

    @server.tool()
    async def deprecation_warning(
        msg: str,
        printer: str | None = None,
        stacklevel: str | None = "0",
    ) -> str:
        """Deprecation warning"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("deprecation_warning")

    @server.tool()
    async def detect_exe_version(
        output: str,
        version_re: str | None = None,
        unrecognized: str | None = "present",
    ) -> str:
        """Detect exe version"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("detect_exe_version")

    @server.tool()
    async def determine_ext(
        url: str,
        default_ext: str | None = "unknown_video",
    ) -> str:
        """Determine ext"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("determine_ext")

    @server.tool()
    async def determine_file_encoding(
        data: str,
    ) -> str:
        """Detect the text encoding used"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("determine_file_encoding")

    @server.tool()
    async def determine_protocol(
        info_dict: str,
    ) -> str:
        """Determine protocol"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("determine_protocol")

    @server.tool()
    async def dfxp2srt(
        dfxp_data: str,
    ) -> str:
        """@param dfxp_data A bytes-like object containing DFXP data"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("dfxp2srt")

    @server.tool()
    async def dict_get(
        d: str,
        key_or_keys: str,
        default: str | None = None,
        skip_false_values: str | None = "True",
    ) -> str:
        """Dict get"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("dict_get")

    @server.tool()
    async def dirs_in_zip(
        archive: str,
    ) -> str:
        """Dirs in zip"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("dirs_in_zip")

    @server.tool()
    async def encode_argument(
        s: str,
    ) -> str:
        """EncodeArgument"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("encode_argument")

    @server.tool()
    async def encode_filename(
        s: str,
        for_subprocess: str | None = "False",
    ) -> str:
        """EncodeFilename"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("encode_filename")

    @server.tool()
    async def encode_base_n(
        num: str,
        n: str | None = None,
        table: str | None = None,
    ) -> str:
        """Convert given int to a base-n string"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("encode_base_n")

    @server.tool()
    async def encode_compat_str(
        string: str,
        encoding: str | None = None,
        errors: str | None = "strict",
    ) -> str:
        """Encode compat str"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("encode_compat_str")

    @server.tool()
    async def encode_data_uri(
        data: str,
        mime_type: str,
    ) -> str:
        """Encode data uri"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("encode_data_uri")

    @server.tool()
    async def error_to_compat_str(
        err: str,
    ) -> str:
        """Error to compat str"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("error_to_compat_str")

    @server.tool()
    async def error_to_str(
        err: str,
    ) -> str:
        """Error to str"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("error_to_str")

    @server.tool()
    async def escape_html(
        text: str,
    ) -> str:
        """EscapeHTML"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("escape_html")

    @server.tool()
    async def escape_rfc3986(
        s: str,
    ) -> str:
        """Escape non-ASCII characters as suggested by RFC 3986"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("escape_rfc3986")

    @server.tool()
    async def expand_path(
        s: str,
    ) -> str:
        """Expand shell variables and ~"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("expand_path")

    @server.tool()
    async def ext2mimetype(
        ext_or_url: str,
    ) -> str:
        """Ext2mimetype"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("ext2mimetype")

    @server.tool()
    async def extract_attributes(
        html_element: str,
    ) -> str:
        """Given a string for an HTML element such as"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("extract_attributes")

    @server.tool()
    async def extract_basic_auth(
        url: str,
    ) -> str:
        """Extract basic auth"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("extract_basic_auth")

    @server.tool()
    async def extract_box_data(
        data: str,
        box_sequence: str,
    ) -> str:
        """Extract box data"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("extract_box_data")

    @server.tool()
    async def extract_cookies_from_browser(
        browser_name: str,
        profile: str | None = None,
        logger: str | None = None,
        keyring: str | None = None,
        container: str | None = None,
    ) -> str:
        """Extract cookies from browser"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("extract_cookies_from_browser")

    @server.tool()
    async def extract_timezone(
        date_str: str,
        default: str | None = None,
    ) -> str:
        """Extract timezone"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("extract_timezone")

