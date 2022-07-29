hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; height: 0px;}
        #Header {height: 0px;}
        </style>
        """

reduce_header_height_style = """
    <style>
        div.block-container {padding-top:0rem;}
    </style>
"""

remove_altair_action_menu = """
    <style type='text/css'>
        details {
            display: none;
        }
    </style>
"""

unblur_header = """
<style>
header[data-testid="stHeader"] {
    background: none;
    visibility: hidden;
}
</style>
"""