from selenium import webdriver
from variables.constants import GRAPHIC_INTERFACE, FIREFOX_PROFILE, FIREFOX_BINARY_LOCATION

def firefox_option():
    OPTIONS = webdriver.FirefoxOptions()

    if not GRAPHIC_INTERFACE:
        OPTIONS.add_argument("-headless")
    
    OPTIONS.set_preference("layers.acceleration.disabled", True)
    OPTIONS.set_preference("layers.acceleration.force-enabled", False)

    
    OPTIONS.set_preference("browser.cache.memory.capacity", 4096)
    OPTIONS.set_preference("browser.sessionhistory.max_entries", 1)

    OPTIONS.set_preference("dom.ipc.processCount", 1)
    OPTIONS.set_preference("permissions.default.image", 2)

    OPTIONS.binary_location = FIREFOX_BINARY_LOCATION
    OPTIONS.profile = FIREFOX_PROFILE

    OPTIONS.set_preference("print.always_print_silent", True)
    OPTIONS.set_preference("print.show_print_progress", False)
    OPTIONS.set_preference('print.save_as_pdf.links.enabled', True)
    
    OPTIONS.set_preference("print_printer", "Save to PDF")
    OPTIONS.set_preference("print.printer_Save_to_PDF.print_to_file", True)
    OPTIONS.set_preference('print.printer_Save_to_PDF.print_to_filename', "mozilla.pdf")

    return OPTIONS
