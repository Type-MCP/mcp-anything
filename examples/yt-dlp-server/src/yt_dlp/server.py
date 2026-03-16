"""MCP server for yt-dlp."""

import os

from mcp.server.fastmcp import FastMCP

server = FastMCP("yt-dlp")

from yt_dlp.backend import Backend

_backend = Backend()

# Import and register tool modules
from yt_dlp.tools.general import register_tools as register_general_tools
register_general_tools(server, _backend)
from yt_dlp.tools.a_cast_channel_ie import register_tools as register_a_cast_channel_ie_tools
register_a_cast_channel_ie_tools(server, _backend)
from yt_dlp.tools.creation import register_tools as register_creation_tools
register_creation_tools(server, _backend)
from yt_dlp.tools.alura_course_ie import register_tools as register_alura_course_ie_tools
register_alura_course_ie_tools(server, _backend)
from yt_dlp.tools.andere_tijden_ie import register_tools as register_andere_tijden_ie_tools
register_andere_tijden_ie_tools(server, _backend)
from yt_dlp.tools.aria2c_fd import register_tools as register_aria2c_fd_tools
register_aria2c_fd_tools(server, _backend)
from yt_dlp.tools.arte_tv_category_ie import register_tools as register_arte_tv_category_ie_tools
register_arte_tv_category_ie_tools(server, _backend)
from yt_dlp.tools.aws_idp import register_tools as register_aws_idp_tools
register_aws_idp_tools(server, _backend)
from yt_dlp.tools.bandcamp_album_ie import register_tools as register_bandcamp_album_ie_tools
register_bandcamp_album_ie_tools(server, _backend)
from yt_dlp.tools.bbcie import register_tools as register_bbcie_tools
register_bbcie_tools(server, _backend)
from yt_dlp.tools.bbvtv_live_ie import register_tools as register_bbvtv_live_ie_tools
register_bbvtv_live_ie_tools(server, _backend)
from yt_dlp.tools.bili_intl_base_ie import register_tools as register_bili_intl_base_ie_tools
register_bili_intl_base_ie_tools(server, _backend)
from yt_dlp.tools.bilibili_base_ie import register_tools as register_bilibili_base_ie_tools
register_bilibili_base_ie_tools(server, _backend)
from yt_dlp.tools.bilibili_collection_list_ie import register_tools as register_bilibili_collection_list_ie_tools
register_bilibili_collection_list_ie_tools(server, _backend)
from yt_dlp.tools.block import register_tools as register_block_tools
register_block_tools(server, _backend)
from yt_dlp.tools.breakline_status_printer import register_tools as register_breakline_status_printer_tools
register_breakline_status_printer_tools(server, _backend)
from yt_dlp.tools.bunny_cdn_fd import register_tools as register_bunny_cdn_fd_tools
register_bunny_cdn_fd_tools(server, _backend)
from yt_dlp.tools.cache import register_tools as register_cache_tools
register_cache_tools(server, _backend)
from yt_dlp.tools.callin_ie import register_tools as register_callin_ie_tools
register_callin_ie_tools(server, _backend)
from yt_dlp.tools.cbcie import register_tools as register_cbcie_tools
register_cbcie_tools(server, _backend)
from yt_dlp.tools.chrome_cookie_decryptor import register_tools as register_chrome_cookie_decryptor_tools
register_chrome_cookie_decryptor_tools(server, _backend)
from yt_dlp.tools.cisco_live_search_ie import register_tools as register_cisco_live_search_ie_tools
register_cisco_live_search_ie_tools(server, _backend)
from yt_dlp.tools.config import register_tools as register_config_tools
register_config_tools(server, _backend)
from yt_dlp.tools.cue_block import register_tools as register_cue_block_tools
register_cue_block_tools(server, _backend)
from yt_dlp.tools.curl_cffi_response_adapter import register_tools as register_curl_cffi_response_adapter_tools
register_curl_cffi_response_adapter_tools(server, _backend)
from yt_dlp.tools.curl_cffi_response_reader import register_tools as register_curl_cffi_response_reader_tools
register_curl_cffi_response_reader_tools(server, _backend)
from yt_dlp.tools.curl_cffirh import register_tools as register_curl_cffirh_tools
register_curl_cffirh_tools(server, _backend)
from yt_dlp.tools.dash_segments_fd import register_tools as register_dash_segments_fd_tools
register_dash_segments_fd_tools(server, _backend)
from yt_dlp.tools.data_parser import register_tools as register_data_parser_tools
register_data_parser_tools(server, _backend)
from yt_dlp.tools.date_range import register_tools as register_date_range_tools
register_date_range_tools(server, _backend)
from yt_dlp.tools.daum_clip_ie import register_tools as register_daum_clip_ie_tools
register_daum_clip_ie_tools(server, _backend)
from yt_dlp.tools.daum_playlist_ie import register_tools as register_daum_playlist_ie_tools
register_daum_playlist_ie_tools(server, _backend)
from yt_dlp.tools.debugger import register_tools as register_debugger_tools
register_debugger_tools(server, _backend)
from yt_dlp.tools.eins_und_eins_tv_live_ie import register_tools as register_eins_und_eins_tv_live_ie_tools
register_eins_und_eins_tv_live_ie_tools(server, _backend)
from yt_dlp.tools.espn_article_ie import register_tools as register_espn_article_ie_tools
register_espn_article_ie_tools(server, _backend)
from yt_dlp.tools.ewetv_live_ie import register_tools as register_ewetv_live_ie_tools
register_ewetv_live_ie_tools(server, _backend)
from yt_dlp.tools.exec_pp import register_tools as register_exec_pp_tools
register_exec_pp_tools(server, _backend)
from yt_dlp.tools.external_fd import register_tools as register_external_fd_tools
register_external_fd_tools(server, _backend)
from yt_dlp.tools.f4m_fd import register_tools as register_f4m_fd_tools
register_f4m_fd_tools(server, _backend)
from yt_dlp.tools.f_fmpeg_concat_pp import register_tools as register_f_fmpeg_concat_pp_tools
register_f_fmpeg_concat_pp_tools(server, _backend)
from yt_dlp.tools.f_fmpeg_extract_audio_pp import register_tools as register_f_fmpeg_extract_audio_pp_tools
register_f_fmpeg_extract_audio_pp_tools(server, _backend)
from yt_dlp.tools.f_fmpeg_fd import register_tools as register_f_fmpeg_fd_tools
register_f_fmpeg_fd_tools(server, _backend)
from yt_dlp.tools.f_fmpeg_post_processor import register_tools as register_f_fmpeg_post_processor_tools
register_f_fmpeg_post_processor_tools(server, _backend)
from yt_dlp.tools.f_fmpeg_sink_fd import register_tools as register_f_fmpeg_sink_fd_tools
register_f_fmpeg_sink_fd_tools(server, _backend)
from yt_dlp.tools.f_fmpeg_thumbnails_convertor_pp import register_tools as register_f_fmpeg_thumbnails_convertor_pp_tools
register_f_fmpeg_thumbnails_convertor_pp_tools(server, _backend)
from yt_dlp.tools.fancode_vod_ie import register_tools as register_fancode_vod_ie_tools
register_fancode_vod_ie_tools(server, _backend)
from yt_dlp.tools.fc2_live_fd import register_tools as register_fc2_live_fd_tools
register_fc2_live_fd_tools(server, _backend)
from yt_dlp.tools.file_downloader import register_tools as register_file_downloader_tools
register_file_downloader_tools(server, _backend)

# Import and register resources
from yt_dlp.resources import register_resources
register_resources(server, _backend)

# Import and register prompts
from yt_dlp.prompts import register_prompts
register_prompts(server)



def main():
    """Run the MCP server."""
    transport = os.environ.get("MCP_TRANSPORT", "stdio")

    if transport == "http":
        host = os.environ.get("MCP_HOST", "0.0.0.0")
        port = int(os.environ.get("MCP_PORT", "8000"))
        server.run(transport="sse", host=host, port=port)
    else:
        server.run(transport="stdio")


if __name__ == "__main__":
    main()
